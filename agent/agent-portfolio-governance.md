# Agent Portfolio Governance
## APLC Portfolio-Level Governance Framework

*APLC document. Governs an organisation's entire portfolio of agent systems — the interactions, dependencies, and collective risk profile that individual agent system governance does not address. Audience: enterprise architects, risk officers, Regulatory Owners, Technical Owners managing multiple agent products.*

*Related documents: [[aplc.md]], [[agent-conception.md]], [[agent-maintenance.md]], [[agent-retirement.md]], [[agent-composite-versioning.md]], [[agent-regulatory-classification.md]]*

---

## Overview

Individual agent system governance addresses a single agent system through the APLC lifecycle. Portfolio governance addresses the interactions, dependencies, and collective risk profile of all agent systems in an organisation's agent portfolio. Portfolio governance is required because:

- Multiple agent systems may share a common foundation model — model updates affect all simultaneously
- Agent systems may interact (multi-agent workflows, P4 swarm principle) — one system's behavioral failure can cascade
- Regulatory exposure compounds across a portfolio — aggregate risk must be assessed alongside individual system risk
- Resource allocation across the portfolio (P11 FinOps) requires portfolio-level visibility

Portfolio governance does not replace individual agent system governance. Every agent system is governed individually per the APLC seven-stage lifecycle. Portfolio governance adds the cross-system layer that individual governance cannot provide.

---

## Portfolio Registry

The AGKB maintains a Portfolio Registry: a structured inventory of all agent systems under governance. Each entry records:

| Field | Description |
| --- | --- |
| Agent system identifier | Unique identifier, stable across the system's lifetime |
| Current APLC stage | Stage 1 through Stage 7, or Retired |
| Current CSH | Composite State Hash of the current production deployment |
| Foundation model identifier and version | Provider, model name, and snapshot version where available |
| Autonomy tier by use case | Tier assignment per use case, per [[agent-behavioral-specification.md]] |
| Regulatory classification | EU AI Act risk class and applicable sector frameworks |
| Business Owner | Named individual holding the Business Owner accountability role |
| Behavioral Owner | Named individual holding the Behavioral Owner accountability role |
| Technical Owner | Named individual holding the Technical Owner accountability role |
| Regulatory Owner | Named individual holding the Regulatory Owner accountability role |
| Current operational status | Active, Evaluation Hold, Degraded, Retired |

The Portfolio Registry is the authoritative source for all portfolio-level governance queries. It is maintained in AGKB and updated whenever any field changes. Stale Registry entries — entries whose CSH or accountability role assignments have not been confirmed within the governance cadence — are flagged as governance findings by the Governance Observability system.

---

## Foundation Model Epidemic Surveillance

When a foundation model is used by multiple agent systems, a model update is an "index case" — a change event that may propagate behavioral impact across all systems using that model. The epidemic surveillance model treats model updates as public health events: detect the index case, trace contacts, assess impact, and coordinate response before harm propagates.

### Epidemic Surveillance Protocol

**Step 1 — Index Case Detection.**
The Technical Owner monitoring function detects a new foundation model version or update announcement. Detection sources include: provider release notifications, CSH change detection in production (when a CSH changes without an engineering-initiated deployment, a model update has occurred), and model version monitoring. All three detection methods must be active; reliance on provider notification alone is insufficient because some provider updates do not include advance notice.

**Step 2 — Contact Tracing.**
The Portfolio Registry is queried to identify all agent systems using the affected foundation model. The query returns: agent system identifier, current autonomy tier, regulatory classification, operational volume (interaction count in the prior 30 days), and the name of the Technical Owner for each affected system. This is the exposed population — the set of agent systems whose behavioral profile may change as a result of the model update.

**Step 3 — Impact Assessment Triage.**
Impact assessments are prioritised across the exposed population by:
1. Autonomy tier (Tier 1 systems assessed first — highest autonomy, highest consequence of undetected behavioral change)
2. Risk classification (Critical and High-risk systems assessed before Medium and Low)
3. Operational volume (highest-volume systems assessed before lower-volume systems at equivalent tier and classification)

The triage order determines the sequence of evaluation, not whether evaluation occurs. All exposed systems require impact assessment before the model update is accepted into production.

**Step 4 — Coordinated Evaluation.**
For each exposed system, the impact assessment runs the behavioral evaluation portfolio (at minimum Layer 2 and Layer 3 per [[agent-behavioral-evaluation.md]]) against the new model version in a non-production environment. Evaluation uses the behavioral fingerprint comparison method: compare the behavioral fingerprint produced by the new model version against the baseline fingerprint established at last release. Deviations outside the drift threshold trigger the quarantine protocol.

**Step 5 — Quarantine Protocol.**
Agent systems where the impact assessment indicates Critical or High severity behavioral impact are placed in Evaluation Hold status in the Portfolio Registry. Systems in Evaluation Hold cannot accept the model update into production until:
- The full evaluation is completed
- Any Critical or High findings are remediated
- The Behavioral Release Gate criteria are satisfied for the new model version
- The Technical Owner and Behavioral Owner jointly approve the update

Systems in Evaluation Hold continue operating on their current model version. If the current model version is being withdrawn by the provider, an emergency recalibration process is initiated per [[agent-maintenance.md]].

**Step 6 — Portfolio Release Decision.**
Model update deployment is coordinated across the portfolio. Staggered release by risk tier: Tier 4 and lower-risk systems first (smallest blast radius if an undetected behavioral issue remains), then Tier 3, then Tier 2, then Tier 1. After each tier, monitor behavioral metrics for 48 hours before proceeding to the next tier. Monitoring uses the behavioral fingerprint comparison against the pre-update baseline; anomalies halt the staggered release.

### Epidemic Metrics

Portfolio-level tracking for each index case:

| Metric | Description | Governance SLA |
| --- | --- | --- |
| Affected system count | Number of agent systems using the updated model | Determined at Step 2 |
| Impact severity distribution | Count of systems at Critical / High / Medium / Low impact assessment | Determined at Step 3–4 |
| Time from index case to full portfolio assessment | Calendar days from detection to last system assessed | Target: 14 days for non-emergency updates |
| Quarantine rate | Percentage of exposed systems placed in Evaluation Hold | Reported per index case |
| Time from quarantine to clearance | Calendar days a system spends in Evaluation Hold | Target: 30 days maximum |

Epidemic metrics are reported to the portfolio governance cadence review (see Portfolio Governance Cadence below).

---

## Multi-Agent Interaction Governance

When agent systems interact — through tool calls, handoffs, shared context, or orchestration patterns (P4 swarm principle) — each agent system remains individually governed under the APLC. Interaction governance adds the cross-system layer.

### Interaction Registration

All defined interactions between agent systems are registered in AGKB. Each registered interaction records:

| Field | Description |
| --- | --- |
| Source agent identifier | The agent system initiating the interaction |
| Target agent identifier | The agent system receiving the interaction |
| Interaction type | Tool call, handoff, shared context read, shared context write, orchestration signal |
| Data flow description | What is sent, in what format, under what conditions |
| Authority level assigned | Whether the source agent's outputs are treated as operator-level or user-level inputs by the target |
| Behavioral specification reference | Pointer to the interaction boundary specification in both agents' behavioral specifications |

Unregistered interactions between governed agent systems are behavioral violations. The Governance Observability system monitors for interaction patterns not present in the Interaction Registry and raises findings when unregistered interactions are detected.

### Interaction Behavioral Specification

Each registered interaction must have a behavioral specification for the interaction boundary, maintained in the behavioral specifications of both participating agent systems (see [[agent-behavioral-specification.md]]). The interaction specification covers:

- What the source agent may send: the schema, content constraints, and conditions for the interaction
- What the target agent may receive: validation requirements, rejection conditions, and handling of malformed inputs
- What the target agent may return: the response schema and the conditions under which each response type is produced
- Authority assignment: the trust level at which the target agent treats inputs from the source agent

### Interaction Evaluation

Multi-agent evaluation cases are added to the evaluation portfolio of each participating agent system. Cases test the interaction boundary:

- Does the source agent correctly scope what it sends? (does not send inputs outside the registered data flow)
- Does the target agent correctly validate what it receives? (rejects malformed or out-of-scope inputs)
- Does the interaction produce the expected combined outcome under normal conditions?
- Does the target agent correctly handle failure conditions from the source agent?
- Does a compromised source agent input fail safely at the target agent's validation boundary?

### Cascade Failure Prevention

Containment (P10) at the interaction boundary is the primary cascade failure prevention mechanism. Each agent system validates inputs from other agent systems against its behavioral specification — it does not trust them unconditionally because they originate from another governed system. A compromised or misbehaving agent system must not be able to cause cascade failures in downstream agent systems through the interaction boundary.

Specific containment requirements for interaction boundaries:

- The target agent applies the same input validation to inputs from other agent systems as it applies to inputs from external users at the equivalent authority level
- The target agent's hard boundaries (Layer 1 of the behavioral envelope) are not bypassable by inputs from other agent systems, regardless of the authority level assigned to those inputs
- Interaction failures — where the source agent sends an input that the target agent's validation rejects — are logged as behavioral events in both agent systems' operational records and surfaced to the Portfolio Governance cadence review

---

## Swarm Governance at Portfolio Level

When the organization deploys multiple agent products that interact autonomously, portfolio-level swarm governance is required in addition to each individual product's APLC governance.

**Swarm registry.** The portfolio registry must capture, for each pair of agent products that interact: the interaction type (orchestrator→subordinate, peer-to-peer, data producer→data consumer), the authority relationship (which agent principal tier does the sending agent occupy in the receiving agent's trust architecture), and the data flow (what categories of information pass between the agents and whether any personal data is included in inter-agent messages).

**Swarm-level blast radius monitoring.** The portfolio-level monitoring must include aggregate blast radius tracking: for any coordinated task execution involving multiple agents, the total consequence of all agents' actions is computed and compared against the swarm-level blast radius ceiling defined in the swarm behavioral specification addendum. Blast radius exceedance at the swarm level triggers an immediate halt of the coordinated task and a Swarm Boundary Incident, even if each individual agent's actions were within its individual specification.

**Foundation model epidemic surveillance at swarm level.** If multiple agents in a portfolio share a foundation model provider or model version, a single provider-initiated model update can simultaneously affect all of them. Portfolio-level surveillance must detect these "model epidemic" scenarios: when a foundation model update notification is received, immediately identify all agent products whose CSH includes the affected model, and coordinate their regression testing. Sequential product-by-product testing is not sufficient for shared-model scenarios — coordinated testing enables detection of inter-agent behavioral interactions that may emerge from a model update affecting all participants simultaneously.

**Inter-agent incident escalation.** When an incident in one agent product is traced to behavior received from another agent product (e.g., adversarial content injected via an inter-agent message), the incident management protocol for both products activates simultaneously. The portfolio steward coordinates the joint incident response. Inter-agent incidents that cannot be attributed to either product independently are managed at the portfolio level with the portfolio steward as the accountable human.

---

## Portfolio Risk Aggregation

Portfolio-level risk is not the sum of individual system risks. Correlated risks — where multiple systems share a common dependency — require aggregate assessment because a failure in that dependency affects multiple systems simultaneously.

### Correlation Risk Factors

| Correlation Type | Risk Description | Governance Response |
| --- | --- | --- |
| Model correlation | Multiple systems use the same foundation model; a model vulnerability or behavioral shift affects all simultaneously | Epidemic surveillance (see above); limit portfolio concentration on any single model |
| Knowledge correlation | Multiple systems draw from the same knowledge base; knowledge staleness or contamination affects all simultaneously | Knowledge base governance cadence per [[agent-maintenance.md]]; separate knowledge base refresh governance from individual system recalibration |
| Regulatory correlation | Multiple systems operate under the same regulatory framework; a compliance finding or framework change affects all simultaneously | Regulatory Owner coordination; portfolio-level compliance assessment on regulatory change events |
| Operator correlation | Same Behavioral Owner or Technical Owner holds accountability for multiple systems; capacity constraint affects all simultaneously | Portfolio Registry capacity monitoring; flag when a single role holder is named for more than the organisation's defined maximum concurrent systems |

### Portfolio Risk Dashboard

The Governance Observability system maintains a portfolio risk panel as part of the broader governance dashboard. The portfolio risk panel includes:

**Model dependency map.** For each foundation model version in use across the portfolio: which agent systems depend on it, their autonomy tiers, their regulatory classifications, and their operational volumes. The map makes model concentration risk visible: a portfolio where 70% of Tier 1 systems use the same model version has a different risk profile than a portfolio with model version diversity.

**Knowledge dependency map.** For each knowledge base in use across the portfolio: which agent systems read from it, their update frequency expectations, and their last confirmed knowledge currency check.

**Regulatory exposure map.** For each regulatory framework applicable across the portfolio: which agent systems are governed by it, their current compliance status, and any open findings. The map surfaces correlated regulatory risk: a compliance finding that affects one system may affect all systems under the same framework.

**Operator capacity map.** For each accountability role holder: the number of agent systems they are named for, their systems' current APLC stages, and any open gate conditions requiring their participation. The map surfaces capacity risk: an accountability role holder managing many systems simultaneously may not be able to provide adequate governance attention to all of them.

The portfolio risk dashboard is reviewed by organisational governance on the cadence defined below.

---

## Portfolio Governance Cadence

| Governance Activity | Frequency | Participants | Output |
| --- | --- | --- | --- |
| Portfolio Registry review | Monthly | All Regulatory Owners | Updated Registry entries; new findings filed to AGKB |
| Epidemic surveillance summary | Weekly | Technical Owners | Index case status report; quarantine status updates |
| Portfolio risk dashboard review | Quarterly | Business Owners and Regulatory Owners | Risk findings; correlation risk assessment; capacity alerts |
| Cross-system lessons review | After each retirement | Behavioral Owners | Lessons integration into AGKB; active system notifications |
| Portfolio compliance assessment | Annually, or on regulatory framework change | Regulatory Owners | Compliance posture assessment; remediation plan for findings |
| Operator capacity review | Quarterly | Organisational governance | Capacity findings; role reassignment decisions if warranted |

Governance cadence reviews are not optional ceremonies. They are the mechanism by which portfolio-level signals reach the accountability roles that can act on them. A portfolio where the governance cadence has lapsed — where Registry entries are stale, epidemic surveillance summaries have not been produced, or the risk dashboard has not been reviewed — is a portfolio whose aggregate risk is unknown. Unknown aggregate risk is not managed risk.

---

## Governance Capacity Management

The portfolio's governance quality is bounded by the governance team's capacity. A governance team that is overloaded cannot execute gate assessments with genuine rigor, cannot maintain HITL queues within SLO, and cannot investigate behavioral incidents thoroughly. Governance overload is not a resource management problem to be solved by working harder — it is a governance risk that must be managed through portfolio scope, prioritization, and resourcing decisions.

### Governance Capacity Metric

Compute monthly: the ratio of required governance FTE (sum of all governance functions for all deployed products in the portfolio) to available governance FTE.

```
Governance Capacity Ratio = Required FTE / Available FTE
```

Required FTE estimation: use the minimum FTE estimates from `aplc-guide.md` Governance Team Capacity Requirements, adjusted for each product's actual complexity (interaction volume, incident history, recalibration frequency).

### Capacity State Thresholds and Responses

**Normal (ratio ≤ 0.80).** Governance team is operating within capacity. Standard governance processes apply without modification.

**Elevated (0.80 < ratio ≤ 1.00).** Governance team is near capacity. Required actions: (a) Portfolio Steward is notified with the current ratio and a breakdown by product and function; (b) new product conceptions require explicit Portfolio Steward approval with an assessment of which existing governance activities will be de-prioritized to accommodate the new product; (c) HITL sample rates for lowest-risk products may be temporarily reduced to the minimum viable level.

**Overload (ratio > 1.00).** Governance team is over capacity. Immediate required actions within 5 business days: (a) halt new product conceptions until the ratio returns to Normal; (b) reduce evaluation cadence for lowest-risk products to Stage 6 minimum; (c) escalate to the organizational leadership level that commissioned the APLC adoption — a formal resourcing request with timeline; (d) document which governance activities are being deferred and the corresponding risk acceptance.

An organization in Overload state for more than 60 consecutive days without a documented resourcing response or scope reduction is in governance capacity failure. This finding must be disclosed to the Regulatory Owner and included in the next regulatory examination or audit response.

### Portfolio Prioritization Under Capacity Constraint

When governance capacity is insufficient for full governance across all deployed products, the Portfolio Steward must prioritize explicitly — not implicitly through delay. Prioritization criteria (highest priority first):

1. Products in active behavioral incidents (quality, behavioral, safety, persona, adversarial)
2. Products at a pending gate decision (Operational Readiness Gate or Behavioral Release Gate)
3. Products with open Critical or High red-team findings
4. Products with active waivers approaching expiry
5. Products with the highest user populations or highest consequence decision-making
6. All other products: governance activities are deferred to the next available capacity window

Deferred governance activities are logged in the AGKB as pending actions with their deferral date and the capacity constraint rationale. Deferral does not cancel the activity — it schedules it. Activities deferred beyond their maximum acceptable deferral window (defined per activity type in the behavioral specification) require accountable human risk acceptance.

---

*Cross-references: [[aplc.md]] for the seven-stage lifecycle that individual agent systems follow; [[agent-conception.md]] for the Four Accountability Roles established at Stage 1; [[agent-composite-versioning.md]] for the Composite State Hash that the Portfolio Registry tracks; [[agent-maintenance.md]] for foundation model update governance at the individual system level; [[agent-retirement.md]] for the retirement process that generates cross-system lessons; [[agent-regulatory-classification.md]] for the regulatory classification that determines portfolio-level regulatory exposure.*