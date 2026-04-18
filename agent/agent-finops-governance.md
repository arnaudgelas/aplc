# Agent FinOps Governance
## APLC Cross-Cutting — Economics Governance Across the Agent Product Lifecycle

*APLC document. Implements manifesto principle P11 (Economics) for agent products governed under the Agentic Product Lifecycle. Governs how agent system economics are specified, monitored, and enforced from Stage 1 Conceive through Stage 7 Retire. Audience: business sponsors, product owners, Technical Owners, and finance stakeholders who need to govern agent operating costs as first-class product governance concerns.*

*Related documents: [[aplc.md]], [[agent-behavioral-specification.md]], [[agent-operations.md]], [[agent-maintenance.md]], [[agent-composite-versioning.md]]. ASDLC reference: ASDLC `finops-governance.md` for the software-delivery FinOps baseline that this document extends for agent products.*

---

## FinOps Governance Rationale

The manifesto's P11 (Economics) governs whether a given loop iteration is cost-justified relative to its outcome. That question is necessary. It is not sufficient for an agent product deployed at scale to real users over an operational lifetime measured in months or years. Agent product FinOps governance governs three concerns that P11 alone does not address.

**Unbounded token consumption as a failure mode.** An agent product whose economics are not specified and monitored can consume tokens at rates that bear no relationship to the value it delivers. Unlike a software service whose compute costs are capacity-bound, an agent product's inference costs are consumption-bound: they scale with context length, with the number of agentic steps taken to complete a task, with the volume of knowledge retrieved, and with the frequency of human review interactions. A system that enters an unresolvable reasoning loop, a retrieval pattern that inflates context with low-signal content, or a misconfigured autonomy tier that routes too many interactions through expensive human review — all of these are agent-specific failure modes that manifest as cost anomalies before they manifest as quality failures. Cost monitoring is therefore a first-line behavioral detection mechanism, not an accounting function appended to operations.

**Economics as a behavioral signal.** A cost spike that cannot be explained by a change in interaction volume or a planned composite state component change is a behavioral anomaly signal. The agent is doing something different: retrieving more, reasoning longer, escalating more frequently, or looping where it should not. An organisation that monitors behavioral quality metrics without monitoring economics is missing a diagnostic dimension. Cost anomalies and behavioral anomalies are correlated; detecting the cost anomaly first may provide earlier warning of the behavioral deviation. The FinOps Drift Indicator defined in this document operationalises this correlation as a production observable.

**ROI as a first-class governance concern.** An agent product that meets all its behavioral quality targets but costs significantly more to operate than its business value warrants is not a well-governed product — it is a liability that has passed its behavioral gate but failed its business case. The ROI projection established at Stage 1 is not a one-time analysis; it is a living metric against which the agent's operating cost is continuously compared. A product whose cost-to-value ratio is degrading deserves the same governance attention as a product whose behavioral quality is degrading. Business Owners who sponsor agent products without committing to ROI tracking over the operational lifetime have not accepted the full scope of their accountability.

---

## Four FinOps Accountability Roles

FinOps governance in the APLC is distributed across the four accountability roles defined in [[aplc.md]]. Each role owns a distinct economic dimension.

| Role | FinOps Accountability | Primary Metric |
| --- | --- | --- |
| **Business Owner** | ROI and business value realisation; product-level cost justification | Cost per successful outcome |
| **Behavioral Owner** | Evaluation cost efficiency; evaluation budget governance | Evaluation cost efficiency |
| **Technical Owner** | Token efficiency; Composite State Hash cost baseline; infrastructure cost attribution | Token efficiency ratio; FinOps drift indicator |
| **Regulatory Owner** | Cost documentation for compliance purposes; cost retention requirements | Governance record completeness |

The Technical Owner is the primary owner of the FinOps governance mechanism — they own the cost envelope specification, the real-time cost monitoring configuration, and the FinOps drift indicator. The Business Owner accepts accountability for whether the product's aggregate economics justify continued operation. The Behavioral Owner governs whether the evaluation investment is yielding behavioral coverage at acceptable efficiency. The Regulatory Owner ensures that cost records are retained as required and that cost governance artefacts are present in regulatory submissions.

---

## Cost Attribution Model

Agent system costs map to the five components of the Composite Agent State and to the APLC lifecycle stages at which they are incurred. Cost attribution must be defined before the agent product enters Stage 3. Retroactive attribution is unreliable; the cost envelope cannot be validated at the Behavioral Release Gate if cost attribution was not instrumented during Stage 3 development and evaluation.

### Cost Components

**Foundation model inference cost.** Cost incurred per inference call, driven by input and output token counts. Input token count is a direct function of context window contents — the product of context engineering decisions made under manifesto P7. A system prompt that is ten times longer than necessary, retrieval that floods context with low-signal passages, or multi-turn conversation that retains full interaction history when only recent turns are relevant: all of these are context engineering failures that manifest as elevated inference costs before they manifest as quality degradation. Foundation model inference cost is the largest variable cost component for most agent products. Its primary technical lever is context engineering quality (P7). Its primary governance lever is the token budget defined in Stage 2.

**Knowledge base retrieval cost.** Cost incurred per retrieval query — encompassing embedding generation, index query, and any reranking operations. Driven by knowledge base design decisions made under manifesto P6. A knowledge base with poor index design, a retrieval strategy that queries broadly and filters narrowly, or a knowledge base whose currency is low (causing the agent to retrieve-and-discard more results): all increase retrieval cost without increasing knowledge utility. Retrieval cost is governed by the Behavioral Owner who owns knowledge base design, and by the Technical Owner who owns the retrieval architecture.

**Evaluation and red-team cost.** Cost incurred per evaluation run — including automated evaluation calls, red-team exercise inference, and human preference evaluation infrastructure. Driven by evaluation portfolio design under manifesto P8 and the red-team protocol defined in [[agent-behavioral-evaluation.md]]. Evaluation cost is incurred primarily during Stage 3 and on the recalibration cadence in Stage 6. It is not a variable cost in the same sense as inference or retrieval; it is a quality investment. The FinOps governance question for evaluation cost is not whether to minimise it, but whether the behavioral coverage gained per evaluation dollar is sufficient to justify the investment.

**Human review cost.** Cost incurred per human-in-the-loop event — comprising reviewer time, routing infrastructure, and HITL platform overhead. Driven by the autonomy tier selected at Stage 1 and Stage 2, and by the routing accuracy of the agent's escalation logic. A Tier 1 or Tier 2 agent product routes a higher proportion of interactions through human review than a Tier 3 or Tier 4 agent. The HITL cost ratio (defined below) tracks whether human review cost is proportionate to the interaction volume and to the escalation rate specified in the behavioral design.

**Governance agent operating cost.** Cost incurred by governance agents that assist APLC stage gate work — behavioral consistency checking, coverage gap analysis, evaluation summary drafting, and cost monitoring. Governed by the governance agent participation framework in [[aplc.md]]. Governance agent cost is typically a small fraction of total operating cost but must be attributed to the product it governs and must not be invisible in the cost model.

### Cost Attribution Tagging

Every cost-incurring component must carry attribution tags before it runs. Required dimensions for agent products:

| Dimension | Description |
| --- | --- |
| Product identifier | Which agent product incurred the cost |
| APLC stage | Which lifecycle stage — development, evaluation, production |
| Cost component type | Inference, retrieval, evaluation, HITL, governance |
| Autonomy tier | The tier at which the interaction was processed |
| Composite State Hash | The CSH active at the time of cost incurrence |
| Business purpose | The business outcome the cost is serving |

The CSH dimension is specific to agent products and has no equivalent in software delivery cost attribution. It enables cost anomaly investigation to be correlated with composite state changes: when a cost spike is detected, the attribution data identifies which CSH was active during the spike, enabling the Technical Owner to determine whether a model update, knowledge base change, or prompt revision is the driver.

---

## FinOps Metrics

### Cost Per Successful Outcome

```
Cost per successful outcome = Total operating cost in period ÷ Count of successful outcomes in period
```

Where "successful outcome" is defined by the success criteria established at Stage 1 and operationalised in the behavioral specification's task success rate definition. This is the primary ROI metric for the Business Owner. It is the per-unit expression of whether the product's economics are improving, stable, or degrading. A cost per successful outcome that is growing without a corresponding improvement in outcome quality or scope is an efficiency degradation signal requiring Business Owner review.

### HITL Cost Ratio

```
HITL cost ratio = Human review cost in period ÷ Total operating cost in period
```

A HITL cost ratio significantly higher than the specification-time design target indicates that the agent is escalating more than its behavioral specification intended — either because the autonomy tier was set too conservatively, because the routing logic is over-escalating, or because the agent is encountering inputs outside its specification. A HITL cost ratio significantly lower than the design target may indicate under-escalation: the agent is handling cases it should be routing to human review. Both deviations warrant investigation. The specification-time HITL cost ratio target must be defined at Stage 2 and referenced in Stage 5 monitoring.

### Evaluation Cost Efficiency

```
Evaluation cost efficiency = Behavioral coverage points gained ÷ Evaluation cost incurred
```

Where "behavioral coverage points gained" is measured as the increase in the fraction of behavioral specification clauses covered by the evaluation portfolio following a Stage 3 sprint or Stage 6 recalibration evaluation run. This metric governs the Behavioral Owner's evaluation investment decisions: is the evaluation strategy producing coverage efficiently, or is cost being incurred on evaluations that do not advance coverage? Evaluation cost efficiency is tracked at the sprint level during Stage 3 and at the recalibration cycle level during Stage 6.

### Token Efficiency Ratio

```
Token efficiency ratio = Count of interactions producing a successful outcome ÷ Total tokens consumed across all interactions
```

The token efficiency ratio is the Technical Owner's primary signal for context engineering effectiveness. A ratio that is degrading over time — more tokens consumed per successful outcome — indicates context engineering regression: context is growing larger without producing more successful outcomes. This can result from prompt bloat, retrieval strategy degradation, or model update effects on generation verbosity. Token efficiency ratio degradation that is not explained by a deliberate composite state change is a technical finding requiring context engineering review.

### FinOps Drift Indicator

```
FinOps drift indicator = Actual cost per interaction in period ÷ Specification-predicted cost per interaction
```

Where specification-predicted cost per interaction is the cost-per-interaction value established at Stage 2 based on the cost model for the selected autonomy tier and Composite Agent State design. The FinOps drift indicator measures whether the agent is operating within its economic specification. A ratio significantly above 1.0 indicates that the agent is consuming more resources per interaction than its specification projected — a behavioral signal as well as a financial one. A ratio significantly below 1.0 indicates that the agent is consuming less than projected, which may reflect positive context engineering improvement or may reflect under-serving users (completing interactions too quickly by refusing or shortcutting).

The FinOps drift indicator is the primary integration point between FinOps governance and behavioral drift detection. When the indicator exceeds the alert threshold (defined at Stage 2), it triggers the same investigation protocol as a behavioral drift event in [[agent-operations.md]]: root cause analysis against the composite state hash, notification to the Technical Owner and Business Owner, and a decision on whether to initiate Stage 6 recalibration or Stage 4 rollback.

---

## Stage-by-Stage FinOps Requirements

### Stage 1 — Conceive

The Agent Product Brief produced at Stage 1 must include a cost model for each autonomy tier option considered. A Stage 1 analysis that selects an autonomy tier without modelling the cost implications of each tier has not completed its economic analysis.

**Required cost model elements at Stage 1:**
- Projected interactions per period (daily, monthly) at expected adoption
- Estimated cost per interaction by component (inference, retrieval, HITL, governance) for each autonomy tier option
- Total projected operating cost per period for each option
- ROI projection: projected operating cost relative to projected business value
- Cost sensitivity analysis: how does the cost model change if adoption is 2× or 0.5× projected?

The autonomy tier decision at Stage 1 is partly an economics decision. Higher autonomy tiers (Tier 3, Tier 4) reduce HITL cost but increase the investment required in behavioral specification depth, evaluation breadth, and containment infrastructure. Lower autonomy tiers (Tier 1, Tier 2) carry higher HITL cost but lower behavioral governance cost. The FinOps analysis at Stage 1 must make this tradeoff explicit; a tier decision made without it is an incomplete business case.

**Conception Gate FinOps condition:** cost model present with projections for each autonomy tier option; ROI projection with measurable success criteria including cost targets; accountable Business Owner named.

---

### Stage 2 — Specify Behaviorally

Stage 2 translates the Stage 1 cost model into a cost envelope: a behavioral constraint on operating economics that is part of the behavioral specification alongside quality and safety constraints. The cost envelope is not a budget ceiling — it is a specification element that defines the expected economic operating range of the agent product.

**Cost envelope definition requirements:**
- Maximum cost per interaction (by component and total)
- Token budget per interaction: the maximum context window utilisation deemed acceptable given the behavioral specification's quality targets
- Escalation rate target: the fraction of interactions expected to reach the HITL queue, derived from the autonomy tier and uncertainty protocol
- Evaluation cost allocation: the evaluation budget for Stage 3 and for each Stage 6 recalibration cycle
- FinOps drift alert threshold: the FinOps drift indicator value above which the Behavioral Drift Monitor Agent triggers an alert

The token budget is a specification element because it constrains context engineering choices made during Stage 3. A system prompt designer who is not aware of the token budget may design a high-quality prompt that exceeds the economic specification. The token budget must be available to the engineering team before Stage 3 begins.

**Behavioral Specification Gate FinOps condition:** cost envelope defined with all required elements; token budget documented; FinOps drift alert threshold specified; cost envelope reviewed and accepted by Business Owner.

---

### Stage 3 — Build & Evaluate

Stage 3 operates the APLC inner loop (see [[aplc-stage3-inner-loop.md]]) under a cost discipline. Evaluation cost is a first-class concern of the inner loop alongside behavioral coverage.

**Evaluation cost budget:** The Stage 3 evaluation budget — the total cost allocation for all evaluation runs across the build phase — must be defined before Stage 3 begins and must be tracked against actual spend. An evaluation strategy that consumes the full evaluation budget before achieving minimum coverage bars has failed FinOps governance as well as behavioral governance.

**Cost regression testing:** Each inner loop sprint must confirm that the current Composite Agent State does not exceed the cost envelope defined at Stage 2. A context engineering change that improves behavioral quality at the cost of significantly increased token consumption per interaction requires a cost envelope review before it can be accepted into the evaluation baseline. "Better quality at any cost" is not a governed development principle.

**Cost efficiency as an evaluation dimension:** Alongside the four behavioral evaluation layers in [[agent-behavioral-evaluation.md]], Stage 3 must confirm that the cost-per-interaction projection from Stage 2 is achievable with the current composite state. If the actual cost per interaction in evaluation runs consistently exceeds the specification-predicted value, the evaluation has identified an economic specification gap that must be resolved before the Behavioral Release Gate.

**Behavioral Release Gate FinOps condition:** cost-per-interaction for evaluation runs within cost envelope tolerance (≤ 1.2× specification-predicted cost per interaction); cost regression testing passed (no sprint produced a cost increase not justified by a behavioral quality improvement); evaluation cost budget utilisation documented.

---

### Stage 4 — Release

Stage 4 establishes the production cost baseline alongside the behavioral baseline.

**Cost envelope certification:** The Composite State Manifest filed at Stage 4 must include the cost envelope specification and the observed cost-per-interaction from Stage 3 evaluation runs. This is the cost baseline against which Stage 5 drift monitoring compares production costs.

**Cost SLA:** The agent product's production cost SLA — the maximum acceptable cost per interaction in production operation — is documented as part of the Behavioral Release Gate conditions. The cost SLA is distinct from the cost envelope: the envelope is the specification, the SLA is the operational commitment. The cost SLA must be achievable within the cost envelope.

**Operational Readiness Gate FinOps condition:** cost envelope certified in the Composite State Manifest; cost SLA defined and instrumented in the monitoring configuration; FinOps drift indicator baseline established from Stage 3 evaluation cost data.

---

### Stage 5 — Operate

Cost monitoring in Stage 5 is a behavioral observability domain, not only a financial reporting function. Cost anomalies are treated with the same operational urgency as behavioral quality anomalies.

**Real-time cost monitoring:** The following cost signals are monitored continuously in production, on the same cadence as behavioral quality signals:
- Cost per interaction vs. cost SLA
- FinOps drift indicator vs. alert threshold
- HITL cost ratio vs. specification target
- Token efficiency ratio vs. Stage 4 baseline

**Cost spike as a behavioral drift trigger:** When the FinOps drift indicator exceeds its alert threshold, it activates the same investigation protocol as a behavioral drift event. The Technical Owner is notified within 1 hour. The investigation follows the same root cause analysis process as behavioral incidents: retrieve the CSH at the time of the spike, compare to the release-baseline CSH, identify which component changed. Cost spikes without a corresponding CSH change are behavioral anomalies — the agent is doing something different with the same configuration.

**Cost anomaly as an incident signal:** A cost anomaly that cannot be explained by interaction volume change, planned composite state change, or input distribution shift is classified as a behavioral incident until investigation determines otherwise. It is not deferred to the next operations review cycle.

**Cost-based HITL escalation:** For runaway agent behavior — an agent that is looping, over-retrieving, or executing excessive agentic steps on a single interaction — cost monitoring provides a circuit-breaker signal. When a single interaction's cost exceeds a defined per-interaction ceiling, the interaction is routed to the HITL queue and the agent's execution is interrupted. This ceiling must be defined at Stage 2 and instrumented before production deployment.

**Stage 5 cost reporting:** The product owner receives a weekly cost report covering: actual cost vs. cost SLA, FinOps drift indicator trend, HITL cost ratio trend, and token efficiency ratio trend. Cost reporting is part of the standard operations report, not a separate financial reporting stream.

---

### Stage 6 — Maintain

Foundation model updates, knowledge base refreshes, and system prompt revisions all affect the cost envelope. Stage 6 maintenance activities must include a cost impact assessment before implementation.

**Cost impact assessment for foundation model updates:** Before a foundation model update is accepted into the Composite Agent State, the Technical Owner must run a cost impact analysis: does the new model version change cost-per-interaction (due to different token generation rates, different context handling, or different pricing)? A model update that improves behavioral quality at materially higher cost per interaction requires a Stage 2 cost envelope revision before acceptance.

**Recalibration ROI analysis:** Before each Stage 6 recalibration cycle, the Business Owner conducts a recalibration ROI analysis: does the expected behavioral quality improvement from recalibration justify the recalibration cost? A recalibration that improves quality metrics by a small margin at high evaluation cost may represent a poor return on investment. The recalibration ROI analysis does not override behavioral safety requirements — a recalibration required to address an out-of-spec behavioral drift must proceed regardless of ROI — but it governs discretionary recalibrations.

**Cost efficiency trend in maintenance decisions:** The cost efficiency trend over the maintenance period — is cost-per-successful-outcome improving, stable, or degrading over time? — informs the maintenance team's prioritisation. A degrading cost efficiency trend that cannot be arrested by recalibration is a retirement signal: the agent product may be reaching the point where its economics no longer justify continued operation. This signal is reported to the Business Owner at the Stage 6 quarterly review.

---

### Stage 7 — Retire

**Total cost of ownership calculation:** The Stage 7 decommission record includes a total cost of ownership calculation for the full product lifecycle: Stage 1–3 development and evaluation cost, Stage 4–7 operating cost, recalibration investment in Stage 6, and retirement execution cost. This calculation is the financial record of the agent product's economic history and is a required input to future product planning for similar agent products.

**Cost efficiency as a retirement signal:** Sustained cost efficiency degradation — cost per successful outcome growing across two consecutive quarterly reviews without a recovery trajectory — is a retirement trigger condition that supplements the behavioral and business retirement triggers in [[agent-retirement.md]]. An agent product that has become uneconomical to operate, even if it continues to meet its behavioral quality targets, warrants a Stage 1 business case review and potentially a retirement decision.

**Cost lessons extraction:** The retirement record must document the cost lessons from the product's operational history: which cost components were underestimated at Stage 1; which context engineering choices had the largest cost impact; which evaluation strategies were most cost-efficient; which recalibration cycles produced the best cost-to-quality improvement ratios. These lessons enter the organisation's governed knowledge base for future agent product conception and cost modelling.

---

## FinOps Gate Criteria Summary

| Gate | FinOps Conditions |
| --- | --- |
| **Conception Gate** | Cost model present; ROI projection with cost targets; Business Owner named |
| **Behavioral Specification Gate** | Cost envelope defined; token budget documented; FinOps drift alert threshold specified; Business Owner acceptance |
| **Behavioral Release Gate** | Cost-per-interaction within tolerance; cost regression testing passed; evaluation budget utilisation documented; cost SLA defined |
| **Operational Readiness Gate** | Cost envelope in Composite State Manifest; cost SLA instrumented; FinOps drift indicator baseline established |

**Cost envelope compliance** is required at every gate. A composite state that cannot operate within its cost envelope at Stage 3 has not met its specification; the gate does not pass until the cost envelope violation is resolved or the cost envelope is revised through a governed Stage 2 specification revision with Business Owner approval.

**Waiving cost envelope violations** requires: documented justification identifying why the violation is acceptable; Business Owner sign-off; Technical Owner root cause analysis; a remediation plan with a specific target date for returning to within-envelope operation. A cost envelope waiver is filed to the Composite State Manifest and is visible in the product's governance record. Waivers are not indefinite; they expire at the next gate unless explicitly renewed with updated justification.

---

## FinOps Governance Agent

A lightweight FinOps Governance Agent may be deployed to assist the Technical Owner in monitoring cost metrics and triggering alerts. This agent operates at advisory autonomy (per the governance agent participation framework in [[aplc.md]]) and performs the following monitored tasks:

- Continuously computes the FinOps drift indicator against the Stage 2 alert threshold
- Monitors HITL cost ratio and token efficiency ratio against Stage 4 baselines
- Detects per-interaction cost ceiling breaches and routes interactions to the HITL queue
- Generates weekly cost reports for product owner review
- Flags cost anomalies that are not explained by known CSH changes

The FinOps Governance Agent integrates with the Behavioral Drift Monitor Agent defined in [[agent-operations.md]]: when the FinOps drift indicator exceeds its threshold, the FinOps Governance Agent files a cost anomaly signal with the Behavioral Drift Monitor, which treats it as a behavioral drift candidate. The integration ensures that cost signals reach the behavioral governance process without requiring a separate investigation path.

All FinOps Governance Agent outputs that inform gate conditions or incident escalations carry the *agent-proposed-with-human-review* epistemic tier label. The Technical Owner is the named reviewer for cost anomaly alerts. Automated circuit-breaker actions (per-interaction cost ceiling breaches routed to HITL) carry the *tool-generated* label and do not require individual human review prior to routing, but the routing event is logged for audit.

The FinOps Governance Agent is itself an agent product governed under the APLC at minimum viable governance level. Its behavioral specification must define: the cost metrics it monitors, the thresholds at which it alerts, the actions it is authorised to take autonomously (HITL routing for ceiling breaches only), and the actions it must propose for human approval (cost envelope waiver recommendations, recalibration ROI assessments).

---

## Cost Transparency Requirements

**Reporting cadence.** Cost metrics are reported on the following cadence:

| Metric | Cadence | Recipient |
| --- | --- | --- |
| FinOps drift indicator | Continuous (alert on threshold breach) | Technical Owner |
| Per-interaction cost vs. SLA | Daily | Technical Owner |
| HITL cost ratio | Weekly | Behavioral Owner, Technical Owner |
| Token efficiency ratio | Weekly | Technical Owner |
| Cost per successful outcome | Monthly | Business Owner |
| Total cost of ownership trend | Quarterly | Business Owner, Regulatory Owner |
| Evaluation cost efficiency | Per evaluation run | Behavioral Owner |

**Cost accountability by role.** Cost reporting is disaggregated by accountability role so that each role receives the cost signals within their remit:

- *Business Owner:* receives cost per successful outcome and total cost of ownership trend. These are the signals that govern the ROI question: is the product economically viable?
- *Technical Owner:* receives FinOps drift indicator, token efficiency ratio, and per-interaction cost. These are the signals that govern the technical implementation question: is the composite state configuration efficient?
- *Behavioral Owner:* receives HITL cost ratio and evaluation cost efficiency. These are the signals that govern behavioral quality investment: is the evaluation and review strategy producing coverage efficiently?
- *Regulatory Owner:* receives cost record completeness confirmation and access to the full cost attribution data set for compliance purposes.

Cost data is retained per the data retention requirements in [[agent-retirement.md]]. For EU AI Act high-risk systems, cost records are part of the technical documentation that must be retained for ten years after market placement.

---

## FinOps and Autonomy Tier Interaction

The autonomy tier decision is the single governance decision with the largest structural impact on the agent product's cost profile. Understanding this interaction is necessary for making informed tier decisions at Stage 1 and Stage 2.

**Higher autonomy tiers (Tier 3, Tier 4):**
- Reduce HITL cost: fewer interactions require human review
- Increase behavioral specification depth: more comprehensive Stage 2 specification is needed to govern autonomous operation safely
- Increase evaluation breadth: more evaluation cases are required to achieve the behavioral coverage necessary for a high-autonomy release
- Increase containment investment: the blast radius of autonomous action requires more robust containment infrastructure (P10)
- Introduce policy envelope escape as an additional red-team category for Tier 4
- Net effect: lower operating cost per interaction at scale, higher upfront governance investment

**Lower autonomy tiers (Tier 1, Tier 2):**
- Increase HITL cost: more interactions require human review
- Reduce behavioral specification depth required for safe operation
- Allow lighter evaluation portfolios at release
- Reduce containment investment
- Net effect: higher operating cost per interaction, lower upfront governance investment

**FinOps analysis must inform tier decisions at Stage 2.** The autonomy tier is not only a behavioral governance decision and a containment decision — it is an economic architecture decision. A product whose Stage 1 ROI projection assumed Tier 3 economics but whose Stage 2 behavioral specification analysis reveals that only Tier 1 or Tier 2 is achievable within the available evaluation budget has a misaligned cost model that must be corrected before the Behavioral Specification Gate can pass.

The correct resolution is to: revise the ROI projection with Tier 1 or Tier 2 economics; assess whether the revised economics still justify the product; and either proceed with the revised business case or return to Stage 1 for a product brief revision. Proceeding with the original ROI projection while operating at a lower autonomy tier is a governance failure — it means the Business Owner is measuring the product's performance against an economics model that does not reflect the product as designed.

**Tier migration and FinOps impact.** When an agent product's autonomy tier is upgraded during Stage 6 maintenance — moving from Tier 2 to Tier 3 as behavioral quality evidence matures — the FinOps governance must be updated: the cost envelope is revised for the new tier's expected HITL ratio and evaluation requirements, the ROI projection is updated, and the FinOps drift indicator baseline is reset. A tier migration that is not reflected in an updated cost envelope produces a FinOps drift indicator that compares production costs against the wrong baseline.

---

*Cross-references: [[aplc.md]] for the full APLC lifecycle, stage gates, and governance agent participation framework; [[agent-behavioral-specification.md]] for the behavioral specification that hosts the cost envelope definition; [[agent-operations.md]] for Stage 5 behavioral drift monitoring that integrates with the FinOps drift indicator; [[agent-maintenance.md]] for Stage 6 recalibration ROI analysis and foundation model update cost assessment; [[agent-composite-versioning.md]] for the Composite State Manifest that hosts the cost baseline and cost attribution data; [[agent-retirement.md]] for the cost efficiency retirement signal and total cost of ownership record; [[aplc-stage3-inner-loop.md]] for the Stage 3 inner loop cost discipline. ASDLC reference: ASDLC `finops-governance.md` for the FOCUS-compatible cost attribution standards and unit economics framework that underpin the agent-product-level metrics defined here.*
