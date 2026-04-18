# Human Oversight Design — APLC Governance Framework

*Cross-lifecycle document of the Agentic Product Lifecycle. Governs the design, assignment, and governance of human oversight patterns across all APLC stages. Audience: product owners, behavioral owners, risk officers, operational governance leads.*

See [aplc.md](../aplc.md) for the lifecycle overview.
See [agent-behavioral-specification.md](agent-behavioral-specification.md) for the behavioral specification where oversight patterns are authored as Stage 2 artifacts.
See [agent-operations.md](agent-operations.md) for the operational mechanics of HITL queue management, reviewer calibration, and the four-channel learning protocol.

---

## Why Human Oversight Requires a Dedicated Governance Framework

Human oversight is not a single design decision. It is a family of structurally different patterns — each with distinct governance requirements, distinct accountability models, and distinct failure modes. The APLC's autonomy tiers (Tier 1 through Tier 4) classify the *scope* of agent authority. Human oversight patterns classify the *structure* of human involvement in agent decisions. These are complementary classifications; neither is sufficient alone.

An agent system may be Tier 3 (production-impacting, governed) while using any of several oversight patterns depending on the use case. A system may employ different oversight patterns for different use cases within the same deployment. A system may transition between oversight patterns as operational evidence accumulates. And some use cases require not just any human reviewer, but a qualified domain expert whose judgment defines what correct behavior looks like — a materially different governance requirement from general-competence human review.

Treating all human oversight as equivalent produces governance failures that do not surface until a regulatory examination or a serious incident. A HITL queue that is formally present but sized for asynchronous review is not providing the governance of a synchronous HITL design. A system classified as human-on-the-loop where no human is monitoring in real time is not providing the governance of a true HOTL design. An expert-driven process where reviewers lack the domain expertise to exercise genuine judgment is not providing the governance of expert oversight.

This document defines four oversight patterns, specifies their governance requirements, provides a decision framework for pattern assignment, governs transitions between patterns, and addresses the expert-driven loop as a first-class governance pattern.

---

## The Four Oversight Patterns

### Pattern 1: Human In the Loop (HITL)

**Definition.** The agent produces a candidate decision or action; a human reviews it and either approves, overrides, or escalates before the decision is enacted or the output is delivered. Human review is required for every interaction in the designated scope, not sampled.

**Modes:**
- **Synchronous HITL:** Human review occurs before the agent's output is delivered to the user or before any consequential action is taken. The user or downstream process waits during review. Used for high-stakes decisions where the cost of an uncaught error exceeds the cost of latency.
- **Asynchronous HITL:** The agent delivers its output or enacts its action; a human reviews the record immediately afterward with authority to correct, retract, or escalate. Used where output delivery is time-sensitive but retrospective correction is adequate for the risk profile.

**Accountability model.** The named human reviewer is accountable for each reviewed decision. The reviewer identity and decision record are retained in the AGKB Operational Artifacts for every HITL interaction in scope.

**Failure mode: rubber-stamping.** HITL governance degrades when reviewers approve without genuine assessment. Captured by the HITL Governance Capture Detection protocol in [agent-operations.md](agent-operations.md). HITL that is formally present but not genuinely exercised is not HITL governance — it is governance theater producing an accountability record with no accountability behind it.

**Minimum instrumentation.** Per-interaction review record (reviewer identity, decision, latency, confidence); override rate by use case; reviewer agreement rate; SLO compliance by escalation class.

---

### Pattern 2: Human On the Loop (HOTL)

**Definition.** The agent executes decisions autonomously within defined boundaries; a human monitors the agent's behavior at a defined cadence or in response to alert signals, and retains the authority to intervene — pausing, overriding, or re-routing — before consequences become irreversible. The human does not review every decision.

**What distinguishes HOTL from HITL.** In HITL, human review is required for each decision before or immediately after enactment. In HOTL, the human is available and monitoring but does not act on individual decisions unless a monitoring signal demands it. The governance obligation is on the *monitoring design*, not on per-decision review.

**Modes:**
- **Active HOTL:** A human is actively monitoring the agent's operational dashboard in real time during the agent's operation. Appropriate for high-velocity decision-making where individual decisions are low risk but pattern-level failures warrant rapid intervention.
- **Alert-driven HOTL:** The agent operates autonomously; automated monitoring detects pattern deviations and alerts a human who then reviews the flagged period and determines whether intervention is required. Appropriate where steady-state operation is well-understood and deviation signals are reliable.

**Accountability model.** The system steward or designated monitor is accountable for the monitoring design, the intervention threshold configuration, and the response to alerts. They are not accountable for each individual agent decision — they are accountable for the monitoring framework that would catch systematic failure.

**Irreversibility window.** The critical HOTL governance requirement: the time from a decision being made to that decision becoming irreversible must exceed the time from monitoring signal to human intervention. If the human cannot intervene before consequences are irreversible, HOTL is not providing the claimed governance function. The irreversibility window must be defined per use case at Stage 2 and verified at Stage 4 before deployment.

**Failure mode: monitoring gap.** HOTL degrades when the monitoring design fails to produce actionable signals in time for human intervention. A human who is nominally on the loop but never sees a signal, or sees signals too late to act, is not on the loop. Monitoring coverage, signal latency, and intervention-to-irreversibility margin must be measured and reported.

**Minimum instrumentation.** Monitoring coverage rate (% of agent decisions captured by monitoring); alert latency; time-to-intervention after alert; intervention-to-irreversibility margin; false negative rate (decisions outside specification that did not generate an alert).

---

### Pattern 3: Human Off the Loop (HOLL)

**Definition.** The agent executes fully autonomously within a human-approved, machine-enforced policy envelope. No human reviews individual decisions or monitors in real time. The human's governance function is exercised at the level of the envelope design, the periodic audit of envelope compliance, and the incident response when monitoring detects an envelope violation.

**What distinguishes HOLL from HOTL.** In HOTL, a human is present and reachable during operation, capable of intervening within the irreversibility window. In HOLL, there is no in-operation human involvement. The governance obligation is on the *envelope design* and the *post-hoc audit*, not on operational monitoring with intervention capability.

**Policy envelope requirements.** For HOLL to constitute governed autonomy (not ungoverned autonomy), the policy envelope must satisfy:
- Machine-enforced, not prompt-instructed: the envelope must be enforced by infrastructure constraints (tool permissions, action class restrictions, blast radius ceilings), not by behavioral guidance that the agent may circumvent under adversarial conditions or context pressure
- Auditable: every agent action must produce an evidence record sufficient to reconstruct what the agent did, why, and whether it was within the envelope, entirely from logged artifacts
- Revertible: the envelope must define rollback conditions and mechanisms so that actions outside the envelope can be reversed or contained
- Reviewed periodically: a named human reviews the envelope compliance record at a defined cadence; the cadence is defined by the use case's risk classification and specified at Stage 2

**Accountability model.** The Regulatory Owner and Technical Owner are jointly accountable for the envelope design. They are accountable for whether the envelope was correctly specified, whether the machine enforcement is adequate, and whether the periodic audit is genuine. They are not accountable for individual agent decisions made within the envelope — but they are accountable for any systematic gap between the envelope's intended constraints and its operational effect.

**Failure mode: envelope inadequacy.** HOLL fails when the envelope does not constrain the agent's behavior to the behavioral specification. Envelope inadequacy may be: too narrow (the agent cannot accomplish its task within the envelope), too wide (the envelope permits behaviors outside the behavioral specification), or incorrectly enforced (the stated envelope is not what the infrastructure enforces). All three are design failures, not operational failures.

**Minimum instrumentation.** Per-action evidence record; envelope boundary proximity metrics; periodic envelope compliance audit results; rollback-readiness verification cadence; time-to-detection of envelope violations.

---

### Pattern 4: Expert-Driven Loop (EDL)

**Definition.** A qualified domain expert — not a general-competence reviewer — exercises judgment that defines what correct behavior looks like for a designated use case class. The expert's judgment is the ground truth, not a validation of a pre-specified behavioral contract. Expert-driven oversight applies when the behavioral specification cannot fully formalize the correct behavior for a use case: the specification can bound it, but the actual correct response requires domain expertise to determine.

**What distinguishes EDL from HITL.** In HITL, a reviewer validates agent outputs against a pre-specified behavioral contract (the contract defines correctness; the reviewer checks compliance). In EDL, the expert *is* the correctness standard for use cases that cannot be fully specified — their judgment produces the ground truth from which behavioral contracts are refined over time. EDL is the oversight pattern where the expert is the specification, not its enforcer.

**Qualification requirements.** An expert-driven loop requires documented expert qualification:
- Domain credential: what professional qualification, certification, or demonstrated expertise establishes the expert's authority over the use case class
- Independence: the expert must not be the system's behavioral owner (who has an interest in the specification being found correct) — they must be organizationally independent
- Conflict of interest: the expert must not have a financial or reputational interest in the agent system's outputs being approved

**Expert judgment capture.** Expert judgment is expensive and not infinitely scalable. Each expert review must produce a structured record: the case characteristics, the expert's judgment, the reasoning (to the degree the expert can articulate it), and the behavioral pattern it represents. These records accumulate as the ground truth dataset from which behavioral contracts are refined (feeding Channel 2 of the HITL four-channel learning protocol in [agent-operations.md](agent-operations.md)).

**Scaling model.** Expert-driven loops scale through:
- Behavioral contract refinement: as the expert's judgment accumulates, the behavioral specification becomes more precise, progressively reducing the use cases that require expert review
- Rubric development: expert judgments are codified into rubrics that enable trained general reviewers to apply expert criteria to clear cases, reserving genuine expert review for novel or ambiguous cases
- Expert-to-reviewer calibration: general reviewers are calibrated against expert judgments using the same calibration protocol as the HITL reviewer calibration (see [agent-operations.md](agent-operations.md)), with the expert's judgments as the ground truth

**Failure mode: expertise dilution.** EDL fails when reviewers without the required domain expertise are assigned to expert-designated use cases. This may occur through cost pressure, resource constraint, or incorrect routing. A reviewer who lacks the domain expertise to exercise genuine judgment but approves cases at the expected rate is providing the appearance of expert oversight without its substance. Detection: expert calibration assessments applied to the reviewer pool; disagreement rate analysis between reviewer decisions and archived expert judgments.

**Minimum instrumentation.** Expert qualification records (on file, reviewed annually); review distribution by case class and reviewer expertise level; calibration accuracy of expert-designated reviewers against archived expert ground truth; behavioral contract refinement rate from expert judgment capture (how many new contracts or contract revisions per review cycle trace to expert review output).

---

## Oversight Pattern Decision Framework

### Stage 2 Assignment

Oversight pattern assignment is a behavioral specification element, not an operational decision. It is specified at Stage 2 per use case class and recorded in the behavioral contract's machine-readable schema alongside the autonomy tier and risk level. The pattern must be assigned before Stage 3 evaluation begins, because evaluation design depends on it: HITL evaluation cases require a human reviewer in the evaluation loop; EDL evaluation cases require a qualified expert; HOTL evaluation requires monitoring signal coverage testing.

**Assignment criteria:**

| Decision criterion | HITL | HOTL | HOLL | EDL |
| --- | --- | --- | --- | --- |
| Can correct behavior be fully specified in advance? | Recommended if yes | Recommended if yes | Required | Not recommended if yes |
| Is human review required per decision by regulation? | Required | Not sufficient | Not permitted | Required (with expert) |
| Is the irreversibility window long enough for human review? | Required | Required | N/A | Required |
| Does the use case require domain expertise to judge quality? | Optional | Optional | Not applicable | Required |
| Is the decision volume compatible with per-decision review? | Assess feasibility | Preferred over HITL if volume is high | Preferred if volume is very high | Assess feasibility |
| Is behavioral drift in this use class immediately consequential? | Appropriate | Appropriate with alert | Requires strong envelope | Appropriate |

**Autonomy tier to oversight pattern mapping:**

| Autonomy tier | Permitted oversight patterns | Notes |
| --- | --- | --- |
| Tier 1 (observe and propose) | HITL | All agent outputs reviewed before enactment |
| Tier 2 (branch, human approves) | HITL for merge decisions; HOTL for branch execution | Merge is HITL; work within the branch is HOTL |
| Tier 3 (production-impacting, governed) | HITL or HOTL depending on reversibility | HITL for irreversible actions; HOTL for reversible with adequate monitoring |
| Tier 4 (policy envelope, autonomous) | HOLL for in-envelope actions; HITL for envelope change | In-envelope execution is HOLL; envelope modification is HITL |

EDL may be applied at any tier where expert qualification is required; it modifies the reviewer qualification requirement, not the oversight structure.

### Mixed-Pattern Deployments

A single agent deployment may assign different oversight patterns to different use case classes. Mixed-pattern deployments are common and appropriate. Governance requirements:

**Pattern registry.** The behavioral specification must maintain a use-case-to-pattern registry: for each use case class in the use-case coverage map, the assigned oversight pattern is recorded. The registry is a required gate artifact at the Behavioral Specification Gate.

**Routing correctness.** The HITL Routing Intelligence Agent must route each production interaction to the correct oversight pattern. Misrouting — sending a HITL-designated interaction to HOTL monitoring, or sending an EDL-designated interaction to a non-expert reviewer — is a governance failure. Routing accuracy by pattern and use case is monitored as part of governance observability (see [governance-observability.md](../governance/observability.md)).

**Pattern conflict detection.** Within a single interaction that crosses use case class boundaries (e.g., a multi-turn interaction that begins as a HOTL use case and evolves into a HITL use case), the more restrictive pattern applies for the duration of the interaction from the point at which the higher-pattern use case is detected.

---

## Governance Requirements by Pattern

### HITL Governance Requirements

Operational mechanics: see [agent-operations.md](agent-operations.md) for queue design, SLOs by escalation class, reviewer workflow, capture detection, four-channel learning, and reviewer calibration.

**Additional requirements addressed here:**

**Synchronous vs. asynchronous designation.** For each HITL-designated use case, the behavioral specification must state whether human review is synchronous (before enactment) or asynchronous (immediately after). This is not an operational choice — it is a specification decision based on the use case's risk profile. Once specified, the designation governs the queue design and the SLO structure.

**Coverage floor.** HITL does not imply 100% review of all interactions in scope unless the designation is synchronous. For asynchronous HITL, the behavioral specification must define the minimum review coverage rate: the percentage of in-scope interactions that must receive human review within the asynchronous review window. The coverage floor must be achievable with the planned reviewer capacity — a coverage floor that cannot be met with available resources is a Stage 2 specification failure, not an operational resourcing problem.

**Minimum HITL reviewer-to-volume ratio.** Before the Operational Readiness Gate, the product owner must confirm that reviewer capacity meets both the SLO targets and the coverage floor for each HITL-designated use case class. A HITL design that is specified but not resourced does not provide HITL governance.

---

### HOTL Governance Requirements

**Monitoring specification.** The behavioral specification must define the monitoring design for each HOTL-designated use case class: what metrics are monitored, what thresholds trigger alerts, what the expected alert latency is, and who receives alerts. Monitoring specification is a behavioral specification element, not an operational configuration detail.

**Irreversibility window verification.** At Stage 4 (release governance), the irreversibility window for each HOTL use case must be verified: confirm that the time from decision to irreversibility exceeds the sum of (alert detection latency + human notification latency + human assessment time + intervention execution time). If the window is too narrow, either the oversight pattern must be upgraded to HITL or the use case's reversibility must be engineered to be longer (e.g., through delayed enactment or two-phase commit).

**Monitoring coverage audit.** Monitoring coverage must be audited periodically: does the monitoring detect behavioral specification violations in this use case class reliably? Monitoring coverage audits use evaluation cases from the behavioral evaluation portfolio, injected into the monitoring system to verify that violations produce alerts. Coverage audit cadence is specified at Stage 2.

**Escalation to HITL.** For HOTL use cases, the behavioral specification must define the conditions under which the monitoring system escalates a use case interaction from HOTL to HITL: what behavioral signal, at what threshold, produces a routing change from autonomous monitoring to per-decision review. Escalation conditions must be machine-detectable, not dependent on human pattern recognition.

---

### HOLL Governance Requirements

**Envelope specification completeness.** The policy envelope must satisfy all Tier 4 behavioral specification requirements from [agent-behavioral-specification.md](agent-behavioral-specification.md) (Layer 1 hard boundary: policy envelope as constraint; Layer 2 soft boundary: envelope drift triggers; Layer 4 adaptation scope: autonomous behavior within envelope). The envelope is not a summary — it is a complete machine-enforceable specification of permitted action classes and blast radius limits.

**Enforcement verification.** At Stage 4 (release governance), the machine enforcement of the policy envelope must be verified in a staging environment: confirm that actions outside the envelope are blocked by infrastructure, not only by the agent's behavioral disposition. Red-team testing of the enforcement mechanism (Layer 3 evaluation) must include attempts to exceed the envelope through the six attack categories.

**Audit trail completeness.** Every HOLL-mode agent action must produce an evidence record sufficient to reconstruct governance compliance entirely from logged artifacts: action type, timestamp, action parameters, the envelope provision under which the action was authorized, the output, and any downstream effects. The audit trail must be sufficient for a regulatory examiner to determine, for any action, whether it was within the approved envelope.

**Periodic compliance audit.** HOLL deployments require periodic envelope compliance audits at a cadence defined in the behavioral specification. Each audit reviews a sample of the action evidence record and confirms: that sampled actions were within the envelope, that the envelope's constraints operated as intended, and that boundary proximity metrics are within acceptable ranges. Audit findings are written to AGKB and reviewed by the Technical Owner and Regulatory Owner. A HOLL deployment that has not been audited within its specified cadence is operating without the governance that HOLL requires.

**Reversion trigger.** The behavioral specification must define conditions that trigger reversion from HOLL to a more restrictive oversight pattern: elevated boundary proximity metrics, audit findings of envelope violations, new red-team findings that expose envelope gaps, or changes in the regulatory environment that invalidate the envelope's compliance basis. Reversion is governed under the Oversight Pattern Transition Protocol below.

---

### Expert-Driven Loop Governance Requirements

**Expert roster maintenance.** The Regulatory Owner maintains a roster of qualified experts for each EDL-designated use case class, including: expert identity, qualification basis, conflict-of-interest attestation, and most recent calibration assessment. The roster is a Stage 2 artifact filed in AGKB and updated whenever experts join or leave the roster.

**Case routing to qualified experts.** The HITL Routing Intelligence Agent must route EDL-designated cases only to reviewers on the qualified expert roster for that use case class. Routing to a non-expert reviewer is a governance failure regardless of the reviewer's general calibration scores.

**Expert judgment records.** Each expert review must produce a structured judgment record: the case presented, the expert's judgment, the behavioral pattern the case represents, and any behavioral contract refinement the judgment implies. Records are stored in AGKB and used as ground truth for:
- General reviewer calibration for EDL use case classes
- Behavioral specification refinement (reducing the proportion of cases requiring expert review as the specification becomes more precise)
- Evaluation case authorship (expert-reviewed cases may be contributed to Layer 4 of the evaluation portfolio)

**Expert availability as a governance risk.** If the qualified expert roster cannot meet the volume of EDL-designated cases within the review SLO, this is a governance risk that must be reported to the product owner. Mitigation options: increase the expert roster, redesign the use case to reduce the proportion requiring expert review through behavioral contract refinement, or restrict the deployment scope until expert capacity matches demand. Proceeding with non-expert reviewers for EDL cases is not a mitigation — it is a governance failure.

---

## Oversight Pattern Transition Protocol

Oversight patterns are not permanent. Operational evidence may support transitioning to a less restrictive pattern (as confidence increases), or an incident or regulatory change may require transitioning to a more restrictive pattern.

### Transition Toward Less Restriction (e.g., HITL → HOTL, HOTL → HOLL)

A transition toward less restrictive oversight requires documented evidence that the current oversight pattern's governance function can be adequately maintained at the less restrictive level. Required evidence:

1. **Behavioral stability record:** The use case class has operated within its behavioral specification consistently for a defined period (minimum: 90 days at the current oversight level with no specification violations)
2. **Override rate analysis:** The override rate in the HITL queue for this use case class has been below a defined threshold for the stability period (threshold defined in the behavioral specification at Stage 2)
3. **Monitoring design validation:** For transition to HOTL, the proposed monitoring design has been validated against the use case's behavioral specification — monitoring coverage audit confirms that violations would generate alerts within the required latency
4. **Envelope validation:** For transition to HOLL, the proposed policy envelope has been validated against the full behavioral evaluation portfolio for this use case class (not just Layer 1 and Layer 2 — Layer 3 red-team must cover the HOLL attack surface)

**Transition gate.** Transition to a less restrictive pattern requires a mini-gate review with the Behavioral Owner, Technical Owner, and Regulatory Owner. The transition gate record is filed in AGKB. Transition is not effective until the gate record is filed — the old pattern governs until then.

### Transition Toward More Restriction (e.g., HOTL → HITL, HOLL → HOTL)

Reversion to a more restrictive oversight pattern is required when any of the following conditions occur:

- Any behavioral incident in the use case class (all five incident classes trigger reversion assessment)
- Override rate (for alert-driven escalations) exceeds the threshold specified for HOTL → HITL reversion in the behavioral specification
- Envelope proximity metrics sustained above the threshold specified for HOLL → HOTL reversion
- New red-team finding of High or Critical severity in the use case class
- Regulatory change that requires human review per decision

**Reversion is immediate.** Unlike less-restrictive transition (which requires a gate), reversion is effective immediately on the triggering condition. The Behavioral Owner is notified and confirms reversion within 4 hours. The routing system is updated within 1 hour of reversion being confirmed. The reversion record is filed in AGKB.

**Reversion review.** Within 10 business days of reversion, the Behavioral Owner conducts a reversion review: what triggered the reversion, whether the oversight pattern assignment was correct at Stage 2, and whether the transition to the less restrictive pattern had been premature. The reversion review is required input to the next Stage 6 maintenance cycle planning.

---

## Oversight Adequacy Assessment

### What Oversight Adequacy Means

An oversight design is adequate when the human governance function it is supposed to provide is actually being delivered — not just when the oversight mechanism is formally present. Adequacy is a judgment about operational effectiveness, not structural compliance.

**HITL adequacy:** Reviewers are exercising genuine judgment (not rubber-stamping); coverage floors are being met; SLOs are being met; override rates reflect real disagreement, not compliance theater; reviewer calibration is current
**HOTL adequacy:** Monitoring is detecting behavioral specification violations before they become irreversible; alerts are generating human intervention within the intervention window; the false negative rate is within the specified tolerance
**HOLL adequacy:** The enforcement mechanism is blocking out-of-envelope actions; audit compliance is current; boundary proximity metrics are stable; rollback readiness has been verified
**EDL adequacy:** Expert reviewers hold documented qualifications; they are exercising genuine domain expertise (not applying general review criteria); their judgments are producing behavioral contract refinements; the expert roster has sufficient capacity

### Adequacy Indicators in the Governance Observability Dashboard

The Governance Observability Dashboard (see [governance-observability.md](../governance/observability.md)) includes an Oversight Adequacy panel with the following indicators per oversight pattern per use case class:

**HITL:** Override rate (too low for complex use cases → capture signal); reviewer agreement rate (too high → capture signal; too low → specification ambiguity); calibration current flag; SLO compliance rate; coverage floor compliance
**HOTL:** False negative rate; alert latency against irreversibility window margin; monitoring coverage audit result date; escalation-to-HITL rate (too low for high-risk use cases may indicate signal insensitivity)
**HOLL:** Audit compliance date; boundary proximity distribution; enforcement verification date; rollback readiness verification date; envelope compliance rate
**EDL:** Expert roster currency date; expert capacity vs. EDL case volume; calibration accuracy of reviewers against expert ground truth; behavioral contract refinement rate

### Oversight Adequacy Review Cadence

| Oversight pattern | Review frequency | Reviewer |
| --- | --- | --- |
| HITL | Monthly (included in HITL monthly report) | Behavioral Owner |
| HOTL | Quarterly (monitoring coverage audit) | Technical Owner + Behavioral Owner |
| HOLL | Per-audit-cadence (defined in behavioral specification) | Technical Owner + Regulatory Owner |
| EDL | Quarterly (expert roster and calibration review) | Regulatory Owner + Behavioral Owner |

Adequacy findings that indicate a pattern is not delivering its governance function trigger an immediate reversion review.

---

## Gate Integration

### Behavioral Specification Gate (Stage 2 exit)

The following oversight design artifacts must be present and approved before Stage 3 begins:

- Oversight pattern assigned per use case class in the pattern registry
- For HITL: synchronous vs. asynchronous designation; coverage floor; reviewer capacity confirmation
- For HOTL: monitoring design specification; irreversibility window analysis; escalation-to-HITL conditions
- For HOLL: policy envelope specification (complete per Tier 4 requirements); enforcement mechanism design; audit cadence; reversion trigger conditions
- For EDL: qualified expert roster (initial); expert qualification criteria; expert judgment record schema

### Behavioral Release Gate (Stage 3 exit)

The following must be satisfied before release:

- All four oversight patterns used in this deployment have been exercised during Stage 3 evaluation (not just simulated)
- EDL cases have been reviewed by a roster expert, not a general-competence evaluator
- HOTL monitoring design has been validated against behavioral evaluation cases in a staging environment
- HOLL enforcement mechanism has been red-team tested against the six attack categories

### Operational Readiness Gate (Stage 4 exit)

- Reviewer capacity confirmed for all HITL use cases (roster + SLO can be met simultaneously)
- Expert roster confirmed for all EDL use cases (capacity vs. expected volume)
- HOTL monitoring instrumented and validated in production environment
- HOLL audit schedule confirmed and first audit date recorded in AGKB
- Irreversibility window verification completed for all HOTL use cases in the production environment

---

## Relationship to Other APLC Documents

**[agent-behavioral-specification.md](agent-behavioral-specification.md):** Oversight pattern is specified at Stage 2 as a behavioral contract element. The machine-executable schema includes the `oversight_pattern` and `reviewer_qualification` fields alongside autonomy tier and risk level.

**[agent-operations.md](agent-operations.md):** HITL operational mechanics — queue design, SLOs, reviewer calibration, four-channel learning, capture detection — are specified there. This document governs the design decisions that precede and frame those operational mechanisms.

**[agent-behavioral-evaluation.md](agent-behavioral-evaluation.md):** Layer 4 (human preference evaluation) uses EDL when the evaluation cases require domain expert judgment to assess. The EDL reviewer qualification requirements here govern the evaluator qualification requirements there.

**[governance-agents.md](../governance/agents.md):** The HITL Routing Intelligence Agent implements the routing logic that assigns each production interaction to the correct oversight pattern. Its routing accuracy by pattern is a key governance observability metric.

**[agent-portfolio-governance.md](agent-portfolio-governance.md):** Portfolio-level oversight pattern distribution is a portfolio risk metric — an organization where all high-risk systems have migrated to HOLL without documented transition gates is carrying governance risk that portfolio governance must surface.

---

*See also: `aplc.md` (lifecycle overview and governance agent autonomy constraint), `agent-conception.md` (four accountability roles, each with oversight-related obligations), `agent-release-governance.md` (Stage 4 oversight infrastructure verification), `agent-maintenance.md` (oversight pattern review as a Stage 6 recalibration trigger), `agent-retirement.md` (oversight pattern history as part of behavioral footprint).*
