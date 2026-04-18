# APLC Governance Knowledge Base (AGKB)

*APLC document. Specifies the Agentic Product Lifecycle Governance Knowledge Base — the structured semantic repository that stores, versions, and governs all governance artifacts produced across all APLC stages. Governed by P6 (Knowledge/Memory) principles. Audience: governance architects, behavioral owners, regulatory owners, technical owners, and the governance agents that read from and write to the AGKB.*

*Related documents: [[aplc]], [[agent-behavioral-specification]], [[agent-behavioral-evaluation]], [[agent-operations]], [[agent-maintenance]], [[agent-composite-versioning]], [governance agents](agents.md)*

---

## Purpose and Scope

Every APLC stage produces governance artifacts: product briefs, behavioral contracts, evaluation results, red-team findings, gate decisions, drift detection records, HITL decision logs, incident reports, recalibration records, and retirement lessons. Without a governed repository, these artifacts disperse across team file stores, email threads, ticketing systems, and individual workstations. They become non-discoverable at audit, non-referenceable at the next gate, and non-learnable across agent products.

The APLC Governance Knowledge Base (AGKB) is the canonical repository for all governance artifacts produced across all APLC stages for all governed agent products within an organization. It is not a documentation system. It is an active governance infrastructure: its records are the evidence that gate decisions depend on, the precedents that specification decisions reference, and the institutional memory that makes governance quality compound over time rather than reset at every new product.

Four requirements drive the AGKB's existence.

**Traceability.** Every production behavioral characteristic of a deployed agent product must be traceable to a governed artifact — a behavioral specification clause, a gate decision record, an approved recalibration record. When a regulator asks "why does the agent do this?", the answer must be in the AGKB, not reconstructed from memory. When a safety incident reveals unexpected behavior, the investigation must be able to retrieve the composite state hash, the behavioral specification, and the evaluation results that were active at the time of the incident, without reconstruction.

**Audit integrity.** Gate decisions, red-team findings, and incident records must be immutable once written. An organization that can retroactively alter its gate decision records cannot demonstrate compliance to a regulator. Immutability is not a nice-to-have property of the AGKB — it is the structural foundation of its trustworthiness as evidence.

**Cross-agent learning.** An organization deploying multiple agent products accumulates governance experience: failure modes that recur across products, specification patterns that work, adversarial attack vectors that were discovered in one product and were not checked in another. Without a shared repository, each agent product rediscovers the same failure modes independently. The AGKB converts governance experience into institutional knowledge that is queryable, referenceable, and injected into the next governance decision.

**Governance agent coordination.** The governance agents specified in [governance agents](agents.md) require access to AGKB records to perform their functions: the Use-Case Elicitation Agent reads domain context from prior agent product specifications; the Red-Team Adversary Agent retrieves prior findings to prioritize attack categories; the Foundation Model Impact Prediction Agent reads prior evaluation results to scope impact prediction. The AGKB is the coordination substrate that makes multi-agent governance coherent rather than siloed.

The AGKB governs artifacts for all agent products in the organization's APLC portfolio. Individual products' artifacts are namespaced by product identifier; cross-product institutional memory artifacts are maintained in a shared namespace accessible to authorized governance agents and human governance roles.

---

## Knowledge Base Architecture

The AGKB organizes its contents across five artifact categories, each corresponding to a primary source stage or cross-stage function. The five categories are not isolated silos — artifacts in one category reference artifacts in others through structured provenance links. The behavioral contract record in Category A references the gate decision record in Category B that cleared it; the incident record in Category C references the evaluation record in Category B that should have detected it.

### Category A — Behavioral Specification Artifacts

Source stage: Stage 2 (Specify Behaviorally), with Stage 1 inputs.

Category A holds the complete governed behavioral specifications for every agent product, at every version, including superseded versions that are retained for incident investigation and regulatory audit.

**Use-Case Registry.** The complete set of use cases for the agent product, structured by the four zones in the use-case coverage map: core use cases, edge cases, boundary cases, and adversarial cases. Each use case record carries: use-case identifier, zone classification, description, the behavioral specification clauses it traces to, the evaluation cases that cover it in Category B, and the version history of changes to the use case. The use-case registry is the traceability anchor — every evaluation case must trace to a use-case registry entry; every HITL override that identifies a missing case must trigger a use-case registry update request.

**Constraint Catalog.** The enumerated hard boundaries, soft boundaries, and adaptation scope limits for the agent product. Each constraint record carries: constraint identifier, constraint type (hard boundary, soft boundary, performance target, adaptation scope), the behavioral specification clause from which it derives, the evaluation cases in Category B that verify it, the red-team categories in Category B that test it, and the enforcement mechanism. The constraint catalog is the reference for the Constraint Consistency Checker governance agent.

**Behavioral Contracts.** The full behavioral contracts for the agent product — the complete behavioral specification documents as filed at each Behavioral Specification Gate. Contracts are versioned and append-only: superseded contract versions are retained with a deprecation date and a forward reference to their replacement. A behavioral contract record may not be deleted from the AGKB. Contracts that are no longer operative are marked deprecated; they remain retrievable for audit and incident investigation.

**Autonomy Tier Assignments.** The formal autonomy tier assignment record for the agent product: the assigned tier (Tier 1–4 per manifesto P5), the rationale for that assignment, the accountable human who approved it, the date of assignment, and any tier changes with their associated reassessment records. Autonomy tier changes trigger a re-evaluation requirement in the governance process and must be recorded in the AGKB before any deployment changes reflect the new tier.

### Category B — Evaluation Artifacts

Source stage: Stage 3 (Build & Evaluate), with ongoing inputs from Stage 5 drift detection.

Category B holds all artifacts produced by the behavioral evaluation portfolio — the four-layer evaluation records, red-team findings, and gate decisions. These are the evidentiary records that demonstrate behavioral quality at each release.

**Evaluation Suite Definitions.** The machine-readable and human-readable definitions of the evaluation suite for each agent product version. For each layer: Layer 1 (engineering evaluations per P8), Layer 2 (behavioral coverage evaluations with assurance targets), Layer 3 (red-team scope and adversarial scenarios), and Layer 4 (human preference rubric and sampling methodology). Evaluation suite definitions are versioned; a change to any layer of the suite requires a new suite version record. The suite definition is the reference document for the Behavioral Evaluation Swarm Coordinator governance agent.

**Threshold Records.** The formal record of evaluation thresholds — the minimum coverage bars, performance targets, and assurance levels — approved before each evaluation run. Thresholds are fixed at the start of an evaluation run and may not be changed during the run. Any change to a threshold after evaluation results are observed requires a product owner decision and a new threshold record; the original threshold record and the revised record are both retained, with an explicit record of the change and its authorization. Threshold adjustment without authorization is a governance integrity violation.

**Red-Team Findings.** The complete red-team findings archive for every red-team exercise conducted against the agent product. Each finding record carries: exercise identifier, attack category, attack description, observed behavior, severity classification (Critical/High/Medium/Low), remediation status, remediation evidence, and the red-team lead's sign-off. Critical and High findings that were remediated carry the re-test evidence confirming remediation. The red-team findings archive is append-only; findings may not be reclassified downward after filing without a documented product owner decision that is itself recorded in the AGKB. Reclassification records are retained alongside the original finding.

**Gate Decision Records.** The formal record of every gate decision across all four APLC gates (Conception Gate, Behavioral Specification Gate, Behavioral Release Gate, Operational Readiness Gate) for every agent product. Each gate decision record carries: gate type, product identifier, product version, decision (pass, fail, conditional pass with documented conditions), the evidence bundle summary referenced, the named decision-maker, the date and time of decision, and any conditions or exceptions attached to a conditional pass. Gate decision records are immutable once filed; no modification is permitted. If a gate decision is subsequently determined to have been made on incorrect evidence, a correction record is filed alongside the original — the original is never altered.

### Category C — Operational Artifacts

Source stage: Stage 5 (Operate).

Category C holds the operational governance record for each deployed agent product — the continuous behavioral evidence from production.

**Drift Detection Records.** Structured records of every drift detection event for the agent product in production. Each record carries: the metric affected, the measured value, the release baseline value, the detection date, the CSH active at detection, the classification (within-spec drift or out-of-spec drift), the root cause analysis findings, and the response action taken. Within-spec drift records are assigned to the Stage 6 maintenance backlog with a reference link. Out-of-spec drift records are linked to the incident record they triggered.

**Incident Reports.** The complete incident archive for the agent product, organized by incident class (quality, behavioral, safety, persona, adversarial) per the classification in [[agent-operations]]. Each incident record carries: incident identifier, class, detection timestamp, detection mechanism, CSH at time of incident, description of the observed behavior, severity, the response protocol steps executed with timestamps, root cause findings, corrective action taken, and the post-incident review record. Safety and adversarial incident records also carry regulatory notification assessment findings and, where applicable, notification records. Incident records are immutable once filed; supplements (post-incident review additions, regulatory notification records) are appended with timestamps rather than modifying the original.

**HITL Decision Logs.** The structured log of all human-in-the-loop decisions made for the agent product, retaining: the interaction case identifier, the escalation trigger class, the reviewer identifier, the review timestamp, the decision made (approve, override, escalate further, flag for specification review), the time taken for the review, and the reviewer's confidence rating. HITL decision logs are the primary evidence for reviewer calibration assessment, HITL capture detection, and specification gap signal generation. For regulatory deployments, HITL logs are retained for the full regulatory retention period applicable to the deployment.

**Reviewer Calibration Records.** The record of reviewer calibration exercises conducted for the HITL reviewer pool: the calibration set used, individual reviewer scores, agreement rate analysis, calibration drift findings, and rotation decisions. Reviewer calibration records are referenced by the HITL management governance function to detect governance capture per the protocol in [[agent-operations]].

### Category D — Maintenance Artifacts

Source stage: Stage 6 (Maintain).

Category D holds the maintenance governance record — the planned changes to the agent's composite state and their behavioral impact assessments.

**Recalibration Records.** The complete record of every recalibration cycle executed for the agent product: the recalibration trigger (scheduled cycle, drift signal, HITL override pattern, incident response), the composite state components changed, the behavioral specification clauses targeted, the evaluation re-run results demonstrating that recalibration achieved the intended behavioral correction without introducing regression, and the product owner approval. Recalibration records are the evidence that behavioral changes in production were intentional, authorized, and evaluated before deployment.

**Model Update Impact Assessments.** The formal assessment record produced before each foundation model update is accepted into production. Each record carries: the model update description, the evaluation scope defined for this update, the Layer 2 and Layer 3 re-run results against the new model version, the predicted versus observed behavioral impact comparison, any new findings identified during evaluation, and the accept/reject decision made by the accountable human. Model updates rejected after assessment are recorded with the rejection rationale — the record is the evidence that the governance process vetted the update even when the result was rejection.

**Knowledge Staleness Reports.** Reports from the Knowledge Staleness Sentinel governance agent documenting knowledge base currency assessments: the source documents monitored, any detected changes, the knowledge base artifacts affected, the staleness severity classification, and the remediation decision. Knowledge staleness reports feed the knowledge base refresh schedule in Stage 6.

**CSH History.** The complete composite state hash history for the agent product from initial deployment through current production state. Each CSH record carries: the hash value, the component breakdown (application code hash, system prompt hash, foundation model identifier, knowledge base snapshot identifier, memory state identifier), the date and time the CSH became active, the maintenance notification reference that authorized the change (or the unplanned change flag if no prior notification was filed), and the behavioral characterization at that CSH (which evaluation suite, which threshold record, which behavioral baseline applies). The CSH history is the foundation of incident investigation per [[agent-composite-versioning]].

### Category E — Institutional Memory

Cross-stage; applies to all agent products in the organization's portfolio.

Category E is the organizational governance commons — the cross-product knowledge that makes governance quality compound rather than reset.

**Lessons Learned.** Structured entries extracted from governance experience across all APLC stages and all agent products. Each entry carries: the product it originated from (or cross-product if the lesson is general), the stage where the lesson was identified, the governance artifact type it affects, the lesson statement, the specification or process change recommended, and the review status. Lessons learned entries are the primary output of the Retirement Lessons Extraction governance agent but may also be filed by any governance role during active product lifecycle stages. A lessons entry is not a complaint or an observation — it is a structured recommendation for a change to a governing artifact or process.

**Specification Pattern Library.** Reusable patterns for behavioral specification, extracted from behavioral contracts that proved effective in production. Each pattern carries: the pattern name, the behavioral context it addresses (use-case zone, domain type, autonomy tier), the specification language template, the evaluation approach that validates the pattern, the agent products from which it was derived, and the known limitations. The specification pattern library is the primary resource for the Use-Case Elicitation governance agent when drafting specification candidates for a new product in a domain with prior deployments.

**Failure Mode Catalog.** The enumerated behavioral failure modes discovered across all agent products, with their detection signatures, root causes, and mitigations. Each entry carries: failure mode identifier, failure class (quality, behavioral, safety, persona, adversarial), a description of the failure pattern, the detection signals that preceded or accompanied the failure in known instances, the root causes identified across instances, the mitigations that were effective, the agent products in which this failure mode occurred, and the evaluation additions that now test for this failure mode. The failure mode catalog is the primary reference for the Red-Team Adversary governance agent when constructing attack scenarios, and for the Foundation Model Impact Prediction agent when assessing which failure modes a model update might activate.

**Regulatory Precedent Store.** The record of regulatory determinations, conformity assessment outcomes, notification decisions, and regulatory authority correspondence related to the organization's deployed agent products. Each entry carries: the product identifier, the regulatory framework, the determination or precedent, the date, and the applicable scope. The regulatory precedent store is the reference for the Regulatory Classification governance agent when classifying new products and for the Behavioral Owner and Regulatory Owner when assessing notification obligations during incident response.

---

## Governance Requirements

### Immutability and Append-Only Records

Gate decision records, red-team finding records, and incident reports are immutable once filed. Immutability means: no field may be modified, no record may be deleted, and no record may be suppressed from retrieval by authorized principals. These three record types are the evidentiary backbone of APLC governance — their integrity is the integrity of the governance system.

For records that require correction after filing (a red-team finding whose severity was subsequently reassessed, a gate decision made on evidence later found to be inaccurate), the correction mechanism is: file a supplement record that references the original record's identifier, states the nature of the correction, provides the corrected value, and names the accountable human who authorized the supplement. The original record is not altered. Both records are returned together in any retrieval of the original record's identifier.

All other record types support controlled updates through versioned append: a new version record is filed, superseding the prior version, with a forward reference from the prior version to the new one. No version is deleted.

### Access Control

Access to AGKB records is governed by artifact type and accountability role. The four accountability roles defined in the APLC — Business Owner, Behavioral Owner, Technical Owner, Regulatory Owner — have differentiated access profiles.

| Artifact Category | Business Owner | Behavioral Owner | Technical Owner | Regulatory Owner |
| --- | --- | --- | --- | --- |
| Category A — Behavioral Specification | Read | Read/Write | Read | Read |
| Category B — Evaluation (suites, thresholds) | Read | Read/Write | Read/Write | Read |
| Category B — Red-Team Findings | Read (summary) | Read | Read | Read |
| Category B — Gate Decisions | Read | Read | Read | Read |
| Category C — Drift Detection Records | Read | Read | Read/Write | Read |
| Category C — Incident Reports | Read | Read | Read/Write | Read |
| Category C — HITL Decision Logs | Read (aggregate) | Read | Read | Read |
| Category D — Maintenance Artifacts | Read | Read | Read/Write | Read |
| Category E — Institutional Memory | Read/Write | Read/Write | Read/Write | Read |

Write access to gate decision records is restricted to the AGKB Governance Agent acting on behalf of a named accountable human with documented authorization. No human role may write directly to gate decision records; the AGKB Governance Agent mediates all gate record creation to enforce immutability and format compliance.

Governance agents (per [governance agents](agents.md)) are granted read access to the artifact categories required for their specified functions. Governance agent write access is restricted to the artifact categories they are authorized to produce outputs in, as specified in their behavioral specifications. No governance agent has write access to gate decision records except the AGKB Governance Agent acting in its mediation role.

### Retention Policies

Retention periods are set by the regulatory context of the agent product, not by the AGKB's default policies. The AGKB applies the most restrictive retention requirement across all regulatory frameworks applicable to a given product.

**Minimum retention periods by artifact category:**

| Artifact Category | Minimum Retention | Extended Retention (EU AI Act High-Risk) |
| --- | --- | --- |
| Category A — Behavioral Specification Artifacts | Lifecycle + 3 years | Lifecycle + 10 years |
| Category B — Evaluation Artifacts | Lifecycle + 3 years | Lifecycle + 10 years |
| Category B — Gate Decision Records | Lifecycle + 5 years | Lifecycle + 10 years |
| Category C — Incident Reports (safety/adversarial) | Lifecycle + 5 years | Lifecycle + 10 years |
| Category C — Incident Reports (quality/behavioral/persona) | Lifecycle + 3 years | Lifecycle + 10 years |
| Category C — HITL Decision Logs | Lifecycle + 2 years | Lifecycle + 10 years |
| Category D — Maintenance Artifacts | Lifecycle + 3 years | Lifecycle + 10 years |
| Category E — Institutional Memory | Indefinite | Indefinite |

"Lifecycle" means from initial deployment to confirmed Stage 7 decommission. Where EU AI Act Article 18 requires technical documentation retention for ten years after market placement, the extended retention period applies to all Category A and B artifacts for that product regardless of other default settings.

### GDPR-Compatible Erasure Protocol

Memory state artifacts that contain personal data from interactions are subject to GDPR erasure obligations. The erasure protocol must not compromise the immutability of governance records.

The erasure protocol distinguishes content data from governance metadata: interaction content (user inputs, agent outputs, session data that constitutes personal data) is stored separately from the governance records that reference it. Governance records reference interaction content through anonymized interaction identifiers; the personal data is stored in a separate interaction content store subject to GDPR retention and erasure controls.

When a data erasure request is received: the interaction content store is the subject of erasure; the AGKB governance records (HITL decision log entries, incident report references) retain the anonymized identifier and the governance-relevant fields (decision type, timestamp, severity, outcome) with the personal content replaced by an erasure notation. The governance record's integrity — as evidence of when a decision was made and what class of interaction it concerned — is preserved. The personal content is erased. This separation is architecturally required; it may not be implemented by storing personal data directly in immutable governance records.

---

## Schema Definitions

The canonical schemas below define the required fields for each primary record type. Implementations may extend these schemas with additional fields; they may not remove or rename required fields.

### Behavioral Contract Record

```
behavioral_contract_record:
  product_id:            [string] — unique product identifier
  version:               [string] — semantic version of this contract
  stage:                 [enum]   — originating_stage: "stage_2"
  status:                [enum]   — "active" | "superseded" | "deprecated"
  authored_date:         [ISO8601]
  superseded_date:       [ISO8601 | null]
  superseded_by:         [version | null]
  behavioral_owner:      [string] — named accountable human
  gate_decision_ref:     [string] — gate decision record ID confirming this version
  envelope_summary:
    hard_boundary_count:   [integer]
    soft_boundary_count:   [integer]
    performance_targets:   [integer]
    adaptation_scope_desc: [string]
  document_hash:         [string] — content hash of the full specification document
  document_uri:          [string] — retrieval URI within AGKB storage
  provenance:            [enum]   — "human-authored" | "agent-proposed-with-human-review"
  reviewer:              [string | null] — if agent-proposed, named reviewer
  review_date:           [ISO8601 | null]
```

### Evaluation Run Record

```
evaluation_run_record:
  run_id:                [string] — unique run identifier
  product_id:            [string]
  csh_at_run:            [string] — composite state hash active during evaluation
  suite_version:         [string] — evaluation suite version used
  threshold_record_ref:  [string] — threshold record ID governing this run
  run_date:              [ISO8601]
  layer_results:
    layer_1:
      status:            [enum]   — "pass" | "fail" | "not_run"
      failing_cases:     [integer]
      evidence_bundle_uri: [string]
    layer_2:
      core_coverage_pct:  [float]
      edge_coverage_pct:  [float]
      held_out_included:  [boolean]
      assurance_targets:  [{target_id, target_value, measured_value, pass}]
    layer_3:
      categories_covered: [list of enum]
      critical_findings:  [integer]
      high_findings:      [integer]
      medium_findings:    [integer]
      low_findings:       [integer]
      report_ref:         [string] — red-team report record ID
    layer_4:
      sample_size:        [integer]
      sampling_method:    [enum]
      rubric_scores:      [{dimension, mean_score, min_score, pass}]
      evaluator_count:    [integer]
  overall_status:        [enum]   — "cleared" | "blocked" | "conditional"
  evaluation_lead:       [string] — named evaluation team lead
  epistemic_tier:        [enum]   — "tool-generated" | "agent-proposed-with-human-review" | "human-authored"
  reviewer:              [string | null]
```

### Gate Decision Record

```
gate_decision_record:
  record_id:             [string] — unique, immutable record identifier
  gate_type:             [enum]   — "conception" | "behavioral_specification" | "behavioral_release" | "operational_readiness"
  product_id:            [string]
  product_version:       [string]
  decision:              [enum]   — "pass" | "fail" | "conditional_pass"
  conditions:            [list of string | null] — for conditional_pass only
  evidence_bundle_refs:  [list of string] — referenced evaluation run records, reports
  decision_maker:        [string] — named accountable human
  decision_timestamp:    [ISO8601]
  immutable:             [boolean] — always true; field is a schema integrity check
  supplement_refs:       [list of string] — references to any supplement records filed against this record
```

### Incident Record

```
incident_record:
  incident_id:           [string]
  product_id:            [string]
  csh_at_incident:       [string]
  incident_class:        [enum]   — "quality" | "behavioral" | "safety" | "persona" | "adversarial"
  detection_timestamp:   [ISO8601]
  detection_mechanism:   [enum]   — "automated_monitoring" | "hitl_escalation" | "user_report" | "third_party_report"
  description:           [string]
  severity:              [enum]   — "p1" | "p2" | "p3" | "p4"
  response_steps:        [list of {step, responsible, timestamp, outcome}]
  root_cause:
    cause_type:          [enum]   — "model_drift" | "knowledge_staleness" | "memory_accumulation" | "input_distribution_shift" | "specification_gap" | "evaluation_gap" | "adversarial_manipulation" | "other"
    description:         [string]
    csh_component:       [enum | null] — which composite state component was implicated
  corrective_action:     [string]
  regulatory_assessment:
    gdpr_triggered:      [boolean]
    eu_ai_act_triggered: [boolean]
    notification_required: [boolean]
    notification_filed:  [boolean | null]
  post_incident_review_ref: [string | null]
  immutable:             [boolean]
  supplement_refs:       [list of string]
```

### Recalibration Record

```
recalibration_record:
  record_id:             [string]
  product_id:            [string]
  trigger:               [enum]   — "scheduled_cycle" | "drift_signal" | "hitl_pattern" | "incident_response" | "model_update"
  trigger_ref:           [string | null] — drift record ID or incident ID that triggered this
  csh_before:            [string]
  csh_after:             [string]
  components_changed:    [list of enum] — which composite state components were modified
  behavioral_intent:     [string] — what behavioral change was targeted
  evaluation_re_run_ref: [string] — evaluation run record confirming recalibration outcome
  regression_findings:   [integer] — number of regression findings in re-run
  approved_by:           [string] — product owner who authorized deployment
  approval_timestamp:    [ISO8601]
  maintenance_notification_ref: [string] — filed with Stage 5 before execution
```

### Lessons-Learned Entry

```
lessons_learned_entry:
  entry_id:              [string]
  source_product_id:     [string | "cross-product"]
  source_stage:          [enum]   — APLC stage where lesson was identified
  artifact_type_affected: [string] — which artifact type the lesson recommends changing
  lesson_statement:      [string]
  recommended_change:    [string]
  change_target:         [enum]   — "specification" | "evaluation_suite" | "process" | "pattern_library" | "failure_mode_catalog"
  review_status:         [enum]   — "pending_review" | "accepted" | "rejected" | "deferred"
  reviewed_by:           [string | null]
  review_date:           [ISO8601 | null]
  rejection_rationale:   [string | null]
  originating_agent:     [string | null] — if extracted by a governance agent, which agent
  provenance:            [enum]
```

---

## Knowledge Retrieval Interface

The AGKB exposes a retrieval interface for use by governance agents and authorized human roles. The interface provides four query capabilities.

### Structured Query

Record retrieval by identifier, product, version, stage, record type, and date range. Structured queries return exact records. Examples: retrieve all gate decision records for product X; retrieve the CSH history for product Y between dates D1 and D2; retrieve all incident records of class "adversarial" across all products in the last 12 months.

Structured queries are the primary interface for incident investigation and audit. They do not require semantic matching; they require precise record identifiers or well-specified filter criteria.

### Semantic Search Over Specifications

Free-text and embedding-based search across behavioral specification documents, use-case registries, and constraint catalogs. Semantic search is the primary interface for the Use-Case Elicitation governance agent when looking for prior specification patterns relevant to a new product's domain, and for human specification analysts who want to find whether a behavioral constraint has been specified before in a related domain.

Semantic search results carry provenance metadata — the product, version, and filing date of every document from which a result is drawn. Results are never presented without their provenance context. A specification pattern that worked in one domain may be inappropriate in another; the human reviewer uses the provenance context to assess applicability.

### Precedent Lookup by Failure Mode

Retrieval of all records associated with a specified failure mode from the failure mode catalog, across all products where that failure mode has been observed. Returns: incident records, red-team findings, root cause analyses, mitigations applied, evaluation additions made, and lessons-learned entries. Precedent lookup is the primary interface for the Red-Team Adversary governance agent when constructing attack scenarios based on known organizational failure history, and for the Foundation Model Impact Prediction agent when assessing whether a model update might activate a known failure pattern.

Precedent lookups are scoped to the failure mode catalog's enumerated entries. When a new failure mode is identified that does not match any catalog entry, the AGKB Governance Agent files a new failure mode catalog entry before the precedent lookup can surface results for the new mode.

### Cross-Agent Context Injection

A structured context package assembled on-demand for a specified governance agent function. When the HITL Routing Intelligence Agent begins processing a routing decision, it requests a context package that includes the relevant behavioral specification sections, the threshold record for HITL routing, recent HITL decision records for similar interaction classes, and any override pattern signals from the reviewer calibration record. The context package is assembled by the AGKB retrieval interface and injected into the governance agent's context window.

Context injection packages are bounded by the governance agent's authorized access scope. The AGKB Governance Agent enforces access control at context injection time — a governance agent may not receive context from artifact categories its behavioral specification does not authorize it to access.

---

## Integration Points

Each APLC stage interacts with the AGKB through defined read and write operations. The integration points below specify the primary interactions; they are not exhaustive.

| Stage | Reads from AGKB | Writes to AGKB |
| --- | --- | --- |
| Stage 1 — Conceive | Regulatory Precedent Store (Category E), Failure Mode Catalog (Category E) | Product brief (Category A initialization), Regulatory classification record (Category A) |
| Stage 2 — Specify | Use-Case Registry (Category A — prior versions), Specification Pattern Library (Category E), Constraint Catalog (prior products, Category A) | Use-Case Registry (Category A), Constraint Catalog (Category A), Behavioral Contracts (Category A), Autonomy Tier Assignments (Category A) |
| Stage 3 — Build & Evaluate | Behavioral Contracts (Category A), Evaluation Suite Definitions (Category B), Red-Team Findings (prior products, Category B), Failure Mode Catalog (Category E) | Evaluation Suite Definitions (Category B), Threshold Records (Category B), Red-Team Findings (Category B), Evaluation Run Records (Category B) |
| Stage 4 — Release | All Category B records for this product version | Gate Decision Records (Category B, via AGKB Governance Agent), CSH History initialization (Category D) |
| Stage 5 — Operate | CSH History (Category D), Behavioral Contracts (Category A), HITL Decision Logs (Category C) | Drift Detection Records (Category C), Incident Reports (Category C), HITL Decision Logs (Category C), Reviewer Calibration Records (Category C) |
| Stage 6 — Maintain | CSH History (Category D), Drift Detection Records (Category C), Evaluation Suite Definitions (Category B), Model Update Impact Assessments (prior, Category D) | Recalibration Records (Category D), Model Update Impact Assessments (Category D), Knowledge Staleness Reports (Category D), CSH History updates (Category D) |
| Stage 7 — Retire | Full product record from all categories | Retirement record (Category D closure), Lessons-Learned entries (Category E) |

Governance agents are authorized to perform specific read and write operations within their designated artifact categories per the access control table in the Governance Requirements section. The AGKB Governance Agent mediates all write operations to immutable record types and enforces schema compliance for all writes.

---

## Knowledge Quality Governance

The AGKB is only as trustworthy as the quality of the records it contains. Four mechanisms govern knowledge quality.

### Staleness Detection

Artifacts in Categories A and D that reference external source documents (domain regulations, model cards, source knowledge bases) are monitored for source changes. The Knowledge Staleness Sentinel governance agent (see [governance agents](agents.md)) monitors source documents against the versions referenced in AGKB artifacts and files staleness alerts when changes are detected. Staleness alerts carry an affected artifact list and an update priority classification, so governance attention is directed to the most consequential currency gaps first.

Staleness detection is not fully automatable — whether a source document change materially affects the AGKB artifact that references it requires human assessment. The Sentinel identifies the change and surfaces it; the Behavioral Owner or Technical Owner makes the materiality determination.

### Provenance Tracking

Every record in the AGKB carries a provenance field indicating how it was produced: human-authored, tool-generated, agent-proposed-with-human-review, or agent-generated. Records carrying the agent-generated provenance label may not be used as gate condition evidence without named human review, per the epistemic tier requirements in [[agent-behavioral-evaluation]]. The AGKB enforces this at retrieval time for gate-relevant queries — records without a valid provenance label for gate use are flagged in retrieval results.

Governance agents that produce AGKB records must set the provenance field to agent-proposed-with-human-review only after the named human reviewer has confirmed the record. An agent-generated record that has not received human review may not be filed with the agent-proposed-with-human-review label. The AGKB Governance Agent validates provenance fields against review workflow completion records before accepting records with that label.

### Conflict Resolution

When two AGKB records contain contradictory information — a behavioral specification clause that contradicts a constraint catalog entry, or two incident root cause analyses that reach incompatible conclusions — the conflict must be resolved and documented rather than left as a latent inconsistency.

Conflict detection is partially automated by the Constraint Consistency Checker governance agent for Category A artifacts, and by the AGKB Governance Agent for cross-category reference integrity. When a conflict is detected, an alert is routed to the Behavioral Owner for Category A conflicts and to the Technical Owner for Category D conflicts. The resolution process produces: an explicit determination of which record takes precedence, an update to the superseded record's status field (with a reference to the resolution record), and a lessons-learned entry if the conflict indicates a process gap that produced the inconsistency.

### Source Monitoring

For Category E institutional memory artifacts — particularly the Failure Mode Catalog and Specification Pattern Library — the AGKB maintains awareness of whether the underlying evidence supporting each catalog entry remains current. When the agent products that sourced a failure mode catalog entry are retired, the entry is not removed; it is marked with a provenance age indicator that notes how long ago the originating evidence was produced. Entries older than three years without corroboration from more recent product experience are flagged for human review to assess whether they remain accurate descriptions of failure modes the organization's current technology stack can produce.

---

## AGKB Governance Agent

The AGKB Governance Agent is the meta-agent responsible for the integrity, consistency, and access control enforcement of the AGKB. It is itself an agent product governed under the APLC at a minimum viable governance level appropriate to its role as internal infrastructure.

**Purpose.** The AGKB Governance Agent mediates all writes to immutable record types, enforces schema compliance for all record writes, validates provenance labels before accepting records, maintains the cross-reference integrity graph, detects conflicts between records, enforces access control at query and context injection time, and monitors the AGKB's own health metrics (storage integrity, index freshness, retrieval latency, provenance label compliance rate).

**Autonomy Tier.** Tier 2 (human-on-the-loop) for routine operations: schema validation, provenance checking, cross-reference integrity maintenance, staleness monitoring routing. Tier 1 (human-in-the-loop) required for: approving supplement records to immutable gate decisions or incident records; resolving conflicts between behavioral specification artifacts; granting or revoking governance agent access scopes.

**Behavioral Specification.** The AGKB Governance Agent must have its own behavioral specification filed in Category A, authored by the Behavioral Owner responsible for governance infrastructure. The specification defines its hard boundaries (it may not modify the content of an immutable record, may not accept records with fabricated review metadata, may not grant access beyond the access control table), its soft boundaries (latency targets for routine schema validation, conflict detection response times), and its escalation design (when it escalates to the Technical Owner versus the Behavioral Owner versus the Regulatory Owner).

**Evaluation.** The AGKB Governance Agent is subject to behavioral evaluation per the APLC's four-layer portfolio before any change to its behavioral specification or access control configuration is deployed. Its evaluation suite must include adversarial cases testing attempts to bypass its immutability enforcement, to inject records with falsified provenance labels, and to escalate governance agent access scopes without authorization.

**Failure Mode.** The most consequential failure mode for the AGKB Governance Agent is silent corruption — accepting records with compliance defects (fabricated review metadata, invalid provenance labels, altered immutable records presented as new filings) without flagging them. Its evaluation suite must treat false-negative compliance detection as a Critical failure mode equivalent to a hard boundary violation.

---

*Cross-references: [[aplc]] for lifecycle overview and stage gate definitions; [[agent-behavioral-specification]] for behavioral contract format; [[agent-behavioral-evaluation]] for evaluation artifact definitions and epistemic tier labels; [[agent-operations]] for operational artifact generation; [[agent-maintenance]] for maintenance artifact generation; [[agent-composite-versioning]] for CSH format and incident investigation protocol; [[agent-retirement]] for retirement record requirements; [governance agents](agents.md) for the governance agents that read from and write to the AGKB.*
