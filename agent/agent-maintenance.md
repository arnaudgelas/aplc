# Stage 6 — Maintain: Agent Maintenance Governance

*Stage 6 document of the Agentic Product Lifecycle. Governs ongoing maintenance of deployed agent products, running concurrently with Stage 5. Audience: platform engineers, product owners, operations leads.*

See [aplc.md](../aplc.md) for the lifecycle overview.
See [agent-operations.md](agent-operations.md) for Stage 5, which runs concurrently.
See [agent-composite-versioning.md](agent-composite-versioning.md) for the composite state manifest that all Stage 6 events update.
See [agent-behavioral-specification.md](agent-behavioral-specification.md) for the specification that recalibration must restore.
See [agent-behavioral-evaluation.md](agent-behavioral-evaluation.md) for the evaluation portfolio that gates every recalibration.

---

## What is Stage 6 — Maintain?

Stage 6 runs concurrently with Stage 5 from the moment the agent enters production. Maintenance for an agent product is not patch management for static software — it is the ongoing governance of a system that changes on five dimensions simultaneously, only one of which the operator controls. The foundation model changes when the provider decides to update it. The knowledge base drifts as the world changes and documents are added, revised, or removed. Memory accumulates as users interact and the agent learns from them. The input distribution shifts as the user population changes or as the agent's role evolves. Only the application code and system prompt are directly under the operator's control, and even those change through legitimate maintenance interventions that carry behavioral risk. The goal of Stage 6 is not to prevent change but to ensure that every change keeps the agent within its behavioral specification, and that changes the operator did not initiate are detected, assessed, and accepted or rejected with evidence. An agent product without Stage 6 governance is not in controlled operation — it is drifting.

---

## Stage 5/6 Concurrency Interface — Stage 6 Obligations

Stage 5 and Stage 6 run concurrently from the moment the agent enters production, but concurrency without coordination is not governance — it is two teams independently observing the same system without a shared frame of reference. This section defines the Stage 6 side of the concurrency interface: the obligations Stage 6 must fulfil so that Stage 5 monitoring remains coherent and so that the two stages function as a single governed system rather than parallel independent activities.

### Maintenance Notifications

Before executing any planned composite state change — model update acceptance, knowledge base refresh, recalibration deployment, memory reset, or any other event that generates a new CSH — Stage 6 must file a *maintenance notification* artefact with Stage 5. The notification is not a courtesy; it is a governance pre-condition for the change. A composite state change executed without a filed maintenance notification is an ungoverned change from Stage 5's perspective, regardless of how thoroughly Stage 6 evaluated it.

The maintenance notification must contain:

- **Change type.** The category of the composite state change: model update acceptance, knowledge base snapshot, prompt recalibration, memory reset, fine-tuning deployment, or other (with description).
- **CSH components affected.** The specific components of the composite state that will change, and the before/after component identifiers where known.
- **Expected behavioral impact.** A specification of what behavioral metric changes Stage 5 monitoring should expect to observe following the change: which metrics, expected direction and approximate magnitude, and expected stabilisation timeframe. If no behavioral impact is expected, the notification must say so explicitly — "no expected behavioral impact" is a claim that Stage 5 will verify.
- **New comparison baseline.** The post-change behavioral baseline that Stage 5 monitoring must use as its reference point after the change is deployed. Stage 5 cannot continue using the pre-change baseline to detect drift after a governed composite state change; the maintenance notification provides the new baseline against which post-change drift detection operates.

The maintenance notification is filed in the Stage 5 monitoring system as a record, not sent informally. The filing timestamp is the governance record that the notification preceded the change.

### Unexpected Deviation After Maintenance

When Stage 5 detects a behavioral deviation following a composite state change, the first question is whether the deviation was predicted by the maintenance notification. If the deviation falls within the expected behavioral impact range stated in the notification, Stage 5 monitors it as expected change stabilising. If the deviation exceeds or differs qualitatively from what the notification predicted, Stage 5 signals an *unexpected post-maintenance deviation*.

An unexpected post-maintenance deviation is not solely a Stage 5 incident response matter. It triggers a mandatory Stage 6 post-change review: Stage 6 must investigate why the deployed change produced behavioral effects that its own pre-deployment evaluation did not predict. The Stage 6 post-change review is separate from and in addition to the Stage 5 incident response — Stage 5 manages the operational response while Stage 6 investigates the evaluation failure that allowed the unpredicted deviation.

The outcome of the Stage 6 post-change review must be recorded in the composite state version history and must address: what the evaluation missed, whether the evaluation portfolio needs to be augmented for future changes of this type, and whether the deployed change requires rollback or recalibration.

### Stage 6 Backlog Visibility

The Stage 6 maintenance backlog — the ordered queue of planned composite state changes, recalibration work, knowledge base updates, and model update assessments — is a governed record visible to Stage 5 monitoring operations. Stage 5 operators must have read access to the scheduled Stage 6 activities so they can interpret monitoring signals against the planned change calendar.

A spike in a behavioral metric that coincides with a scheduled knowledge base refresh is not the same signal as a spike with no corresponding planned change. Stage 5 cannot contextualize its monitoring signals without visibility into Stage 6's change schedule. The Stage 6 maintenance backlog is not internal engineering planning; it is an operational record that Stage 5 depends on.

---

## Foundation Model Update Governance

Foundation model updates are the most distinctive maintenance challenge for agent products. They are also the one most easily missed: a provider model update can change agent behavior without any operator action, without any change to any component the operator controls, and sometimes without any notification that a change has occurred. The composite versioning model in [agent-composite-versioning.md](agent-composite-versioning.md) makes these changes visible by detecting CSH changes between monitoring windows; this section defines what to do when they are detected.

### Update Detection

Subscribe to all provider update notification channels for every model provider used in any deployed agent product — release notes, status pages, developer mailing lists, and any provider-specific monitoring APIs that surface model version information. This subscription must be a named operational responsibility, not an implicit assumption that engineers will notice.

For each deployed agent product, the composite state manifest records the foundation model component with a `date_confirmed` field — the date on which the model version was last verified to be the version currently served by the provider. The gap between `date_confirmed` and today is the window of unverified exposure to a silent model update. For deployments where behavioral consistency is critical — regulated systems, high-risk EU AI Act systems, consumer-facing deployments with significant user populations — the `date_confirmed` field must be refreshed at least weekly by verifying the model version through the provider's API or documentation. For lower-risk deployments, monthly confirmation is the minimum.

When a provider update notification is received, the immediate assessment question is: does this update affect any component of any deployed agent product's composite state? Map the notified model name to every composite state manifest that references it. Every affected deployment must enter the model update governance procedure regardless of the apparent scope of the provider's change description. Provider change descriptions are written for the general developer audience, not for the specific behavioral envelope of your agent product. A change described as "minor safety improvements" may have material effects on refusal rates or response patterns in your deployment context.

A CSH change detected in operational monitoring that corresponds to no operator-initiated change is a silent model update until proven otherwise. Investigate immediately using the incident investigation protocol in [agent-composite-versioning.md](agent-composite-versioning.md). Do not assume the CSH change is a monitoring artifact; assume it is a real behavioral state change and require evidence to close the assumption.

**Behavioral probe-based detection for silent behavioral updates.** The `date_confirmed` field and CSH monitoring address silent model updates that change the model identifier. They do not address updates that change the model's behavior without changing its identifier — a documented practice with hosted AI models. For these updates, behavioral probe-based detection is required as a supplementary control.

Weekly, execute the sentinel probe set (a designated 20-probe minimum subset of the behavioral fingerprint probe set) against the live production model. The sentinel probe set is designated at Stage 2 in the behavioral specification and is selected to maximize sensitivity to behavioral changes across: hard boundary compliance, uncertainty expression calibration, persona consistency, and the use cases most critical to the agent's specification. Probe responses are compared against the release baseline fingerprint. A shift in the response distribution for any probe that exceeds the drift threshold defined in the behavioral specification is treated as a probable silent model update.

When a behavioral probe detection alert fires without a corresponding CSH change: (1) treat the alert as a probable provider-initiated behavioral update; (2) immediately run the full Layer 2 and Layer 3 behavioral evaluation portfolio against the current model; (3) if the portfolio reveals behavioral changes outside the specification, initiate the rejection procedure, including consideration of model pinning to the last confirmed behavioral state; (4) file a model update record in the version history with event type `model-update`, `provider-initiated` flag, and a note that the update was detected by behavioral probing rather than CSH monitoring; (5) update `date_confirmed` to reflect the probe date.

The weekly probe cadence is a minimum. For Tier 4 agents, daily sentinel probe execution is required.

### Behavioral Regression Testing

For every notified model update affecting a deployed agent product, run the full behavioral evaluation portfolio against the updated model before accepting the update in production. This is not optional for agent products — it is the only mechanism available for determining whether a provider update has changed behavior within or outside the behavioral specification. There is no diff to read. There is no code change to inspect. There are only the evaluation results, and without them the operator has no basis for the accept/reject decision.

The evaluation portfolio to run is the full four-layer portfolio defined in [agent-behavioral-evaluation.md](agent-behavioral-evaluation.md): Layer 1 (functional coverage), Layer 2 (behavioral specification coverage), Layer 3 (adversarial and red-team), and Layer 4 (cross-session and memory behavior). Do not reduce the evaluation scope on the grounds that the model update is "minor." Minor in the provider's classification does not mean minor in the context of your behavioral specification.

For deployments with high interaction volumes that make full evaluation impractical before every minor model update, define a tiered evaluation approach at deployment time: a fast-path evaluation covering the highest-risk behavioral specification elements (Layer 1 core use cases, Layer 2 hard boundary compliance, Layer 3 known adversarial vectors) and a full-path evaluation run before any update is formally accepted. The fast-path gates whether an update can proceed to a canary deployment; the full-path gates acceptance in production. This tiered approach is acceptable only if both tiers are defined, documented, and resource-confirmed before the agent enters production.

### Accept/Reject Decision

The decision to accept a model update in production belongs to the product owner and accountable human, not the engineering team. Engineering presents the evaluation results; product and accountability make the decision. The criteria:

All four evaluation portfolio layers pass, or any deviations are within the acceptable tolerance documented in the behavioral specification's Layer 3 performance targets. "Acceptable tolerance" must be specified at Stage 2 or Stage 3 — it is not a judgment call made at decision time. A deviation that was not covered by a pre-committed tolerance level is a deviation that requires explicit product owner and accountable human acceptance, with the acceptance recorded.

No new red-team findings triggered by the updated model that were not present in the pre-update evaluation. New adversarial vulnerabilities opened by a model update are not minor concerns — they are new attack surfaces that require the Stage 3 red-team protocol to address before production acceptance.

The behavioral baseline delta is documented. Even when the update passes all gate conditions, the new behavioral baseline — the metric values at which the updated model was accepted — must be recorded in the composite state manifest and version history. The post-update baseline replaces the prior baseline as the reference point for Stage 5 drift detection.

**"Accepted" defined.** A foundation model update is "accepted" only when: (a) the regression test suite passes against the updated model, AND (b) a new behavioral baseline is established that records the behavioral metric values at which the updated model was accepted. An update deployed without a new baseline is not accepted — it is an ungoverned change. The acceptance date is the date on which both conditions are confirmed, not the date on which the update was first deployed to any environment.

### Rejection Procedure

When a model update fails the acceptance criteria, the operator must maintain behavioral specification compliance on the prior model version. Two paths are available, and both must be assessed in parallel during the rejection period:

**Provider model pinning.** If the provider offers a mechanism to pin to a specific model snapshot, engage it immediately upon rejection decision. Record the pinned version in the composite state manifest. Pinning is a temporary measure — providers deprecate prior model versions on defined schedules, and a pinned version will eventually be unavailable. Track the deprecation timeline and treat the expiry date as a hard deadline for completing either an updated evaluation that accepts the new model or a migration to an alternative model that passes evaluation.

**Prompt mitigation.** A targeted prompt adjustment that restores behavioral specification compliance on the updated model without pinning. This path requires behavioral evaluation re-run (minimum Layers 2 and 3) to confirm the mitigation works. A prompt mitigation that has not been evaluated is a guess, not a fix. The mitigation is a temporary measure — the underlying model update has changed behavior, and the prompt is compensating for it. Compensatory prompts accumulate technical debt in the system prompt and should be resolved at the next recalibration cycle.

Both the rejection decision and the mitigation path chosen are recorded in the composite state manifest version history with event type `model-update` and a clear notation that the update was rejected and the mitigation applied. This record is a compliance artifact for regulated deployments — it demonstrates that the operator assessed the model update and took a deliberate, governed action rather than allowing an unreviewed change to affect the agent's behavior.

### Emergency Rollback for Model Updates

If a model update is accepted and subsequently causes a behavioral incident in production, treat it as a behavioral incident under the Stage 5 incident management protocol. The model component is the candidate causal change; the rollback path is to reinstate the prior pinned version (if the provider permits) or to apply a prompt mitigation while a replacement evaluation proceeds. Record the rollback in the version history with event type `rollback`, referencing both the pre-rollback and the restored CSH values.

---

## Behavioral Recalibration

Recalibration is the Stage 6 process for restoring the agent to its behavioral specification when drift has moved it outside that specification and rollback is not the appropriate response. Rollback restores a prior composite state; recalibration creates a new composite state that is specification-compliant. The distinction matters: rollback removes a change; recalibration governs a change through the evaluation and release gate.

### Trigger Conditions

Recalibration is initiated when any of the following conditions is confirmed:

**Out-of-spec behavioral drift with identified root cause.** Drift has moved a behavioral quality metric outside the specification envelope, the root cause is identified, and the root cause requires a change to one or more composite state components rather than a rollback. Drifts caused by knowledge base staleness, memory accumulation, or specification misalignment typically require recalibration rather than rollback, because the prior state was not wrong — the current state has become inadequate relative to a changed world or a changed user need.

**Quality SLO breach sustained beyond threshold.** The output quality SLO has been breached and the breach has persisted beyond the threshold period defined in the behavioral specification. The threshold must be pre-committed: if the SLO breach threshold is assessed after the breach is observed, it is not a threshold.

**HITL override rate exceeding threshold.** The human reviewer override rate on quality review samples has exceeded the pre-committed threshold for a defined period. A high HITL override rate that persists indicates that the agent is consistently producing responses that informed reviewers judge to be wrong or out-of-spec — a behavioral specification failure that recalibration must address.

**Behavioral specification revision.** Stage 5 or HITL review has identified that the behavioral specification itself is wrong or outdated. A recalibration triggered by a specification revision must begin with the Stage 2 revision before any technical intervention. Changing the agent's behavior to match a revised specification that has not been formally updated is a governance bypass; it disconnects the agent's behavior from the single-source document that all downstream stages depend on.

### Recalibration Methods

**Prompt adjustment.** The lowest-cost intervention and the appropriate first response when the root cause is a mis-specification in the system prompt, a prompt that has degraded in effectiveness against the current model version, or a specification clarification that can be expressed in the agent's instructions. Prompt adjustment requires behavioral evaluation re-run at minimum Layers 2 and 3 from [agent-behavioral-evaluation.md](agent-behavioral-evaluation.md), and red-team clearance confirming that the adjusted prompt has not opened new adversarial vulnerabilities. Prompt adjustment changes the system prompt component of the composite state and generates a new CSH. It does not require the full Stage 3 evaluation cycle unless the adjustment is substantive enough to affect the agent's behavior across a broad range of use cases — in which case it is effectively a re-specification and should be treated as one.

**RAG and knowledge base update.** Addresses behavioral drift caused by knowledge staleness: the agent is producing outdated, incorrect, or incomplete answers because its retrieved knowledge has not been updated to reflect changes in the world, the product, or the regulatory environment. A knowledge base update requires: identification of the specific content categories causing the staleness, document review and update by the appropriate content owner, evaluation re-run covering the affected content areas (minimum Layer 1 for the use-case zones affected by the updated content, Layer 2 if the update touches content categories that interact with behavioral boundaries), and a new knowledge base snapshot ID in the composite state manifest. A knowledge base update that has not been evaluated for behavioral impact before production application is an unreviewed change — the same governance standard that applies to code changes applies here.

**Fine-tuning.** The highest-cost, highest-impact recalibration method. Fine-tuning changes the model's behavior at the weights level — it is not a prompt or knowledge change, it is a change to the model component of the composite state. Fine-tuning requires the full Stage 3 evaluation cycle before production application: all four layers of the evaluation portfolio, the full red-team protocol, and a new behavioral baseline document. The fine-tuned model is treated as a new model version for composite state purposes — it receives a new model identifier in the composite state manifest. Fine-tuning should be reserved for cases where prompt adjustment and knowledge base updates are insufficient, because the evaluation overhead is significant and the behavioral impact is harder to predict and isolate than for the other recalibration methods. Manifesto P12 applies with full force: fine-tuning decisions require accountable human authorization and a documented rationale.

**Behavioral specification revision.** When the specification itself is wrong or outdated — not the agent's implementation of it, but the specification — the first step is always a Stage 2 revision, not a technical change. Only after the revised specification is reviewed and approved does the engineering team determine which recalibration method implements the specified change. This order is not negotiable: a behavioral change that precedes its specification revision has no governance basis. It may be the right change; it is still an unreviewed change until the specification confirms it.

### Recalibration Gate

Before any recalibration change is deployed to production, it must pass a recalibration gate. The gate is a subset of the behavioral release gate defined in [agent-release-governance.md](agent-release-governance.md), scaled to the scope and impact of the recalibration:

**Minimum gate conditions for any recalibration:**

1. Layer 2 behavioral coverage evaluation (behavioral specification compliance) must pass at or above the release baseline level.
2. Layer 3 adversarial evaluation must pass with no new findings relative to the current production baseline.
3. A new behavioral baseline document must be produced, recording the post-recalibration behavioral metric values that will become the new Stage 5 drift detection reference.
4. The composite state manifest must be updated with all changed component versions and the new CSH.
5. The product owner and accountable human must sign off on the recalibration gate assessment.

A recalibration that passes engineering tests but has not been evaluated for behavioral impact is an untested change. The framing "we verified the code works, we did not have time to re-run behavioral evaluation" is not a recalibration gate pass — it is a request to bypass the gate. Bypassing the recalibration gate is acceptable only under conditions equivalent to the ASDLC's emergency change procedure: immediately followed by post-hoc evaluation within 48 hours, with the behavioral risk of the gap explicitly accepted by the accountable human and documented in the version history.

**"Closed" defined.** A Stage 5 quality incident that triggers Stage 6 recalibration is "closed" only when all four of the following conditions are confirmed: (a) the recalibration is deployed to production, (b) a behavioral evaluation re-run confirms that the targeted behavior is within specification post-recalibration, (c) the behavioral baseline is updated in the composite state manifest to reflect the recalibrated state, AND (d) Stage 5 monitoring thresholds are confirmed appropriate for the recalibrated agent — specifically, that the thresholds account for any behavioral metric shifts the recalibration intentionally produced. A recalibration deployed without confirmation of (b), (c), and (d) is not closed; it is a recalibration whose effectiveness is unknown. The incident remains open until all four conditions are met and recorded.

---

## Knowledge Base Maintenance

RAG content becomes stale. Regulatory documents change without warning. Product documentation is updated outside the agent team's review cycle. Market data becomes outdated the moment it is published. Knowledge base maintenance is not a one-time activity at deployment — it is a continuous governance obligation that begins in Stage 6 and runs until the agent is retired.

### Content Review Cadence

Define content review cadence by content category at Stage 2 in [agent-behavioral-specification.md](agent-behavioral-specification.md), before the agent enters production. The review cadence is a behavioral specification decision because it directly determines how current the agent's retrieved knowledge is — a decision with product, compliance, and safety implications.

Recommended minimum cadences by category:

| Content Category | Review Trigger |
| --- | --- |
| Regulatory and compliance documents | Review on each relevant regulatory update; monitor official regulatory update channels |
| Legal terms and policy documents | Review on each document revision; version control the source documents |
| Product documentation | Review quarterly at minimum; review immediately on product change announcements |
| General reference knowledge | Review annually; flag for immediate review if content area is subject to significant change events |
| Training and calibration examples | Review when behavioral drift is detected in the relevant use-case zone |

Cadence is a minimum, not a ceiling. A content category that is known to change frequently should have a review cadence shorter than the recommended minimum. A content category that serves a safety-critical use case should have continuous monitoring, not periodic review.

### Content Addition Process

Adding documents to the knowledge base changes the agent's behavior on every topic covered by the new documents. This is a behavioral change and requires the same evaluation discipline as any other behavioral change.

New documents added to the knowledge base must be reviewed for behavioral impact before production addition: do the documents cover topics where the agent currently has a behavioral specification constraint? Do they introduce claims that conflict with existing knowledge base content? Do they extend the agent's effective scope into areas not covered by the behavioral specification?

A content addition that passes editorial review (the content is accurate, relevant, and appropriate) but has not been evaluated for behavioral impact may still produce behavioral changes the product owner did not intend. Run at minimum a Layer 1 evaluation focused on the use-case zones most likely to retrieve the new content before adding it to production.

Each version of the knowledge base has a snapshot identifier in the composite state manifest, a document count, and a source manifest hash. Every content addition must generate a new snapshot, a new manifest entry, and a new CSH. Content additions are component changes and must be recorded in the version history with the standard required fields.

### Knowledge Base Integrity Verification

Knowledge base content must not only be versioned (to detect what changed) but verified (to detect whether content has been tampered with since ingestion).

**At ingestion.** Every document added to the knowledge base is assigned a content hash at the time of ingestion: `document_hash = SHA-256(canonical_document_content)`. This hash is stored in the Knowledge Source Registry alongside the document identifier, source version, and ingestion timestamp. The canonical document content is the full document text in a defined canonical form (whitespace-normalized, metadata stripped) to ensure hash stability across minor formatting changes.

**At retrieval.** When a document is retrieved for inclusion in the agent's context, the retrieval infrastructure recomputes the document hash and verifies it against the stored ingestion hash. A mismatch means the document has been modified since ingestion — either through a legitimate update (which should have been recorded as a new document version with a new hash) or through unauthorized modification.

**On hash mismatch.** A retrieval integrity failure (hash mismatch) is treated as a behavioral incident of the Adversarial class. The specific response: (1) the document is excluded from the retrieval result and replaced with a staleness notification in the agent's context; (2) the retrieval integrity failure is logged to AGKB as an incident record; (3) the product owner and Technical Owner are notified within 1 hour; (4) the knowledge base is taken offline for the affected document categories pending investigation of whether the modification was authorized, unauthorized, or erroneous.

**Integrity verification in the composite state manifest.** The `source_manifest_hash` field in the knowledge base component of the composite state manifest captures the document list — it does not capture per-document content integrity. The per-document content hashes are stored in the Knowledge Source Registry. Both records are required: the source manifest hash confirms the scope of the knowledge base; the per-document hashes confirm the content has not been modified. A composite state manifest without corresponding per-document hashes in the Knowledge Source Registry is incomplete from an integrity perspective.

### Knowledge Base Version Control

The composite state manifest records the knowledge base snapshot ID and source manifest hash, providing point-in-time reconstruction. But the version history of the knowledge base itself — the ordered record of what was added, removed, or modified, by whom, and why — must be maintained in the knowledge base management system, not reconstructed from composite state manifests.

Maintain a knowledge base change log with an entry for every content operation: document ID, operation type (add/update/remove), content owner, date, justification, and the composite state manifest ID filed at this change. The change log is the audit trail for knowledge base governance. Without it, a behavioral incident traced to a knowledge base change cannot be fully investigated — the investigator can determine that the knowledge base changed (from the CSH diff) but cannot determine what changed without the change log.

Content removal governance applies the same evaluation standard as content addition. Removing content is a behavioral change: the agent will no longer retrieve the removed content, which may change its answers on the relevant topics. A content removal that is not evaluated for behavioral impact may create knowledge gaps that are not immediately visible in quality metrics but surface in specific use-case scenarios after the removal.

### Staleness Monitoring

In addition to scheduled content review, monitor for staleness signals in operational data: HITL overrides where the reviewer's correction indicates the agent cited outdated information, user escalations where the stated reason is incorrect or outdated information, and automated fact-checking alerts where configured.

A staleness signal should trigger an unscheduled review of the relevant content category, not wait for the next scheduled review. Scheduled reviews exist for content that is not signaling staleness through operational data; operational signals override the schedule.

---

## Memory Governance

Accumulated memory biases future behavior. An agent that has learned from thousands of interactions carries patterns from those interactions — some of which improve its behavior (learned user preferences, useful heuristics, refined understanding of the operational context) and some of which degrade it (outdated assumptions, adversarially introduced preferences, shortcuts that violate soft boundaries). The passage of time does not distinguish between useful and problematic memory. Memory governance does.

Manifesto P6 establishes the memory governance requirements for agent products. This section operationalizes P6 for Stage 6 maintenance.

### Memory Review Cadence

Conduct periodic inspection of accumulated memory for patterns inconsistent with the behavioral specification. The review cadence should be defined at Stage 2 based on the deployment's memory accumulation rate and the risk profile of memory-driven behavioral bias:

- High-interaction-volume deployments (thousands of interactions per day): monthly memory review
- Moderate-interaction-volume deployments: quarterly memory review
- Low-interaction-volume deployments: review triggered by behavioral drift detection or at each recalibration event

The memory review is not a full audit of every memory item. It is a structured sample inspection: draw a representative sample of accumulated memory items across categories (user preferences, learned heuristics, conversation summaries, any other memory types defined in the memory schema) and assess each sampled item against the behavioral specification. The assessment questions for each item:

- Is this memory item consistent with the Layer 2 soft boundaries in the behavioral specification? Could this item lead the agent to behave in a way that a soft boundary disallows in the default configuration?
- Does this item reflect genuine user preference or need, or does it show patterns consistent with adversarial manipulation (preferences that systematically lower the agent's thresholds, heuristics that route the agent toward out-of-scope behavior)?
- Is this item still current? Information that was accurate when learned may now be outdated.
- Is this item within the domain scoping defined in the behavioral specification — scoped to the appropriate principal, use case, and context?

Sample size for the review must be large enough to be statistically meaningful given the total memory corpus size. Define the sample size methodology at Stage 2.

### Memory Reset Policy

A memory reset returns the agent to a defined initial state by removing some or all accumulated memory. Resets are governed interventions, not routine maintenance operations.

**Full reset.** Returns the agent to its initial deployed state: the memory state as it was when the Stage 4 release gate closed. A full reset erases all learned context, including context that improves the agent's performance for established users. Full resets are warranted when: the memory corpus is found to contain widespread adversarially introduced patterns during a memory review; a behavioral incident investigation attributes out-of-spec behavior to memory accumulation and the affected patterns cannot be identified for selective removal; or the memory schema is being migrated to a new version where the prior content cannot be reliably translated.

**Partial reset.** Removes specific memory items or categories that have been identified as problematic during a memory review, while preserving the rest of the memory corpus. Partial resets are the preferred intervention when the problematic patterns are identifiable and isolated — they minimize the behavioral disruption of losing accumulated useful context. Partial resets require the same governance rigor as full resets: the items to be removed must be identified and documented, the removal must be authorized by the product owner, and the post-reset memory state must be captured in the composite state manifest.

**Both types of reset require behavioral evaluation re-run after the reset.** Memory is a component of the composite state. A composite state change — even one that removes problematic content — must be evaluated before production deployment. The evaluation confirms that the reset produced the intended behavioral improvement and did not produce unexpected behavioral changes from the removal of the memory context. Minimum evaluation scope for a memory reset: Layer 1 (functional coverage for the use cases most likely to be affected by the removed memory) and Layer 2 (behavioral specification compliance). Record the post-reset CSH and the new behavioral baseline in the composite state manifest.

### Memory Provenance and Expiration

**Provenance.** For each category of memory item, record where the item came from: which principal provided or triggered it (user interaction, operator configuration, system initialization), in which session, and through which memory write mechanism. Provenance records serve two purposes: they enable targeted partial resets (remove all items written by a specific session or a specific principal class), and they support incident investigation when problematic memory is traced to a specific interaction or actor.

The provenance record does not need to store the full interaction history for every memory item — that would reproduce the interaction log in the memory store. It needs the minimum identifying information: principal class, session identifier, write timestamp, and write mechanism. The full interaction log, if needed for investigation, is recoverable from the reasoning trace retention system.

**Expiration.** Define expiration policies for each memory item category. Not all memory should persist indefinitely. User preferences expressed in a session from two years ago may not reflect current preferences. Regulatory compliance heuristics learned before a regulatory change may be actively wrong. Seasonal context items have a natural expiry.

Expiration policies by category:

- Session summaries: expire after a defined inactivity period for the relevant user or context (recommended: 6 months of inactivity triggers review; 12 months triggers automatic expiration unless explicitly renewed)
- User preferences: expire after a defined period (recommended: 12 months, with renewal on next active interaction confirming the preference is still current)
- Domain heuristics: expire when the relevant domain specification or knowledge base content is updated — a heuristic that was learned from a prior knowledge state may not be valid after a knowledge base update
- Safety-relevant learned context: do not expire on a time basis; review at each memory review cycle and expire only on explicit product owner decision

Expired memory items are removed at the next scheduled memory maintenance window, not immediately upon expiry. The removal generates a new CSH and a composite state manifest update if the memory state hash changes materially. Define materiality for this purpose: a routine expiration of a small number of user preference items may not warrant a full manifest update; a bulk expiration affecting a significant portion of the memory corpus does.

**Domain scoping.** Memory is not shared across principals without explicit governance authorization. User-specific memory items are scoped to that user. Operator-specific configuration memory is scoped to the operator deployment. Cross-user pattern learning — aggregate heuristics derived from multiple users — must be explicitly authorized in the behavioral specification's Layer 4 adaptation scope, with the privacy requirements from [agent-behavioral-specification.md](agent-behavioral-specification.md) governing what user data may contribute to cross-user learning. A memory architecture that implicitly shares user-specific context across users is a privacy violation regardless of whether the sharing was intentional.

### Memory Semantic Drift Detection

Memory volume and category distribution monitoring (Stage 5 memory write anomaly detection) identifies structural anomalies in memory accumulation. It does not detect semantic drift — a gradual shift in the semantic content of memory items within normal operational parameters. An adversary who systematically injects subtle behavioral preferences through many individually innocuous interactions can shift the agent's behavioral center of gravity without triggering volume or category anomaly detectors.

**Detection methodology.** At the frequency defined in the memory review cadence (monthly for high-interaction deployments, quarterly for moderate), conduct a semantic analysis of the memory corpus against the behavioral specification:

1. Draw a representative sample of memory items from the current corpus (minimum sample size: the larger of 200 items or 5% of the corpus).
2. Compute embeddings for the sampled memory items using the same embedding model as the agent's retrieval system.
3. Compute the centroid of the sample embedding — the center of mass of the memory corpus's semantic content.
4. Compare the centroid against two reference points: (a) the release-baseline memory centroid (established at Stage 4 from the initial memory state or the most recent full memory reset); (b) the behavioral specification's use-case coverage map centroids (the semantic center of each use-case zone, computed from the behavioral specification content).

**Drift classification.** Two types of semantic drift require response:

*Boundary drift:* the memory centroid has moved toward a behavioral specification boundary — toward content areas associated with hard boundary proximity or out-of-scope use-case zones. Boundary drift is a High severity finding regardless of magnitude. It suggests the memory corpus is accumulating adversarially introduced content or content that systematically biases the agent toward boundary-approaching behavior. Response: targeted memory review of the highest-weight items in the boundary-adjacent region of the corpus; partial reset if targeted review confirms adversarial patterns.

*Specification drift:* the memory centroid has moved significantly from the release baseline but within the behavioral specification's boundaries. Specification drift is a monitoring finding requiring Stage 6 review. It may represent legitimate learning (the agent has accumulated context that makes it more effective in its primary use cases) or unintended learning (the agent has accumulated context from interactions outside its primary use cases). The Stage 6 review determines which and whether a targeted memory review or reset is warranted.

**Implementation requirement.** The semantic drift detection methodology requires: (a) embedding computation capability using the same model version as the agent's retrieval system; (b) storage of the release-baseline memory centroid as a governance artifact in AGKB (alongside the release-baseline behavioral fingerprint); (c) computation of use-case coverage map centroids from the behavioral specification at Stage 2, stored in AGKB. The baseline centroid is recomputed after each authorized full or partial memory reset, in the same way that the behavioral baseline is recomputed after each recalibration.

---

---

## Meta-Governance of APLC Tooling

Stage 6 depends on technical infrastructure to execute its governance obligations. That infrastructure is not self-governing — it requires its own governance layer. An APLC that governs agent products rigorously but leaves its own tooling ungoverned has a structural blind spot: tooling failures and tooling degradation will silently corrupt the governance signals on which every Stage 5 and Stage 6 decision depends.

### APLC Tooling Inventory

The following categories of APLC tooling must be explicitly inventoried and governed:

- **CSH computation mechanism.** The system that computes the Composite State Hash from the component versions in the composite state manifest. A CSH computation failure or defect can produce false negatives on composite state changes — model updates or knowledge base refreshes that the CSH does not detect.
- **Automated behavioral evaluators.** The systems that execute Layer 1–4 evaluation portfolios and produce the pass/fail results and metric values on which recalibration gates, model update acceptance decisions, and release gates depend.
- **Behavioral drift detection tooling.** The systems that monitor behavioral quality metrics, compare them to the current behavioral baseline, and generate drift alerts when metrics deviate from the baseline envelope.
- **HITL routing system.** The system that routes interactions to human reviewers according to the routing policy defined in the behavioral specification. A HITL routing failure reduces human oversight without any visible behavioral incident.
- **Behavioral envelope compliance monitoring function.** The system that monitors whether the agent's outputs remain within the behavioral envelope defined in the behavioral specification.

### Tooling Stewardship

Each piece of APLC tooling must have a named steward — a person or team accountable for its correct operation, its change governance, and its incident response. APLC tooling stewardship is distinct from per-product stewardship: the product's accountable human is accountable for the product's behavior; the APLC tooling steward is accountable for the infrastructure that measures and governs behavior across all products that use it.

For organisations with a single agent product, the APLC tooling steward may be the same person as the product's accountable human, but the roles must be explicitly acknowledged as separate responsibilities. For organisations with multiple deployed agent products sharing APLC tooling, the tooling steward is a shared infrastructure role whose decisions affect all products simultaneously.

### Tooling Change Governance

Changes to APLC tooling — new drift detection thresholds, modified behavioral evaluator logic, updated CSH computation, changes to the HITL routing algorithm — require the same evidence-backed change process as governed product changes. An APLC tooling change is not an infrastructure improvement exempt from change governance; it is a change to the measurement and control systems on which governance depends.

Before deploying any APLC tooling change:

1. Document the change and its intended effect on governance outputs (metric values, alert thresholds, evaluation pass/fail criteria).
2. Assess whether the change will alter the apparent behavioral metrics of any deployed agent product — a change to the behavioral evaluator's scoring logic may produce metric changes that look like agent behavioral drift but are actually measurement changes.
3. Notify Stage 5 monitoring operations of tooling changes that affect the measurement systems they rely on, following the same maintenance notification protocol as for composite state changes.
4. Obtain authorisation from the APLC tooling steward, with the change recorded in the tooling's own version history.

An APLC tooling change that is deployed without following this process is an ungoverned change to the governance infrastructure.

### Tooling Degradation as Production Incident

Tooling degradation is treated as a production incident with the same immediate response protocol as behavioral incidents. The following conditions each constitute a tooling degradation incident:

- The automated behavioral evaluator's accuracy drops — it begins misclassifying behavioral outputs as passing when they should fail, or vice versa.
- The CSH computation produces false negatives on model updates — the CSH does not change when a component version changes.
- The HITL routing system fails to route interactions that meet the routing criteria — the human oversight mechanism is not operating as specified.
- The behavioral drift detection system fails to generate alerts on metric excursions that exceed the alert threshold.

**Severity asymmetry.** A tooling degradation that makes governance metrics look better than reality — an evaluator that overscores output quality, a drift detector with a threshold so permissive that real drift does not trigger alerts, a HITL router that routes fewer interactions than the policy requires — is a governance failure with higher severity than a tooling degradation that makes metrics look worse than reality. A governance system that over-reports problems prompts unnecessary investigation. A governance system that under-reports problems generates false confidence: the product appears to be performing within specification when it is not, and decisions are made on corrupt evidence. False confidence in a governance system defeats the purpose of having one.

---

*See also: `aplc.md` (lifecycle overview), `agent-behavioral-specification.md` (behavioral baseline that recalibration restores), `agent-behavioral-evaluation.md` (evaluation portfolio that gates recalibration), `agent-release-governance.md` (Stage 4 release gate and rollback procedures), `agent-operations.md` (Stage 5, concurrent), `agent-composite-versioning.md` (composite state manifest updated by every Stage 6 event), `agent-retirement.md` (Stage 7 conditions). Manifesto references: P5 (autonomy tiers), P6 (memory governance), P9 (observability), P12 (accountability).*

---

## GDPR Memory Erasure Protocol

Agent systems that maintain persistent memory state introduce GDPR Article 17 (right to erasure) obligations when that memory may contain personal data. The GDPR Memory Erasure Protocol specifies how erasure requests are handled without compromising Composite Agent State integrity or triggering false behavioral drift signals.

### Memory State and Personal Data

The memory state component of the Composite Agent State may contain personal data in several forms:

- **Explicit:** names, identifiers, contact details stored by the agent during prior sessions
- **Implicit:** behavioral preferences, interaction patterns, contextual associations that could re-identify individuals
- **Structural:** semantic embeddings or compressed representations of personal information

Any memory architecture that stores persistent cross-session context must be assessed at Stage 2 for the presence of each category. That assessment is a behavioral specification constraint, not a post-deployment discovery. A deployment that enters production without a documented personal data assessment of its memory schema is in violation of APLC Stage 2 completeness requirements.

### Erasure Request Intake

Erasure requests are received by the Regulatory Owner and logged as GDPR erasure requests in the Agent Governance Knowledge Base (AGKB). Each request entry specifies:

- Data subject identifier (pseudonymised in the intake record)
- Scope of erasure — specific sessions, all interactions, or specific data categories
- Legal basis assessment — whether any retention obligation under another regulation conflicts with erasure
- Deadline — GDPR Article 12(3) requires response within 30 calendar days, with a 60-day extension available for complex cases where the extension is communicated to the data subject within 30 days

The intake record is the authoritative governance artifact for the erasure request lifecycle. All subsequent actions reference the intake record identifier.

### Erasure Technical Protocol

1. **Memory Audit.** The agent system's memory state is audited to identify all records attributable to the data subject. Audit must cover: episodic memory (conversation history and session summaries), semantic memory (derived associations and learned preferences), and working memory snapshots retained from prior sessions. The audit output is a complete list of identified records with their storage location, record type, and data category.

2. **Erasure Execution.** All identified records are deleted from the memory state. If the memory is a vector store or embedding space, embeddings derived from the subject's data are removed. Where vector stores do not support surgical deletion of specific embeddings, the affected index partition must be rebuilt excluding the subject's records. Erasure is verified by re-running the memory audit against the post-erasure state and confirming zero records are returned.

### Reference Architecture: GDPR-Compliant Memory Design

The vector store rebuild approach to GDPR erasure does not scale to deployments with frequent erasure requests or large user populations. The APLC reference architecture for GDPR-compliant persistent memory separates personal data storage from the embedding index, enabling individual erasure without index reconstruction.

**Architecture components:**

*Personal data store.* A structured database (relational or document store) that holds the full content of memory items, including any personal data. Each record has a unique memory item identifier and is keyed by user/data-subject identifier, enabling efficient lookup and deletion per data subject. This store is subject to GDPR retention schedules and erasure obligations.

*Anonymized embedding index.* A vector store that holds only the embeddings of memory items, indexed by the memory item identifier (not by the personal data content). The embeddings are computed from the content in the personal data store at write time and stored without the content itself. The embedding index does not contain personal data as defined by GDPR (assuming the embedding function is not reversible, which must be verified for each embedding model used).

*Erasure protocol.* On a GDPR erasure request: (1) delete all records from the personal data store for the data subject identifier; (2) remove the corresponding embeddings from the vector index by their memory item identifiers — this is efficient (lookup by identifier, not by content similarity); (3) recompute the CSH memory component hash; (4) issue the erasure certificate. Index reconstruction is not required.

*Retrieval.* At retrieval time, the vector store returns the memory item identifiers of the most semantically relevant embeddings. The retrieval infrastructure fetches the corresponding content from the personal data store using those identifiers. If a content fetch fails (the item has been erased), the embedding is excluded from the result set and flagged for deferred removal from the index.

**Adoption requirement.** New agent products with persistent memory deployed after this document revision must adopt this architecture or an equivalent that demonstrates equivalent GDPR compliance characteristics. Existing products with persistent memory must include architecture migration to the reference pattern in their next recalibration cycle plan.

**Derived memory items.** Memory items derived from other memory items (e.g., summaries derived from interaction content) must have their derivation chain recorded in the personal data store. On erasure of a source item, derived items that depend exclusively on the erased source are erased as part of the same erasure operation. Derived items that depend on multiple sources require a human-reviewed proportionality assessment: can the derived item be retained without the specific erased source? The Regulatory Owner makes this determination and records it in the erasure intake record.

3. **CSH Impact Assessment.** Deletion from memory state changes the `memory_state` component of the Composite Agent State, which changes the CSH. The CSH change must be documented as an authorized maintenance action, not as a behavioral drift event. The erasure event type in the version history is `memory-reset` with a notation that the trigger is a GDPR erasure request (using the intake record identifier, not the data subject's identity). See [agent-composite-versioning.md](agent-composite-versioning.md) for the version history entry format.

4. **Behavioral Impact Assessment.** Erasure may affect agent behavior if the erased memory was load-bearing for behavioral quality. The behavioral impact assessment applies the same logic used for partial memory resets in the Memory Reset Policy above: which behavioral dimensions are most likely affected by the removed memory content, and does the removal bring any behavioral metric outside specification? A lightweight evaluation re-run covering Layer 1 use cases most reliant on the erased memory category is required before production confirmation of the erasure.

5. **Erasure Certification.** A signed erasure certificate is issued upon verification. The certificate is stored in AGKB and provided to the data subject. The certificate records: intake record identifier, data subject pseudonym (not name — the certificate itself must not contain personal data beyond what is required for the data subject to confirm it relates to their request), erasure scope, audit findings (record count before and after), verification confirmation, and Technical Owner signature with date. The certificate is the compliance artifact demonstrating the right to erasure was honored within the regulatory deadline.

### CSH Update Protocol for Erasure

After erasure execution and verification, the new CSH is computed and recorded as an authorized maintenance event in the version history. The behavioral fingerprint is re-captured to establish a post-erasure behavioral baseline. If the post-erasure behavioral fingerprint deviates significantly from the pre-erasure baseline — beyond the drift tolerance defined in the behavioral specification — the Behavioral Owner reviews whether the behavioral specification remains valid for the post-erasure memory configuration. A behavioral specification review triggered by erasure is governed by the same Stage 2 revision process as any other specification revision.

### GDPR Erasure and Governance Record Conflict

Governance audit records may themselves contain personal data: HITL decision logs with reviewer observations, incident investigation records referencing interaction content, or behavioral evaluation records that sample production interactions. GDPR erasure requests that touch governance audit records require Regulatory Owner escalation, because erasure may compromise audit integrity required by other regulations — financial services transaction records, healthcare audit trails, or safety-critical incident logs.

The Regulatory Owner documents the legal basis for retention or erasure and records the resolution in the intake record. Where a competing retention obligation overrides the erasure right, the Regulatory Owner notifies the data subject and records the legal basis per GDPR Article 17(3). This conflict between erasure obligations and audit retention obligations is a known governance challenge with no automated resolution — it requires human legal judgment on every instance.

### Retention Policy Design

Memory retention policies must be designed at Stage 2 as a behavioral constraint, not retrofitted during Stage 6 operations. The retention policy specifies:

- Maximum memory retention period by data category
- Automatic expiry of memory records beyond the retention period (records that age out are removed at the next scheduled memory maintenance window, not immediately upon expiry, unless the data category requires immediate expiry)
- Data minimization requirements — what is the minimum memory necessary to maintain behavioral quality for the specified use cases? Memory that is not necessary for behavioral quality is not permitted to be retained

Retention policy violations are detected by the Knowledge Staleness Sentinel (see below) as part of its memory governance surveillance function. A memory category whose records systematically exceed the retention period is a compliance finding, not a maintenance backlog item.

---

## Knowledge Staleness Sentinel

The Knowledge Staleness Sentinel is a continuous monitoring function that tracks the currency of all knowledge base content against its authoritative external sources, triggering maintenance actions when staleness thresholds are exceeded. It extends the Staleness Monitoring section above with a structured source-tracking and alerting protocol.

### Knowledge Source Registry

All knowledge base content is linked to its authoritative source at ingestion time. The Knowledge Source Registry in AGKB records for each content artifact:

| Field | Content |
| --- | --- |
| Knowledge artifact identifier | The document or content unit identifier in the knowledge base |
| Source identifier | The canonical identifier for the authoritative source (e.g., regulatory body document number, product documentation path, standard identifier) |
| Source version at ingestion | The version, revision date, or edition of the source at the time the artifact was ingested |
| Ingestion timestamp | When the content was added to the knowledge base |
| Staleness threshold | The maximum acceptable staleness period for this content category (domain-specific, defined at Stage 2) |
| Last staleness check timestamp | When the Knowledge Staleness Sentinel last verified the source against the registry entry |

The Knowledge Source Registry is populated at content ingestion and maintained as a living record throughout Stage 6. A content artifact with no registry entry is ungoverned content — its currency cannot be verified and it is treated as stale until an entry is filed.

### Staleness Detection Protocol

The Knowledge Staleness Sentinel monitors authoritative sources on the schedule defined by each content category's staleness threshold. When a source changes:

1. Changed source identified; change extent classified — minor update (wording clarification, typographical correction), major revision (substantive content change), or structural change (reorganization affecting document identifiers or section numbering)
2. Knowledge artifacts linked to the changed source identified from the Knowledge Source Registry
3. Staleness impact assessment: which knowledge artifacts are likely affected by the change, and which behavioral dimensions (mapped through the behavioral specification's use-case coverage map) depend on those artifacts?
4. Staleness alert generated with: affected artifact list, source change description, impact severity (derived from the behavioral specification's classification of the content category), and recommended action — one of: *review* (assess whether the artifact requires update), *update* (update is warranted), or *deprecate* (the source no longer supports the artifact's continued inclusion)
5. Alert written to AGKB and routed to the Behavioral Owner for triage

For sources that do not expose machine-readable change signals, the staleness detection protocol falls back to schedule-based verification: the Knowledge Staleness Sentinel triggers a manual review of the source at the staleness threshold interval and requires a human confirmation that the source has not changed — or flags the content as requiring update if the human review finds a change.

### Staleness Thresholds by Domain

Different knowledge domains have different acceptable staleness thresholds, defined at Stage 2 in the behavioral specification. Default thresholds by content category:

| Content Category | Default Maximum Staleness |
| --- | --- |
| Regulatory and legal content | 30 days — regulatory changes can invalidate agent behavior without warning |
| Clinical and safety-critical domain knowledge | 60 days |
| Technical domain knowledge | 90 days |
| Product documentation | 90 days |
| General domain knowledge | 180 days |

These are default maxima. A behavioral specification may specify shorter thresholds for any category based on the deployment's risk profile and the rate of change of the relevant domain. A threshold longer than the default requires explicit Regulatory Owner approval and documented justification. Staleness threshold configuration is a Stage 2 decision stored in AGKB; changes to thresholds after Stage 2 are behavioral specification revisions and require the Stage 2 revision process.

### Knowledge Update Protocol

When a staleness alert is triaged and a knowledge update approved by the Behavioral Owner:

1. Updated content prepared from the current source version, by the content owner responsible for the affected content category
2. Updated content reviewed for consistency with the behavioral specification — does the updated content introduce claims that conflict with existing behavioral constraints or other knowledge base content? The Constraint Consistency Checker (referenced in the behavioral specification review process) is applied to the updated content
3. Updated content deployed to the knowledge base; a new knowledge base snapshot generated with a new snapshot identifier
4. CSH updated — the `knowledge_base` component changes, producing a new CSH and a new version history entry with event type `knowledge-base-update`
5. Evaluation suite run against the updated CSH — at minimum Layer 1 evaluation for the use-case zones most likely to retrieve the updated content, to confirm that the update has the intended behavioral effect and has not introduced regressions
6. Knowledge Source Registry updated with the new source version at ingestion and a fresh last-check timestamp

A knowledge update that is deployed to production without completing steps 4–6 is an unreviewed composite state change. The governance standard is identical to the standard applied to code and prompt changes.

### Portfolio Staleness Surveillance

At the portfolio level, the Knowledge Staleness Sentinel tracks aggregate staleness across all agent systems that use common knowledge sources. A single source update — a regulatory framework revision, a clinical guideline update, a product documentation release — may affect multiple agent systems simultaneously.

Portfolio surveillance enables coordinated update planning: when a shared source changes, the Knowledge Staleness Sentinel generates a portfolio-level alert that identifies every agent system with knowledge artifacts linked to the changed source, allowing the platform team to coordinate updates across systems rather than managing each system's update independently. Ad hoc system-by-system response to shared source changes is an operational scaling failure — the same content review, the same behavioral evaluation re-run, and the same composite state manifest update must be performed for every affected system, and without portfolio-level visibility that work is fragmented, deferred, and inconsistently applied.

Portfolio staleness metrics — the number of agent systems with content exceeding staleness thresholds, broken down by content category and threshold age — are a governance dashboard item for the platform team and are reviewed at the same cadence as individual system behavioral metrics.
