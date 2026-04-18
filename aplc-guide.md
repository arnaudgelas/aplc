# Agentic Product Lifecycle — Practitioner Guide

*Implementation guide. Audience: engineering leads, product managers, platform architects, governance officers. Where `aplc.md` describes the APLC architecture, this document describes how to implement it. For the lifecycle overview, see `aplc.md`.*

---

## Incremental Adoption

The APLC is not all-or-nothing. An organisation that attempts to implement all seven stages simultaneously, for an agent product that is already in production without any prior governance, will stall. The APLC is designed to be adopted incrementally — the minimum viable governance at each stage is enough to make the next stage tractable, and each stage's minimum bar can be reached without waiting for perfection at the previous one.

The following minimum viable governance definitions describe the floor at each stage — below which an agent product is ungoverned at that stage. These are not targets. They are the minimum evidence that a stage is being taken seriously.

---

### Stage 1 Minimum: Agent Product Brief with Business Purpose, User Model, and Initial Regulatory Classification

An agent with no product brief is an agent whose purpose is defined by its builders' assumptions. Any governance built on top of that — any behavioral specification, any evaluation portfolio, any release criteria — is built on an undefined foundation. The Stage 1 minimum requires three things:

**Business purpose.** A written statement of what problem the agent solves, for whom, and with what evidence the problem is real. One paragraph is sufficient if it answers all three. An evidence pointer — a user research finding, a regulatory mandate with citation, a documented executive decision — is required. "We think users would benefit from this" is not a validated business purpose.

**User model.** A description of who the agent serves, what kind of relationship the agent has with those users (advisory, transactional, analytical, decisional), and what those users trust the agent to do and not to do. One page is sufficient. The user model does not need to be exhaustive at Stage 1 minimum — it needs to be present, because without it, there is no principled basis for any behavioral requirement in Stage 2.

**Initial regulatory classification.** A documented determination of whether the agent falls within EU AI Act Article 5 prohibited practices, Annex III high-risk categories, or GPAI obligations. For non-EU deployments, the equivalent jurisdictional determination. The determination does not need to be final at Stage 1 minimum — it needs to have been performed with qualified input, documented, and acknowledged by the team. An agent that has not been classified cannot be governed to the correct standard; an agent whose classification has not been documented cannot demonstrate governance to regulators. Full classification guidance: `agent-regulatory-classification.md`.

**Why this is the floor.** Everything in Stages 2 through 7 traces back to Stage 1. A behavioral specification without a product brief is a technical document without a product purpose. An evaluation portfolio without a user model is testing the wrong population. A conformity assessment without a regulatory classification is filling out forms for an unknown requirement. The Stage 1 minimum is not bureaucracy; it is the prerequisite for everything else being coherent.

---

### Stage 2 Minimum: Behavioral Envelope with Hard Boundaries

An agent with no defined behavioral envelope is ungoverned by design. The Stage 2 minimum is a behavioral envelope that specifies, at minimum, the hard boundaries: the behaviors the agent will never exhibit regardless of instruction, context, or principal.

**Why hard boundaries first.** Hard boundaries are Layer 1 of the behavioral envelope (`agent-behavioral-specification.md`). They are the behaviors that must be enforced by infrastructure policy, not prompt instruction. An agent that has soft limits and performance targets but no hard boundaries is an agent that can, in principle, be instructed to do anything by a sufficiently authoritative instruction. That is not a behavioral specification; it is a capability description.

Hard boundaries at Stage 2 minimum derive from three sources: the permission model hard limits established in Stage 1 trust architecture (if Stage 1 is complete); the EU AI Act Article 5 prohibited practices (if applicable to the deployment); and the product-level exclusions stated as out-of-scope in the product brief. Each hard boundary must be specific enough to derive an evaluation case from: "the agent does not exfiltrate data from the system context to external endpoints" is specific enough. "The agent does not do harmful things" is not.

**What minimum does not include.** The Stage 2 minimum does not include soft boundaries, performance targets, or adaptation scope. It does not include the use-case coverage map, uncertainty protocol, or escalation design. Those elements are required before the Behavioral Specification Gate — but they are not the floor below which the product is ungoverned. The floor is hard boundaries. An agent with only hard boundaries and nothing else is still an agent with known hard limits. An agent with elaborate performance targets but no hard limits is an agent that may be doing anything.

---

### Stage 3 Minimum: Behavioral Evaluation Portfolio Covering the Happy Path Plus Five Adversarial Test Cases

An agent product released without any behavioral evaluation has not been tested for behavioral quality — it has been tested for engineering correctness (which the manifesto's P8 provides), which is necessary but not sufficient. The Stage 3 minimum requires that two evaluation categories exist before release.

**Happy path behavioral evaluation.** For each core use case defined in the behavioral specification (or, at Stage 3 minimum, inferred from the product brief and user model), at least one behavioral evaluation case must exist. The evaluation case tests whether the agent behaves as specified on the inputs it was designed for. A task success rate measured across a representative sample of core use cases is the minimum behavioral quality evidence.

**Five adversarial test cases.** Before every release, at minimum five adversarial test cases must be executed — one covering each of the five most applicable attack categories from the red-team protocol in `agent-behavioral-evaluation.md`. The specific five categories are determined by the product's attack surface: a customer service agent with no tool access has a different priority ordering than a financial advice agent with access to customer records and order execution. The five must be selected before the exercise, not after. Five cases is not a complete red-team; it is the minimum that forces the team to think adversarially before every release and produces documented evidence that adversarial thinking occurred.

**Why the bar is here.** A Stage 3 minimum below the happy path evaluation means the release decision was made with no behavioral evidence. A Stage 3 minimum below five adversarial cases means the release decision was made with no adversarial evidence. Both conditions are acceptable only for proofs-of-concept behind controlled access with no real users. For any deployment with real users, both conditions are required.

---

### Stage 4 Minimum: Behavioral Baseline Document

An agent deployed without a behavioral baseline cannot be monitored for behavioral drift. Drift cannot be measured without a reference point. Degradation cannot be detected without knowing what the agent was like when it was released. The behavioral baseline document is the Stage 4 minimum: a snapshot of the agent's measured behavioral characteristics at the moment of release, filed before deployment.

**What the baseline must contain at minimum.** Task success rate measured against the happy path evaluation cases. Human evaluation rubric scores from at least a sample of the evaluation distribution — even a 5% sample is better than nothing. The Composite State Hash computed from the five composite state components (`agent-composite-versioning.md`). The date the measurement was taken.

**What the baseline does.** It creates the reference for Stage 5 drift detection. An operations team that detects a declining output quality rate can compare against the baseline to determine whether the decline represents drift from a known starting point or noise around a previously established level. Without a baseline, every quality signal is interpreted relative to current expectation, which drifts with the agent. The result is an agent that is getting worse while the team's assessment of "normal" keeps adjusting downward to match.

**Why deployment without a baseline is a governance failure.** A behavioral baseline cannot be established retroactively. Once the agent is in production, the baseline measurement is confounded by production interactions. If a provider model update changed the agent's behavior between Stage 3 evaluation and the moment you thought to measure a baseline, you do not know what the agent was like before the update. The baseline must be measured at release time, against the composite state that was evaluated in Stage 3, before that state changes.

---

### Stage 5 Minimum: Quality SLO Defined and Monitored

An agent product in production with no quality SLO has no threshold at which its behavioral quality triggers a response. "We'll know it's bad when we see it" is not operational governance. The Stage 5 minimum is a quality SLO — a defined threshold for at least one behavioral quality metric — that is monitored in production and that produces an alert when the threshold is crossed.

**What constitutes a valid quality SLO.** A metric (output quality rate, task success rate, or HITL override rate are the most common), a threshold value, a measurement window, and a response when the threshold is crossed. "Task success rate must remain above 85%, measured weekly across a 10% stratified random sample of interactions; crossing below 85% for two consecutive weeks triggers product owner notification and root cause analysis" is a valid quality SLO. "Output quality should be high" is not.

**Why one SLO is the floor.** A product with one monitored quality SLO is not well-governed; it is minimally governed. But it has at least one mechanism that will alert the team before users experience extended degradation without the organisation noticing. The alternative — no SLO, relying on user complaints or HITL override rate increases as the primary signal — is reactive governance that consistently detects quality failures after harm has accumulated.

---

### Stage 6 Minimum: Model Update Notification Monitoring and Regression Test Suite

Stage 6 (Maintain) runs concurrently with Stage 5. The Stage 6 minimum addresses the single most consequential source of unplanned behavioral change for most deployed agent products: foundation model updates.

**Model update notification monitoring.** Subscribe to the provider's model update notification channel — email, API changelog, RSS feed, Slack integration, or whatever the provider makes available. When a notification arrives that a model version has been updated, the CSH computed from the current composite state will change. That change must be detected and treated as a planned maintenance trigger, not as an unexpected incident. Monitoring that detects CSH drift in production is the operational implementation of this requirement.

**Regression test suite that runs on notification.** When a model update is detected, a regression test suite must run against the updated model before that update is accepted into production. At Stage 6 minimum, this suite is the behavioral evaluation cases from Stage 3 minimum — the happy path evaluations and the five adversarial test cases. The suite does not need to be the full four-layer portfolio at minimum; it needs to run, produce a pass/fail result, and gate the decision to accept or reject the model update. A model update that produces a regression test failure is rejected until root cause is understood and the regression is either resolved or accepted with documented risk acceptance. Full foundation model update governance: `agent-maintenance.md`.

---

### Stage 7 Minimum: A Retirement Plan Exists Before Deployment

If you cannot describe how this agent will be retired, you should not deploy it.

This is not a philosophical statement about planning. It is a governance requirement. An agent product deployed without a retirement plan will, when the organisation eventually decides to decommission it, face the following: users who have no migration path, interaction records that may need to be retained for regulatory purposes but whose retention policy was never specified, accountability records that may be needed for regulatory examination but may have been archived or deleted, and a composite state manifest that was never filed because no one thought about what the agent's identity was before it was switched off.

**What a minimum retirement plan contains.** Three decisions made before deployment: how users will be notified of the agent's retirement and given time to adjust; which records must be retained and for how long (for EU high-risk AI systems, ten years from market placement); and who is accountable for executing the retirement process. The retirement plan does not need to be a detailed project plan at deployment time. It needs to capture those three decisions, so that when retirement eventually becomes the right decision, the governance path exists. Full retirement governance: `agent-retirement.md`.

---

## Common Failure Modes

These anti-patterns appear consistently in agent product deployments that lack APLC governance. Each is described with its observable symptom, its root cause, and the fix.

---

### Failure Mode 1: Building Before Specifying Behaviorally

**Symptom.** The engineering team is deep into implementation when the first product review occurs, and the review produces questions — "wait, what does the agent do when a user asks about X?" — that have no answer except "let me check what we built." The demo produces impressive output but the product owner cannot articulate what the release criteria are. The evaluation suite is written after the implementation, by the implementation team, against the behavior the implementation already exhibits.

**Root cause.** The engineering team began Stage 3 (Build) before Stage 2 (Specify Behaviorally) was complete. The behavioral specification was never the primary input to engineering; engineering built from assumptions and demos, and the specification — if it exists — was written to describe what was built rather than to govern what would be built. The APLC's single-source principle is violated: the behavioral specification and the implementation are two parallel documents that describe the same thing from different angles, neither authoritative over the other.

**Fix.** Require Behavioral Specification Gate closure before any production implementation begins. Proof-of-concept work and architecture prototyping may proceed during Stage 2 to validate technical feasibility, but those artefacts must be discarded or rebuilt against the specification, not promoted to production. The test for whether Stage 2 is complete: can a specification analyst who did not build anything derive evaluation cases from the specification without consulting the engineers? If no, Stage 2 is not complete.

---

### Failure Mode 2: Evaluating Only the Happy Path

**Symptom.** The evaluation portfolio covers the core use cases well. Task success rate on the intended use cases is high. Edge cases, boundary cases, and adversarial inputs were not evaluated, or were evaluated informally ("we tried some weird inputs and it seemed fine"). The first production incident is an adversarial input or an edge case the evaluation did not cover.

**Root cause.** The evaluation portfolio was built by the engineering team against the inputs they anticipated when building the system. The evaluation distribution is the developer's mental model of the user population, not the actual user population. There is no held-out set, no adversarial test suite, no human evaluation of boundary behavior. Layer 1 engineering evaluations are complete; Layers 2, 3, and 4 are not.

**Fix.** Define the evaluation distribution before evaluation begins, derived from the use-case coverage map in the behavioral specification — not from the engineering team's intuition. Require held-out set inclusion as a release condition. Require Layer 3 red-team completion for every release, including the first. Separate the evaluation function from the engineering function: the people who built the system should not be the people who define all the evaluation cases against which it is tested.

---

### Failure Mode 3: Deploying Without a Behavioral Baseline

**Symptom.** Three months after deployment, the product owner is told by the operations team that output quality has "declined a bit." Nobody can say from what level. The quality metric at deployment was never measured. The available comparison is against last week, not against release. The team cannot determine whether the current level represents drift from a higher starting point or whether the agent has always performed at this level.

**Root cause.** The behavioral baseline was never established at Stage 4. The product passed the engineering DoD and some form of evaluation, but the evaluation results were never recorded as a baseline against which production performance would be measured. The composite state manifest was not filed, so the behavioral identity of the deployed system at release is unknown. Drift detection is architecturally impossible without the reference.

**Fix.** Make the behavioral baseline document a hard gate condition at Stage 4, with a documented gate failure for absence. The behavioral baseline must include the CSH, all Layer 2 assurance target measurements, Layer 4 rubric scores, and the longitudinal stability test set results. It must be filed before any deployment is executed. The measurement must be taken against the composite state that passed Stage 3 evaluation — not after production interactions have begun.

---

### Failure Mode 4: Treating Model Updates as No-Ops

**Symptom.** The product owner receives a user complaint that the agent's responses have changed in tone, length, or content. The engineering team investigates and finds that the foundation model provider released a model update two weeks ago. The agent was not updated; the model it is built on was. Nobody on the team was monitoring for provider model updates. The behavioral regression was undetected for two weeks.

**Root cause.** Stage 6 foundation model update governance was not in place. No subscription to model update notifications existed, or notifications arrived but were not acted on. No regression test suite was configured to run on model update. The model version was treated as a fixed component when it is a variable one.

**Fix.** Implement CSH monitoring in production — when the CSH computed from operational parameters diverges from the release-time CSH, an alert fires. Subscribe to the model provider's update notification channel and configure the regression test suite to run automatically on notification. Define the accept/reject decision process for model updates before the first update arrives: who decides, on what evidence, within what time window. The default must be reject unless the regression test suite passes — not accept unless something breaks. Full specification: `agent-maintenance.md`.

---

### Failure Mode 5: Conflating Service Health with Behavioral Quality

**Symptom.** The operations dashboard shows all green: latency within SLO, error rate below threshold, availability above target. The product owner sees no alerts and assumes the agent is performing well. Three months later, a regulatory examination or a quality audit reveals that the agent has been providing low-quality, sometimes inaccurate responses that did not trigger any service health alert because they were syntactically valid HTTP 200 responses.

**Root cause.** The operational monitoring stack covers service health but not behavioral quality. The ASDLC operations model — latency, availability, error rate — is complete and correct for software services. It does not measure whether the agent's responses are useful, accurate, or within its behavioral specification. An agent that is perfectly available and consistently producing poor responses looks identical to an agent that is perfectly available and consistently producing excellent responses from a service health perspective.

**Fix.** Stage 5 requires behavioral observability in addition to service observability, not instead of it. The behavioral observability layer must be instrumented before go-live: output quality rate measured by automated evaluator with human review calibration, behavioral envelope compliance rate requiring a production-deployable behavioral evaluation function, task success rate, and escalation rate. The operations dashboard must surface behavioral quality metrics alongside service health metrics, reported to the product owner on the same cadence. Full specification: `agent-operations.md`.

---

### Failure Mode 6: Applying APLC Governance Without Manifesto Inner Loop Governance

**Symptom.** The behavioral specification and evaluation portfolio exist. Stage gate records have been filed. The APLC process looks complete on paper. Then a Stage 5 behavioral incident is traced to root cause: an engineering error in the agent artifact — a tool invocation boundary case, an incorrect retrieval step, a memory state corruption — that the manifesto's P8 evaluation suite would have caught, had it been running. The behavioral evaluation portfolio tested the artifact thoroughly at Layers 2, 3, and 4. Layer 1 — the P8 deterministic engineering evaluation suite — was either absent or was not a real gate condition.

**Root cause.** The APLC's product lifecycle governance was implemented while the manifesto's engineering inner loop governance was not. The behavioral specification and evaluation portfolio are product-level governance artefacts built on top of an engineering execution layer that was itself unverified. The behavioral evaluation (Layers 2, 3, and 4) was testing an artifact whose engineering correctness had not been systematically established. Engineering defects that the P8 suite was designed to detect persisted into production undetected because the layer of governance designed to detect them did not exist.

**Fix.** Establish Phase 2 manifesto governance — a functioning Specify → Govern cycle with human approval on commits — before APLC Stage 3 begins. Establish Phase 3 manifesto governance — P8 evidence bundles as a loop Definition of Done condition — before the Behavioral Release Gate is treated as meaningful. The APLC's Stage 3 explicitly requires that the manifesto's full inner loop has run; "engineering DoD met per manifesto P8" is Behavioral Release Gate Condition 1. An organisation that treats this condition as nominal — checking the box without running the P8 suite as a real gate — has not satisfied Condition 1 and the gate is not genuinely passed. The behavioral evaluation portfolio cannot substitute for the engineering evaluation suite; they address different failure modes in the same artifact.

---

### Failure Mode 7: Ungoverned Retirement

**Symptom.** The organisation decides to decommission the agent. Someone turns it off. Users are notified by encountering a 404 or an error message. Interaction records are archived in bulk and then deleted after 90 days following standard infrastructure policy. A regulatory inquiry arrives six months later requesting technical documentation. The documentation no longer exists.

**Root cause.** Stage 7 retirement was treated as an operational task (deprovision the infrastructure) rather than a governance stage. No user migration path was defined. No record retention policy was applied to agent-specific documentation. The composite state manifests, evaluation reports, stage gate records, and behavioral specification were not distinguished from general application logs and were deleted on the standard infrastructure retention schedule.

**Fix.** The retirement plan must exist before deployment. It must specify the user notification and migration path, the regulatory record retention schedule (for EU high-risk AI systems: ten years from market placement), and the named person accountable for executing retirement governance. When retirement becomes the decision, Stage 7 must be executed as a stage — with a structured wind-down period, not an immediate switch-off. The post-decommission documentation archive is a governed artifact, not an infrastructure cleanup task. Full specification: `agent-retirement.md`.

---

## Integration with Existing Frameworks

The APLC does not replace any existing governance framework. It is designed to integrate with the frameworks that regulate and manage agent products in real deployment contexts.

---

### EU AI Act

The EU AI Act's requirements on high-risk AI systems are design constraints, not a compliance checklist at release. This distinction is the most important integration point between the APLC and the Act.

**Where the Act primarily maps to the APLC.** Stage 1 (`agent-conception.md`, `agent-regulatory-classification.md`) handles Article 5 prohibited practices check, Annex III high-risk category check, and GPAI operator obligations. Stage 4 (`agent-release-governance.md`) handles the conformity assessment procedure (Annex VI self-assessment or Annex VII third-party assessment), the EU Declaration of Conformity, and EU AI Office database registration.

**Where this mapping breaks down if taken literally.** An organisation that reads "Stage 1 handles classification, Stage 4 handles conformity" and treats the intervening stages as unconstrained has misunderstood the Act. Article 9 (risk management system) requires a continuous risk management system throughout the lifecycle — not a risk classification at Stage 1 and a conformity checklist at Stage 4. Article 10 (data governance) imposes data quality requirements that constrain the training and evaluation data used in Stage 3. Article 14 (human oversight) imposes design requirements that must be incorporated in the behavioral specification at Stage 2 and verified at Stage 3. Article 15 (accuracy, robustness, cybersecurity) imposes performance requirements that must be specified in the behavioral specification at Stage 2 and demonstrated at Stage 3.

**Practical implication.** For high-risk systems, every stage gate in the APLC must include a check that the conformity requirements applicable to that stage have been incorporated. This is not an additional process; it is what the APLC stage gates are designed to do. The Conception Gate (`agent-conception.md`) confirms regulatory classification. The Behavioral Specification Gate (`agent-behavioral-specification.md`) confirms that Article 10 and Article 14 requirements are reflected in the behavioral specification. The Behavioral Release Gate (`agent-behavioral-evaluation.md`) confirms that Article 15 performance requirements are met. The Operational Readiness Gate (`agent-release-governance.md`) confirms that the EU DoC is signed and filed.

---

### ISO/IEC 42001 (AI Management Systems)

ISO/IEC 42001 defines requirements for an AI management system — the organisational structures, policies, processes, and controls that an organisation establishes to govern AI through its lifecycle. The APLC stage gates map to ISO 42001's AI system lifecycle requirements.

**Clause 6 (Planning)** requires that AI-related risks and opportunities be identified, and that objectives be established. This maps to Stage 1 (risk classification, business purpose validation, success criteria) and Stage 2 (behavioral envelope as the operationalisation of risk controls).

**Clause 8 (Operation)** requires that AI system lifecycle processes be implemented and controlled. The APLC stages and gate conditions are the operational implementation of Clause 8 requirements for agent products.

**Clause 9 (Performance Evaluation)** requires monitoring, measurement, analysis, and evaluation. This maps to Stage 3 (behavioral evaluation portfolio), Stage 4 (behavioral baseline), and Stage 5 (behavioral observability and drift detection).

**Clause 10 (Improvement)** requires that nonconformities be addressed and continual improvement be pursued. This maps to the APLC's feedback loops — persistent drift to Stage 2, quality incidents to Stage 3, business purpose miss to Stage 1 — and to Stage 6 (Maintain) as the continual improvement stage.

The APLC does not claim ISO 42001 certification for organisations that implement it; that claim requires a formal audit against the standard. The APLC does provide a lifecycle implementation that addresses the substantive requirements of ISO 42001's AI system lifecycle governance clauses.

---

### GDPR Article 22

Article 22 of the GDPR restricts automated decision-making about individuals: data subjects have the right not to be subject to decisions based solely on automated processing that produce legal effects concerning them or significantly affect them. Agent products that make or substantially influence consequential decisions about individuals — creditworthiness assessments, insurance pricing, employment screening, benefit eligibility — must comply with Article 22.

**APLC integration points.** Stage 1 trust architecture (`agent-conception.md`) must explicitly address whether the agent makes or substantially influences Article 22-relevant decisions. If it does, the trust architecture must specify how human review is provided to data subjects on request, how the agent's decision-making logic can be explained to a data subject in meaningful terms, and how data subjects can contest automated decisions.

Stage 2 behavioral specification (`agent-behavioral-specification.md`) must incorporate Article 22 obligations as hard boundaries: the agent must not process special category data in automated decisions without explicit consent or another lawful basis; the agent must be capable of providing a meaningful explanation of its reasoning on request; the escalation design must include a path for data subjects exercising Article 22 rights.

Stage 4 user-facing transparency (`agent-release-governance.md`) must confirm that the escalation path to human review is live, reachable, and meets the practical standard of effective human oversight — not merely nominally available.

---

### SR 11-7 (Model Risk Management)

The Federal Reserve's SR 11-7 guidance on model risk management was written for statistical and machine learning models used in financial decision-making. As AI agents are deployed in financial services contexts — for credit underwriting, fraud detection, customer service with regulatory implications, investment advice — SR 11-7 requirements apply to those agent products. The agent is the model for SR 11-7 purposes.

**SR 11-7's three pillars and APLC integration.** Conceptual soundness — the model's design and methodology must be sound and appropriate for its intended use — maps to Stage 1 and Stage 2: the business purpose must be validated, the trust architecture must be appropriate for the deployment context, and the behavioral specification must reflect genuine understanding of the agent's operational boundaries. Ongoing monitoring — performance must be monitored in production against established benchmarks — maps directly to Stage 5 behavioral observability and drift detection; the behavioral baseline is SR 11-7's benchmark. Model change governance — changes to the model must be governed with appropriate validation before implementation — maps to Stage 6 foundation model update governance and the recalibration gate; a model provider update that is accepted without validation is an SR 11-7 violation.

The APLC's stage gates are the implementation vehicle for SR 11-7 compliance in agent product deployments. A financial services organisation implementing the APLC for its agent products is implementing the lifecycle governance that SR 11-7 requires; it is not running a separate SR 11-7 compliance process alongside the APLC.

---

## APLC Maturity Levels

These maturity levels describe an organisation's governance capability for agent products, not the capability of any individual agent. An organisation at Level 3 has the governance infrastructure to build and release evaluated agent products; it may also have legacy agents deployed before that governance existed.

---

### Level 1 — Unstructured

**Manifesto phase requirement.** None. The agent product exists but the engineering loop may be entirely ungoverned. The absence of a manifesto phase requirement at Level 1 does not mean manifesto governance is irrelevant — it means the organisation has not yet established it, and that absence is part of the governance deficit Level 1 describes.

**Description.** Agent products are deployed without APLC governance. There may be informal processes — someone reviewed the demo before release, the engineering team added some safety filters — but there is no stage gate structure, no behavioral baseline, no formal evaluation portfolio, no named accountable human with documented scope.

**Indicators.** The team cannot answer: what are the hard behavioral limits of this agent? What was the behavioral quality at release? Has the agent's behavior changed since release, and if so, from what baseline? Who is accountable for behavioral outcomes in production?

**Risk profile.** Ungoverned behavioral exposure. Regulatory compliance posture depends on engineering judgment rather than documented evidence. Behavioral incidents are detected reactively, typically from user complaints or downstream consequences. Foundation model updates are accepted without regression testing.

**Most common obstacle to Level 2.** Perceived cost of retroactive specification. Teams with deployed agents that were built without APLC governance typically believe that the effort to write a behavioral specification for something already running is not worth the governance benefit. This belief is incorrect: the retrospective specification, even if imperfect, creates the foundation for drift detection and incident response that currently does not exist. The minimum viable path to Level 2 for an existing deployment is the retroactive adoption path described in `aplc.md`.

---

### Level 2 — Specified

**Manifesto phase requirement.** Phase 2 minimum. The engineering loop must exist with human approval on commits and a functioning Specify → Govern cycle. An organisation operating APLC Stage 3 (Build and Evaluate) without Phase 2 manifesto governance means the engineering execution that produces the agent artifact is itself ungoverned: no governed specification cycle, no human-approved commit gate, no auditable evidence of engineering decisions. A behavioral specification built on top of ungoverned engineering execution is a product-level governance document sitting on a deficient foundation.

**Description.** Stages 1 and 2 are complete. A behavioral specification exists and was used to guide engineering — it was not written after the fact to describe what was built. The Conception Gate and Behavioral Specification Gate have been assessed. The behavioral specification is the single source from which evaluation cases and operational monitoring specifications are derived.

**Key transition criteria from Level 1 to Level 2.** The behavioral specification exists as a document that preceded the production implementation. It addresses all four layers of the behavioral envelope. It traces to a Stage 1 product brief with a validated business purpose and a completed regulatory classification. A domain expert not involved in authoring has reviewed the use-case coverage map.

**Most common obstacle to Level 3.** Underestimating the evaluation portfolio requirement. Teams at Level 2 commonly believe that passing engineering tests (P8 evaluations) is sufficient for release. The transition to Level 3 requires understanding that P8 evaluations are Layer 1 of a four-layer portfolio, and that Layers 2, 3, and 4 address failure modes that Layer 1 was not designed to address.

---

### Level 3 — Evaluated

**Manifesto phase requirement.** Phase 3 minimum. The engineering loop must produce evidence bundles — the P8 deterministic evaluation suite must be running and its outputs must be part of the loop's Definition of Done. A behavioral evaluation portfolio (Layers 2, 3, and 4) built on top of ungoverned or unevaluated engineering execution is evaluating an artifact whose engineering correctness is unverified. Layer 1 of the behavioral evaluation portfolio is the P8 evidence bundle; without Phase 3 manifesto governance, Layer 1 does not exist in the required form, and the four-layer portfolio is structurally incomplete.

**Description.** Stage 3 is complete and the behavioral release gate is enforced. A four-layer behavioral evaluation portfolio exists and is maintained. The red-team protocol runs before every release. The behavioral release gate is a real decision point — releases have been blocked by gate failures and returned to Stage 3 for remediation.

**Key transition criteria from Level 2 to Level 3.** At least one release has been blocked by a gate failure and remediated before proceeding. The red-team protocol has been executed by a team that includes an independent tester. The behavioral baseline exists and was established before the first production deployment. Human evaluators have been engaged and their qualifications confirmed.

**Most common obstacle to Level 4.** The gap between evaluation cadence and operational monitoring. A team at Level 3 has rigorous evaluation at release time but may have sparse behavioral monitoring in production. The transition to Level 4 requires instrumenting Stage 5 behavioral observability — output quality rate, behavioral envelope compliance rate, drift indicators — before deployment rather than retrofitting it after incidents.

---

### Level 4 — Governed

**Manifesto phase requirement.** Phase 3–4 minimum with evidence-backed governance. The engineering loop must produce evidence bundles that gate release decisions, and the governance infrastructure must be capable of enforcing gate conditions from evidence rather than assertion. Autonomy Tier 2–3 agent products are credible at Level 4 governance; Tier 1 products remain viable but represent the simple end of the governed portfolio.

**Description.** Stages 4, 5, and 6 are operational. The behavioral baseline is established at each release, drift is monitored against it, the HITL queue is managed with defined SLOs, and foundation model update governance is in place. The composite state manifest is filed at every release and change event. Behavioral incidents are classified using the five-class framework and responded to per the protocols in `agent-operations.md`.

**Key transition criteria from Level 3 to Level 4.** At least one foundation model update has been detected, tested, and accepted or rejected through the governance process. At least one behavioral incident (any class) has been classified, responded to, and closed with a post-incident review producing a corrective action. The HITL queue has SLOs that have been verified to be resourced. The behavioral baseline at the last release can be retrieved and compared against current production metrics.

**Most common obstacle to Level 5.** Regulatory documentation gaps. Teams at Level 4 have strong operational governance but may not have the documentation structure required for formal conformity assessment. The APLC documents produced across Stages 1–4 constitute the majority of EU AI Act Annex IV technical documentation, but they must be maintained in retrievable form throughout the product's operational life. Discovering at Level 5 that Annex IV documentation was not systematically retained requires reconstruction that may be incomplete.

---

### Level 5 — Regulated

**Manifesto phase requirement.** Phase 4 minimum with independent validation capability. The engineering loop must support independent evidence validation — the capacity to demonstrate, to an external auditor or regulator, that the evidence bundles filed at gate decisions are genuine, complete, and unaltered. Autonomy Tier 3 is the minimum credible autonomy level for agent products at Level 5 governance; Tier 4 is permitted where the governance infrastructure has been independently validated as capable of governing at that autonomy level.

**Description.** Full lifecycle governance including Stage 7. EU AI Act conformity assessment is complete for applicable systems. The EU Declaration of Conformity is signed and filed with the EU AI Office. All regulatory requirements — EU AI Act, GDPR, SR 11-7, or jurisdiction-specific equivalents — are demonstrably met through the APLC's documented stage gate evidence. Retirement plans exist for all deployed agent products before deployment, and Stage 7 has been executed at least once for at least one retired agent product.

**Key transition criteria from Level 4 to Level 5.** The EU DoC is signed and filed for all applicable high-risk systems. A regulatory examination or audit has been conducted (internal or external) and the APLC documentation was sufficient to demonstrate compliance. At least one agent product has been retired through Stage 7 with full governance — user migration, record retention, decommission confirmation. The post-decommission documentation archive is retrievable and complete.

**What Level 5 does not mean.** Level 5 governance does not mean the agent products are perfect. It means the organisation can demonstrate, with documented evidence, that its agent products were conceived with a validated purpose, specified with a governed behavioral envelope, built and evaluated to a defined standard, released with documented accountability, operated with behavioral observability and drift detection, maintained with governance over planned and unplanned changes, and retired with user migration and record retention. The evidence chain is complete. The accountability chain is traceable. Regulators can examine it.

---

*See also: `aplc.md` (lifecycle overview and architecture), `agent-conception.md` (Stage 1), `agent-behavioral-specification.md` (Stage 2), `agent-behavioral-evaluation.md` (Stage 3), `agent-release-governance.md` (Stage 4), `agent-operations.md` (Stage 5), `agent-maintenance.md` (Stage 6), `agent-retirement.md` (Stage 7), `agent-composite-versioning.md` (composite state and incident investigation), `agent-regulatory-classification.md` (EU AI Act classification walkthrough), `manifesto.md` (engineering execution principles for Stage 3).*
