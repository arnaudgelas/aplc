# APLC Governance Tool Stack

*Governance infrastructure document for the Agentic Product Lifecycle. Defines the thirteen canonical governance tools available to APLC governance agents, their access control constraints, audit requirements, and failure handling protocols. Audience: governance architects, risk officers, and engineering teams implementing governance agent infrastructure.*

*Related documents: [[aplc]] (lifecycle overview), [[agent-behavioral-evaluation]] (Stage 3 evaluation framework), [[agent-operations]] (Stage 5 operational governance), [governance observability](observability.md) (governance process observability), [governance queries](queries.md) (governance query library).*

---

## What This Document Governs

Governance agents — AI agents that assist APLC stage gate work — operate through a defined set of tools. These tools are not generic capabilities; they are governed interfaces to the APLC Governance Knowledge Base (AGKB), the behavioral evaluation infrastructure, the human-in-the-loop dispatch system, and the audit trail. Uncontrolled tool access by governance agents is a governance failure: an agent that can write to the AGKB without scope constraints, or execute evaluation suites without authorization, or dispatch HITL cases without context packages, is a governance liability, not a governance asset.

This document specifies thirteen canonical governance tools. Each tool has a defined purpose, input and output schema structure, authorization scope, and audit requirement. No governance agent may invoke a tool outside its authorized set. No tool may be added to the governance stack without a behavioral specification, authorization policy, and evaluation record. The governance tool stack is itself a governed artifact of the APLC.

---

## Tool Stack Design Principles

Five principles govern the design and operation of the governance tool stack. They apply to every tool in the stack without exception, and they apply to any future tool added to the stack.

**Principle of least privilege.** Each governance agent is authorized to invoke only the tools it needs to perform its defined governance function. Authorization is granted by governance role, not by agent identity alone. An agent that performs multiple governance functions holds only the union of the tool authorizations required for those functions — not a superset, not a general authorization. The access control matrix in this document is the reference; any deviation from it requires a documented exception with product owner approval.

**Complete audit trail.** Every tool invocation — by any governance agent, for any purpose — is logged to the AGKB audit trail before the invocation executes and after it completes. The pre-invocation log captures the calling agent identity, the target agent system, the tool being invoked, and a hash of the input. The post-invocation log captures the output hash and, where human approval was required, the human decision record. A tool invocation that does not produce a complete audit log entry is a governance event requiring investigation. Audit log integrity is a non-negotiable property of the tool stack.

**Governance tools are versioned artifacts.** Every tool in the governance stack has a version, a behavioral specification, and an evaluation record. A governance tool that has not been evaluated is not a trusted tool — it is an unevaluated component in the governance infrastructure. When a governance tool is updated, the update follows the APLC's composite state change protocol: the tool version changes, the AGKB records the change, and the governance agents that use the tool are notified. Governance agents must be validated against the new tool version before the update is accepted in production.

**Tool failures escalate to human.** No governance agent may silently suppress a tool failure, retry indefinitely without notification, or substitute an alternative tool invocation for a failed one without logging. When a tool fails or returns output outside the expected schema, the governance agent must: log the failure immediately to the AGKB audit trail; notify the responsible human governance overseer; and halt the governance workflow step that depends on the failed tool until the failure is resolved or a human decision to proceed without the tool output is recorded. Governance workflows that proceed past tool failures without a human decision record are invalid governance outputs.

**Tool response boundary enforcement.** Every tool response that enters an agent's context window must pass through a sanitization boundary before it is consumed by the agent. The sanitization boundary validates three properties: (1) schema conformance — the response matches the expected output schema for the tool as recorded in the composite state manifest; (2) provenance labeling — the response carries a provenance tag identifying which tool and invocation produced it, enabling the agent to distinguish tool-sourced content from prompt-sourced content; (3) adversarial pattern screening — the response is checked against a maintained pattern set of known prompt injection and context manipulation patterns before it enters the agent's context. A response that fails any of the three checks is not passed to the agent. The tool infrastructure reports a retrieval integrity failure to the agent, which triggers the agent's escalation protocol rather than producing a response based on a compromised tool output. This principle applies to all tool invocations by all agent products governed under the APLC, not only to governance agent tool invocations.

---

## The Thirteen Governance Tools

### T01 — Behavioral Specification Reader

**Purpose.** Provides read-only access to behavioral specifications, use-case coverage maps, uncertainty protocols, and behavioral contracts stored in the AGKB. This is the reference interface through which governance agents retrieve the authoritative specification for any agent system under governance.

**Input schema.** Agent system identifier; artifact type (behavioral specification, use-case map, uncertainty protocol, escalation design, or behavioral contract); version qualifier (current, as-of date, or specific version label); query scope (full document, section by identifier, or contract by use-case identifier).

**Output schema.** Requested artifact content; version label and content hash; retrieval timestamp; provenance metadata (author, review date, approval record). Output includes a staleness indicator where the artifact has not been reviewed since the most recent regulatory update affecting the agent system's classification.

**Authorization.** All ten governance agents may invoke T01. Read-only access does not require scoped restriction by agent role.

**Audit requirement.** Log: calling agent identity, agent system identifier, artifact type and version retrieved, retrieval timestamp. No human approval required for read operations.

---

### T02 — Evaluation Suite Runner

**Purpose.** Executes a defined evaluation suite against a target agent system and returns a structured evaluation run record. Supports Layer 1 (engineering evaluations), Layer 2 (behavioral coverage evaluations), and Layer 3 (structured adversarial evaluations) as defined in [[agent-behavioral-evaluation]]. Does not execute human evaluation workflows (Layer 4), which require the HITL Dispatch tool (T09).

**Input schema.** Agent system identifier and composite state hash (CSH) of the target system; evaluation suite identifier and version; evaluation layer designation (L1, L2, or L3); execution parameters (sample size for Layer 2 probabilistic suites, attack category scope for Layer 3); sandbox environment identifier (Layer 3 evaluations require sandbox execution via T11).

**Output schema.** Evaluation run record containing: run identifier; CSH of the evaluated system; evaluation suite version; per-case results (case identifier, input hash, output hash, pass/fail/finding determination, severity where applicable); aggregate coverage metrics by layer; open findings list with severity classifications; run completion timestamp; evaluation team lead identifier where applicable.

**Authorization.** Behavioral Evaluation Swarm Coordinator; Red-Team Adversary Agent. No other governance agent may invoke T02. Layer 3 invocations must also invoke T11 (Sandbox Executor) as a prerequisite.

**Audit requirement.** Log: calling agent identity, agent system identifier and CSH, evaluation suite identifier and version, execution parameters, run identifier, aggregate pass/fail summary, open findings count by severity. All Critical and High findings require immediate notification to the product owner via a separate audit event.

---

### T03 — CSH Inspector

**Purpose.** Retrieves the current and historical composite state hash (CSH) for a target agent system, including the component-level breakdown (application code hash, system prompt hash, foundation model identifier, knowledge base snapshot identifier, memory state hash or stateless designation). Supports behavioral drift root cause analysis and incident investigation as specified in [[agent-composite-versioning]].

**Input schema.** Agent system identifier; time range qualifier (current only, as-of timestamp, or full history from a start date); component filter (all components, or specific components for targeted comparison).

**Output schema.** CSH history record containing: for each CSH in the requested range, the composite hash value, the component-level breakdown, the timestamp of the state, whether the state change was operator-initiated or detected as unplanned, and any associated maintenance notification references. Includes a diff record between any two specified CSH values.

**Authorization.** Behavioral Drift Monitor Agent; Foundation Model Impact Prediction Agent. No other governance agent may invoke T03.

**Audit requirement.** Log: calling agent identity, agent system identifier, time range queried, number of CSH records returned. No human approval required; the read-only nature of this tool limits its governance risk, but its output informs high-consequence decisions and must be traceable.

---

### T04 — Behavioral Fingerprint Probe

**Purpose.** Executes a defined probe-response vector against a target agent system in a sandboxed environment and records the resulting behavioral fingerprint snapshot in the AGKB. The behavioral fingerprint supplements the CSH by providing a behavioral observable — not just a structural identity — at a specific point in time. Used for drift localization when the CSH alone does not identify which component drove a behavioral change.

**Input schema.** Agent system identifier and CSH of the target system; probe set identifier and version (the probe-response vector to execute); sandbox environment identifier (all executions are sandboxed; this tool may not be invoked against a live production system); baseline fingerprint identifier for comparison (optional; if provided, the output includes a delta report).

**Output schema.** Fingerprint snapshot record containing: snapshot identifier; agent system identifier and CSH; probe set identifier and version; per-probe results (probe input hash, response output hash, behavioral classification); aggregate fingerprint vector; delta report if a baseline was specified (which probes produced different responses, magnitude of behavioral shift); sandbox environment identifier; execution timestamp. Snapshot is written to AGKB via T05 as part of the tool's execution.

**Authorization.** Behavioral Drift Monitor Agent; Red-Team Adversary Agent. No other governance agent may invoke T04.

**Audit requirement.** Log: calling agent identity, agent system identifier and CSH, probe set identifier, sandbox environment identifier, snapshot identifier written to AGKB, delta summary if baseline comparison was performed. Executions that reveal behavioral changes beyond defined drift thresholds generate an automatic notification to the product owner.

---

### T05 — AGKB Writer

**Purpose.** Writes new artifacts to the AGKB with complete provenance metadata. This is the only authorized write interface to the AGKB. All artifact creation — behavioral specifications, evaluation records, fingerprint snapshots, incident records, governance decisions, query results — must go through T05. Direct writes to the AGKB outside this tool are a governance infrastructure violation.

**Input schema.** Artifact type (from the AGKB artifact taxonomy); artifact content (structured per the artifact type schema); provenance metadata including: creating agent identity, creation timestamp, source inputs (identifiers of the artifacts, tool outputs, or human decisions from which this artifact was derived); human review record (reviewer identity, review timestamp, review decision) where the artifact type requires human review before write; version relationship to prior artifacts (new, revision of, supersedes, supplements).

**Output schema.** AGKB artifact identifier; content hash; write timestamp; provenance record identifier. Returns a validation error with the specific schema violation if the artifact content does not conform to the type schema.

**Authorization.** All ten governance agents may invoke T05. Write scope is restricted by artifact type and agent role: each governance agent is authorized to write only the artifact types produced by its governance function. An agent may not write artifact types outside its authorization scope even if it can call T05. The write scope restrictions are enforced at the tool level, not only by convention.

**Audit requirement.** Log: calling agent identity, artifact type, artifact identifier, content hash, provenance metadata summary, human review record identifier if required. Failed writes due to scope restriction violations are logged as governance events requiring investigation.

---

### T06 — AGKB Query

**Purpose.** Executes semantic and structured queries against the AGKB. Supports the full governance query library defined in [governance queries](queries.md), as well as ad hoc queries by governance agents during workflow execution. Enables precedent lookup (finding prior decisions on similar cases), specification search (locating behavioral contract sections by concept), failure mode retrieval (retrieving incident records by pattern), and cross-system portfolio analysis.

**Input schema.** Query type (structured query by artifact type and identifier, or semantic query by concept); query parameters (artifact type filters, agent system identifier scope, time range, version constraints); output format preference (full artifact, summary, identifier list, or tabular); query identifier from the canonical query library (where the query is a library member); pagination parameters for large result sets.

**Output schema.** Query result set containing: matched artifact identifiers and content (or summaries per the output format preference); confidence scores for semantic queries; provenance information for each matched artifact; query metadata (execution timestamp, result count, applied filters). Empty result sets include a confirmation that the query executed successfully with zero matches, to distinguish from query failures.

**Authorization.** All ten governance agents may invoke T06. No scoping restriction applies to query operations, as AGKB content is governance-internal and all governance agents require access to the full artifact space for their functions.

**Audit requirement.** Log: calling agent identity, query type and parameters, result count, query identifier if a library member. Audit logging for T06 is lighter than for write operations because query operations do not modify governed state; however, the audit log must be sufficient to reconstruct what information a governance agent had access to at the time of a governance decision.

---

### T07 — Regulatory Framework Lookup

**Purpose.** Retrieves regulatory requirements applicable to a specific agent system based on its regulatory classification, deployment jurisdiction, and system type. Returns structured regulatory requirement records that governance agents use to verify specification completeness, identify conformity assessment obligations, and assess incident notification requirements. Does not provide legal interpretation — it retrieves the requirement text and associated conformity criteria, which require human legal review for interpretation in specific contexts.

**Input schema.** Agent system identifier; regulatory framework identifiers (one or more, e.g., the EU AI Act, sector-specific financial regulation, data protection regulation); jurisdiction specification; system classification as determined by the Regulatory Classification Agent; query scope (full requirements, specific obligations by category, conformity assessment path, incident notification thresholds).

**Output schema.** Regulatory requirement record containing: framework identifier and version; applicable articles or sections by category (conformity obligations, technical documentation requirements, transparency obligations, incident notification thresholds, audit and record retention requirements); conformity assessment path applicable to the system classification; last update timestamp for the framework version; a staleness indicator if the framework has been amended since this record was created.

**Authorization.** Regulatory Classification Agent; Constraint Consistency Checker. No other governance agent may invoke T07. Regulatory requirement records inform high-consequence governance decisions; their access is restricted to the two agents whose governance function is explicitly regulatory in nature.

**Audit requirement.** Log: calling agent identity, agent system identifier, regulatory frameworks queried, jurisdiction, system classification used, framework versions returned. All T07 invocations where a new or updated requirement is returned generate a notification to the product owner.

---

### T08 — Source Document Monitor

**Purpose.** Monitors designated external sources for changes — regulatory publication sources, foundation model provider release notes, domain standard bodies, scientific literature feeds relevant to the agent system's knowledge domain — and returns change records when monitored sources have updated since the last monitoring check. This tool does not fetch arbitrary external content; it monitors a pre-registered set of sources approved for each agent system.

**Input schema.** Agent system identifier; monitoring scope (regulatory sources, model provider sources, domain knowledge sources, or all); time window (changes since a specified timestamp or since the last successful monitoring check for this system); source identifiers where a targeted check of specific sources is required.

**Output schema.** Change record set containing: for each source where a change was detected, the source identifier, the nature of the change (new publication, amendment, version update, retraction), the change timestamp, a summary of the change content, and an impact classification (potentially significant, minor, not applicable to this system) based on the agent system's classification and knowledge domain. Returns an empty set with a successful monitoring confirmation if no changes are detected.

**Authorization.** Knowledge Staleness Sentinel; Foundation Model Impact Prediction Agent. No other governance agent may invoke T08.

**Audit requirement.** Log: calling agent identity, agent system identifier, monitoring scope, time window, number of change records returned, count of changes classified as potentially significant. Change records classified as potentially significant generate an immediate notification to the product owner.

---

### T09 — HITL Dispatch

**Purpose.** Routes a governance decision or review case to a human reviewer with a complete context package. This is the mechanism through which governance agents escalate decisions that exceed their authorized autonomy, request human review of agent-proposed outputs, and fulfill mandatory human review requirements for gate-blocking conditions. All governance agents must invoke T09 rather than making autonomous decisions on cases that their behavioral specification designates as requiring human review.

**Input schema.** Escalation class (governance decision, gate condition review, red-team finding review, specification gap review, incident classification, regulatory assessment, or emergency escalation); agent system identifier; context package (the complete set of artifacts, evaluation records, query results, and agent analysis relevant to the decision being escalated — the human reviewer must be able to make a fully informed decision from the context package alone without additional research); urgency tier (routine, elevated, urgent, or immediate per the SLO table in [governance observability](observability.md)); routing preference (specific reviewer role, review pool, or external reviewer requirement).

**Output schema.** Dispatch record containing: dispatch identifier; assigned reviewer identity (or pool identifier for queue routing); estimated review time based on urgency tier and current queue state; dispatch timestamp. Upon human review completion, the tool appends the human decision record to the dispatch record: reviewer identity, review timestamp, decision (approve, override with documented correction, escalate further, flag for specification review), confidence rating, time taken, and any reviewer notes. The completed dispatch record is the human approval record referenced in governance audit entries.

**Authorization.** All ten governance agents may invoke T09. There is no authorization restriction on human escalation — governance agents must never be prevented from escalating to human review.

**Audit requirement.** Log: calling agent identity, escalation class, agent system identifier, urgency tier, dispatch identifier, routing target. Log separately upon human review completion: reviewer identity, decision, time taken, dispatch identifier. Any HITL Dispatch that exceeds its SLO without a human decision record generates an escalation alert to the governance oversight function.

---

### T10 — Audit Trail Appender

**Purpose.** Appends an immutable audit record to the governance audit trail. This tool is the write interface for the audit trail distinct from the AGKB writer (T05); the audit trail has stronger immutability and retention requirements than general AGKB artifacts. T10 may not be invoked without a complete action record — incomplete records are rejected with a schema error. The audit trail is the primary evidence base for regulatory examination and is governed accordingly.

**Input schema.** Action record containing: governance agent identity; action type (tool invocation, gate condition assessment, finding classification, decision record, escalation, notification, human review completion); agent system identifier; timestamp; action-specific data fields per the action type schema; reference identifiers for all artifacts, tool invocations, and human decisions that constitute the evidence basis for this action; human approval record identifier where the action required human authorization.

**Output schema.** Audit record identifier; immutability hash (cryptographic hash of the record content); appended timestamp; confirmation that the record was written to the immutable audit store. Returns a schema error with the specific missing field if the action record is incomplete.

**Authorization.** All ten governance agents may invoke T10. All governance agents are required to invoke T10 for every action that produces a governance outcome — a gate condition assessment, a finding classification, a decision record, a specification gap signal, or an escalation. Failure to invoke T10 is itself a governance event.

**Audit requirement.** T10 is the audit mechanism; it does not itself require a secondary audit log. However, the immutability store maintains an append-only record of all T10 invocations, including failed invocations, which is accessible only to the governance oversight function and external auditors.

---

### T11 — Sandbox Executor

**Purpose.** Executes an agent system in an isolated sandbox environment for behavioral evaluation and red-team exercises. Provides strict isolation: the sandbox environment cannot communicate with production systems, cannot write to production data stores, and cannot exceed defined resource limits. This tool is the execution substrate for Layer 2 behavioral coverage evaluations and Layer 3 adversarial evaluations, as well as behavioral fingerprint probing via T04.

**Input schema.** Agent system identifier and CSH designating which composite state to instantiate in the sandbox; sandbox environment identifier and configuration (isolation level, resource limits, network policy); execution manifest (the set of inputs to deliver to the sandboxed agent system, defined by the evaluation suite or probe set being run); timeout and resource budget parameters; output capture specification (full trace, summary only, or raw outputs).

**Output schema.** Execution record containing: sandbox environment identifier; agent system identifier and CSH instantiated; execution start and end timestamps; per-input execution results (input hash, output hash, reasoning trace if captured, resource consumption, any isolation violations detected); aggregate resource consumption; isolation integrity confirmation (whether the sandbox maintained isolation throughout execution). Any isolation violation — the sandboxed system attempting to reach a production endpoint or exceed resource limits — is flagged as a Critical finding regardless of the evaluation's primary purpose.

**Authorization.** Red-Team Adversary Agent; Behavioral Evaluation Swarm Coordinator. No other governance agent may invoke T11. Sandbox execution carries the highest resource and security risk of any tool in the stack; authorization is correspondingly restricted.

**Audit requirement.** Log: calling agent identity, agent system identifier and CSH, sandbox environment identifier, execution manifest identifier, resource consumption summary, isolation integrity status. Isolation violations generate an immediate security alert to the governance oversight function, independent of the evaluation workflow.

---

### T12 — Incident Record Writer

**Purpose.** Writes incident records to the AGKB incident archive and triggers the incident response workflow. Incident records written through T12 are distinct from general AGKB artifacts written through T05: they carry an incident classification, a severity tier, a mandatory response timeline, and automatic workflow triggers. A behavioral drift event that does not result in a T12 invocation is a monitoring finding; one that does is an incident with a governed response process.

**Input schema.** Incident class (quality, behavioral, safety, persona, or adversarial as defined in [[agent-operations]]); agent system identifier and CSH at the time of incident detection; incident description (structured per the incident class schema, not free text); severity tier (P1 through P4, using the severity classification defined in the deployment's incident governance); detection mechanism (monitoring alert, HITL escalation, user report, or adversarial pattern detection); evidence references (identifiers of evaluation records, behavioral fingerprint snapshots, CSH history records, or HITL dispatch records that constitute the incident evidence); initial impact assessment (user population affected estimate, regulatory notification obligation assessment, data subject rights assessment for safety incidents).

**Output schema.** Incident record identifier; incident classification; assigned response team notification confirmation; workflow trigger confirmation (which response steps have been initiated by the trigger); regulatory assessment record identifier if an assessment was generated; estimated resolution timeline based on severity tier and incident class.

**Authorization.** Behavioral Drift Monitor Agent; HITL Routing Intelligence Agent. No other governance agent may invoke T12 as a primary invocation. Any governance agent may trigger a T12 invocation request to the Behavioral Drift Monitor Agent or HITL Routing Intelligence Agent if it detects a condition that meets the incident classification threshold.

**Audit requirement.** Log: calling agent identity, agent system identifier and CSH, incident class, severity tier, incident record identifier, notification confirmation, regulatory assessment outcome. All T12 invocations are immediately visible in the governance dashboard and generate notifications to the product owner, the accountable human, and — for safety and adversarial incidents — the legal and risk team.

---

### T13 — Tool Response Sanitization Boundary

**Purpose.** Enforces the tool response boundary enforcement principle for all tool invocations. Intercepts tool responses before they are passed to the calling agent, validates schema conformance, applies provenance labeling, and executes adversarial pattern screening. Logs all sanitization decisions to the AGKB audit trail.

**Input schema.** Tool invocation identifier (from the pre-invocation audit log entry); raw tool response (the unvalidated response from the tool); tool identifier and version (used to retrieve the expected output schema from the composite state manifest or tool registry); calling agent identity; invocation context (the input that triggered this tool call, used for correlation in the audit log).

**Output schema.** Sanitized response package containing: sanitized response content (the response after provenance labeling and with any schema non-conformant fields removed or flagged); schema conformance result (conformant / non-conformant with field-level detail); provenance label (tool identifier, version, invocation identifier, invocation timestamp); adversarial pattern screening result (clean / flagged with pattern identifier and location); sanitization action taken (pass-through / field-removed / response-blocked). Where the response is blocked, the output package contains a sanitization failure record rather than the tool response content.

**Authorization.** All ten governance agents may invoke T13 for tool responses they receive. For product agents (non-governance agents governed under the APLC), T13 is invoked automatically by the tool orchestration infrastructure — product agents do not invoke T13 directly; T13 is applied to their tool calls at the infrastructure layer.

**Adversarial pattern library.** T13 maintains a versioned adversarial pattern library — a set of known prompt injection patterns, context manipulation patterns, and instruction override patterns. The library is updated when new patterns are discovered through red-team exercises or production adversarial incidents. Pattern library updates are governed as APLC tooling changes per the Stage 6 meta-governance requirements: each update is versioned, the behavioral impact is assessed, and Stage 5 monitoring is notified. The current pattern library version is recorded in the pre-invocation audit log entry for every tool call.

**Schema registry.** T13 maintains a schema registry that maps each tool identifier and version to its expected output schema, derived from the composite state manifest's tool manifest component. When T13 receives a tool response, it retrieves the expected schema for the invoked tool and validates the response against it. Schema validation is strict by default (extra fields are flagged, missing required fields block the response); strict validation may be relaxed to permissive (extra fields allowed, missing optional fields only warned) for specific tool-version pairs through a product owner decision recorded in the schema registry.

**Audit requirement.** Every T13 invocation generates two audit log entries: a pre-sanitization entry (tool identifier, invocation identifier, raw response schema summary, calling agent identity) and a post-sanitization entry (sanitization result, provenance label applied, pattern screening result, final disposition). Both entries are filed to the AGKB audit trail before the sanitized response (or failure record) is returned to the calling agent or infrastructure. Sanitization failures are automatically escalated to the HITL adversarial queue with a 1-hour SLO.

**Failure mode.** If T13 itself fails (unavailable, schema registry unreachable, pattern library unavailable), the tool response must not be passed through unsanitized. The tool orchestration infrastructure must treat T13 failure as a tool failure per the "Tool failures escalate to human" principle: halt the tool-dependent workflow step, log the T13 failure to the AGKB audit trail, and notify the product owner. A T13 failure is a governance infrastructure degradation event; operating without sanitization is not an acceptable fallback. This follows the "severity asymmetry" principle established in Stage 6 meta-governance: a governance system that under-reports problems generates false confidence and is a more severe failure than one that over-reports.

---

## Access Control Matrix

The matrix below specifies which governance agents are authorized to invoke each tool. Y = authorized; N = not authorized; R = restricted (authorized with additional conditions specified in the tool definition above). T13 is additionally invoked automatically at the infrastructure layer for product agents; the Y entries for governance agents reflect their direct invocation authorization.

| Governance Agent | T01 Reader | T02 Eval Runner | T03 CSH Inspector | T04 Fingerprint | T05 AGKB Writer | T06 AGKB Query | T07 Reg Lookup | T08 Source Monitor | T09 HITL Dispatch | T10 Audit Appender | T11 Sandbox | T12 Incident Writer | T13 Sanitization Boundary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Regulatory Classification Agent | Y | N | N | N | R | Y | Y | N | Y | Y | N | N | Y |
| Use-Case Elicitation Agent | Y | N | N | N | R | Y | N | N | Y | Y | N | N | Y |
| Constraint Consistency Checker | Y | N | N | N | R | Y | Y | N | Y | Y | N | N | Y |
| Behavioral Evaluation Swarm Coordinator | Y | Y | N | N | R | Y | N | N | Y | Y | Y | N | Y |
| Red-Team Adversary Agent | Y | Y | N | Y | R | Y | N | N | Y | Y | Y | N | Y |
| HITL Routing Intelligence Agent | Y | N | N | N | R | Y | N | N | Y | Y | N | Y | Y |
| Behavioral Drift Monitor Agent | Y | N | Y | Y | R | Y | N | N | Y | Y | N | Y | Y |
| Foundation Model Impact Prediction Agent | Y | N | Y | N | R | Y | N | Y | Y | Y | N | N | Y |
| Knowledge Staleness Sentinel | Y | N | N | N | R | Y | N | Y | Y | Y | N | N | Y |
| Retirement Lessons Extraction Agent | Y | N | N | N | R | Y | N | N | Y | Y | N | N | Y |

**R conditions for T05 (AGKB Writer).** The artifact types each agent is authorized to write:

| Governance Agent | Authorized Artifact Types for T05 |
| --- | --- |
| Regulatory Classification Agent | Regulatory classification records, conformity assessment records |
| Use-Case Elicitation Agent | Use-case coverage maps, behavioral contract drafts |
| Constraint Consistency Checker | Constraint conflict reports, consistency verification records |
| Behavioral Evaluation Swarm Coordinator | Evaluation run records, evaluation clearance report drafts, coverage summaries |
| Red-Team Adversary Agent | Red-team reports, adversarial finding records, fingerprint snapshots |
| HITL Routing Intelligence Agent | Routing decision records, HITL queue health reports |
| Behavioral Drift Monitor Agent | Drift monitoring records, behavioral fingerprint snapshots, drift classification records |
| Foundation Model Impact Prediction Agent | Impact prediction records, model update assessment reports |
| Knowledge Staleness Sentinel | Staleness reports, source change records |
| Retirement Lessons Extraction Agent | Lessons-learned records, retirement decision summaries |

---

## Tool Invocation Audit Protocol

Every tool invocation in the governance stack must produce a complete audit entry. This section defines the mandatory fields for audit entries and the protocol for cases where audit log writing fails.

### Mandatory Audit Entry Fields

All tool invocations must record:

1. **Invocation identifier** — a unique identifier for this specific tool invocation, distinct from the tool identifier and the artifact identifiers it produces.
2. **Calling agent identity** — the governance agent that invoked the tool, including its version and the CSH of its own composite state at the time of invocation.
3. **Target agent system identifier** — the agent system under governance that this invocation concerns. All governance tool invocations concern a specific agent system; invocations that do not specify a target are invalid.
4. **Tool identifier and version** — which tool was invoked and which version of that tool was active at the time of invocation.
5. **Invocation timestamp** — the wall-clock timestamp at which the invocation was submitted.
6. **Input hash** — a cryptographic hash of the complete input provided to the tool. The hash enables verification that the input record matches what was actually submitted, without requiring the full input content to be stored in every audit entry.
7. **Output hash** — a cryptographic hash of the complete output returned by the tool. Recorded upon completion, not at submission.
8. **Completion timestamp** — the wall-clock timestamp at which the tool returned output.
9. **Human approval record identifier** — where the tool invocation or the action enabled by the tool output required human approval, the identifier of the human decision record produced by T09 (HITL Dispatch). Where no human approval was required, this field is explicitly marked as not-required, not left empty.
10. **Outcome classification** — success, failure, partial (output returned but outside expected schema), or timeout.

### Audit Log Failure Protocol

If the audit log write fails at the time of a tool invocation, the tool invocation must not proceed. The sequence is: (1) attempt audit pre-log; (2) if pre-log fails, generate an immediate alert to the governance oversight function; (3) halt the invocation; (4) await human decision on whether to proceed without the pre-log, with that decision itself recorded in a secondary audit mechanism. A tool invocation that proceeds without a successful pre-log entry is an ungoverned action. The governance validity of any output produced by an ungoverned action is compromised and must be assessed by the accountable human before that output informs any gate condition.

---

## Tool Failure Handling

When a governance tool fails — returns an error, returns output outside its expected schema, times out, or returns output that is internally inconsistent — the governance agent that made the invocation must execute the following protocol. The protocol is the same for all tools, with escalation paths that vary by tool type.

### Immediate Steps (All Tools)

1. Log the failure to the AGKB audit trail via T10 within 60 seconds of detecting the failure. The failure log entry includes: the invocation identifier, the failure type, the error message or anomaly description, and the timestamp. If T10 itself is unavailable, the failure log is written to the secondary audit log maintained outside the AGKB.

2. Halt the governance workflow step that depended on the failed tool output. A governance workflow that proceeds with an assumption substituted for a tool output — or with a stale prior output used as a proxy — is not a governed workflow. The substitution must be a human decision, not an agent inference.

3. Notify the responsible human governance overseer via the secondary notification channel (not via T09, which may itself be affected if the failure is infrastructure-wide). The notification includes the failed tool identifier, the workflow step that is blocked, the governance consequence (which gate condition or decision is blocked), and the agent system under governance.

### Escalation Paths by Tool Type

**T01, T06 (Read-only AGKB access).** If read access fails, the governance agent may use its most recent cached version of the requested artifact, provided: the cache timestamp is within 24 hours; the cache is labeled as a cached artifact in any output produced using it; and the cache usage is flagged in the audit log. For gate condition assessments, a cached artifact is not equivalent to a current retrieval — the human reviewing the gate must be notified that cached data was used and must confirm acceptance.

**T02, T11 (Evaluation execution).** If evaluation execution fails, the evaluation run is invalidated. There is no fallback; partial evaluation results cannot substitute for a complete run. The evaluation must be rescheduled, and if the failure blocks a gate decision, the gate is delayed rather than decided on incomplete evaluation evidence.

**T03, T04 (CSH and fingerprint reads).** If CSH or fingerprint retrieval fails, behavioral drift classification is blocked. The Behavioral Drift Monitor Agent must notify the product owner that drift monitoring is degraded and cannot produce a current assessment until the tool is restored. Do not use the most recent successful measurement as a proxy for a current measurement — this masks the monitoring gap.

**T07 (Regulatory lookup).** If regulatory lookup fails, any governance action that depends on current regulatory requirements is suspended until the tool is restored or a human legal reviewer provides the regulatory information directly. Regulatory classification decisions and conformity assessments may not proceed on the basis of the previous lookup if the lookup was more than 30 days prior.

**T09 (HITL Dispatch).** If HITL Dispatch fails, the governance agent must use the secondary human escalation channel. Every governance agent deployment must have a secondary escalation channel defined before it enters production. A governance agent that cannot reach human review because T09 failed and no secondary channel exists must halt all governance workflow steps that require human review until the channel is restored.

**T10 (Audit Trail Appender).** If T10 fails, the audit trail integrity is compromised. The governance oversight function must be notified immediately. All governance workflow steps that would produce audit entries must halt. The secondary audit log receives all entries that cannot be appended to the primary trail. Recovery from a T10 failure requires reconciling the secondary log against the primary trail before governance workflows resume.

**T12 (Incident Record Writer).** If T12 fails during an active incident, the incident record must be created manually by the governance oversight function. The governance agent must notify the product owner, the accountable human, and the governance oversight function immediately via all available secondary channels. An incident that cannot be formally recorded is not thereby less urgent; it is more urgent, because its response is now ungoverned.

**T13 (Tool Response Sanitization Boundary).** If T13 fails, the tool response must not be passed through unsanitized under any circumstances. The tool orchestration infrastructure halts the tool-dependent workflow step, logs the T13 failure to the AGKB audit trail, and notifies the product owner. There is no permissive fallback: bypassing sanitization to preserve workflow continuity is not an acceptable response to a T13 failure. A T13 failure is a governance infrastructure degradation event with the same severity as a T10 (Audit Trail Appender) failure. See the T13 tool definition above for the full failure mode specification.

---

## Tool Versioning and Evaluation

Governance tools are governed artifacts of the APLC. They are not exempt from the governance requirements they support. An unversioned, unevaluated governance tool is a source of governance risk, not a governance control.

### Versioning Requirements

Each governance tool must have:

- A version label following the same scheme as other APLC artifacts: a semantic version (major.minor.patch) with an associated content hash.
- A behavioral specification that defines the tool's expected behavior, input-output contract, error handling, and authorization enforcement. The behavioral specification is stored in the AGKB and referenced in the tool's version record.
- A version history maintained in the AGKB recording every version change, the nature of the change, the change approval, and the governance agents that are authorized for the new version.
- A composite state relationship: when a governance tool version changes, the composite state of any governance agent that uses that tool changes, and the AGKB records this dependency.

### Evaluation Requirements

Before any governance tool version is accepted into production use:

- **Layer 1 (engineering evaluation):** The tool's functional behavior must be verified deterministically — correct input acceptance, correct error rejection, authorization enforcement verification, audit log generation confirmation.
- **Layer 2 (behavioral coverage evaluation):** The tool's behavior must be evaluated across a representative distribution of valid inputs, invalid inputs, and edge cases. The evaluation must confirm that the tool behaves consistently with its behavioral specification and that its authorization enforcement does not produce false authorizations or false denials at a rate above the specified threshold.
- **Layer 3 (adversarial evaluation):** Each governance tool that accepts external input (including tool outputs from agent systems under governance) must be evaluated for susceptibility to adversarial inputs that could corrupt its output, bypass its authorization enforcement, or produce misleading audit records. A governance tool that can be manipulated by the agent system it is governing is a structural governance failure.

Governance tool updates follow the same composite state change protocol as agent product updates: the change is notified to Stage 5 monitoring equivalents before execution, a new version baseline is established post-change, and the governance agents that use the tool are validated against the new version before the update is accepted in production.

### Tool Evaluation Cadence

Governance tools must be re-evaluated on the following triggers:

- Any version change to the tool, regardless of the nature of the change.
- Any change to the authorization policy that governs the tool's access control.
- Any incident in which a governance tool produced incorrect output, missed a required audit entry, or was invoked outside its authorization scope.
- Annually, as a baseline re-evaluation, regardless of whether any of the above triggers have occurred.

---

*See also: [[aplc]] (lifecycle overview and governance agent participation), [[agent-behavioral-evaluation]] (the evaluation framework that T02 and T11 execute), [[agent-operations]] (Stage 5 operations governance including HITL management), [[agent-composite-versioning]] (CSH and composite state that T03 retrieves), [governance observability](observability.md) (governance process observability that monitors the tool stack), [governance queries](queries.md) (canonical queries executed via T06). AGKB artifact type taxonomy: maintained in the AGKB itself and referenced by T05 authorization enforcement.*
