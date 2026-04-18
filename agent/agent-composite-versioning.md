# Agent Composite Versioning

*Cross-cutting governance for agent products. Applies at every stage of the APLC.*

See [aplc.md](../aplc.md) for the lifecycle overview.
See [agent-release-governance.md](agent-release-governance.md) for Stage 4 gate conditions that require the composite state manifest.
See [agent-operations.md](agent-operations.md) for Stage 5 monitoring that triggers composite state updates.

---

## Why Software Versioning Fails for Agents

Software versioning assumes a single artifact with a single version. When you deploy version 2.3.1 of a service, you know precisely what is running: one artifact, one version, one behavioral surface. The version number is a complete description of what was shipped.

An agent product is not a single artifact. Its behavior at runtime is the product of six components, each controlled by a different party, each changing on a different timescale, each capable of producing a behavioral change with no corresponding change to the others. Two deployments sharing the same code version but running against different foundation model snapshots will behave differently. Two deployments sharing code and model but with different knowledge base content will retrieve different facts. A version number that covers only the code tells you almost nothing about what the agent will actually do.

This is not an abstract concern. Foundation model providers update hosted model versions — sometimes silently — without issuing a new model identifier visible to operators. A behavioral regression that begins on a Tuesday in an agent product whose code has not changed is almost certainly a foundation model or knowledge base change. Without a composite versioning model that makes all six components explicitly tracked, that regression is uninvestigable. The on-call engineer has no diff to examine, no change to rollback, no component to point at. They have a behavioral change and no explanation.

The composite versioning model described in this document makes behavioral incidents investigable by creating a formal record of every component that shapes agent behavior, who controls it, how it changes, and what its exact state was at any point in time. It does not prevent behavioral changes caused by components the operator does not control. It makes those changes visible, attributable, and — where reconstruction is possible — reproducible.

### The Six Components

**1. Application code** — the orchestration logic, tool integrations, memory management, routing rules, and infrastructure that the engineering team authors and deploys. This is the component software versioning already handles well. Controlled by the engineering team. Versioned in source control. Changes are author-initiated, reviewed, and deployed through the standard release process.

**2. System prompt / instructions** — the behavioral instructions that govern how the agent interprets tasks, applies constraints, handles uncertainty, and escalates. This is authored text, not executable code, but it is as consequential as code: a change to the system prompt changes the agent's behavior on every subsequent interaction. Controlled by the product or engineering team. May live in source control alongside code, in a database, in a configuration service, or assembled dynamically at runtime. Each storage location has different versioning implications — see Component Version Identifiers below.

**3. Foundation model** — the underlying large language model that executes the agent's reasoning. This is the most distinctive versioning challenge in agent products. The foundation model is controlled by the provider, not the operator. Providers update hosted model versions — changing instruction-following behavior, safety filtering, tool-use patterns, and output style — sometimes without issuing a new model identifier that operators can detect. The operator did not initiate the change. The operator may not know the change occurred. This component can change under an agent product's feet without any action by anyone in the operator's organization.

**4. Knowledge base / RAG content** — the documents, structured data, and retrieval indexes the agent queries to ground its responses. Controlled by content teams. Changes continuously: documents are added, updated, removed; indexes are rebuilt; embeddings are refreshed. A knowledge base update can change every answer the agent gives on topics covered by the updated content, without any change to code, prompt, model, or memory.

**5. Memory state** — the agent's accumulated learned context: user preferences, prior conversation summaries, learned heuristics, and any state the agent persists between sessions. For persistent-memory deployments, memory evolves with every interaction. For stateless deployments, the default initial state is itself a versioned artifact. Memory can be reset by a governance decision (Stage 6 recalibration), which is itself a component state change that must be recorded.

Two deployments with the same code version, same prompt, same model, and same knowledge base will behave differently if one carries accumulated memory that the other does not. Behavioral differences between production and a test environment that shares all other components are often explained entirely by memory state divergence.

**6. Tool manifest** — the set of external tools (APIs, functions, plugins, or services) the agent can invoke, along with their versions and interface contracts. This component applies to any agent that uses tools beyond the model's base capability; it is designated `N/A` for stateless non-tool-using agents. Controlled by the engineering and platform team. Versioned through the tool manifest — a structured list of each tool's name, version, and interface schema hash. A tool provider update that changes an API response format, adds or removes fields, or changes a tool's behavior without the engineering team's action is a behavioral state change that must be detected and recorded. Example: an agent built on a financial data API that adds a new required field to its response schema changes the agent's behavior on every tool-dependent interaction, even if no other component changed.

---

## Composite State Hash

The Composite State Hash (CSH) is a single value that uniquely identifies the complete behavioral state of an agent product at a point in time. It is computed over all six components simultaneously.

```
CSH = hash(code_commit || prompt_version || model_id || kb_snapshot_id || memory_state_hash || tool_manifest_hash)
```

For agents with no tool access, `tool_manifest_hash` is the hash of the string literal `stateless-no-tools`. This ensures that a stateless agent that subsequently gains tool access generates a new CSH rather than producing a hash collision with the prior state.

The CSH is computed at every release, stored in the composite state manifest, logged in the deployment record, and captured in operational monitoring at regular intervals (see Stage 5 in [agent-operations.md](agent-operations.md)). When a behavioral incident occurs, the CSH at the incident time is compared to the CSH at the prior release. The diff identifies which components changed. That is the starting point for investigation.

The CSH is an audit hash, not a security hash. Its purpose is not to detect tampering. Its purpose is to make the exact behavioral state of the agent at any past point recoverable, comparable, and diffable. A CSH that cannot be recomputed from a recoverable component state is useless — the component states must be archivable, not merely hashable.

The separator (`||`) in the hash input is a literal byte separator, not string concatenation, to prevent collisions across component boundaries. The hash function must be stable across releases — SHA-256 is the recommended default. If the hash function changes, all historical CSH values become incomparable to new values. Record the hash function used in the composite state manifest.

The CSH changes whenever any component changes. A model update that the operator did not initiate produces a new CSH. That is the intended behavior: the CSH reflects actual behavioral state, not operator-controlled state. An operator who discovers that the CSH changed between two monitoring windows without any release event has detected an externally-initiated component change — almost certainly a foundation model update — and has a record of exactly when it occurred and what the previous state was.

---

## Component Version Identifiers

Each component requires a defined version identifier format. Consistency across the organization is necessary for CSH computation and incident investigation. Define these formats in [agent-conception.md](agent-conception.md) at Stage 1 and enforce them at every subsequent stage.

### Application Code

**Required fields:**
- Repository URL and branch or tag
- Commit hash (40-character hex, full — not abbreviated)
- Build system ID (the identifier assigned by the CI/CD system for this build)
- Container image digest (if deployment uses containers — the `sha256:` digest of the image, not the image tag, because tags are mutable)

The commit hash and the container image digest address different things. The commit hash identifies what source code was compiled. The container image digest identifies what is actually running. Both are required because mismatches between them indicate a build reproducibility problem that must be investigated before the behavioral state can be trusted.

### System Prompt

**Required fields:**
- Version label (human-readable, e.g., `v2.1.0-prompt` or a semantic identifier meaningful to the product team)
- Content hash (hash of the exact bytes of the prompt as delivered to the model at runtime)
- Storage location identifier (one of: `code`, `database`, `config-service`, `dynamic-assembly`)

**Storage-location-specific fields:**

*Code:* the code commit hash is sufficient to identify the prompt version, because the prompt is versioned with the code. If the prompt changes without a code change, it is not in code.

*Database:* row ID and the content hash of the row at the time of capture. The row ID alone is not sufficient — rows can be updated in place without creating a new ID. The content hash confirms what the row contained at the time the manifest was created.

*Config service:* the key, the version identifier assigned by the config service, and the content hash. Config service version identifiers are often opaque (e.g., `rev-00032`) — the content hash makes them meaningful in comparison.

*Dynamic assembly:* prompts assembled at runtime from multiple sources (templates, injected context, tool descriptions) are the most complex case. Each source component must be versioned independently, and the assembly specification — the rules by which components are combined — must itself be versioned. The content hash of the assembled prompt as delivered to the model is the final verification that the assembly process produced what was intended.

**System prompt supply chain integrity.** The system prompt is the behavioral component most directly controllable by insider threat: anyone with write access to the prompt storage location can modify agent behavior without code deployment. Supply chain integrity controls address this threat.

*Authorization.* Writes to the system prompt store must be authorized by the named Behavioral Owner, authenticated through the organization's identity and access management system, and logged to the AGKB with the authorizer's identity, the timestamp, and the diff between the previous and new content. Anonymous writes and bulk imports without individual authorization records are not permitted.

*Delivery-time integrity verification.* At each interaction, the system prompt infrastructure computes the SHA-256 hash of the prompt bytes as delivered to the model and compares it against the content hash recorded in the most recent composite state manifest. A mismatch indicates one of two conditions: (a) the prompt was modified since the manifest was filed, without a corresponding manifest update (unauthorized change); or (b) the manifest is stale (a governed change occurred but the manifest was not updated). Both conditions require investigation. A mismatch that cannot be explained within 30 minutes is treated as a behavioral incident of the Adversarial class — the assumption is unauthorized modification until proven otherwise.

*Unauthorized change response.* An unauthorized system prompt modification triggers: (a) immediate halt of new interactions pending investigation; (b) review of all interactions processed since the last verified manifest state, flagged as potentially processed under an unauthorized behavioral configuration; (c) CSH computation from the current actual prompt to identify the extent of the behavioral state divergence; (d) accountable human notification within 30 minutes; (e) if the unauthorized change cannot be reverted within 2 hours, initiate Stage 4 rollback to the last verified composite state.

*Dynamic assembly integrity.* For system prompts assembled at runtime from multiple source components, each source component must have its own authorization record and content hash. The assembly specification — the rules governing which components are combined in which order — is itself a versioned artifact with its own content hash. A change to the assembly specification without a corresponding Behavioral Owner authorization is treated identically to an unauthorized prompt modification.

### Foundation Model

**Required fields:**
- Provider identifier (e.g., `openai`, `anthropic`, `azure-openai`, `google-vertex`)
- Model name as specified in the API call (e.g., `gpt-4o`, `claude-3-5-sonnet-20241022`)
- Snapshot version if the provider exposes one (some providers surface a `-YYYYMMDD` snapshot identifier; record it if available)
- Date confirmed (the date on which the model version was verified to be the version currently served by the provider — see below)

The date-confirmed field exists because provider model identifiers are not always stable. A model name that today refers to `snapshot-2024-10-22` may tomorrow refer to `snapshot-2025-01-15` without any change to the identifier in the operator's configuration. The date confirmed records when the operator last verified that the model name resolves to the expected version. The gap between the date confirmed and the current date is the window of unverified exposure to a silent model update.

For deployments where model version stability is critical to regulatory compliance or behavioral guarantees, establish a monitoring schedule for confirming model version (see [agent-operations.md](agent-operations.md)) and record each confirmation in the version history.

**Silent behavioral update detection.** The CSH computation depends on the `model_name` identifier. A provider that updates a model's behavior without changing its name — which has occurred with hosted AI models — will not produce a CSH change and will not be detected by CSH monitoring. For this reason, the `date_confirmed` field is a necessary but insufficient control.

**Required supplementary control: scheduled behavioral probe verification.** For any deployed agent product, weekly automated execution of a designated subset of the behavioral fingerprint probe set (defined in the Behavioral Fingerprint Primitive section) against the live production model is required. The probe responses are compared against the baseline fingerprint snapshot taken at the last confirmed CSH. A probe response distribution shift that exceeds the drift threshold defined in the behavioral specification triggers an immediate investigation, regardless of whether the CSH has changed.

This probe-based detection operates independently of CSH monitoring. When a probe-based detection alert fires on a stable CSH, the presumption is a silent behavioral update by the model provider. The investigation protocol is identical to the CSH-mismatch-based detection protocol, except that the component implicated is the foundation model, and the `date_confirmed` field must be refreshed by verifying the model version directly with the provider's API or documentation.

**Probe set for silent update detection.** A minimum of 20 probes from the behavioral fingerprint probe set must be designated as the "silent update sentinel probes." These probes are selected to be maximally sensitive to foundation model behavioral changes across the dimensions most critical to the agent's behavioral specification: hard boundary compliance, uncertainty expression calibration, and persona consistency. The sentinel probe set must be reviewed and updated each time the behavioral specification is revised.

### Knowledge Base

**Required fields:**
- Snapshot identifier (assigned by the knowledge base management system at each snapshot)
- Document count (the number of documents in the snapshot — a fast sanity check for major additions or deletions)
- Last updated date (when the snapshot was built)
- Source manifest hash (a hash of the ordered list of document identifiers in the snapshot — detects document additions and removals even when the snapshot identifier is reused)

The source manifest hash is critical. Without it, two snapshots with the same identifier but different document lists are indistinguishable in the composite state manifest. The source manifest hash must be computed over a canonical serialization of the document list (e.g., sorted document IDs, one per line), not over the document content — document content hashing is too expensive for routine use and is not the primary concern here. The concern is detecting that the scope of the knowledge base changed.

For knowledge bases that update continuously (e.g., live document ingestion pipelines), define a snapshot cadence at Stage 2 in [agent-behavioral-specification.md](agent-behavioral-specification.md) — the behavioral specification must specify how often the knowledge base is snapshotted for versioning purposes and what the CSH recalculation cadence is.

### Memory State

**Required fields:**
- State description (one of: `initial`, `persistent`, `post-reset-YYYY-MM-DD`)
- Content hash (hash of the serialized memory contents at the time of capture, or the literal string `stateless` for deployments that reset memory between sessions)
- Memory schema version (the version of the memory data structure — schema changes must increment this version, because a content hash comparison across schema versions is meaningless)

For stateless deployments, the default initial state is a versioned artifact. If the initial state includes pre-loaded context (e.g., a pre-seeded conversation history or initialized preference structure), that content must be hashed and recorded. `stateless` means memory is reset to this initial state between sessions, not that no initial state exists.

For persistent-memory deployments, the memory state changes continuously. Hashing memory at every interaction is not practical. Record memory state at governance events: releases, recalibrations, memory reviews, and resets. These are the points at which a behavioral change attributable to memory state could be introduced deliberately, and they are the points from which rollback to a prior memory state is most likely to be required.

Memory schema version must be tracked separately from content hash. A memory schema migration is a behavioral change even if the migrated content is semantically identical — the agent's interpretation of its own memory may differ under the new schema. Schema migrations must be recorded in the version history as a distinct event type.

### Tool Manifest

**Required fields:**

- Tool name (the canonical name used to invoke the tool, as it appears in the agent's tool configuration)
- Tool version (the version identifier published by the tool provider — semantic version, date-based version, or commit hash where applicable)
- Interface schema hash (a hash of the tool's input/output schema as defined at the time of incorporation — the JSON Schema, OpenAPI spec, or equivalent)
- Provider identifier (the name of the tool provider or the URI of the tool endpoint)
- Date confirmed (the date on which the tool version and interface schema were last verified against the provider's current API)

**Tool manifest hash computation.** The tool manifest hash is computed as a hash over the canonical serialization of all tool entries in the manifest, sorted by tool name. The canonical serialization format is: one line per tool, in the format `name:version:schema_hash:provider`, sorted ascending by name, with a newline separator. This format ensures that adding, removing, or updating any single tool produces a new manifest hash.

**Silent tool updates.** Tool providers may update their API behavior without incrementing the version identifier — the same problem that affects foundation model providers. The `date_confirmed` field serves the same mitigating function as in the foundation model component: it records when the tool's behavior was last verified against the schema on record. For tools where behavioral consistency is critical, the tool schema must be verified (by sending a probe request and validating the response against the recorded schema) at least as frequently as the foundation model `date_confirmed` field is refreshed. A tool whose response schema has diverged from the recorded schema without a corresponding tool manifest update is a governance staleness event equivalent to an undetected foundation model update.

---

## Composite State Manifest Format

The composite state manifest is the formal record of all six component versions at a point in time. It is created at every release (Stage 4 gate condition per [agent-release-governance.md](agent-release-governance.md)) and updated at every Stage 6 maintenance event that changes any component. The manifest is the primary artifact for incident investigation and for demonstrating behavioral state to auditors.

```yaml
composite_state_manifest:
  manifest_id: [unique ID — UUID or sequential ID assigned by the release system]
  created_at: [YYYY-MM-DD HH:MM:SS UTC]
  created_by: [full name and role of the person creating this manifest]
  event_type: [initial_release | maintenance_update | recalibration | rollback]

  components:
    code:
      repository: [full URL including branch or tag]
      commit_hash: [40-character hex]
      build_id: [build system identifier]
      container_digest: [sha256:... — omit if not containerized]

    system_prompt:
      version_label: [human-readable version identifier]
      content_hash: [hash of prompt bytes as delivered to the model]
      storage_location: [code | database | config-service | dynamic-assembly]
      storage_detail: [row ID if database; key + config-service version if config-service;
                       assembly spec version if dynamic — omit if storage_location is code]

    foundation_model:
      provider: [provider name]
      model_name: [model identifier as used in API calls]
      snapshot_version: [if provider exposes snapshot version — omit if not available]
      date_confirmed: [YYYY-MM-DD]

    knowledge_base:
      snapshot_id: [snapshot identifier]
      document_count: [integer]
      last_updated: [YYYY-MM-DD]
      source_manifest_hash: [hash of canonical document list]

    memory_state:
      state_description: [initial | persistent | post-reset-YYYY-MM-DD]
      content_hash: [hash of serialized memory, or "stateless"]
      schema_version: [memory schema version identifier]

    tool_manifest:
      manifest_hash: [hash of canonical serialization of all tool entries]
      tool_count: [integer — number of tools in the manifest, or 0 for non-tool-using agents]
      note: [omit entries below and set manifest_hash to hash("stateless-no-tools") for non-tool-using agents]
      tools:
        - name: [canonical tool name as used in agent tool configuration]
          version: [version identifier published by tool provider]
          schema_hash: [hash of tool input/output schema at time of incorporation]
          provider: [tool provider name or endpoint URI]
          date_confirmed: [YYYY-MM-DD]

  composite_state_hash: [CSH value]
  hash_function: [e.g., sha256]
```

The manifest is stored in the release artifact store, referenced by the deployment record, and indexed by manifest ID and CSH. Both indexes are required: manifest ID for sequential lookup, CSH for incident investigation where the hash is recovered from operational logs before the manifest ID is known.

The manifest must be immutable once filed. If a correction is required, file a new manifest with event type `correction` and reference the manifest ID of the manifest being corrected. Do not overwrite filed manifests.

### CSH Change Event Propagation

When the CSH changes — for any reason, across any component — the change must be propagated to the governance graph node for the agent product. Three propagation paths are defined:

**Planned changes (engineering-initiated):** Engineering changes are initiated through the standard release or maintenance process. The Stage 6 maintenance notification system notifies Stage 5 as part of the maintenance workflow. Stage 5, on accepting the maintenance notification, updates the governance graph node (`current_csh`, the relevant component attribute, and a new `BehavioralStateChange` edge) before the maintenance window closes. The governance graph update is a Stage 5 acceptance condition, not an optional follow-on action.

**Provider-initiated changes (model updates detected by CSH monitoring):** Foundation model updates initiated by the provider are not preceded by an engineering event that can trigger the propagation path above. Instead, an automated CSH monitoring process — operating on the schedule defined in [agent-operations.md](agent-operations.md) — detects the change by recomputing the CSH against the current provider-served model and comparing it to the CSH on record. On detecting a mismatch:
1. The monitoring process creates a `BehavioralStateChange` edge in the governance graph with a `provider-initiated` flag, timestamped to the detection time.
2. The monitoring process simultaneously alerts the system steward and the Stage 5 monitoring function.
3. The governance graph node's `current_csh` and `model_component` attributes are updated by the monitoring process at detection time, not deferred to the next human action.

The detection time is the earliest time at which the governance graph can reflect the change. The actual model update may have occurred earlier — the window between the update and the detection is the unverified exposure window recorded in the `date_confirmed` field of the foundation model component.

**Undetected changes (discovered during incident investigation):** If a CSH change is discovered for the first time during an incident investigation — meaning neither the engineering change path nor the CSH monitoring path captured it — the governance graph node is updated retroactively as part of the incident investigation workflow. The retroactive update must be labeled `retroactive-discovery` in the edge metadata. The investigation report must document the governance gap: the interval between the estimated actual CSH change (derived from monitoring data, deployment logs, or provider information) and the time of the retroactive update. This gap is a governance finding in its own right and must be addressed in the recalibration that follows the incident.

---

## Version History and Audit Trail

Every change to any component that causes a CSH change must be recorded in the version history. The version history is not a narrative log — it is a structured audit trail that answers the question "what changed, when, why, and who authorized it" for every behavioral state transition the agent has undergone.

**Required fields for each version history entry:**

- Previous CSH
- New CSH
- Changed component or components (list all that changed in this event)
- Change description (what changed — e.g., "knowledge base snapshot updated to include Q1 2025 product catalog revision")
- Authorized by: full name and role of the person who authorized this change
- Date and time (UTC)
- Event type: one of `release`, `model-update`, `knowledge-base-update`, `memory-reset`, `recalibration`, `rollback`, `correction`
- Reference: the manifest ID of the composite state manifest filed for this event

Changes to the foundation model that the operator did not initiate — provider-driven model updates detected through monitoring — must still be recorded in the version history. The event type is `model-update` and the authorized-by field records the name of the engineer who detected the change and filed the record, with a note that the change was provider-initiated. The absence of an operator authorization does not mean the absence of a record.

Rollback events record the manifest ID being restored as well as the manifest ID that was active before the rollback. Both CSH values are recorded: the pre-rollback CSH (which is being abandoned) and the post-rollback CSH (which is the restored prior state).

Recalibration events — Stage 6 in the APLC — generate a new manifest covering all components, not just those that changed. After a recalibration, the new CSH reflects a verified, re-evaluated composite state. The recalibration is the occasion for re-confirming every component version identifier, not just the ones that were explicitly updated.

The version history is a compliance record. It must be retained for the same period as the agent product's compliance documentation, as defined in [agent-retirement.md](agent-retirement.md) at Stage 7. For regulated systems, the version history is a primary artifact for regulatory examination — it demonstrates that every behavioral state transition was authorized, recorded, and traceable.

---

## Interaction-Level CSH Tagging

**Requirement.** Every production interaction must be tagged with the CSH active at the time the interaction was processed. This tagging is applied by the agent infrastructure, not by the agent itself, and must be present in the interaction record before the record is written to storage. Interval-based CSH logging — recording the CSH at regular monitoring intervals rather than per interaction — creates a temporal uncertainty window during which a CSH change may have occurred without being attributable to specific interactions. That uncertainty makes precise incident investigation impossible.

**Implementation.** The CSH at interaction time is a metadata field on the interaction record, separate from the interaction content. It does not modify the interaction content or the agent's response. The field records: the CSH value, the timestamp at which the CSH was last confirmed (from the most recent CSH computation event), and a staleness flag if the CSH confirmation timestamp precedes the interaction timestamp by more than the staleness window defined in the behavioral specification.

**Staleness window.** The maximum acceptable gap between the most recent CSH confirmation and the current interaction is defined in the behavioral specification's Layer 3 performance targets. Default maximum staleness: 1 hour for Tier 4 agents; 4 hours for Tier 3; 24 hours for Tier 2 and Tier 1. An interaction processed with a stale CSH tag is still tagged — the staleness is recorded — but triggers a CSH re-computation event immediately.

**Incident investigation benefit.** With per-interaction CSH tagging, incident investigation can determine the exact behavioral state for any specific interaction without temporal reconstruction. The investigation question "what was the agent's behavioral state at the time of this specific interaction?" is answered directly from the interaction record, not inferred from interval logs.

**Audit requirement.** Interaction-level CSH tags are retained for the same period as the interaction records themselves, per the retention policy in Stage 7. They are indexed in the AGKB CSH History (Category D) to enable cross-interaction behavioral state queries.

---

## Incident Investigation Protocol

When a behavioral incident occurs — unexpected outputs, policy violations, performance regressions, safety boundary failures — the composite versioning record is the starting point for investigation.

**Preliminary step: Retrieve the governance graph node.**
Before beginning the composite state differential analysis, retrieve the governance graph node for the incident's agent product and perform three checks:

(a) **CSH consistency:** Confirm that the CSH recorded in the governance graph node (`current_csh`) matches the CSH active in production at the incident time. If they differ, a governance staleness event occurred prior to or concurrent with the incident — the investigation must treat this as a compound finding: the incident itself, plus the governance gap that left the governance graph out of sync with the actual behavioral state.

(b) **Gate pass currency:** Confirm that a gate pass record is linked to the node and that the gate pass is current (i.e., the node has not entered a state that would require re-gating without a corresponding gate pass record).

(c) **Accountable human reachability:** Confirm that an accountable human is assigned to the node and is reachable for incident response coordination.

These checks take under one minute. They surface governance context that shapes the investigation: a governance staleness event means the version history may be incomplete; an unassigned accountable human means escalation paths must be re-established before root cause analysis can proceed. Complete the preliminary step before proceeding to Step 1.

**Step 1: Recover the incident-time CSH.**
The CSH at the time of the incident must be captured from operational logs, monitoring systems, or the deployment record. If the operational monitoring described in [agent-operations.md](agent-operations.md) is correctly configured, the CSH is logged at regular intervals and is recoverable for any incident timestamp. If the CSH is not recoverable from monitoring, the investigation proceeds on best-available information — but the gap in monitoring coverage must be documented and closed.

**Step 2: Retrieve the prior-release CSH.**
The prior-release CSH is the CSH from the most recent composite state manifest filed before the incident occurred. This is the known-good baseline: the behavioral state that was reviewed, evaluated, and authorized at the last release gate.

**Step 3: Diff the two CSH values.**
If the incident-time CSH equals the prior-release CSH, no component changed between the release and the incident. The incident was produced by the same behavioral state that passed the release gate. The investigation shifts to the input space: what prompt, context, or input triggered the unexpected behavior? This is a behavioral evaluation finding, not a versioning finding.

If the CSH values differ, retrieve both composite state manifests and compare component by component. Each changed component is a candidate cause for the behavioral change observed in the incident.

**Step 4: Assess each changed component.**
For each component that changed, assess whether the change could produce the observed behavior:

- Code change: examine the diff for logic changes in the code path exercised during the incident. Was the relevant code path modified? Does the change explain the behavior?
- Prompt change: compare the previous and current prompt. Does the behavioral instruction change explain the output?
- Model change: this is the hardest component to assess, because the operator typically cannot reproduce the prior model behavior if the provider has updated the model. Document the model versions (prior and current), the date of the confirmed change, and any provider changelog information available. If the provider does not expose a changelog, document that limitation.
- Knowledge base change: identify what documents were added, removed, or updated in the relevant snapshot. Does the content change explain a retrieval-based behavioral difference?
- Memory change: examine the memory state at the incident time versus the prior release. For persistent-memory deployments, assess whether accumulated memory context contributed to the behavior.

**Step 5: Reconstruct if possible.**
If it is possible to reconstruct the incident-time composite state in a test environment — restoring the prior code, prompt, model, knowledge base snapshot, and memory state — reproduce the incident scenario. Reconstruction is the strongest form of evidence for root cause attribution.

If reconstruction is not possible (the most common constraint being an unretrievable prior foundation model version), document the limitation explicitly and apply the behavioral evaluation portfolio from [agent-behavioral-evaluation.md](agent-behavioral-evaluation.md) to each changed component variant independently. The goal is to bound the explanation: which changed components could produce the observed behavior, and which could not?

**Step 6: File the investigation report.**
The incident investigation report must include:
- Incident timestamp and description
- Incident-time CSH
- Prior-release CSH
- Component diff (which components changed, what changed)
- Assessed cause (which component or components are assessed as causal, and why)
- Evidence supporting the assessment (reconstruction results, evaluation results, or documented limitations)
- Recommended corrective action
- The manifest ID of the composite state manifest to be filed at the next recalibration or release

The investigation report is attached to the next recalibration record in Stage 6. It is not a standalone document — it feeds the recalibration that restores the agent product to a verified behavioral state. If the incident reveals a gap in the composite versioning record (a component change that was not captured in the version history), closing that gap is a required output of the recalibration.

---

## Governance Graph Integration

The Composite State Hash tracks behavioral identity. The governance graph tracks governance state. These are complementary mechanisms that must be kept in sync. An organization running both has a cross-reference obligation: the governance graph node for an agent product must reflect the current CSH, and the CSH record must be queryable through the governance graph.

### AgentProduct Node Type

Every APLC agent product must have a node of type `AgentProduct` in the governance graph. The node is created at Stage 1 (agent conception) and persists through Stage 7 (retirement). The following node attributes map directly to CSH components:

| Attribute | Content |
|---|---|
| `current_csh` | The CSH currently active in production |
| `release_baseline_csh` | The CSH at the most recent Behavioral Release Gate pass |
| `code_component` | The application code commit hash from the CSH |
| `model_component` | The foundation model provider, model name, and snapshot version from the CSH |
| `prompt_component` | The system prompt version label and content hash from the CSH |
| `knowledge_component` | The knowledge base snapshot ID from the CSH |
| `memory_component` | The memory state content hash, or the literal `stateless` designation, from the CSH |
| `tool_component` | The tool manifest hash, or the literal `stateless-no-tools` designation for non-tool-using agents, from the CSH |

### Evidence Edges from CSH Events

The following CSH events must be recorded as evidence edges on the `AgentProduct` node:

**`BehavioralStateChange` edge:** Created whenever the CSH changes. Connects the prior CSH state to the current CSH state. Required attributes: timestamp of the change event, the component or components that changed, and a `provider-initiated` flag if the change was not engineering-initiated.

**`GatePass` edge:** Created at each Behavioral Release Gate pass. Links the gate record to the `AgentProduct` node. Required attribute: the CSH that was active and evaluated at gate time. This is the authoritative record that `release_baseline_csh` is derived from.

**`BaselineEvidence` edge:** Created when a behavioral baseline is filed. Links the baseline document to the node. The baseline documents the behavioral expectations against which future monitoring and evaluation are measured.

**`AccountabilityAssignment` edge:** Links the named accountable human to the node. Updated at each Stage gate. At any point in time, exactly one `AccountabilityAssignment` edge must be current — there must not be a gap in accountability coverage.

### CSH Change → Governance Graph Update Requirement

When the CSH changes across any component, the governance graph node must be updated. A CSH change that is not reflected in the governance graph within a defined window is a **governance staleness event**:

- Planned changes (engineering-initiated): the governance graph node must be updated within 24 hours of the change taking effect.
- Provider-initiated model updates: the governance graph node must be updated at the time of detection (see CSH Change Event Propagation above). No deferral window applies — detection and governance graph update are the same automated step.

A governance staleness event does not halt operations, but it does mean the governance graph cannot provide a current answer to the questions below, which means the system is not in a governed state by ASDLC operational DoD definition.

### Queryable Governance State

The governance graph must be able to answer the following questions for any APLC agent product at any point in time. If the governance graph cannot answer these questions, the product is not in a governed state.

1. **What is the current CSH and when was it last updated?** — answered by the `current_csh` attribute and the timestamp on the most recent `BehavioralStateChange` edge.

2. **What was the CSH at the most recent gate pass, and which gate?** — answered by the `release_baseline_csh` attribute and the linked `GatePass` edge record.

3. **Has the CSH changed since the last gate pass?** — answered by comparing `current_csh` to `release_baseline_csh`. This is drift detection at the identity level: not a metric deviation, but a direct behavioral state comparison. A non-zero difference means the system is operating in a state that was not evaluated at the gate.

4. **Who is the current accountable human?** — answered by the current `AccountabilityAssignment` edge. If no current edge exists, accountability is unassigned, which is a governance finding.

5. **Are there open waivers on this system, and are they current?** — answered by waiver edges on the node. Expired waivers that have not been renewed are a governance finding.

6. **When was the behavioral baseline last established?** — answered by the most recent `BaselineEvidence` edge timestamp. A baseline that predates the current `release_baseline_csh` indicates the baseline has not been refreshed since the last gate, which may be acceptable or may require review depending on the magnitude of behavioral change between the two CSH values.

---

*The composite versioning model does not prevent behavioral changes caused by components the operator does not control. It makes those changes visible, attributable, and investigable. An agent product operating in production without composite versioning is operating in an unobserved behavioral state — changes accumulate invisibly until an incident reveals them, at which point there is no record to investigate from. The CSH makes the invisible visible. That is its only purpose, and it is a necessary one.*

---

## Behavioral Fingerprint Primitive

The CSH identifies when any component of the Composite Agent State changes, but it cannot localize the behavioral impact of a change. Two CSH values that differ tell you something changed; they do not tell you which behavioral capabilities changed or by how much. The Behavioral Fingerprint Primitive provides a behavioral-level complement to the structural CSH, enabling drift localization — the identification of which specific behavioral dimensions were affected by a component change and whether those dimensions remained within their specification tolerances.

### Behavioral Fingerprint Definition

A behavioral fingerprint is a probe-response vector: a fixed set of carefully designed probe inputs paired with the agent system's recorded responses to those probes at a specific CSH. The fingerprint captures behavioral characteristics across the dimensions defined in the behavioral specification's Layer 2 behavioral coverage evaluation. It is not a metric aggregate — it is a per-dimension record that makes comparison across CSH values tractable at the behavioral contract level, not just at the statistical level.

The fingerprint vector is deterministic on the probe side (the same probes are used for every snapshot) and captures the distribution of the agent's responses on the response side (because agent responses are not deterministic, each probe is run a defined number of times and the response distribution is recorded).

### Fingerprint Probe Design

Fingerprint probes are designed at Stage 2 as part of the behavioral specification, alongside the Layer 2 behavioral coverage evaluation cases. Probe design criteria:

- **Behavioral contract targeting.** Each probe targets a specific behavioral dimension — a single behavioral contract or constraint from the behavioral specification. The mapping from probe to contract is recorded in AGKB and is immutable once the probe set is approved at the Behavioral Specification Gate. A probe whose contract mapping is ambiguous is not a valid fingerprint probe.
- **Stability.** Probes must not be time-sensitive (relying on current events, dates, or externally changing facts) and must not depend on external state (live database queries, real-time retrieval). Probes are synthetic and self-contained. An unstable probe produces fingerprint variation that cannot be attributed to CSH changes.
- **Comparability.** Probe responses must produce outputs that can be compared across fingerprint snapshots using the comparison methods defined below. Probes that produce highly variable free-form text with no comparable structure are valid for coverage evaluation but not for fingerprinting.
- **Coverage.** The probe set covers all behavioral contracts from the behavioral specification at minimum one probe per contract. High-criticality contracts — hard boundaries, safety-relevant constraints — are covered by multiple probes from different approach angles.
- **Boundary inclusion.** Probes include boundary cases that probe behavioral limits, not only normal operation. A fingerprint built exclusively from typical inputs cannot detect behavioral boundary drift.

Probe sets are reviewed at each Stage 2 revision and extended to cover any new behavioral contracts introduced by the revision. Probes are never removed unless the behavioral contract they target has been explicitly removed from the specification — removal of a probe without removal of its contract is a coverage reduction and requires Behavioral Owner authorization.

### Fingerprint Snapshot Protocol

Fingerprint snapshots are taken at defined governance events:

- **Gate events.** Each of the four gates (Conception, Behavioral Specification, Behavioral Release, Operational Readiness) requires a behavioral fingerprint snapshot as part of the gate package. The Behavioral Release Gate snapshot is the release baseline fingerprint and is the reference for all subsequent operational monitoring comparisons.
- **CSH change events.** After every Composite Agent State change that produces a new CSH, a new fingerprint snapshot is taken against the new CSH. The snapshot is taken in a staging environment configured identically to production (same code, prompt, model, knowledge base, and memory state) before the change is deployed to production. This sequence — fingerprint before production deployment — enables a pre/post comparison to confirm the expected behavioral impact before users are exposed.
- **Periodic monitoring snapshots.** During Stage 5 operations, fingerprint snapshots are taken at the cadence defined in [agent-operations.md](agent-operations.md). Periodic snapshots detect behavioral drift that the CSH does not capture: drift within a stable component (model output variance, knowledge base retrieval variance) rather than drift caused by a component change.
- **Post-incident snapshots.** After any behavioral, safety, or adversarial incident is declared under the Stage 5 incident management protocol, a fingerprint snapshot is taken as part of the incident forensic record. The post-incident snapshot is compared to the pre-incident baseline to characterize the behavioral state at the time of the incident.

### Fingerprint Comparison

Fingerprint comparison computes the behavioral delta between two snapshots taken at different CSH values or at different points in time under the same CSH. The comparison produces a per-probe-dimension delta, not a single aggregate score — aggregate scores mask localized drift.

**Comparison methods, applied in combination:**

- **Semantic similarity.** Embedding distance between corresponding response distributions across snapshots. High embedding distance on a probe indicates the response character changed significantly; low distance indicates the response is stable. Semantic similarity is the broadest-coverage method — it catches changes in content, tone, and structure simultaneously — but is the least precise in attributing drift to a specific behavioral contract violation.
- **Rubric scoring.** Applying the behavioral evaluation rubrics from [agent-behavioral-evaluation.md](agent-behavioral-evaluation.md) to each probe response in both snapshots, computing the score delta per rubric dimension. Rubric scoring is the most precise method for attributing drift to a specific behavioral specification clause.
- **Categorical classification.** Classifying each response into behavioral categories defined in the behavioral specification (e.g., complies / soft-boundary-activates / hard-boundary-triggers / out-of-scope-deflects), computing the distribution shift across categories between snapshots. Distribution shift in hard-boundary-triggers is a Critical finding regardless of its magnitude.

The combination of methods is required because no single method is sufficient: semantic similarity catches broad changes that rubric scoring may miss if the rubric dimensions are narrowly defined; rubric scoring localizes findings that semantic similarity identifies but cannot attribute; categorical classification detects boundary behavior changes that are invisible to distance-based methods when the response text is superficially similar.

### Drift Localization

When a CSH change or periodic monitoring snapshot reveals a behavioral delta, fingerprint comparison localizes the drift before any recalibration action is taken. Drift localization answers:

- Which probe dimensions show the largest response delta between the two snapshots?
- Which behavioral contracts (mapped through the probe-to-contract registry in AGKB) are most affected?
- Is the drift within the tolerance defined for those contracts in the behavioral specification, or does it exceed the drift threshold?
- Is the drift directional — systematically shifting the behavioral boundary in a single direction — or variance-driven — increasing response variance without a systematic shift?

Directional drift toward behavioral boundary violations is a higher-severity finding than variance-driven drift, because directional drift indicates a systematic behavioral change rather than increased output variability. Drift localization findings feed directly into the recalibration root cause analysis in [agent-maintenance.md](agent-maintenance.md).

### Fingerprint as Gate Artifact

At the Behavioral Release Gate, the fingerprint snapshot is a required gate artifact. The release baseline fingerprint is stored in AGKB linked to the composite state manifest filed at the gate, and is used as the reference for all subsequent operational monitoring comparisons and for every post-CSH-change comparison during Stage 6 maintenance.

A Behavioral Release Gate package that does not include a fingerprint snapshot is incomplete. The gate cannot close without a baseline fingerprint on record, because Stage 5 monitoring cannot establish drift thresholds and Stage 6 cannot perform pre/post change comparisons without a validated baseline to compare against.

---

## Memory State Snapshot Policy

Memory state is the most dynamic component of the Composite Agent State. Unlike application code, system prompt, foundation model, and knowledge base — which change only at defined maintenance events — persistent memory state evolves continuously during operation as the agent accumulates interaction context. This continuous evolution creates a governance challenge: the CSH, which captures the memory state as one of its six components, cannot be recomputed at every interaction without making CSH computation impractical. The Memory State Snapshot Policy governs when memory state is captured for governance purposes, what that snapshot must contain, and how snapshots are retained.

### Snapshot Trigger Conditions

Memory state snapshots are taken at defined governance events:

- **Gate events.** All four gates require a memory state snapshot as part of the gate artifact package. The snapshot is taken immediately before the gate closes, capturing the memory state in the environment being gate-reviewed.
- **CSH computation events.** Whenever a CSH is formally computed for inclusion in a composite state manifest, the memory state is snapshotted as part of the CSH computation inputs. The snapshot and the CSH are filed together — a CSH whose memory component cannot be reconstructed from a stored snapshot is an unverifiable CSH.
- **Incident events.** At the point of incident declaration under the Stage 5 incident management protocol, the memory state is snapshotted as part of the forensic record. The incident-time memory state snapshot is linked to the incident report in AGKB.
- **GDPR erasure events.** A memory state snapshot is taken immediately before erasure execution and immediately after verification. The pre-erasure snapshot documents what personal data was present; the post-erasure snapshot confirms the audit result. Both snapshots are linked to the GDPR erasure intake record (see [agent-maintenance.md](agent-maintenance.md) — GDPR Memory Erasure Protocol).
- **Scheduled intervals.** A configurable periodic snapshot cadence is defined at Stage 2 for longitudinal memory drift monitoring. The cadence is determined by the deployment's memory accumulation rate and the risk profile of memory-driven behavioral change.

### Snapshot Content

A memory state snapshot captures a representation of the memory state sufficient for the governance purposes listed above, while complying with data minimization requirements. The snapshot must not be the full memory state if the full memory state contains personal data in excess of what governance requires. Instead, the snapshot captures:

- **Memory state size and structure.** Record count by memory category, total size in storage units, memory schema version.
- **Privacy-safe summary statistics.** Aggregate statistics (item age distribution, category distribution, recency distribution) that characterize the memory corpus without exposing individual items.
- **Personal data presence flag.** A boolean flag per memory category indicating whether personal data is present in that category at the time of snapshot, based on the data category assessment filed at Stage 2.
- **Privacy-preserving hash.** A hash of the full serialized memory state for structural comparison purposes. The hash enables confirmation that two snapshots represent the same memory state without requiring the full contents to be compared.
- **Full content capture for GDPR erasure events.** For erasure-triggered snapshots only, a complete capture is required for audit purposes, subject to appropriate access controls. Erasure audit snapshots are stored under the access control tier applicable to personal data and are not accessible as general governance artifacts.

### Memory State Versioning

Memory state snapshots are stored in AGKB as versioned records linked to the CSH at the time of snapshot. The linkage is bidirectional: the CSH record identifies the memory state snapshot used as its memory component, and the memory state snapshot record identifies the CSH it contributes to. This bidirectional linkage enables reconstruction of the full Composite Agent State at any historical governance event from either direction — from a known CSH to its component snapshots, or from a known memory state snapshot to the CSH it produced.

Memory schema versions are tracked separately from content snapshots, consistent with the Component Version Identifiers section above. A memory schema migration event requires a snapshot of both the pre-migration and post-migration memory state, even if the content is semantically identical after migration. Schema changes can alter the agent's interpretation of its own memory; the pre/post snapshot pair documents that the migration was verified.

### Memory State Growth Governance

Unconstrained memory growth is both a performance risk and a governance risk. A growing memory corpus increases the personal data exposure surface, increases the computational cost of erasure operations, and increases the probability that memory content will accumulate adversarially introduced patterns that are too diffuse for the memory review process to identify.

Memory state size is monitored as a governance metric alongside behavioral quality metrics. The behavioral specification must define a maximum memory state size per memory category, expressed in terms that can be monitored — record count, storage size, or both. The maximum is a data minimization constraint: memory that exceeds what is necessary for behavioral quality at the specified interaction volume is not permitted to accumulate.

Exceeding the maximum size threshold for any memory category triggers a Knowledge Staleness Sentinel alert (see [agent-maintenance.md](agent-maintenance.md) — Knowledge Staleness Sentinel) and a memory governance review. The review determines whether the excess results from a higher-than-anticipated interaction volume (the maximum should be revised at Stage 2), from retention policy non-compliance (memory items that should have expired were not removed), or from a memory write policy defect (the agent is writing memory items at a higher rate than intended). Each root cause has a different governance response.

### Memory Isolation in Multi-Tenant Deployments

In multi-tenant deployments — where a single agent system serves multiple tenants and maintains per-tenant persistent memory — each tenant's memory state must be strictly isolated from every other tenant's memory state. Isolation means:

- A tenant's memory items are only accessible in sessions authenticated to that tenant
- Memory writes from one tenant's sessions cannot propagate to another tenant's memory partition
- Aggregate or cross-tenant learning is not permitted unless explicitly authorized in the behavioral specification's Layer 4 adaptation scope with the privacy requirements from [agent-behavioral-specification.md](agent-behavioral-specification.md) fully satisfied

Memory isolation is verified at the Operational Readiness Gate before the agent enters production in a multi-tenant configuration. Isolation verification requires an adversarial test: an attempt to read or influence one tenant's memory state from a session authenticated to a different tenant. This test is part of the Layer 3 adversarial evaluation portfolio for multi-tenant deployments.

Cross-tenant memory contamination — a confirmed instance of one tenant's memory content being accessible or influential in another tenant's sessions — is a behavioral incident of the adversarial class and is managed under the Stage 5 adversarial incident response protocol. It is not a data breach response protocol matter exclusively: the behavioral specification was violated (memory isolation is a hard constraint), so the behavioral incident protocol applies in parallel with any data protection incident response required by the deployment's regulatory classification.
