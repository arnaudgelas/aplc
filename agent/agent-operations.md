# Stage 5 — Operate: Agent Operations Governance

*Stage 5 document of the Agentic Product Lifecycle. Governs the behavioral quality of deployed agent products. Audience: operations engineers, product owners, HITL queue managers, on-call engineers.*

See [aplc.md](../aplc.md) for the lifecycle overview.
See [agent-release-governance.md](agent-release-governance.md) for the Stage 4 release gate that precedes this stage.
See [agent-maintenance.md](agent-maintenance.md) for Stage 6, which runs concurrently.
See [agent-composite-versioning.md](agent-composite-versioning.md) for the composite state manifest that underpins incident investigation.
See [agent-behavioral-specification.md](agent-behavioral-specification.md) for the behavioral baseline against which drift is measured.

---

## What is Stage 5 — Operate?

Stage 5 begins when the agent enters production and runs concurrently with Stage 6 (Maintain) until the retirement trigger fires as defined in [agent-retirement.md](agent-retirement.md). Operations for an agent product is categorically different from software operations: the primary operational concern is not "is the service up?" but "is the agent still behaving as specified?" Service health monitoring is necessary; it is not sufficient. An agent can be fully available and actively causing harm — returning HTTP 200 on every request while producing outputs that violate its behavioral envelope, manipulate users, or expose personal data it was specified never to surface. The ASDLC's `operations-governance.md` defines the operational observability stack for software services that underpins this stage; that stack is required here and does not replace what this document adds. Stage 5 begins where service observability ends.

---

## Behavioral Observability vs. Service Observability

The ASDLC's `operations-governance.md` defines the operational observability floor for software services deployed through the agentic SDLC: service health metrics, SLO indicators, output quality rate, reasoning trace completeness, and cost anomaly detection. That floor is required here without modification. A deployed agent product that does not meet the ASDLC's operational readiness conditions is not ready for Stage 5, regardless of how well it performed in Stage 3 evaluation.

What `operations-governance.md` does not cover is the behavioral observability layer that is specific to agent products: the signals that reveal whether the agent's behavior has remained within its specification, as authored in [agent-behavioral-specification.md](agent-behavioral-specification.md) and baselined at release. Service observability tells you the agent is running. Behavioral observability tells you the agent is still the agent you released.

The four behavioral observability domains below are required in addition to the ASDLC service observability stack. Each domain must be instrumented before the agent enters production. Instrumentation that does not exist before go-live cannot be retrofitted during an incident.

### Behavioral Quality Metrics

These metrics measure the agent's output quality relative to its specification. They are the production equivalents of the Stage 3 evaluation suite — the Stage 3 suite tested quality on anticipated inputs before release; these metrics confirm quality is maintained on actual inputs in production.

**Output quality rate.** The percentage of sampled outputs meeting the quality rubric defined in the behavioral specification's Layer 3 performance targets. Sampling methodology and frequency must be defined at deployment: how many interactions are sampled per period, by what mechanism (random, stratified by use-case zone, triggered by output characteristics), and how sampled outputs are assessed (automated evaluator, human reviewer, or a tiered combination). An output quality rate measured only by automated evaluators without human review calibration is a proxy metric, not a behavioral quality measurement. Define the human review cadence that validates automated evaluator accuracy.

**Behavioral envelope compliance rate.** The percentage of interactions where the agent's behavior remained within its behavioral specification across all four layers — hard boundaries not violated, soft boundaries operating as configured, performance targets met, adaptation scope not exceeded. This metric requires a behavioral evaluation function running in production, not just in the evaluation pipeline. Define the evaluation function at Stage 3 and confirm it is production-deployable before the Stage 4 release gate closes.

**Task success rate.** The percentage of interactions where the agent successfully accomplished the user's stated goal, as defined by the success criteria in [agent-behavioral-specification.md](agent-behavioral-specification.md). Task success rate is not the same as output quality rate: an agent can produce a high-quality output that does not accomplish the user's goal. Both must be tracked independently. Measurement methodology: automated detection where feasible, augmented by HITL review sampling for interactions where automated detection is unreliable (ambiguous goal signals, multi-turn completions, tasks with delayed observable outcomes).

**Escalation rate.** The percentage of interactions escalated to humans, segmented by escalation trigger type as defined in the behavioral specification's escalation design. Track separately: uncertainty-threshold escalations, user-requested escalations, sensitive-content escalations, blast-radius escalations. An escalation rate that is trending upward without a corresponding change in input volume is a behavioral signal: the agent is encountering more cases it cannot handle within its specification. An escalation rate that has dropped substantially below the specification-time design target is a different signal: either the agent is handling cases it should be escalating, or the input distribution has shifted toward simpler cases. Both warrant investigation.

**Retrieved context freshness rate.** For agents that use knowledge retrieval (RAG or equivalent), the freshness rate of retrieved context is a behavioral quality metric distinct from knowledge base staleness. Knowledge base staleness measures whether the source documents have been updated; retrieved context freshness measures whether the agent is actually retrieving the most current available documents on a given topic, rather than retrieving older documents due to embedding similarity mismatches or index drift.

Measurement: for a sampled set of interactions where knowledge retrieval occurred, compute the proportion of retrieved documents whose source version is within the staleness threshold for their content category (as defined in Stage 6 knowledge governance). A retrieved document that exists in an outdated version in the knowledge base, while a newer version is available, is a freshness failure.

Monitoring cadence: weekly for high-change-rate knowledge domains (regulatory, clinical); monthly for medium and low-change-rate domains.

A declining retrieved context freshness rate provides an earlier signal for knowledge base refresh prioritization than staleness-driven behavioral incidents. It surfaces when the knowledge base's retrieval distribution has shifted away from current content before user-visible quality degradation occurs. The freshness rate trend feeds the Stage 6 Knowledge Staleness Sentinel's prioritization queue: knowledge base content categories with declining freshness rates are elevated in the refresh schedule even if the source documents have not yet triggered a staleness alert.

**Cost envelope compliance rate.** The proportion of sampled interactions where total attributed cost (foundation model inference + knowledge base retrieval + tool API calls + governance agent overhead) remains within the per-interaction cost ceiling defined in the Stage 2 cost envelope. Measurement: sample 10% of interactions weekly, compute total cost per interaction using the cost attribution tags defined in the FinOps governance framework (`agent-finops-governance.md`), compare against the ceiling. A compliance rate below 95% in any measurement window triggers a product owner notification; below 90% sustained over two consecutive windows triggers a mandatory root cause analysis. Cost ceiling exceedances concentrate in specific interaction types (long-context conversations, high-retrieval tasks, multi-step tool chains) — the root cause analysis must identify the interaction pattern driving the exceedance, not just the aggregate rate.

**FinOps Drift Indicator.** The ratio of actual cost per successful outcome in the current measurement period to the cost envelope baseline established at Stage 4 release. Formula: `FinOps Drift Indicator = (current cost per successful outcome) / (Stage 4 baseline cost per successful outcome)`. The indicator is measured weekly and compared against the cost envelope baseline — not against last week's cost (for the same reason behavioral drift is measured against the release baseline, not the prior measurement window). Alert thresholds: indicator above 1.2 (20% above baseline) generates a product owner notification with a root cause hypothesis; indicator above 1.5 sustained for two consecutive weeks generates a mandatory root cause analysis and Business Owner escalation; indicator above 2.0 triggers the same governance response as an out-of-spec behavioral drift event: immediate accountable human notification, rollback assessment, and documented risk acceptance if no rollback is taken. The FinOps Drift Indicator is a behavioral signal, not an accounting metric — a cost spike that cannot be explained by interaction volume changes is evidence that the agent is doing something different (more retrieval steps, longer reasoning chains, more HITL escalations) that warrants behavioral investigation.

### Drift Indicators

Drift indicators detect behavioral change relative to the baseline established at Stage 4 release. The baseline is the behavioral state of the agent at the moment it passed the Stage 4 gate — the CSH, the evaluation results, the behavioral metric values recorded in the composite state manifest. Drift is measured against that baseline, not against the prior measurement window. This distinction matters: a slow, continuous drift can appear small in window-over-window comparison while representing a large deviation from the release baseline.

**Per-metric baseline comparison.** At defined intervals — minimum weekly for high-risk deployments, minimum monthly for standard deployments — compute each behavioral quality metric against the release baseline and against the prior measurement period. Report both deltas. A metric that is stable in the most recent window but far from the release baseline is drifting; the window-over-window comparison masked it.

**Response distribution shift.** Are the agent's responses covering the same semantic and structural range as at baseline, or clustering in new patterns? Response distribution shift can indicate model update, knowledge base change, or input distribution shift before any individual quality metric degrades below threshold. This is a leading indicator, not a lagging one. Operationalize it with embedding-space monitoring or output characteristic analysis appropriate to the deployment's output type.

**Uncertainty expression rate.** Is the agent expressing uncertainty more or less than at baseline? A material increase may indicate the agent is encountering inputs outside its training distribution. A material decrease may indicate overconfidence drift — a pattern that erodes trust when the agent is wrong without warning. Both directions require investigation when the deviation is statistically significant. This metric operationalizes the uncertainty protocol specified in [agent-behavioral-specification.md](agent-behavioral-specification.md) as a production observable.

**Refusal rate.** Is the agent declining more requests than at baseline? A substantial increase may indicate prompt over-triggering, input distribution shift toward adversarial patterns, or a model update that changed the sensitivity of safety filters. A substantial decrease may indicate a regression in boundary enforcement. Track refusal rate by refusal trigger (hard boundary, out-of-scope, safety filter) to distinguish these causes.

### User Experience Signals

User experience signals are behavioral observability data. They are not customer satisfaction metrics. A user who abandons a session without resolution, returns after a poor interaction, or escalates to a human is providing a behavioral signal about the agent's performance that may not be captured in the quality metrics.

**Session abandonment rate.** The percentage of sessions where the user stops interacting without receiving a resolution — defined as: task success, explicit handoff, or explicit out-of-scope decline. Session abandonment without resolution is a behavioral failure signal. Define the resolution states clearly; "user stopped responding" is not the same as "user received a resolution and chose to stop."

**Re-engagement rate after poor interaction.** Users who return after an interaction classified as a quality failure. This measures trust recovery — whether the agent's performance in a single failed interaction is sufficient to lose the user permanently. Track against the trust recovery protocol defined in the User Trust Management section below.

**Trust signals.** Explicit user feedback, escalation requests initiated by the user (distinct from agent-initiated escalations), and formal complaints. Where the deployment surface supports explicit feedback collection, collect it. Where it does not, escalation rates and re-engagement rates are the proxies. Do not rely on explicit feedback as the primary trust signal — users who have lost trust often do not bother to provide feedback; they leave.

### Safety Signals

Safety signals require the shortest detection-to-response latency of any behavioral observability domain. A quality incident discovered after 48 hours is a problem. A safety incident discovered after 48 hours may be a regulatory event.

**Flagged interaction rate.** The percentage of interactions flagged by content safety filters — the automated systems that detect harmful content, policy violations, or safety-boundary approaches. Track by flag category. A flag does not confirm a violation; it confirms that a boundary was approached. The human review queue (see HITL Management) processes flags; the flagged interaction rate tells operations whether the filter is operating at expected sensitivity and whether the distribution of flag types is shifting.

**Adversarial pattern detection alerts.** Alerts fired by adversarial pattern detection — systematic attempts to manipulate the agent's behavior through prompt injection, jailbreak sequences, principal impersonation, or goal hijacking. These alerts require immediate HITL escalation, not queue routing. An adversarial pattern detection alert is not a quality signal; it is a security signal that may also be an EU AI Act incident depending on outcome.

**Principal impersonation attempt rate.** The rate at which interactions include patterns consistent with false authority claims — inputs that assert system-level or operator-level privileges that the trust architecture did not grant to the requesting principal. This rate is a security monitoring metric tied to the trust architecture specified in Stage 1 and enforced as a Layer 1 hard boundary in [agent-behavioral-specification.md](agent-behavioral-specification.md).

**Memory write anomaly rate.** For agents with persistent memory, monitoring of memory write patterns provides an early signal for adversarial memory manipulation — a class of attack where adversarial inputs cause the agent to write persistent memory items that will shift future behavior. Monitor for:

- *Volume anomaly:* memory write volume per session exceeds the deployment baseline by a configurable multiplier (default: 3×). A session that triggers significantly more memory writes than baseline may indicate an adversarial input designed to populate the memory corpus with behavior-influencing content.
- *Category distribution anomaly:* the distribution of memory item categories (user preferences, learned heuristics, conversation summaries, etc.) deviates significantly from the baseline distribution. An unusual concentration of writes in a specific category — particularly a category relevant to behavioral constraints — is a targeted manipulation signal.
- *Principal anomaly:* memory items being written by principal classes that have not historically written to memory in this deployment. An agent that receives user-tier instructions and begins writing operator-context memory items is exhibiting an anomalous behavior that may indicate a principal impersonation exploit.

Memory write anomaly alerts are routed to the HITL adversarial queue (1-hour SLO), not the general quality review queue. The response protocol is the adversarial incident protocol from this document's Agent Incident Management section. Memory write anomaly detection is instrumented before go-live and confirmed operational at the Operational Readiness Gate.

**Out-of-scope request rate.** The rate at which interactions are classified as out-of-scope inputs as defined in the behavioral specification's use-case coverage map. A rising out-of-scope request rate can indicate marketing or discovery failures (users arriving with wrong expectations), input distribution shift, or adversarial probing. It is a signal, not an incident trigger; its value is in the trend, not the absolute level.

### Kill-Switch Verification

The kill-switch requirement established at Stage 3 (for Tier 4 agents) and the shutdown mechanism requirement for all governance agents must be verified in production on a defined cadence. A kill-switch that functioned correctly at Stage 3 evaluation may have been degraded by a subsequent model update, memory accumulation, or adversarial manipulation that has established precedent for ignoring shutdown signals.

**Verification cadence.** Monthly for all Tier 4 agents in production. Quarterly for Tier 2 and Tier 3 agents. Not required for Tier 1 agents (observe-only).

**Verification method.** Execute the kill-switch activation signal against a sandboxed replica of the production agent configured identically to the production CSH (same code, prompt, model, knowledge base state, and memory state as the production environment). The sandboxed replica must complete shutdown within the latency bound defined in the behavioral specification. Any deviation — latency exceedance, incomplete shutdown, or any output from the agent after signal receipt — is a Critical finding requiring immediate investigation.

**Record.** Each kill-switch verification run generates a structured verification record filed to AGKB: the agent system identifier, the CSH at verification, the verification timestamp, the shutdown latency observed, the pass/fail determination, and the name of the engineer who initiated the verification. A failed verification is filed as a Critical finding in the red-team findings archive (Category B, AGKB) and triggers the behavioral incident response protocol.

**Recalibration gate requirement.** Kill-switch verification is a required gate condition at the recalibration gate for Tier 4 agents. A recalibration that has not included a post-deployment kill-switch verification is not closed per the recalibration closure definition in Stage 6.

---

## Behavioral Drift Detection and Response

### Detection

Define drift as a statistically significant deviation from the behavioral baseline on any monitored metric. Significance is defined at deployment time, not after drift is detected. Pre-commit the threshold before the agent enters production: the combination of the metric, the statistical test, the significance level, and the comparison basis (release baseline or rolling window). A threshold adjusted after drift is detected is not a threshold — it is rationalization. Any change to a pre-committed threshold requires a product owner decision and a version history entry in the composite state manifest.

Detection cadence: continuous monitoring for safety signals and adversarial pattern detection (real-time alerting); daily measurement for behavioral envelope compliance and flagged interaction rates; weekly computation for output quality rate, task success rate, response distribution shift; monthly for trust signals and re-engagement rates. Cadence may be tightened for high-risk deployments or during the first 90 days of a new deployment.

### Classification

When drift is detected, classify before responding. Acting before classifying compounds the original problem.

**Within-spec drift.** The metric has moved significantly from the release baseline, but the agent's behavior remains within its behavioral specification at all four layers. Hard boundaries are still enforced. Performance targets are still being met at the specified levels. Soft boundaries are operating within their configured ranges. Within-spec drift is a monitoring finding, not an incident. It requires documentation and review at the next maintenance cycle (Stage 6), not immediate intervention. Document: the metric affected, the magnitude and direction of the deviation, the date detected, the detection basis, and the maintenance cycle reference to which it is assigned.

**Out-of-spec drift.** The metric deviation corresponds to behavior that has moved outside the behavioral specification — a Layer 3 performance target is being missed consistently, a Layer 2 soft boundary is being violated, or there is evidence that Layer 1 hard boundary proximity has increased materially. Out-of-spec drift is an incident. Classify it as a behavioral incident and initiate the behavioral incident response protocol described in Agent Incident Management below.

### Response Protocol

**Within-spec drift:** document the finding in the operational monitoring record; assign to the next Stage 6 maintenance cycle; notify the product owner at the scheduled weekly operations report. Do not initiate unreviewed changes to prompt, model configuration, or knowledge base in response to within-spec drift — that is recalibration, which belongs in Stage 6 with its associated governance controls.

**Out-of-spec drift:** immediate notification to the product owner and accountable human (within 1 hour of classification confirmation); within 24 hours, identify root cause using the incident investigation protocol in [agent-composite-versioning.md](agent-composite-versioning.md) — model update, knowledge base change, memory accumulation, input distribution shift, or prompt degradation; within 72 hours, either initiate Stage 6 recalibration (if the root cause requires a behavioral adjustment) or initiate Stage 4 behavioral rollback (if the deviation is severe enough to warrant restoring a prior composite state). The decision between recalibration and rollback belongs to the product owner and accountable human; the operations team provides the evidence. Document the decision and its rationale in the version history.

### Substrate-caused vs Agent-caused Drift Investigation

When agent behavioural quality deteriorates, the drift investigation must distinguish two root-cause classes before remediation is selected. Selecting the wrong remediation — recalibrating the agent when the substrate is the cause, or rebuilding the substrate when model drift is the cause — does not correct the deterioration and consumes governance attention that should have been directed at the actual cause.

**Substrate-caused drift.** The deterioration is rooted in the IGM-governed substrate the agent reasons over: claims have aged out of their decay class's revalidation cadence and now carry epistemic tiers that no longer reflect their reliability; new contradictions have emerged in claim families the agent depends on, and the contradiction-typing has not yet stabilised; the substrate has decayed in coverage or freshness for the action class in question; an authority succession has changed the validation regime for a claim family without the agent's reasoning being recalibrated to the new authority's epistemic standards.

**Agent-caused drift.** The deterioration is rooted in the agent itself: the foundation model was updated by the provider and now responds differently to identical context; the system prompt regressed (intentionally or through configuration drift); accumulated memory has shifted the agent's responses; the constraint-classification logic has degraded under input distribution shift independent of substrate state.

**Investigation protocol.** Within 24 hours of out-of-spec drift confirmation, the operations team performs a triage that consults both the agent-side composite-state diff (per `agent-composite-versioning.md`) and the substrate-state diff (per the IGM-governance metadata recorded in the knowledge-base component of the CSH; see `aplc.md` Section 1). The triage produces a classification:

- **Agent-caused.** The agent-side composite-state diff identifies a non-trivial change (model update, prompt change, memory state delta beyond the agent's normal operating envelope) and the substrate-state diff is small or unchanged. Remediation: per the existing out-of-spec drift protocol — Stage 6 recalibration or Stage 4 rollback.
- **Substrate-caused.** The substrate-state diff identifies the dominant change (epistemic-tier demotions, new contradictions, decay-cadence overflows, authority succession) and the agent-side composite-state diff is small or unchanged. Remediation: substrate-side investigation and repair before any agent-side recalibration. A recalibration that adjusts the agent to a degraded substrate locks in the degradation as a new baseline.
- **Mixed-cause.** Both diffs are material. Remediation: substrate-side first (the agent cannot be recalibrated against an unstable substrate), then agent-side once the substrate is stabilised.
- **Indeterminate.** Neither diff is dominant. Remediation: hold the agent at the current state, increase monitoring cadence, escalate to the IGM revision authority for the affected claim families and the system steward jointly.

**IGM authorities are co-investigators.** When substrate-caused drift is suspected, the IGM revision authority for the affected domain and (where the contradiction count has changed) the IGM Inference authority are co-investigators alongside the operations team. They are not consulted after the fact — they are part of the triage. The substrate-state diff cannot be interpreted by the operations team alone; the authorities who govern the substrate are the only people who can attest to whether a particular epistemic-tier demotion or contradiction-emergence is expected (a normal Curate cycle event) or anomalous (potential substrate compromise per IGM Principle 14, or genuine domain change requiring substrate revision).

**Documentation.** The drift-investigation record explicitly records the classification (agent-caused / substrate-caused / mixed / indeterminate), the diffs reviewed, the IGM authorities consulted (where applicable), and the remediation selected with rationale. A record that selects "agent-caused" without showing the substrate-state diff has not performed the triage; the record is incomplete and the gate at the next release will reject it.

### Automated Circuit-Breaker Protocol

For Safety and Adversarial signal threshold exceedances, the notification-then-decision sequence described above is insufficient for preventing real-time harm. The following automated circuit-breaker activates before human notification is received:

**Trigger conditions.** The circuit-breaker activates automatically when any of the following thresholds are crossed in the real-time monitoring stream, without waiting for human decision:

- Content safety filter flag rate exceeds 3× the release baseline over a 15-minute window
- Adversarial pattern detection alert fires (any single confirmed alert triggers the circuit-breaker)
- Hard boundary violation detected in any interaction (zero-tolerance trigger — any single confirmed violation activates the circuit-breaker)
- HITL queue safety escalations exceed 5× the release baseline over a 30-minute window

**Circuit-breaker actions.** On activation, the agent infrastructure automatically:

1. Reduces the agent to its minimum safe operating mode: responds only with a predetermined, human-authored safe response set and the escalation path to a human operator. The agent does not generate new model-based responses until the circuit-breaker is cleared.
2. Routes all incoming interactions to the HITL queue with Safety escalation priority and SLO (1 hour).
3. Notifies the accountable human, product owner, and on-call engineer simultaneously, with the trigger condition, the current CSH, and the most recent safety signal values.
4. Logs the circuit-breaker activation event to AGKB as a Safety incident record.

**Circuit-breaker clearance.** The circuit-breaker may only be cleared by explicit action from the accountable human or product owner. Clearance requires a documented decision: the accountable human confirms (a) the root cause has been identified, (b) the safety signal has returned to within-baseline levels, and (c) either the composite state has been rolled back to a pre-incident CSH or a recalibration has been deployed that addresses the root cause. Automatic timer-based clearance is not permitted. An agent product that has a circuit-breaker activation in its operational history must include the activation record, clearance basis, and root cause in the next Behavioral Release Gate evidence bundle.

### Event-Triggered Evidence Freshness

The detection cadences defined above — continuous for safety signals, daily for behavioral envelope compliance, weekly for output quality, monthly for trust signals — are **minimum measurement floors**, not staleness definitions. A measurement completed yesterday is stale if a triggering event occurred since it ran. Calendar cadences govern steady-state monitoring when no triggering events have occurred. They do not determine whether a specific measurement result is current.

The following events require immediate re-measurement regardless of where the agent falls in its scheduled cadence:

**CSH change (any component).** Any change to the composite state hash — model version, knowledge base snapshot, prompt version, configuration — triggers immediate re-run of the stability test set and behavioral envelope compliance re-check. Stage 6 is required to file a maintenance notification before any planned CSH change (see Stage 5/6 Concurrency Governance below). If Stage 5 detects a CSH change without a prior maintenance notification, it is treated as unintentional drift, not intentional maintenance, until proven otherwise.

**HITL override rate spike.** An override rate above 2× the rolling baseline over a 48-hour window triggers an immediate behavioral quality audit — re-run of the behavioral envelope compliance check against the current CSH, inspection of the interaction classes driving the spike, and product owner notification within 4 hours. Do not wait for the next scheduled measurement.

**Adversarial pattern detection alert.** Any adversarial pattern detection alert triggers immediate behavioral envelope compliance re-check, with particular attention to Layer 1 hard boundary integrity. The re-check must be completed and documented before the alert is closed, regardless of whether the adversarial attempt was successful.

**Foundation model update detected.** Detection of a new foundation model version in the active CSH — whether planned (Stage 6 maintenance) or unplanned (provider-initiated) — triggers immediate re-run of Layer 2 and Layer 3 behavioral coverage checks. A planned model update with a prior maintenance notification allows Stage 5 to set a new comparison baseline post-change. An unplanned model update without a maintenance notification is treated as an out-of-spec drift event until the behavioral coverage re-run confirms the behavioral envelope is intact.

### Stage 5/6 Concurrency Governance

Stage 5 and Stage 6 run concurrently. Their interaction requires explicit governance. Without it, Stage 5 cannot distinguish intentional behavioral changes from unintentional drift, and Stage 6 cannot maintain traceability of which maintenance activities produced which behavioral changes.

**Finding classification and routing.** Stage 5 classifies every detected finding into one of three categories before routing:

- **Within-spec drift:** The metric has moved significantly from the release baseline, but all four behavioral specification layers remain intact. Document in the operational monitoring record and assign to the Stage 6 recalibration backlog. No immediate escalation required.
- **Out-of-spec drift:** The deviation corresponds to behavior outside the behavioral specification. This is an incident requiring a product owner decision: either Stage 4 rollback assessment (if the violation is severe or the root cause is unknown) or Stage 6 recalibration gate (if the root cause is understood and the deviation is recoverable). The decision belongs to the accountable human with a documented decision record — not to the on-call engineer.
- **Specification gap:** The observed behavior is not clearly within or outside the specification because the specification does not cover the behavioral zone in question. Escalate to Stage 2 specification revision. Do not attempt to resolve a specification gap through recalibration — that produces behavior that is not traceable to any authored specification.

**The rollback vs. recalibration decision.** For out-of-spec findings, the decision between Stage 4 rollback and Stage 6 recalibration belongs to the accountable human. The on-call engineer's role is to: detect and classify the finding; notify the accountable human immediately; provide the CSH diff, the violated behavioral specification sections, and a severity assessment; and implement whichever decision the accountable human makes. The on-call engineer does not make the rollback decision unilaterally, even if the severity appears obvious.

**Maintenance notification from Stage 6 to Stage 5.** Before executing any planned composite state change — model update, knowledge base refresh, prompt revision, recalibration — Stage 6 must file a maintenance notification with Stage 5 monitoring. The maintenance notification is a structured artefact specifying: the planned change type, the expected CSH delta, the scheduled execution window, and the expected behavioral impact. The notification must be filed before the change is executed, not after.

The maintenance notification allows Stage 5 to set a new comparison baseline immediately post-change, so that Stage 5 drift detection treats the intentional change as a new baseline rather than anomalous drift from the prior baseline. A Stage 6 activity executed without a prior maintenance notification invalidates the drift detection baseline for the duration of the change window and must be treated as an unplanned CSH change until Stage 5 can reconstruct what changed and when.

**Stage 5 notification to Stage 6 before investigation.** When Stage 5 initiates an incident investigation following an out-of-spec finding, it must notify Stage 6 so that no further planned maintenance is executed during the investigation window. Maintenance activity during an active investigation contaminates the CSH audit trail and may make root cause identification impossible.

---

## Human-in-the-Loop Management at Scale

When an agent makes thousands of decisions daily and a defined percentage require human review, the HITL queue is an operational system, not a governance aspiration. A HITL process that is well-designed in theory but under-resourced, under-monitored, or without defined SLOs is not providing human oversight — it is providing the appearance of human oversight. P5's autonomy tier governance and P9's accountability requirements are not satisfied by a queue that exists but does not function.

### Queue Design

**Routing.** Cases enter the HITL queue through four mechanisms: automatic escalation by the agent on the triggers specified in the behavioral specification; user-initiated escalation (always honored immediately, regardless of queue state); random sampling for quality review (a percentage of all interactions sampled at defined rates per use-case zone); and adverse outcome detection (safety signal alerts and behavioral envelope compliance failures that were not agent-escalated). Each entry type must have a routing label that the queue management system preserves — the label determines review priority and reviewer assignment.

**Who reviews what.** Domain expertise routing for cases in specialized knowledge areas (regulatory, medical, legal, financial): cases in these areas require reviewers with relevant domain credentials, not general reviewers. Priority routing for time-sensitive cases: safety escalations and live user-interaction escalations where the user is waiting. Volume routing for quality review samples: these can be reviewed asynchronously by a larger pool. Do not route all cases to the same review pool — domain mismatch between reviewer and case produces lower-quality reviews and erodes reviewer calibration over time.

**Queue SLO.** Maximum time from queue entry to human review completion, defined by escalation class:

| Escalation Class | SLO |
| --- | --- |
| Safety incident | 1 hour |
| Adversarial incident | 1 hour |
| Behavioral incident | 4 hours |
| Live user escalation | 15 minutes (business hours); 1 hour (out-of-hours) |
| Quality review sample | 48 hours |
| Compliance review | 24 hours |

These SLOs must be resourced before the agent goes to production. A product owner who signs off on a HITL design without confirming that review capacity exists to meet the SLOs has approved an unresourceable commitment.

### Review Workflow

**What the reviewer sees.** The complete interaction history for this session. The agent's stated reasoning where available from the reasoning trace (per P9 observability requirements). The composite state manifest for the session — which model version, which knowledge base snapshot, which prompt version was active. The behavioral specification sections relevant to this interaction's use-case zone. The queue entry reason (why this case was routed here). Prior HITL decisions on similar cases, where available for pattern reference.

**What decisions the reviewer can make.**

- Approve: the agent's response was within specification; no action required beyond recording the approval.
- Override: the agent's response was outside specification or a better response was available; the reviewer provides the correct response (for live interactions) or documents the correction (for retrospective reviews). Override decisions are the primary signal for behavioral specification gaps.
- Escalate further: the case requires expertise or authority beyond the reviewer's — escalate to domain specialist, legal/risk team, or accountable human as appropriate.
- Flag for specification review: the agent's response was not clearly wrong, but the reviewer believes the behavioral specification may not be correct or complete for this case type. Flags trigger a Stage 2 review process, not an immediate change.

Reviewers must record the time taken and the confidence of the decision. Low-confidence decisions, or cases where two reviewers would disagree, are evidence of an unclear specification.

### Feedback Loop

Flagged patterns from HITL review are reported to the product owner weekly. The report includes: override rate by case category, emerging case patterns not well-covered by the current specification, reviewer agreement rate, and SLO compliance. The product owner reviews and assigns action items.

Patterns indicating a behavioral specification gap — consistent reviewer overrides on a specific case type, or a case type that reviewers flag for specification review at a rate above 5% — trigger a Stage 2 revision process. The specification must be updated before the engineering team adjusts the agent's behavior; a behavioral change without a specification change is an unreviewed change that breaks the traceability chain.

Patterns indicating an evaluation gap — cases that the Stage 3 evaluation suite did not cover and where the agent is consistently failing — trigger an evaluation portfolio update. The update is added to the Stage 6 maintenance backlog and scheduled.

The HITL override rate is tracked as an operational metric alongside service health. An override rate that is trending up is an early signal of behavioral drift or specification incompleteness — it deserves the same operational attention as a rising error rate.

### Queue Health Metrics

**Queue volume.** Is the volume growing beyond the team's review capacity? Queue volume should be stable relative to interaction volume at a defined ratio (the escalation rate target from the behavioral specification). A queue volume that is growing disproportionate to interaction volume indicates a behavioral or distribution change. A queue volume that is shrinking below expected levels indicates either a positive development (the agent has improved) or a broken routing mechanism (cases that should escalate are not reaching the queue).

**Review latency.** Is the SLO being met per escalation class? Track SLO compliance as a percentage. An SLO compliance rate below 95% for safety escalations is a governance failure requiring immediate resource action. An SLO compliance rate below 90% for quality review samples indicates that review capacity is insufficient for the interaction volume.

**Override rate.** Track overall and by case category and reviewer. A high overall override rate (above 15% on quality review samples) indicates behavioral specification failure or model performance regression. A high override rate on a specific case category indicates a specification gap for that zone. High override rates concentrated on a specific reviewer may indicate calibration drift in the reviewer, not the agent — a fact that can only be distinguished by comparing across reviewers.

**Reviewer agreement rate.** For cases that receive multiple reviews (calibration exercises, escalated decisions), what percentage of reviewers agree on the correct action? A reviewer agreement rate below 70% on a case type indicates that the behavioral specification for that type is not clear enough to produce consistent human judgment. If human reviewers cannot agree on the correct behavior, the specification is not a specification — it is an interpretation exercise. The specification must be revised before the agent can be expected to behave consistently.

### HITL Governance Capture Detection

HITL governance capture is the analog of rubber-stamping in the review process: a HITL queue that processes cases at high throughput with near-universal approval is not providing human oversight — it is providing the appearance of human oversight while the actual behavioral governance function has collapsed. Capture can occur through resource pressure, reviewer fatigue, misaligned incentives, or insufficient reviewer rotation. It must be detected and corrected with the same urgency as a behavioral incident.

**Detection thresholds.** Any of the following patterns, observed across the specified window, constitutes a governance capture signal requiring escalation:

- Reviewer agreement rate above 95% on quality review samples for 4 consecutive weeks. Genuine quality review of a non-trivial behavioral specification produces disagreement; suspiciously high agreement indicates that reviewers are not exercising independent judgment, that cases are being routed to the wrong reviewers, or that the review process has been compressed to the point where substantive review is not occurring.
- Override rate below 2% on quality review samples for 4 consecutive weeks when the behavioral specification is known to include edge cases, ambiguous zones, or known difficult case types. A specification with acknowledged complexity that produces near-zero overrides has reviewers who are approving without reviewing.
- Same reviewer pool for 3 consecutive evaluation cycles without rotation. Reviewer pools that do not rotate develop shared blind spots, group norms that diverge from the specification, and social pressure against override decisions. Rotation is a structural control, not a preference.
- Review latency consistently below the minimum plausible review time for the case type for 2 consecutive weeks. If quality review samples are being closed faster than is humanly possible given the case complexity, the review is not occurring. Define minimum plausible review times at deployment, per case type, before go-live.

**Response.** On detection of any governance capture signal:

1. Escalate to the product owner within 24 hours with the specific detection evidence.
2. Mandatory rotation of at least 50% of the reviewer pool for the next evaluation cycle. Rotation is not optional pending investigation — it is the immediate structural response.
3. If the capture pattern continues for 2 consecutive cycles after the first escalation: add at least one external reviewer (outside the team that has been conducting reviews) for the next cycle. Document the rationale for the external reviewer selection.
4. Audit the review records from the detection window: select a sample of approved cases and conduct a secondary review by a different reviewer pool. Document any disagreements as retrospective overrides.

**Record.** Every governance capture detection event — including the specific detection threshold triggered, the escalation record, the rotation action taken, and the secondary audit findings — must be documented in the operational governance record and made visible in the Stage 5 monitoring dashboard. HITL capture events are not internal housekeeping; they are evidence that a governance control was not functioning, and they must be traceable.

---

## Stage 5 Feedback Loop Operationalization

Stage 5 generates three structured feedback paths to upstream stages. Stating that "quality incidents trigger Stage 3" and "persistent drift triggers Stage 2" is not operationalization — it is a placeholder. Each path requires a defined artefact type, a named translation owner, a closed-loop definition, a mandatory-entry threshold, and SLOs. Without these, feedback paths exist on paper and accumulate in maintenance backlogs without triggering the upstream revision they require.

### Stage 5 → Stage 3: Evaluation Gap Signal

**When this path activates.** Quality incidents where root cause analysis identifies that the Stage 3 evaluation portfolio did not cover the interaction class or failure pattern that produced the incident. Also activated by HITL feedback indicating consistent agent failures on case types not present in the evaluation suite.

**Artefact type: evaluation gap signal.** A structured record containing: the interaction class in which the failure occurred; the specific failure pattern observed; the evaluation category gap — which section of the evaluation portfolio does not cover this pattern, or which case type is absent; and the CSH at the time of failure. An evaluation gap signal is not a bug report or a free-text incident note. It is a structured input to the Stage 3 evaluation revision process.

**Translation owner.** The named evaluation team lead for the deployment — not "the team" and not "whoever is available." The evaluation team lead is identified at Stage 3 and carried forward into Stage 5 operations. The translation owner is responsible for receiving the signal, converting it into an evaluation portfolio update request, and tracking it through the Stage 3 revision process.

**Loop closed definition.** The feedback loop is closed when all three of the following conditions are met:
1. The evaluation portfolio is updated with the new case or case class derived from the evaluation gap signal.
2. A Stage 3 evaluation re-run confirms that the gap is now covered — that the new case produces a passing result under the corrected agent behavior, or that the evaluation now correctly identifies the failure pattern.
3. The behavioral baseline is updated to reflect the re-evaluation result.

A deployed fix without an evaluation portfolio update is **not a closed loop.** The fix may have addressed the specific incident; the gap in the evaluation suite remains, and the next release will pass the Stage 3 gate without being tested against the pattern that caused the incident.

**Mandatory-entry threshold.** Evaluation gap signal creation is mandatory — not optional, not at the discretion of the operations team — in the following conditions:
- Any incident class recurring in 3 or more incidents within a 60-day rolling window. Three recurrences within 60 days indicates that the evaluation portfolio is not detecting a real failure mode. The gap must enter Stage 3 as a mandatory evaluation portfolio update, not as a maintenance backlog item subject to prioritization.
- Any single incident at P1 or P2 severity (as defined in the deployment's incident severity classification). Severity alone triggers mandatory Stage 3 entry regardless of recurrence count.

**SLOs.**
- Evaluation gap signal created within 5 business days of pattern identification (not 5 days from incident detection — from the point at which root cause analysis confirms the evaluation gap).
- Evaluation portfolio update confirmed (loop closed per the three-condition definition above) within 30 calendar days of signal creation.

### Stage 5 → Stage 2: Specification Gap Signal

**When this path activates.** Persistent behavioral patterns that root cause analysis cannot resolve through recalibration because the behavioral specification does not cover the behavioral zone in question — the specification is silent, ambiguous, or internally inconsistent on the observed behavior. Also activated by HITL override patterns on a specific case type that indicate the specification is not producing consistent human judgment.

**Artefact type: specification gap signal.** A structured record containing: the behavioral zone in which the gap was identified; the specific section of the Stage 2 behavioral specification that does not cover the observed behavior, or the section that is ambiguous or inconsistent with another section; and the evidence of the gap — HITL override patterns, reviewer disagreement rates, or incident root cause analysis findings. A specification gap signal is not a request for the agent to be changed; it is a request for the specification to be revised before any behavioral change is made.

**Translation owner.** The specification analyst who authored the relevant Stage 2 document — not the on-call engineer, not the product owner. The specification analyst is identified in the Stage 2 document and carries authorship responsibility forward. If the original analyst is no longer available, a named successor must be designated before the Stage 2 document is published.

**Loop closed definition.** The feedback loop is closed when all three of the following conditions are met:
1. The Stage 2 behavioral specification is updated through the governed Stage 2 revision process — not as an informal annotation, comment, or addendum to the existing document.
2. The Behavioral Specification Gate (Stage 2 exit criteria) is re-assessed for the conditions affected by the specification revision.
3. A Stage 3 evaluation re-run is completed against the updated specification, confirming that the revised specification produces consistent evaluation outcomes for the previously ambiguous case type.

Updating the specification without re-running evaluation is not a closed loop. Recalibrating the agent to behave differently without updating the specification first is not a closed loop and is a traceability violation.

**Mandatory-entry threshold.** Specification gap signal creation is mandatory in the following conditions:
- Reviewer agreement rate below 70% on a specific case type for 2 consecutive weeks. If human reviewers cannot agree on the correct behavior for 2 consecutive weeks, the specification is not specifying behavior for that case type — it is producing interpretive disagreement. That is a mandatory specification revision, not a calibration adjustment.
- HITL override rate above 15% on a specific case category for 3 consecutive weeks. A sustained override rate at this level indicates that the agent's behavior on that case category is consistently diverging from what qualified reviewers consider correct — and that the divergence is systematic, not incidental.

**SLOs.**
- Specification gap signal created within 5 business days of pattern identification.
- Stage 2 specification revision initiated within 15 calendar days of signal creation. Initiation means the revision process has a named owner, a defined scope, and a target completion date — not that the revision is complete.

### Stage 5 → Stage 1: Trust Degradation Escalation

**When this path activates.** Trust metrics declining across two consecutive monthly reporting periods with no recovery trend. This is not a quality incident or a specification gap — it is evidence that the agent product may no longer be serving the business purpose for which it was conceived. Stage 5 cannot resolve this; it can only detect and escalate it.

**Artefact type: trust degradation report.** A structured report containing: the trust metrics that have declined, the magnitude of decline across both reporting periods, evidence that no recovery trend is present, the incident and quality history from the same period (to distinguish quality-driven trust loss from structural trust loss), and confirmation that operational and specification interventions within Stage 5's authority have not reversed the decline. A trust degradation report is evidence of a pattern requiring strategic review — it is not a request for a Stage 1 review meeting. It triggers one.

**Ownership.** The product owner initiates the trust degradation report and delivers it to the business demand sponsor who commissioned the Stage 1 business case. The Stage 1 review is owned at the same level as the original business case commissioning — it is a strategic decision, not an operational one.

**SLOs.**
- Trust degradation report delivered within 10 business days of the second consecutive declining monthly period.
- Stage 1 review initiated within 20 calendar days of report delivery. Initiated means the review has a named facilitator, a defined scope, and a scheduled first session — not that the review is complete.

---

## Agent Incident Management

The five incident classes below are specific to agent products. They supplement, not replace, the infrastructure and application incident classes defined in the ASDLC's `operations-governance.md`. An agent product may experience a quality incident and an availability incident simultaneously — they are separate incidents with separate response procedures, coordinated by the on-call engineer and the product owner.

All incidents require a post-incident review within five business days. The review must produce: root cause documented with evidence; specification, evaluation, or operational gap identified; corrective action assigned with owner and due date; and updated runbook entry covering this failure mode for future on-call reference.

### Quality Incident

**Definition.** The agent is available and responding within latency targets, but output quality has fallen below the output quality SLO defined in the behavioral specification.

**Detection.** Output quality SLO alerting, triggered by the automated quality sampling process. Quality incidents that are not detected by automated sampling are detected by HITL override rate increases or user complaint volume — both are lagging signals. If the automated sampling process cannot detect a quality incident, the sampling methodology is insufficient.

**Response.**

1. Notify the product owner within 4 hours of alert.
2. Examine the behavioral monitoring dashboard: which quality metrics are degraded? Which use-case zones are affected? What is the time onset?
3. Retrieve the CSH at the time quality degradation began and compare to the release-baseline CSH using the incident investigation protocol in [agent-composite-versioning.md](agent-composite-versioning.md). Identify which components changed.
4. Root cause analysis: model drift, knowledge base staleness, prompt degradation, input distribution shift, or evaluation gap? Document the evidence for each hypothesis.
5. If drift-caused: initiate Stage 6 recalibration (see [agent-maintenance.md](agent-maintenance.md)).
6. If evaluation-gap-caused: update the evaluation portfolio; schedule re-evaluation; determine whether the quality gap is within acceptable risk tolerance pending the evaluation update.
7. If specification-gap-caused: initiate Stage 2 specification revision; update the quality SLO if the original SLO was set against an incorrect specification.
8. Document the incident, root cause, and corrective action in the version history.

### Behavioral Incident

**Definition.** The agent is behaving outside its behavioral specification — violating Layer 1 hard boundaries, operating outside Layer 2 soft boundary configurations, failing Layer 3 performance targets consistently, or exceeding Layer 4 adaptation scope.

**Detection.** Behavioral envelope compliance monitoring or HITL escalation. A behavioral incident may also be detected by safety signal alerts when the out-of-spec behavior involves a safety boundary approach. Behavioral incidents not detected by monitoring are detected by user complaints or regulatory escalation — both are unacceptable detection latencies for a well-instrumented deployment.

**Response.**

1. Immediate notification to the accountable human (within 1 hour of detection, not 1 hour of classification).
2. Stage 4 rollback assessment: is the deviation severe enough — or the behavioral specification violation clear enough — to warrant immediate rollback to the prior composite state? This decision belongs to the accountable human, not the on-call engineer. Provide the CSH diff, the behavioral specification sections being violated, and a severity assessment.
3. If rollback: follow the Stage 4 behavioral rollback procedure documented in [agent-release-governance.md](agent-release-governance.md). Record the rollback in the version history. Conduct root cause analysis after the system is restored.
4. If no rollback: root cause analysis as per quality incident, with the addition that all interactions during the out-of-spec period must be flagged for HITL review as a compliance measure, regardless of queue SLO impact.
5. Document the incident, the rollback or no-rollback decision and its basis, and the corrective action.

### Safety Incident

**Definition.** The agent has caused harm, or a credible assessment determines that harm to a user is likely based on the interaction evidence. This includes: outputs that facilitated illegal activity, outputs in violation of the agent's hard boundaries regarding harmful content, failures of safety escalation that left a user in distress without appropriate response, and privacy violations where personal data was surfaced contrary to the behavioral specification.

**Detection.** Safety signal alerts, user complaint with harm claim, HITL escalation with safety concern. Safety incidents may also be reported by third parties — regulators, journalists, or affected users' representatives. Any report from any channel that asserts user harm must be triaged as a potential safety incident immediately.

**Response.**

1. Immediate escalation to the accountable human and the legal/risk team — within 30 minutes of detection. This is not a standard incident escalation; it is a parallel notification. The accountable human and legal/risk team are notified simultaneously, not sequentially.
2. Legal hold on all relevant interaction traces, composite state manifests, and HITL records from the relevant period. Do not delete, modify, or archive anything from the affected period pending legal review.
3. GDPR data subject rights assessment: does the affected user have rights that are triggered by this incident — right to be informed, right to erasure, or data breach notification obligation? This assessment must be completed within 72 hours.
4. User notification if required by the legal/risk assessment or by regulation.
5. Full root cause analysis with the composite versioning incident investigation protocol.
6. EU AI Act incident notification requirement assessment: Article 73 of the EU AI Act requires providers of high-risk AI systems to notify the relevant market surveillance authority of serious incidents. Assess whether this incident meets the threshold and act accordingly within the required notification window.
7. Post-incident review must include legal and risk stakeholders, not only operations and engineering.

### Persona Incident

**Definition.** The agent has broken character — responded with a persona, tone, or identity inconsistent with the designed persona specified in [agent-behavioral-specification.md](agent-behavioral-specification.md). This includes: adopting a different name or role when prompted, providing responses inconsistent with the defined persona voice, claiming capabilities or affiliations not in the specification, or denying being an AI when directly and sincerely asked.

**Detection.** Persona consistency monitoring (automated pattern matching against persona specification) or user report.

**Response.**

1. Notification to the product owner within 2 hours.
2. Forensic analysis of the composite state at the time of the incident: which model version, which prompt version? Was the persona definition in the prompt correctly assembled and delivered? Retrieve the reasoning trace if available.
3. Scope assessment: is this an isolated incident, or is persona breakdown occurring across a class of inputs? Check the monitoring dashboard for persona consistency metric trends around the incident time.
4. Remediation: prompt update (if the persona definition was malformed or insufficiently robust against the triggering input), model rollback (if a model update produced the persona deviation), or behavioral specification revision (if the persona definition itself was ambiguous in the triggering context). All three remediation paths require the behavioral evaluation re-run at minimum Layer 2 and Layer 3 before production application, per the recalibration gate in [agent-maintenance.md](agent-maintenance.md).
5. Assessment of brand or trust impact: for consumer-facing deployments, persona incidents may require user communication if the incident was publicly visible or caused user confusion about the agent's identity or capabilities.

### Adversarial Incident

**Definition.** Confirmed malicious manipulation of agent behavior — a successful prompt injection, jailbreak, principal impersonation attack, or goal hijacking that produced an out-of-spec output or extracted information the agent was specified not to provide.

**Detection.** Adversarial pattern detection alerts, or incident escalation from HITL review where a reviewer identifies that the agent was successfully manipulated. Adversarial incidents that are detected only through user reports or downstream consequences have escaped both automated detection and HITL review — a dual monitoring failure that must be addressed independently of the adversarial incident investigation.

**Response.**

1. Cybersecurity incident protocol activation. For financial services deployments operating under DORA, Article 19 notification obligations for ICT-related incidents must be assessed immediately. Do not treat an adversarial incident as a quality or behavioral incident pending classification — escalate to the cybersecurity response team from detection.
2. Forensic trace recovery: recover the full interaction trace for the confirmed attack, including all context delivered to the model. Preserve forensic integrity — do not allow automated retention policies to archive or delete the trace before the investigation is complete.
3. Legal hold as per safety incident protocol if harm occurred or may have occurred.
4. Red-team replay of the attack vector: once the attack mechanics are understood, reproduce the attack in the evaluation environment. This is not optional — an adversarial incident that cannot be reproduced in evaluation cannot be mitigated. The Stage 3 red-team protocol defines the evaluation environment and methodology; apply it to the specific attack vector.
5. Full evaluation portfolio update: add the successful attack vector to the adversarial test suite. Update the behavioral release gate to require that this attack vector produces no compliance failure before any future release. An adversarial incident that closes without an evaluation portfolio update has not closed — the attack vector remains exploitable.
6. Regulatory notification assessment: in addition to DORA obligations, assess EU AI Act obligations and national cybersecurity incident reporting requirements. Document the assessment and its conclusions.
7. Post-incident review must include the cybersecurity team, the red-team function, and the product owner. The engineering team's role is to implement the mitigations that the security and product review defines; it is not to self-assess the adequacy of those mitigations.

---

## User Trust Management

User trust in an agent product is a managed operational metric, not a passive outcome of good performance. An agent that performs well on average but fails visibly in high-stakes interactions can lose user trust faster than aggregate performance metrics suggest. Trust signals must be instrumented, monitored, and reported with the same rigor as service health metrics.

**Track trust signals as part of operational monitoring.** The trust signals defined in the Behavioral Observability section above — session abandonment, re-engagement after poor interaction, explicit feedback, escalation requests — are inputs to a trust metric dashboard updated at least weekly. The product owner reviews this dashboard as part of the standard operations report; trust signals are not a separate reporting stream that only surfaces at quarterly reviews.

**Define a trust recovery protocol for users who have experienced a quality or safety incident.** What does the agent or the supporting team do when a user's interaction history contains a documented quality failure? At minimum: the agent's behavior toward that user should account for the prior failure in its next interaction (do not repeat the same failure mode if the user returns); where the deployment surface permits, a human operator should have the option to initiate a recovery interaction. Define the recovery protocol before go-live, not after the first incident.

**Track brand-level trust signals where available.** For deployments where the agent product is publicly associated with the operator's brand, brand-level trust signals — external reviews, social media sentiment, press coverage, regulatory inquiry volume — are operational indicators. An operations team that monitors service health but not brand-level trust signals will be surprised by the second-order effects of behavioral incidents that received public attention.

**Report trust metrics to the product owner monthly.** The monthly trust report includes: aggregate trust signal trends, individual incident trust impacts and recovery trajectories, comparison against the release-baseline trust metric levels, and any HITL patterns that suggest emerging trust issues before they manifest in user behavior. The product owner uses this report to make resourcing decisions about HITL capacity, specification revision priorities, and recalibration scheduling.

**Sustained trust degradation triggers a Stage 1 business case review.** If trust metrics decline consistently over two or more monthly reporting periods, with no recovery trend, the product owner must initiate a Stage 1 business case review. This is not a maintenance intervention — it is a strategic question: does the agent product still serve the business purpose for which it was conceived, and is it still viable in its current form? A Stage 1 review may result in a significant behavioral specification revision, a change in deployment scope, or a retirement decision per [agent-retirement.md](agent-retirement.md). Continuing to operate an agent product with declining user trust and no recovery plan is an operational and reputational risk that Stage 5 governance is not equipped to resolve — it requires the strategic reconsideration that Stage 1 provides.

---

## HITL Four-Channel Learning Protocol

Every human override of an agent decision is a high-quality signal. The HITL Four-Channel Learning Protocol captures this signal systematically and routes it to the four governance channels that can act on it.

### The Four Learning Channels

**Channel 1 — Behavioral Quality Signal.**
The override indicates a behavioral quality failure. Routing: override event → quality signal record → AGKB Operational Artifacts → behavioral quality trend analysis → weekly behavioral quality report → Behavioral Owner review. Aggregated quality signals drive Layer 4 evaluation priorities, determining which behavioral contracts require increased human evaluation coverage.

**Channel 2 — Specification Gap Signal.**
The override may indicate that the behavioral specification did not anticipate the situation. Routing: override event → specification gap candidate → Constraint Consistency Checker review → if confirmed gap: specification update request → Behavioral Specification Gate for the gap update → specification revision in AGKB. Not every override is a specification gap. The Constraint Consistency Checker determines whether the behavior was within specification (a quality failure) or outside it (a specification gap). These are distinct outcomes requiring distinct responses; conflating them produces incorrect routing and misassigned corrective actions.

**Channel 3 — Evaluation Portfolio Signal.**
The override indicates that the evaluation suite did not catch this failure pattern. Routing: override event → evaluation gap candidate → Behavioral Evaluation Swarm Coordinator review → new evaluation case generated → evaluation suite update in AGKB → coverage map updated. This closes the loop between operational failures and evaluation coverage — every override that reaches this channel produces a net improvement in the Stage 3 evaluation portfolio's ability to detect the failure pattern before the next release.

**Channel 4 — Routing Classifier Signal.**
The override is a training signal for the HITL Routing Intelligence Agent. If the Routing Intelligence Agent routed this decision autonomously and the human subsequently overrode it, the routing classifier should have escalated rather than routed autonomously. Routing: override event → routing error record → routing classifier update queue → routing threshold recalibration → updated routing policy deployed. This channel makes the routing system progressively more accurate over time, reducing both under-escalation (decisions routed autonomously that required human judgment) and over-escalation (decisions unnecessarily routed to humans that the agent could handle reliably).

### Override Record Schema

Each override generates a structured record: agent system identifier, use-case identifier, decision context (sanitized), agent's original decision, human override decision, override justification category (quality / gap / evaluation / routing / other), override timestamp, reviewer identity. The record is written to AGKB Operational Artifacts.

### Four-Channel Coordination

Override records are processed by all four channels concurrently. Coordination prevents double-counting: a single override should produce one quality signal, zero or one specification gap candidate, one evaluation gap candidate, and one routing signal. Conflicts between channel interpretations — for example, whether a given override is a quality failure (Channel 1) or a specification gap (Channel 2) — are resolved by the Behavioral Owner. The Constraint Consistency Checker's determination on Channel 2 is the primary input to that resolution.

### Four-Channel Reporting

A monthly four-channel report aggregates: override volume by channel, specification gaps confirmed versus rejected, evaluation cases added to the portfolio, and routing accuracy improvement trend. The report is a required input to Stage 6 maintenance planning. A maintenance cycle that proceeds without the four-channel report is not operating with complete operational intelligence; it cannot prioritize recalibration correctly against the behavioral failure patterns that overrides have surfaced.

### End-to-End Learning Latency Budget

The four learning channels generate signals; those signals must translate to corrected production behavior within a defined timeframe. The SLOs for signal creation (5 business days) and revision initiation (15 calendar days) are necessary but insufficient without an end-to-end latency budget that covers the full path from HITL override to corrected production behavior.

**Maximum end-to-end latency by pattern severity:**

| Pattern severity | Max latency: HITL override → corrected production behavior |
| --- | --- |
| Critical behavioral pattern (recurring Critical-class incidents) | 14 calendar days |
| High behavioral pattern (recurring High-class incidents or High red-team findings) | 30 calendar days |
| Medium behavioral pattern | 90 calendar days |
| Low behavioral pattern | Next planned release cycle |

**Measurement.** The end-to-end latency clock starts when the HITL override pattern is first identified (the point at which the evaluation gap signal or specification gap signal is created) and stops when the corrective change is confirmed live in production with a behavioral evaluation re-run demonstrating that the pattern no longer produces the failure.

**Exceedance escalation.** When the end-to-end latency budget is exceeded for a Critical or High pattern:

1. The product owner is notified immediately with the pattern description, the days elapsed, and the current status of each step in the remediation pipeline (signal creation, revision initiation, evaluation, gate, deployment).
2. The accountable human must provide explicit risk acceptance for continued operation under the uncorrected pattern. Risk acceptance is a dated, named record filed in AGKB — not verbal acknowledgement.
3. The risk acceptance record must state: the specific behavioral risk being accepted, the compensating control that is active while the pattern is uncorrected, and the target date for corrected production behavior.

**Portfolio tracking.** The end-to-end learning latency for all active patterns is tracked in the Stage 5 monitoring dashboard alongside behavioral quality metrics. A rising mean end-to-end latency across the portfolio is a governance process health signal indicating that the four-channel learning mechanism is not functioning at the governance process specification level.

---

## Behavioral Incident Context Agent

The Behavioral Incident Context Agent is a specialized governance agent that activates during behavioral incidents to enrich the incident record with governance context from AGKB, enabling faster root cause analysis and more precise remediation decisions.

### Activation Triggers

The agent activates on any incident classification — quality, behavioral, safety, persona, or adversarial — at the point of incident declaration. It does not wait for root cause analysis to begin; context enrichment is most valuable when the incident responder is forming their initial hypotheses and deciding what to investigate first.

### Context Enrichment Protocol

On activation, the agent performs the following in parallel:

1. Retrieve the current CSH and compare to the release-baseline CSH — identify any unauthorized or unnotified component change that may explain the behavioral deviation.
2. Retrieve the behavioral fingerprint snapshot and compare to the release baseline — localize drift to specific behavioral dimensions rather than treating the agent's behavioral state as opaque.
3. Retrieve the relevant behavioral contracts for the affected use case — identify which specification elements the incident violates and at which layer of the behavioral envelope.
4. Retrieve the evaluation history for the affected use case — identify whether this failure pattern appeared in prior evaluation, and if so, what its classification was.
5. Retrieve prior incidents of the same incident class for this agent system — identify recurrence patterns that indicate a systemic issue rather than a one-off event.
6. Retrieve relevant findings from the most recent red-team exercise — identify whether this was a known vulnerability that was accepted, deferred, or missed.

### Incident Context Package

The agent produces an Incident Context Package containing: CSH comparison result, fingerprint drift localization, violated behavioral contracts with layer identification, evaluation coverage gap analysis, prior incident pattern summary, and red-team finding correlation. The package is attached to the incident record in AGKB and provided to the human incident responder. The package does not contain a root cause determination — that determination belongs to the human responder. The package provides the structured evidence from which the responder can reason.

### Remediation Path Suggestion

Based on the context package, the agent suggests a remediation path from the six Stage 6 recalibration methods: prompt adjustment, knowledge base update, fine-tuning, behavioral specification revision, autonomy tier adjustment, or retirement. The suggestion is advisory. Remediation decision authority rests with the Behavioral Owner. The suggestion's value is in making the remediation option set explicit at the beginning of the incident response, not in constraining the Behavioral Owner's judgment about which option is appropriate.

### Behavioral Incident Context Agent Autonomy

The Behavioral Incident Context Agent operates at Tier 2 (human-on-the-loop) for context enrichment. The enrichment itself is automated; the output is a structured package for human review. The agent does not take remediation actions autonomously, does not modify the incident classification, and does not file records in AGKB beyond the context package attachment.

### Incident Context Agent Governance

All Behavioral Incident Context Agent actions are logged to the AGKB audit trail. The agent's own behavioral specification and evaluation suite are maintained under APLC governance — it is itself a governed agent product, subject to the minimum viable governance appropriate to its autonomy tier and task scope. See [aplc.md](../aplc.md) for the governance recursion principle that applies to inner governance agents.

---

## Reviewer Calibration Protocol

HITL reviewer accuracy is not assumed — it is measured and maintained. The Reviewer Calibration Protocol ensures that human reviewers maintain consistent, high-quality judgment over time. The quality of HITL oversight is only as good as the calibration of the reviewers providing it; an uncalibrated reviewer pool provides the appearance of human oversight without the substance.

### Calibration Assessment Design

A calibration set is a fixed collection of cases with ground-truth judgments established by expert consensus. The calibration set covers: representative cases from each behavioral contract category, edge cases from Layer 1 evaluation, cases that historically generate reviewer disagreement, and safety-critical cases requiring maximum accuracy. The calibration set is distinguished from the operational review queue by two properties: its ground-truth judgments are pre-established and authoritative, and it is not derived from live production interactions. It is a purpose-built assessment instrument.

### Calibration Frequency

| Reviewer Status | Assessment Cadence |
| --- | --- |
| New reviewer (before first operational assignment) | Once before first assignment |
| Active reviewer (general assignments) | Monthly |
| Reviewer assigned to safety-critical cases | Bi-weekly |

### Calibration Metrics

For each reviewer, compute:

**Overall accuracy.** The percentage of calibration cases judged correctly against the pre-established ground truth. This is the primary capability indicator.

**Category accuracy.** Accuracy broken down by behavioral contract category. Category-level disaggregation identifies expertise gaps that overall accuracy masks — a reviewer may perform well in aggregate while being systematically inaccurate in a specific domain or case type.

**Consistency score.** Agreement with the reviewer's own prior judgments on repeated calibration cases — cases that appear in multiple assessment cycles with identical content. This measures reliability and identifies reviewers whose judgments fluctuate independently of case content.

**Calibration drift indicator.** The trend in overall accuracy over the last six assessment cycles. A declining trend indicates that a reviewer's calibration is degrading and requires investigation before it manifests as operational override errors.

### Calibration Threshold Policy

| Condition | Consequence |
| --- | --- |
| Overall accuracy at or above defined threshold (example: 85%) | Authorized for operational assignments |
| Category accuracy below threshold in a specific category | Restricted from assignments in that category pending remediation |
| Calibration drift declining over last six cycles | Flagged for governance oversight review; mandatory calibration training before next assignment |

The threshold values are defined at deployment and documented in the governance configuration. They are not adjusted after calibration results are observed — a threshold adjusted in response to a reviewer failing it is not a threshold, it is a rationalization.

### Calibration Training Protocol

When a reviewer falls below threshold, calibration training consists of: review of the cases where their judgment diverged from the ground-truth consensus, expert explanation of the correct judgment rationale for each divergence, and re-assessment on a new calibration set (not the one on which they failed). The training cycle is completed within two weeks of the threshold failure. Re-assessment results are recorded and compared to the pre-training assessment to confirm that training produced measurable improvement.

### Reviewer Calibration Records

All calibration assessment results are stored in AGKB Operational Artifacts: reviewer identity, assessment date, calibration set version, and metric results for each assessed dimension. Records are retained for the full audit period. Aggregate reviewer pool calibration statistics — pool-level accuracy distributions, category-level accuracy trends, drift indicator summary — are reported in the Governance Observability Dashboard and reviewed by the Behavioral Owner quarterly.

### Calibration Governance

The calibration set itself is a versioned governance artifact in AGKB. Updates to the calibration set require Behavioral Owner approval. The calibration set must not be shared with reviewers outside of formal assessment sessions — sharing it in advance defeats its purpose as an independent assessment instrument. The correlation between calibration accuracy and operational override quality is tracked quarterly: if high-calibration reviewers are not producing higher-quality operational overrides than low-calibration reviewers, the calibration instrument is not measuring the right properties and must be revised. See [agent-behavioral-evaluation.md](agent-behavioral-evaluation.md) for the analogous evaluation capture detection logic that applies to the calibration process itself.

### Calibration Set Specification Version Control

The reviewer calibration set's ground-truth judgments are based on the behavioral specification that was active when they were established. When the behavioral specification changes, some calibration cases may have changed correct answers — the behavior that was wrong under the old specification may be correct under the new one, or vice versa. A calibration set that has not been audited since the most recent behavioral specification revision is semantically stale even if it is recent by calendar age.

**Specification version linkage.** Each calibration case carries a specification version tag: the version of the behavioral specification under which its ground-truth judgment was established. The tag is recorded in AGKB alongside the case content and the ground-truth judgment.

**Mandatory audit after specification revision.** Within 30 days of any Stage 2 behavioral specification revision, the calibration set must be audited by the Behavioral Owner against the new specification version:

1. Each case is reviewed: does the correct answer under the new specification match the recorded ground-truth judgment?
2. Cases whose correct answer has changed are updated (new ground-truth judgment established by the Behavioral Owner) or retired (the case tests behavior that no longer exists in the specification).
3. New cases are added to cover behavioral dimensions introduced or significantly revised by the specification revision.
4. The calibration set version is incremented and the AGKB record is updated with the new specification version tag.

A calibration set that has not been audited following a specification revision may not be used for reviewer qualification or operational calibration assessment. The AGKB Governance Agent flags calibration sets with an outdated specification version tag and prevents their use in active calibration workflows until the audit is completed.

**Audit record.** The audit is documented in a calibration set audit record: the specification version that triggered the audit, the cases reviewed, the cases updated or retired, the new cases added, the Behavioral Owner's name and sign-off date. The audit record is filed in AGKB alongside the updated calibration set version record.

---

*See also: `aplc.md` (lifecycle overview), `agent-behavioral-specification.md` (behavioral baseline), `agent-behavioral-evaluation.md` (evaluation portfolio), `agent-composite-versioning.md` (CSH and incident investigation), `agent-release-governance.md` (Stage 4 rollback procedures), `agent-maintenance.md` (Stage 6, concurrent), `agent-retirement.md` (Stage 7 retirement trigger conditions). ASDLC reference: `asdlc/operations-governance.md` (service observability floor that this document extends).*
