# APLC Governance Process Observability

*Governance infrastructure document for the Agentic Product Lifecycle. Specifies the observability system applied to the APLC governance process itself — the meta-level application of P9 (Observability is accountability) to governance as an operational system. Audience: governance architects, risk officers, product owners, and human governance oversight functions.*

*Related documents: [[aplc]] (lifecycle overview), [[agent-operations]] (Stage 5 behavioral observability, which this document extends to the governance layer), [governance tool stack](tool-stack.md) (governance tool stack, whose operations this document monitors), [governance queries](queries.md) (canonical queries that surface governance health data).*

---

## Governance Observability Rationale

The manifesto's P9 principle — Observability is accountability — applies to the APLC governance process as fully as it applies to the agent products the APLC governs. A governance process that cannot be observed cannot be held accountable. A governance process that is not measured cannot be improved. A governance process that does not surface its own failures in time to correct them is not a governance process — it is a procedure that provides the appearance of governance while its actual function degrades undetected.

Four failure modes make governance observability necessary. Each one is real, not hypothetical; each one can occur in a well-intentioned governance program that lacks the meta-observability layer this document specifies.

**Governance drift.** The governance process's behavior changes not because of intentional design revision but because of accumulated informal adaptations, reviewer calibration degradation, resource pressure, or organizational norm shift. Governance drift is the meta-level analog of behavioral drift in agent products: the process is no longer doing what its specification says it does, but no single decision point reveals the divergence. Only a longitudinal view of governance metrics, compared against the governance process specification, can detect it.

**Process performance degradation.** Gate decisions take longer, evaluation coverage narrows, HITL queues back up, and incident response times extend — each change small enough to appear within normal variation, collectively representing a governance capability that has fallen below its design level. Performance degradation in governance is self-concealing: a governance team under resource pressure is also a governance team that has less capacity to investigate whether its own performance is degrading. External measurement is the remedy.

**Bottleneck detection.** Governance bottlenecks accumulate at specific lifecycle stages when process design does not match operational reality — a gate condition that requires artifacts that take longer to produce than the gate's nominal timeline; a HITL routing design that concentrates review volume on a reviewer pool that is insufficient for peak load; a regulatory lookup dependency that blocks gate clearance when the lookup service is slow. Bottlenecks that are not detected by observability appear as delays attributed to individual cases rather than structural problems.

**Accountability audit.** When a governance failure produces a harm event — a product that passed governance gates but failed in deployment in ways the governance should have detected — the audit trail must be able to reconstruct what governance actors did, what data they had access to, and whether the governance process was functioning at the time. Without governance observability, the audit reconstructs a narrative. With governance observability, the audit produces evidence.

The observability system specified in this document is not optional for APLC implementations at Governance Level 3 and above (as defined in `aplc-guide.md`). For Level 1 and Level 2 implementations, the gate metrics and HITL performance metrics are the minimum viable implementation.

---

## Governance Process Metrics

Governance metrics are organized by the APLC stage they measure. Each metric is defined with: what it measures, how it is computed, the measurement frequency, and the signal it provides when it deviates from baseline.

---

### Stage 1–2: Conceive and Specify Behaviorally

**Time-to-classification.** The elapsed time from agent product brief submission to completed regulatory classification record in the AGKB, including the legal review step. Measured per product. Aggregated as the rolling mean and 90th percentile across all products completing Stage 1 in the measurement period. A rising 90th percentile indicates a bottleneck in the classification process — either the regulatory lookup capability is degraded, legal review capacity is insufficient, or the product brief quality is too low to enable efficient classification. Measurement frequency: per-product at Stage 1 completion; aggregate weekly.

**Specification completeness score.** The proportion of required behavioral specification sections that are complete and internally consistent at Behavioral Specification Gate review, as assessed by the Constraint Consistency Checker. Computed as: sections complete and consistent at first submission / total required sections. A score below 0.90 at first submission indicates that Stage 2 work is reaching the gate before it is ready — a process discipline issue, not a specification difficulty issue. Measurement frequency: per-product at Behavioral Specification Gate; aggregate monthly.

**Constraint conflict rate.** The proportion of behavioral specifications submitted to the Behavioral Specification Gate that contain at least one constraint conflict identified by the Constraint Consistency Checker. A conflict rate above 10% indicates a systematic issue in how behavioral specifications are authored — either the authoring guidance is insufficient, the use-case elicitation is not sufficiently informing the specification, or domain-regulatory constraint integration is failing. Measurement frequency: per-product at submission; aggregate monthly.

**Use-case coverage ratio.** For each behavioral specification submitted to the Behavioral Specification Gate: the number of use-case categories in the use-case coverage map (core, edge, boundary, out-of-scope, adversarial) that have corresponding behavioral contracts, divided by the total number of use-case categories identified by the Use-Case Elicitation Agent. A coverage ratio below 1.0 means behavioral contracts are missing for identified use cases — the specification is incomplete at a structural level. Measurement frequency: per-product at Behavioral Specification Gate submission.

**Behavioral specifications pending regulatory review.** The count of behavioral specifications that have not been reviewed since the most recent regulatory update affecting the agent system's regulatory classification. This is a staleness metric: it measures the backlog of specifications that may no longer align with current regulatory requirements. A count above zero requires a scheduled review plan. A count growing faster than the review rate indicates a governance backlog accumulation. Measurement frequency: weekly, triggered on each regulatory update that affects any active agent system classification.

---

### Stage 3: Build and Evaluate

**Evaluation coverage percentage by layer.** For each evaluation layer (L1, L2, L3, L4): the percentage of required evaluation cases that have been executed and have current results, as of the most recent evaluation run. Required evaluation cases are derived from the behavioral specification's use-case coverage map and adversarial scenario inventory. A layer whose coverage percentage is below the minimum bar defined in [[agent-behavioral-evaluation]] cannot clear the Behavioral Release Gate regardless of other factors. Measurement frequency: per evaluation run; aggregate trend tracked weekly during Stage 3 build cycles.

**Red-team findings per evaluation cycle.** The count of red-team findings by severity (Critical, High, Medium, Low) per red-team exercise, tracked longitudinally across release cycles for the same agent system. A finding count that is consistently at zero across multiple release cycles is a signal of either a very well-specified agent or a red-team that is not testing effectively — the Evaluation Capture Detection framework in [[agent-behavioral-evaluation]] applies. A finding count that spikes on a specific release cycle correlates with a composite state change that affected the agent's adversarial robustness. Measurement frequency: per red-team exercise; trend tracked per release cycle.

**Gate decision latency.** The elapsed time from submission of all required gate condition evidence to the Behavioral Release Gate decision (approve or reject). Measured separately for approved and rejected gates. A rising latency for approvals indicates a process bottleneck in evidence review. A rising latency for rejections indicates either that rejection decisions are being delayed, or that the remediation and resubmission cycle is lengthening. Target: gate decision within 5 business days of complete evidence submission for standard-risk products; 10 business days for high-risk products requiring external review. Measurement frequency: per gate decision; aggregate monthly.

**Probabilistic gate calibration accuracy.** The Behavioral Evaluation Swarm Coordinator produces a probabilistic pass confidence interval as part of the evaluation clearance report. This metric measures how well-calibrated those confidence intervals are: the proportion of confidence intervals that contain the true gate outcome (pass or fail) at each confidence level. A confidence interval that systematically overstates certainty — products predicted to pass with high confidence that then fail on post-release behavioral monitoring — indicates a calibration failure in the evaluation methodology. This metric can only be computed retrospectively, by comparing pre-gate confidence intervals against post-release behavioral monitoring outcomes. Measurement frequency: quarterly, requiring at least one full production cycle of data.

---

### Stage 4: Release

**Release gate decision latency.** The elapsed time from the product owner's submission of the evaluation clearance report to the Operational Readiness Gate decision. This is the Stage 4 extension of the Stage 3 gate decision latency metric. Target latency: 3 business days for standard-risk products; 7 business days for high-risk products. A rising latency at the Stage 4 gate, where the Stage 3 gate latency is stable, indicates a bottleneck in the conformity assessment, composite state manifest filing, or transparency infrastructure verification steps specific to Stage 4. Measurement frequency: per gate decision; aggregate monthly.

**Waiver rate.** The proportion of behavioral release gate conditions for which a waiver is granted rather than the condition being satisfied in full, across all products in the gate pipeline during the measurement period. A rising waiver rate indicates that governance conditions are being treated as negotiable rather than as release requirements. Waiver governance is specified in [[waiver-governance]]; this metric monitors whether the waiver process is being used as designed (a controlled exception for genuinely justified cases) or as a routinely available bypass. Measurement frequency: monthly.

**Waiver expiry compliance rate.** The proportion of active waivers that are resolved (condition satisfied or waiver formally renewed with updated justification) before their expiry date, across all active waivers in the current period. A compliance rate below 100% means that expired waivers are present in the governance record without resolution — conditions that were acknowledged as not fully satisfied and that have been allowed to lapse without follow-up. An expired waiver is a governance debt entry. Measurement frequency: weekly, triggered by approaching and passing waiver expiry dates.

---

### Stage 5: Operate

**HITL routing accuracy.** The proportion of cases routed by the HITL Routing Intelligence Agent to the correct review tier (domain, priority, volume) and reviewer pool, as assessed by retrospective review quality analysis. Computed as: cases where the routing decision was confirmed as appropriate upon review completion / total cases routed. A declining routing accuracy indicates that the HITL Routing Intelligence Agent's routing logic is diverging from the actual case distribution — cases are arriving that are different from the distribution on which the routing was calibrated, or the routing agent itself has drifted. Measurement frequency: weekly.

**Reviewer calibration score.** A measure of reviewer consistency relative to the behavioral specification: the proportion of HITL review decisions that agree with an independent expert assessment of the same case. Maintained per reviewer and per reviewer pool. A declining calibration score for a specific reviewer indicates reviewer drift — their standard is diverging from the specification. A declining calibration score for the entire reviewer pool indicates specification drift or shared blind spot development, which requires pool rotation and potential specification revision. Measurement frequency: computed monthly from calibration case sets introduced into the review queue.

**Drift detection latency.** The elapsed time from the moment a behavioral drift event begins (as determined retrospectively from the behavioral monitoring record) to the moment the drift is classified and a response protocol activated. Measured per drift detection event. Target latency: continuous monitoring signals (safety, adversarial) detected within 1 hour; daily signals (behavioral envelope compliance) detected within 24 hours; weekly signals (output quality rate, response distribution) detected within 7 days of the measurement that reveals the drift. A latency exceeding these targets indicates that monitoring instrumentation is insufficient, measurement cadence is too low, or the drift classification workflow has a processing bottleneck. Measurement frequency: per drift detection event; aggregate trend tracked monthly.

**Incident mean-time-to-detection (MTTD).** The elapsed time from the moment an incident condition becomes present in the production system to the moment it is formally classified as an incident. Measured per incident class (quality, behavioral, safety, persona, adversarial). Safety and adversarial incidents require MTTD below 1 hour; behavioral incidents below 4 hours; quality incidents below 24 hours. An MTTD that systematically exceeds these targets for a specific incident class indicates that detection instrumentation for that class is insufficient. Measurement frequency: per incident; aggregate by class monthly.

**Incident mean-time-to-resolution (MTTR).** The elapsed time from incident classification to incident closure (root cause identified, corrective action deployed, behavioral verification completed). Measured per incident class and severity tier. MTTR measures the full resolution cycle, not just the immediate containment action — an incident where the agent is stabilized but the underlying cause is not identified and corrected is not resolved. Measurement frequency: per incident; aggregate by class monthly.

---

### Stage 6: Maintain

**Model update impact prediction accuracy.** The Foundation Model Impact Prediction Agent produces an impact assessment when a foundation model update is detected. This metric measures the calibration of those predictions: the proportion of predicted behavioral impacts that materialize in behavioral monitoring post-update, and the proportion of impacts that materialize without having been predicted. Computed retrospectively after each model update cycle completes its post-update behavioral verification. A prediction accuracy below 0.70 indicates that the impact assessment methodology needs recalibration against updated model behavior patterns. Measurement frequency: per model update cycle; aggregate quarterly.

**Recalibration effectiveness.** For each Stage 6 recalibration event: the change in the behavioral quality metrics (output quality rate, behavioral envelope compliance rate, task success rate) from pre-recalibration measurement to the first post-recalibration measurement at the same cadence. Computed as a signed delta — positive means improvement, negative means the recalibration made things worse. A recalibration that produces negative deltas is a corrective action that caused harm; the root cause must be investigated. A recalibration that produces near-zero deltas addressed the wrong component or was too small in scope. Measurement frequency: per recalibration event.

**Knowledge staleness mean age.** The mean age (in days) of the oldest document in each knowledge base source across all active agent systems, weighted by the knowledge domain's rate of change classification (high, medium, low). A rising staleness mean age indicates that the Knowledge Staleness Sentinel is detecting but the knowledge refresh rate is not keeping pace with source changes. For high-change-rate domains, a staleness threshold of 30 days is the maximum before the knowledge base is classified as stale. For low-change-rate domains, 180 days. Measurement frequency: weekly.

**GDPR erasure compliance rate.** For agent systems with memory state components: the proportion of data subject erasure requests (including right-to-be-forgotten requests arising from safety incidents) that are completed within the regulatory deadline (72 hours for safety incidents; 30 days for standard erasure requests). A compliance rate below 100% is a regulatory exposure event, not merely a performance gap. Each missed erasure deadline must be individually documented with the reason for the miss and the corrective action taken. Measurement frequency: per erasure request; aggregate monthly.

---

### Stage 7: Retire

**Retirement decision latency.** The elapsed time from the first formal retirement trigger condition being met (as defined in [[agent-retirement]]) to the product owner's retirement decision record being filed. A retirement trigger that is met but not acted upon because the retirement decision is delayed is a governance debt entry: the product is operating beyond the point at which a governed review should have produced a decision. Target: retirement decision initiated within 15 business days of the first trigger condition being confirmed. Measurement frequency: per retirement event.

**Lessons extraction completeness score.** The Retirement Lessons Extraction Agent produces a lessons-learned record as part of Stage 7. The completeness score measures the proportion of required record sections (incident history analysis, evaluation portfolio effectiveness assessment, specification gap catalogue, behavioral drift history, regulatory examination findings if applicable) that are present and non-empty at the time the retirement record is filed to the AGKB. An incomplete lessons record means that the insights from this agent product's lifecycle are not fully captured for the portfolio — the governance value of Stage 7 is lost. Target: completeness score of 1.0 (all sections complete) at retirement record filing. Measurement frequency: per retirement event.

---

## Governance Health Dashboard

The governance health dashboard provides a real-time and longitudinal view of the APLC governance process across four panels. The dashboard is a required operational artifact for APLC implementations at Governance Level 3 and above. It is reviewed by the governance oversight function weekly and by the product owner monthly. Anomalies in any panel trigger escalation per the Governance Anomaly Detection section below.

### Panel 1 — Gate Pipeline Health

Stage-by-stage throughput and latency for all products currently in the governance pipeline.

| Stage | Metric | Current | 30-Day Trend | SLA Target |
| --- | --- | --- | --- | --- |
| Stage 1–2 | Products in pipeline | Count | Trend | — |
| Stage 1–2 | Mean time-to-classification | Days | Trend | Per risk tier |
| Stage 1–2 | Specification completeness score | Mean | Trend | ≥ 0.90 |
| Stage 3 | Evaluation coverage (L1/L2/L3/L4) | % per layer | Trend | Per layer minimum |
| Stage 3 | Gate decision latency | Days | Trend | 5 / 10 days |
| Stage 4 | Release gate decision latency | Days | Trend | 3 / 7 days |
| Stage 4 | Active waivers | Count | Trend | — |
| Stage 4 | Waiver expiry compliance | % | Trend | 100% |

The gate pipeline health panel includes a visual pipeline view showing each product in the governance pipeline, its current stage, time in stage, and any blocked conditions. Products that have exceeded the stage time target for their risk tier are highlighted.

### Panel 2 — Evaluation Portfolio Health

Coverage and quality across the four evaluation layers and the red-team program.

| Metric | Current | 90-Day Trend |
| --- | --- | --- |
| Layer 1 coverage (% of required engineering evaluations passing) | % | Trend |
| Layer 2 core use-case coverage (portfolio mean) | % | Trend |
| Layer 2 edge case coverage (portfolio mean) | % | Trend |
| Layer 3 adversarial scenario coverage | % | Trend |
| Layer 4 human evaluation sample rate | % | Trend |
| Red-team findings: Critical (last cycle, all products) | Count | Trend |
| Red-team findings: High (last cycle, all products) | Count | Trend |
| Evaluation capture detection signals (active) | Count | — |

The evaluation portfolio health panel includes a per-product view of evaluation portfolio completeness, enabling the governance oversight function to identify which products in the portfolio are approaching their gate with incomplete evaluation evidence.

### Panel 3 — Operational Governance Health

HITL routing performance, drift detection performance, and incident management across all operational agent products.

| Metric | Current | 30-Day Trend | SLA Target |
| --- | --- | --- | --- |
| HITL routing accuracy | % | Trend | ≥ 90% |
| Reviewer calibration score (portfolio mean) | Score | Trend | ≥ 0.80 |
| HITL queue SLO compliance: Safety escalations | % | Trend | ≥ 99% |
| HITL queue SLO compliance: Quality samples | % | Trend | ≥ 90% |
| Drift detection latency: Continuous signals | Mean hours | Trend | < 1 hour |
| Drift detection latency: Daily signals | Mean hours | Trend | < 24 hours |
| Incident MTTD: Safety class | Mean hours | Trend | < 1 hour |
| Incident MTTR: All classes | Median days | Trend | Per class SLA |
| Active governance capture signals (HITL) | Count | — | 0 |

### Panel 4 — Knowledge Base Health

Staleness distribution and artifact age profile across the AGKB and agent system knowledge bases.

| Metric | Current | 30-Day Trend |
| --- | --- | --- |
| Knowledge staleness mean age (weighted) | Days | Trend |
| Knowledge sources exceeding high-change-rate threshold | Count | Trend |
| Knowledge sources exceeding low-change-rate threshold | Count | Trend |
| Behavioral specifications pending regulatory review | Count | Trend |
| GDPR erasure requests: Pending | Count | — |
| GDPR erasure requests: Compliance rate (30-day) | % | Trend |
| Governance tool evaluations overdue | Count | — |

---

## Governance Anomaly Detection

Governance anomalies are patterns in governance metrics that indicate the governance process is failing, not merely performing below target. The distinction matters: a gate decision latency that is 20% above target is a performance issue. A gate that passes every product submitted to it for six consecutive months is an anomaly that may indicate the governance process has become non-functional. Both require attention; they require different responses.

The following patterns constitute governance anomalies. Each has a detection threshold and a required escalation response.

**Gate rubber-stamping.** A 100% gate pass rate — all products submitted to a gate pass on first submission — sustained for more than three consecutive months across a product portfolio of five or more products. In a functioning governance program with a non-trivial behavioral specification gate, some proportion of submissions will be incomplete or will require remediation. A 100% first-submission pass rate either means the gate conditions are set so low that they cannot fail, or that submissions are being approved without full review of gate condition evidence. Required response: governance oversight function conducts a retrospective review of a sample of gate records from the anomaly period; at least one external reviewer reviews a sample of behavioral specifications against the gate conditions that approved them.

**Evaluation coverage plateau.** Layer 2 or Layer 3 coverage percentage that is stable within 2% for more than four consecutive measurement periods, for an agent system that has been actively releasing during that period. Active releasing means the composite state has changed — new evaluation cases should be required. Coverage that does not change as the agent system evolves indicates either that new behavioral territory is not being covered by evaluation, or that the coverage metric itself is not being correctly computed against the current behavioral specification. Required response: evaluation team lead reviews whether the evaluation portfolio is being updated with each composite state change; governance oversight function audits one evaluation portfolio against the current behavioral specification to verify coverage computation accuracy.

**HITL override rate spike.** HITL override rate increasing more than 2× the rolling baseline over a 14-day period, without a corresponding change in input volume or a composite state change that would explain increased agent failure. As defined in [[agent-operations]], this triggers an immediate behavioral quality audit. At the governance observability level, a spike that is not accompanied by a corresponding Stage 5 response within 4 hours is itself an anomaly — the monitoring system detected the spike but the operational response workflow did not activate. Required response: governance oversight function reviews whether the behavioral quality audit was initiated and whether the product owner was notified within the required window.

**Reviewer calibration degradation.** Reviewer calibration score declining below 0.70 for any reviewer or below 0.80 for the full reviewer pool, sustained for two consecutive monthly measurements. This is a stronger signal than a single low-calibration reading, which may be statistical noise. A sustained decline indicates that the reviewer pool's standard is diverging from the behavioral specification — either the specification has evolved and reviewers have not been retrained, or reviewers are developing shared blind spots. Required response: pool rotation per the HITL governance capture detection protocol in [[agent-operations]]; mandatory specification re-briefing for all reviewers before the next evaluation cycle; an external reviewer is added for calibration verification.

**Governance tool audit gap.** Any 24-hour period in which the audit trail records zero tool invocations for an agent system that is in an active governance workflow stage. An active governance workflow that generates no audit entries is a governance integrity failure: either the governance tools are not being invoked, invocations are not being logged, or the audit trail is not functioning. Required response: governance oversight function investigates within 4 hours of detecting the audit gap; the investigation determines whether governance activities occurred outside the tool stack (ungoverned activities) or whether the audit logging infrastructure failed.

**Waiver accumulation.** The total count of active waivers across the portfolio growing for three consecutive monthly periods. A growing waiver count means that gate conditions are being deferred faster than they are being resolved. Over time, a portfolio with a large waiver backlog represents a governance debt that is operationally real but not visible in the gate pass/fail record. Required response: governance oversight function reviews all active waivers to confirm each has a current, non-expired justification and a resolution plan; waivers without a resolution plan within their expiry window are escalated to the accountable human for a decision on whether to satisfy the condition or retire the product.

---

## Governance Audit Trail Requirements

The governance audit trail is the primary evidence base for regulatory examination of APLC governance. It is distinct from the AGKB artifact store: artifacts in the AGKB can be updated and versioned; the audit trail is append-only and immutable. The audit trail records what happened; the AGKB records what was decided.

### What Must Be Logged

Every governance action that produces a governance outcome must be logged to the audit trail. Governance outcomes include: gate condition assessments (pass, fail, or waiver); tool invocations and their results; HITL dispatch events and human decision records; incident classifications and response decisions; specification gap signals and evaluation gap signals; waivers granted, renewed, or allowed to expire; retirement decisions; and governance anomaly detections and their escalation responses.

The audit trail does not log internal agent reasoning processes or intermediate computational steps. It logs the inputs, outputs, and decisions that constitute the governance record — the evidence that a human auditor would need to verify that governance occurred as specified.

### Retention

Audit trail records for each agent system must be retained from the Conception Gate through the later of: (a) ten years after the Operational Readiness Gate for agent products classified as high-risk under the EU AI Act; (b) seven years after the retirement date for all other agent products; or (c) the resolution of any regulatory investigation or legal proceeding that references the agent system, without time limit until resolution.

Retention is not archiving. Archived records that cannot be retrieved within 48 hours of a regulatory request are not retained in the governance sense — they are stored in a way that does not support regulatory accountability. The audit trail must be retrievable, searchable by agent system identifier and time range, and producible in a format suitable for external regulatory examination.

### Immutability Requirements

The audit trail is append-only. Once a record is written, it cannot be modified, deleted, or supplemented with corrections. Corrections to governance records are made by appending a correction record that references the original record, documents the error, and provides the corrected information. The original record and the correction record are both present in the trail; the auditor can see both.

Immutability is enforced at the infrastructure level, not only by convention. An audit trail whose immutability relies on team discipline rather than technical enforcement is not an immutable audit trail. The technical enforcement mechanism must be documented and verified before the governance infrastructure is accepted into production.

### Access Controls on Audit Records

The audit trail is readable by: the governance oversight function; external auditors with appropriate authorization; legal and risk functions when required for regulatory response; and the product owner for products under their responsibility. The audit trail is not readable by the governance agents themselves — governance agents write to the audit trail via T10 but cannot query or read it. This prevents circular governance: a governance agent should not be able to assess its own audit record to adjust its behavior.

Write access is restricted exclusively to T10 (Audit Trail Appender). No other write path to the audit trail is authorized. Evidence of a write to the audit trail that did not originate from T10 is a governance infrastructure security event.

---

## Governance SLA Definitions

Governance SLAs are time-bounded commitments for governance process steps. They are not aspirational targets; they are operational commitments with defined consequences when breached. An SLA breach that is not escalated is a governance failure compounded by a detection failure.

### Gate Decision Latency by Risk Tier

| Gate | Standard Risk | High Risk (EU AI Act Annex III) |
| --- | --- | --- |
| Conception Gate | 3 business days | 5 business days |
| Behavioral Specification Gate | 5 business days | 10 business days |
| Behavioral Release Gate | 5 business days | 10 business days |
| Operational Readiness Gate | 3 business days | 7 business days |

Latency is measured from the moment all required gate condition evidence is submitted and confirmed complete — not from the moment the product team believes submission is complete. A gate decision clock does not start on an incomplete submission.

### Drift Detection Latency by Autonomy Tier

| Autonomy Tier | Safety/Adversarial Signals | Behavioral Envelope Signals | Quality Rate Signals |
| --- | --- | --- | --- |
| Tier 1 — Observe | 4 hours | 48 hours | 7 days |
| Tier 2 — Branch | 2 hours | 24 hours | 7 days |
| Tier 3 — Commit | 1 hour | 12 hours | 48 hours |
| Tier 4 — Operate (autonomous) | 30 minutes | 4 hours | 24 hours |

Tier 4 latency requirements reflect the higher risk of autonomous agents operating outside specification: the time window within which undetected out-of-spec behavior can compound is shorter, so detection must be faster. A Tier 4 deployment whose monitoring infrastructure cannot meet the 30-minute safety signal detection latency is not ready for production.

### HITL Response Time by Escalation Level

| Escalation Level | Response Time SLA | Consequence of Breach |
| --- | --- | --- |
| Immediate (safety, adversarial incidents) | 30 minutes | Automatic escalation to accountable human and governance oversight function |
| Urgent (behavioral incidents, live user escalation — business hours) | 15 minutes | Automatic escalation to team lead |
| Urgent (live user escalation — out-of-hours) | 1 hour | Automatic escalation to on-call governance contact |
| Elevated (behavioral incident investigation) | 4 hours | Notification to product owner |
| Routine (quality review samples) | 48 hours | Queue backlog alert |
| Compliance review | 24 hours | Notification to product owner and risk team |

SLA compliance is measured and reported weekly in Panel 3 of the governance health dashboard. Any SLA class with compliance below 95% over a four-week period requires a formal capacity or process review.

### Regulatory Response Commitments

| Regulatory Event | Response Commitment |
| --- | --- |
| EU AI Act serious incident notification assessment | Complete assessment within 24 hours of incident classification |
| EU AI Act serious incident notification (if required) | Notify market surveillance authority within the regulatory deadline from assessment completion |
| Data subject erasure request (standard) | Complete erasure within 30 calendar days |
| Data subject erasure request (arising from safety incident) | Complete erasure within 72 hours |
| Audit trail production for regulatory examination | Produce within 48 hours of formal request |

---

## Governance Observability Integration

Governance metrics and anomaly signals must flow into the AGKB and surface in operational governance decisions. This section defines how governance observability integrates with the governance infrastructure.

### Governance Metrics in the AGKB

All governance metrics computed in the system described above are written to the AGKB as governance metrics artifacts, distinct from operational behavioral metrics. The governance metrics artifact type includes: the metric identifier, the measurement timestamp, the measurement value, the target value or SLA, and the agent system or portfolio scope. Governance metrics artifacts are written by the Behavioral Drift Monitor Agent (for operational metrics) and by the governance oversight function's monitoring infrastructure (for process metrics).

Governance metrics in the AGKB are queryable via T06 (AGKB Query), supporting the canonical governance queries in [governance queries](queries.md) — specifically the portfolio queries GQ-21 through GQ-25 that cross-reference governance health against agent system behavioral status.

### Governance Health Triggering Escalation

The following governance health states trigger automatic escalation to the human governance oversight function:

**Any governance anomaly detected** (as defined in the Governance Anomaly Detection section) triggers immediate notification to the governance oversight function and a mandatory response initiation within 4 hours of detection.

**Any governance SLA breach for an immediate or urgent escalation class** triggers automatic notification to the accountable human and governance oversight function within 30 minutes of the breach.

**Governance tool audit gap** (as defined in the Governance Anomaly Detection section) triggers an immediate security and governance integrity alert.

**Active waiver count exceeding the portfolio threshold** — defined as the product of the total number of active agent systems and a per-system waiver rate of 0.2 (meaning more than one in five gate conditions across the portfolio is currently under waiver) — triggers a portfolio governance review.

### Governance Observability Feedback to Governance Agent Behavioral Specifications

Governance observability metrics are not passive measurements. When a governance agent's performance on its governance function falls below the thresholds defined in this document — HITL routing accuracy below 90%, reviewer calibration below 0.80, impact prediction accuracy below 0.70 — those metrics constitute evidence that the governance agent's behavioral specification may need revision or that recalibration is required. The governance agents are themselves agent products governed by the APLC; their operational metrics trigger the same feedback loops that operational metrics trigger for any other agent product.

Governance agent recalibration follows the Stage 6 recalibration protocol defined in [[agent-maintenance]], applied to the governance agent as the system under maintenance. The recalibration is approved by the governance oversight function (the accountable human for governance agents) and is logged to the AGKB with the same provenance requirements as any other recalibration event.

---

*See also: [[aplc]] (lifecycle overview), [[agent-operations]] (Stage 5 behavioral observability that this document extends to the governance meta-level), [governance tool stack](tool-stack.md) (governance tool stack whose operations are monitored here), [governance queries](queries.md) (canonical queries that surface governance health data via T06), [[agent-maintenance]] (Stage 6 recalibration protocol applied to governance agents), [[waiver-governance]] (waiver protocol referenced in Stage 4 metrics).*
