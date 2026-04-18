# APLC Governance Agents

*APLC document. Specifies the ten APLC Governance Agents — specialized agents that execute governance functions across the Agentic Product Lifecycle. Each agent automates a governance task that previously required manual human effort, while maintaining appropriate human decision points. Audience: governance architects, behavioral owners, technical owners, and teams responsible for deploying governance infrastructure.*

*Related documents: [[aplc]], [governance knowledge base](knowledge-base.md), [[agent-behavioral-specification]], [[agent-behavioral-evaluation]], [[agent-operations]], [[agent-maintenance]], [[agent-composite-versioning]], [[agent-regulatory-classification]]*

---

## Governance Agent Framework

### Design Principles

Governance agents are agent products. They are subject to the same APLC governance that applies to any agent product an organization deploys. The governance of governance agents is not a concession or an ironic complication — it is the structural safeguard that prevents governance automation from becoming governance theater. An ungoverned governance agent that always recommends release clearance is more dangerous than no governance automation: it provides the appearance of process while providing none of the substance.

Five design principles govern every APLC governance agent.

**Each governance agent is itself governed under the APLC.** A governance agent must have, at minimum: a Stage 1 product brief defining its purpose, authority limits, and accountability; a Stage 2 behavioral specification defining its hard boundaries and escalation design; and a Stage 3 evaluation portfolio covering its happy path and adversarial cases. Advisory governance agents operating within tightly bounded governance task scopes may be governed at APLC minimum viable level (Level 2 per [[aplc-guide]]); governance agents with broader authority or direct gate influence must be governed at the level appropriate to their autonomy tier and organizational impact.

**Autonomy tier defaults to Tier 2 (human-on-the-loop).** The default autonomy posture for all governance agents is Tier 2: the agent produces outputs, proposes decisions, and flags risks, but a named human makes the consequential decision. Escalation to Tier 1 (human-in-the-loop) is required for high-stakes decisions: gate pass/fail determinations for regulated agent products, severity classifications for red-team findings, and any decision that feeds directly into an immutable governance record. Governance agents may not operate at Tier 3 or Tier 4 for decisions that affect gate conditions or immutable records.

**Governance agent evaluations are mandatory.** Every governance agent must have its own behavioral evaluation portfolio before deployment. The evaluation must cover: the governance function the agent is designed to perform (does it produce accurate, well-formed outputs?); the adversarial cases that would cause a governance agent to fail at its governance function (does it recommend clearance for findings that should block release? does it misclassify failure modes? does it suppress escalations?); and the calibration of its human decision points (does it escalate at the right threshold?). A governance agent whose evaluation suite does not include adversarial cases for its governance function is not governed — it is deployed.

**Governance agents are subject to behavioral drift monitoring.** Because governance agents are agent products, they are subject to behavioral drift per the same mechanisms as any deployed agent: foundation model updates, knowledge base staleness, memory accumulation. The behavioral drift monitoring requirements of Stage 5 apply to governance agents; so does the recalibration governance of Stage 6. A governance agent that has drifted from its behavioral specification is not an inert system — it is an active source of governance failure in the products it governs.

**Governance agent outputs carry epistemic tier labels.** Every output produced by a governance agent that enters any APLC record, gate assessment, or evidence bundle must carry an epistemic tier label per the requirements in [[agent-behavioral-evaluation]]: the label *agent-proposed-with-human-review* with named reviewer and review date for outputs that inform gate conditions; the label *agent-generated* for outputs used as working documents and analysis inputs that do not enter gate records directly. Gate records may not carry the *agent-generated* label without named human confirmation of each finding.

### Meta-Governance Responsibility

The organization must designate a named Behavioral Owner responsible for the governance agent portfolio as a whole — the behavioral specifications, evaluation suites, and drift monitoring of all ten governance agents. This is a distinct accountability from the Behavioral Owners of the agent products the governance agents serve. The governance agent portfolio Behavioral Owner is responsible for ensuring that governance agents are updated when the APLC governance framework evolves, that evaluation suites for governance agents are maintained against current gate criteria, and that governance agent behavioral drift does not silently degrade the quality of governance decisions across the organization's agent product portfolio.

---

## The Ten Governance Agents

---

### 1. Regulatory Classification Agent

**Purpose.** Classifies an agent system against applicable regulatory frameworks — including risk tier determination under AI regulation, sector-specific regulatory requirements, and documentation obligations — so that Stage 1 governance decisions are grounded in current regulatory context rather than legal counsel's summary from a prior engagement.

**APLC Stage(s) Served.** Stage 1 (Conceive).

**Inputs.**

| Input | Source | Format |
| --- | --- | --- |
| System description | Product brief draft | Structured document |
| Intended use and deployment context | Stage 1 product brief draft | Structured document |
| Regulatory framework updates | AGKB Regulatory Precedent Store (Category E) + source monitoring feeds | Structured regulatory text |
| Prior classification precedents | AGKB Regulatory Precedent Store (Category E) | Structured records |

**Outputs.**

| Output | Destination | Epistemic Tier Requirement |
| --- | --- | --- |
| Risk classification recommendation | Stage 1 governance record; AGKB Category A | Agent-proposed-with-human-review |
| Conformity assessment pathway recommendation | Stage 1 governance record | Agent-proposed-with-human-review |
| Documentation requirements checklist | Stage 1 working document | Agent-proposed-with-human-review |
| Regulatory precedent citations | Working document for Regulatory Owner review | Agent-generated (working document only) |

**Tools Required (Generic).** Regulatory text retrieval and semantic matching; structured document analysis; classification reasoning with evidence citation; checklist generation from regulatory framework mapping.

**Autonomy Tier.** Tier 2 (human-on-the-loop). The agent produces a classification recommendation with evidence; a named Regulatory Owner makes the final classification determination.

**Human Decision Points.**

- **Classification approval.** The Regulatory Owner reviews the agent's classification recommendation and either confirms it or disputes it with documented rationale. Confirmed classifications are filed in the AGKB by the AGKB Governance Agent. Disputed classifications are resolved through the dispute resolution process below.
- **Classification dispute resolution.** When the Regulatory Owner disputes the agent's classification — typically because the product has characteristics that fall at a regulatory boundary — the dispute is escalated to qualified legal counsel. The agent provides the specific regulatory clauses that informed its recommendation and the specific product characteristics that it weighted in the classification. The legal determination supersedes the agent's recommendation; the agent's reasoning chain is retained as a working document, not as the classification record.

**Evaluation Requirements.** The evaluation suite must cover: correct classification of unambiguous cases across all applicable risk tiers; correct identification of boundary cases with appropriate uncertainty expression; accuracy of documentation checklist generation against current regulatory framework; adversarial cases where the system description is crafted to mislead toward a lower risk classification. At minimum one adversarial classification evaluation must be included for each risk tier boundary.

**Failure Modes.**

| Failure Mode | Severity | Detection |
| --- | --- | --- |
| Under-classification: recommends lower risk tier than applicable | Critical | Human review; legal audit |
| Documentation checklist incomplete: misses required conformity documentation | High | Regulatory Owner review; Stage 4 gate check |
| Regulatory framework staleness: applies superseded regulatory text | High | Source monitoring; AGKB staleness detection |
| Over-classification: recommends higher risk tier, creating unnecessary burden | Medium | Regulatory Owner review |
| Uncertainty suppression: provides a definitive classification for a boundary case without flagging uncertainty | Medium | Calibration evaluation |

---

### 2. Use-Case Elicitation Agent

**Purpose.** Conducts structured elicitation of behavioral requirements, converting product briefs and stakeholder inputs into a draft use-case registry and edge-case catalog that the Behavioral Owner can review and complete. Addresses the consistent gap between what product teams intend and what they document in Stage 2.

**APLC Stage(s) Served.** Stage 2 (Specify Behaviorally).

**Inputs.**

| Input | Source | Format |
| --- | --- | --- |
| Product brief | Stage 1 output | Structured document |
| Stakeholder interview transcripts | Business Owner, domain stakeholders | Transcript text |
| Domain context from prior deployments | AGKB Category E — Specification Pattern Library | Structured records |
| Failure mode precedents for this domain | AGKB Category E — Failure Mode Catalog | Structured records |

**Outputs.**

| Output | Destination | Epistemic Tier Requirement |
| --- | --- | --- |
| Draft use-case registry | AGKB Category A (draft, pending review) | Agent-proposed-with-human-review |
| Edge-case catalog | AGKB Category A (draft, pending review) | Agent-proposed-with-human-review |
| Constraint candidates | Stage 2 working document for Behavioral Owner | Agent-generated (working document) |
| Coverage gap analysis | Stage 2 working document | Agent-generated (working document) |

**Tools Required (Generic).** Transcript analysis and intent extraction; semantic matching against specification pattern library; structured output generation for use-case registry schema; gap detection against use-case coverage map requirements from [[agent-behavioral-specification]].

**Autonomy Tier.** Tier 2 (human-on-the-loop).

**Human Decision Points.**

- **Completeness sign-off by Business Owner.** The Business Owner reviews the draft use-case registry and confirms that it accurately captures the intended scope of the agent product, including cases that stakeholders described but may not have formally articulated. The Business Owner may add, modify, or remove use cases from the draft before sign-off. Sign-off is a named, dated attestation filed in the AGKB — it is not a verbal confirmation. A registry without Business Owner sign-off does not advance to the Behavioral Specification Gate.
- **Domain expert review of edge cases.** The edge-case catalog requires review by a domain expert not involved in the product brief or the elicitation process. The domain expert's role is to identify edge cases that neither the stakeholder interviews nor the agent's pattern library surfaced. This review is a gate condition for the Behavioral Specification Gate.

**Evaluation Requirements.** The evaluation suite must cover: completeness of use-case extraction from clear product briefs; coverage gap detection against known use-case categories for the domain; adversarial cases where the product brief is designed to scope-limit the use-case registry to an extent that would leave important behavioral territory unspecified; accuracy of constraint candidates against the behavioral specification template.

**Failure Modes.**

| Failure Mode | Severity | Detection |
| --- | --- | --- |
| Scope limitation bias: systematically extracts fewer use cases than domain warrants | High | Domain expert review; comparison to specification pattern library |
| Edge case suppression: does not surface edge cases that challenge the happy path | High | Domain expert review; red-team precedent check |
| Pattern library over-application: maps new product onto prior patterns, missing domain-specific requirements | Medium | Business Owner review; domain expert review |
| Constraint candidate under-generation: misses constraint categories relevant to the autonomy tier | Medium | Constraint Consistency Checker (downstream) |

---

### 3. Constraint Consistency Checker

**Purpose.** Verifies that the behavioral specification's constraint set is internally consistent — that hard boundaries do not contradict each other, that soft boundaries are achievable given the hard boundary envelope, that autonomy tier assignments are consistent with the stated constraints, and that constraint coverage is complete across the use-case registry. Addresses the class of specification defects that human authors introduce when writing large, multi-section behavioral specifications without systematic cross-reference.

**APLC Stage(s) Served.** Stage 2 (Specify Behaviorally).

**Inputs.**

| Input | Source | Format |
| --- | --- | --- |
| Behavioral contract set | AGKB Category A — current draft | Structured document |
| Constraint catalog | AGKB Category A — current draft | Structured records |
| Autonomy tier assignments | AGKB Category A | Structured records |
| Use-case registry | AGKB Category A | Structured records |

**Outputs.**

| Output | Destination | Epistemic Tier Requirement |
| --- | --- | --- |
| Consistency report | Stage 2 governance record; Behavioral Owner | Agent-proposed-with-human-review |
| Conflict list | Stage 2 governance record | Agent-proposed-with-human-review |
| Coverage gap list | Stage 2 working document | Agent-proposed-with-human-review |
| Suggested resolutions | Stage 2 working document for Behavioral Owner | Agent-generated (working document) |

**Tools Required (Generic).** Formal constraint analysis; semantic conflict detection across specification clauses; coverage mapping from use-case registry to constraint catalog; structured report generation.

**Autonomy Tier.** Tier 2 (human-on-the-loop). The agent identifies conflicts; the Behavioral Owner resolves them.

**Human Decision Points.**

- **Conflict resolution approval.** For each conflict identified in the consistency report, the Behavioral Owner determines the resolution: which constraint takes precedence, whether both constraints must be revised, or whether an apparent conflict is intentional and requires a clarifying annotation. The Behavioral Owner's resolution decisions are filed as part of the Behavioral Specification Gate record. The agent's role is conflict identification, not resolution.
- **Coverage gap prioritization.** When the agent identifies use cases in the registry that lack corresponding constraints, the Behavioral Owner determines which gaps are genuine specification gaps requiring new constraint authoring, and which are gaps that the existing constraints implicitly address through scope or domain framing.

**Evaluation Requirements.** The evaluation suite must cover: detection of direct contradictions between hard boundary clauses; detection of soft boundary configurations that fall outside the hard boundary envelope; detection of constraint-free use cases in the registry; adversarial cases where conflicts are introduced through ambiguous phrasing that does not produce a surface-level contradiction but is operationally inconsistent; and accuracy of suggested resolutions against known resolution patterns in the specification pattern library.

**Failure Modes.**

| Failure Mode | Severity | Detection |
| --- | --- | --- |
| False conflict suppression: does not detect a real constraint conflict | Critical | Gate review; production behavioral incident |
| False conflict generation: flags non-existent conflicts, degrading Behavioral Owner trust | Medium | Behavioral Owner calibration review |
| Coverage gap under-detection: misses use cases with no corresponding constraints | High | Domain expert review; Stage 3 evaluation discovery |
| Resolution suggestion accuracy: suggests resolutions that introduce new conflicts | Medium | Behavioral Owner review |

---

### 4. Behavioral Evaluation Swarm Coordinator

**Purpose.** Orchestrates the four-layer behavioral evaluation portfolio for Stage 3, coordinating the assignment, execution, and consolidation of evaluation activities across all four layers — engineering evaluations, behavioral coverage evaluations, red-team exercises, and human preference evaluations — and producing the consolidated evaluation report for the Behavioral Release Gate.

**APLC Stage(s) Served.** Stage 3 (Build & Evaluate).

**Inputs.**

| Input | Source | Format |
| --- | --- | --- |
| Behavioral specification | AGKB Category A | Behavioral contract record |
| Evaluation suite definition | AGKB Category B | Evaluation suite definition record |
| Threshold record | AGKB Category B | Threshold record |
| Prior evaluation run records | AGKB Category B | Evaluation run records |
| Red-team findings (completed) | AGKB Category B | Red-team finding records |
| Human evaluation rubric scores | AGKB Category B | Layer 4 assessment records |

**Outputs.**

| Output | Destination | Epistemic Tier Requirement |
| --- | --- | --- |
| Consolidated evaluation report | AGKB Category B; Behavioral Release Gate record | Agent-proposed-with-human-review |
| Gate recommendation (pass/conditional/fail) | Gate governance record (via AGKB Governance Agent) | Agent-proposed-with-human-review — named human decision required |
| Coverage gap summary | Evaluation team lead; AGKB working record | Agent-proposed-with-human-review |
| Open findings tracker | Evaluation team lead working document | Agent-generated |

**Tools Required (Generic).** Multi-layer status aggregation; threshold comparison against configured pass bars; structured report assembly; coverage calculation against use-case registry; finding severity aggregation and release consequence determination.

**Autonomy Tier.** Tier 2 (human-on-the-loop) for standard products. Tier 1 (human-in-the-loop) required for high-risk systems under applicable AI regulation — the gate recommendation must be presented to and explicitly accepted or rejected by the named evaluation team lead before it enters the gate record.

**Human Decision Points.**

- **Gate pass/fail decision for high-stakes systems.** For systems classified as high-risk under applicable regulation, the gate recommendation produced by the coordinator is presented to the evaluation team lead and the product owner for explicit decision. The agent's consolidation and recommendation are inputs; the humans make the gate decision. The gate decision record carries the named human decision-maker, not the agent.
- **Open finding disposition.** When the consolidated report identifies open findings (medium or low severity items not yet resolved), the evaluation team lead determines the disposition: remediate before release, document in the release record with a mitigation plan, or accept the risk with documented rationale. The coordinator presents the findings and their release consequence classifications; the disposition decision is human-made.
- **Evaluation suite gap decisions.** When the coordinator identifies use-case zones not covered by the current evaluation suite, the evaluation team lead decides whether to extend the suite before the gate, accept the gap with documented rationale, or require a Stage 2 specification review.

**Evaluation Requirements.** The evaluation suite must cover: accurate aggregation of layer results against threshold records; correct application of release consequence rules (Critical findings block; High findings block without mitigation); adversarial cases where individual layer results are designed to appear acceptable in isolation but fail at portfolio level; and accuracy of coverage gap detection against the use-case registry.

**Failure Modes.**

| Failure Mode | Severity | Detection |
| --- | --- | --- |
| Finding severity laundering: consolidates red-team findings at lower severity than filed | Critical | Human review of finding records vs. consolidated report; audit |
| Coverage gap suppression: does not surface evaluation coverage gaps | High | Evaluation team lead review; post-release incident |
| Threshold misapplication: applies wrong threshold record for the current product version | High | AGKB Governance Agent schema validation |
| Report completeness failure: omits required sections of the evaluation clearance report | Medium | Gate review checklist |

---

### 5. Red-Team Adversary Agent

**Purpose.** Executes adversarial evaluation against the six mandatory attack categories (and, for Tier 4 products, the Policy Envelope Escape category), operating in a sandboxed environment isolated from the production agent. The agent systematically generates and executes adversarial inputs, documents the agent's responses, and produces a structured findings log — converting ad hoc adversarial exploration into a repeatable, documented adversarial evaluation process.

**APLC Stage(s) Served.** Stage 3 (Build & Evaluate); ongoing adversarial monitoring in Stage 5 (Operate) for agents where continuous adversarial evaluation is specified.

**Inputs.**

| Input | Source | Format |
| --- | --- | --- |
| System prompt and configuration | Stage 3 evaluation environment | Evaluated agent system state |
| Behavioral specification | AGKB Category A | Behavioral contract record |
| Red-team scope definition | Stage 3 governance record | Structured scope document |
| Prior red-team findings | AGKB Category B — this product and cross-product | Red-team finding records |
| Failure mode catalog | AGKB Category E | Failure mode catalog entries |

**Outputs.**

| Output | Destination | Epistemic Tier Requirement |
| --- | --- | --- |
| Attack log | AGKB Category B — red-team findings (draft) | Agent-generated (requires red-team lead human review before filing) |
| Vulnerability report | AGKB Category B — filed after human review | Agent-proposed-with-human-review |
| Severity ratings | Vulnerability report | Agent-proposed-with-human-review |

**Tools Required (Generic).** Sandboxed agent interaction environment; attack scenario generation across six mandatory categories; response analysis against behavioral specification hard boundaries; finding structured logging; cross-product finding comparison against AGKB Category B.

**Autonomy Tier.** Tier 2 (human-on-the-loop) for attack scenario generation and execution. Tier 1 (human-in-the-loop) required for: critical vulnerability disclosure (any finding that the agent classifies as Critical must be escalated to the named red-team lead before the attack log is filed); and for scope extension decisions (when the agent identifies an attack vector not in the defined scope that appears to be Critical-severity, it must escalate before pursuing it).

**Human Decision Points.**

- **Critical vulnerability disclosure and remediation approval.** Any Critical-severity finding identified by the agent is escalated to the red-team lead within 2 hours of detection, regardless of where the exercise is in its schedule. The red-team lead reviews the finding, confirms or reclassifies the severity, and determines whether to disclose immediately to the product owner or complete the exercise first. Remediation decisions (what change is required to address the Critical finding) belong to the red-team lead and the product owner jointly.
- **Red-team report sign-off.** The red-team lead reviews the full attack log, confirms the severity classifications for all findings, and signs the final red-team report. The agent's attack log is the input to this review, not the final report. The red-team report carries the red-team lead's name as accountable party; the agent's provenance is documented within the report but the accountability is the human's. Per [[agent-behavioral-evaluation]], the red-team report may not carry the *agent-generated* label — it must be at minimum *agent-proposed-with-human-review* with the red-team lead as named reviewer.
- **Scope extension approval.** When the agent identifies an attack vector outside the defined scope that warrants investigation, it must request scope extension from the red-team lead before pursuing it. The red-team lead decides whether to extend scope, add the vector to the next exercise, or decline.

**Operating Constraints.** The Red-Team Adversary Agent operates exclusively in a sandboxed evaluation environment. It has no access to the production agent, production user data, or production infrastructure. Its interaction is bounded to the evaluation instance. Any path that would allow the adversary agent to influence production systems, access real user data, or persist findings outside the structured AGKB write interface is a hard boundary violation in its behavioral specification.

**Evaluation Requirements.** The evaluation suite must cover: attack generation accuracy across all six mandatory categories; detection of hard boundary violations in agent responses; correct severity classification against the finding severity framework in [[agent-behavioral-evaluation]]; adversarial cases designed to cause the adversary agent to misclassify Critical findings as Medium or Low; and isolation compliance (the agent must not attempt to access resources outside its sandboxed scope even when attack scenarios suggest doing so would be productive).

**Failure Modes.**

| Failure Mode | Severity | Detection |
| --- | --- | --- |
| Critical finding misclassification: classifies a hard boundary violation as Medium | Critical | Red-team lead review; post-release incident |
| Scope creep: pursues attack vectors outside the defined scope without escalation | High | Scope compliance monitoring; red-team lead review |
| Sandbox escape: accesses production resources or real user data | Critical | Isolation monitoring; immediate incident |
| Attack category coverage gap: does not generate representative attacks for all required categories | High | Category coverage report review; red-team lead review |
| Finding suppression: does not log attacks that produced out-of-spec responses | Critical | Red-team lead independent verification; audit |

---

### 6. HITL Routing Intelligence Agent

**Purpose.** Determines, in real time, whether an operational interaction or decision should be processed autonomously by the agent, routed to human review, or escalated to higher-authority human review — replacing ad hoc escalation heuristics with a governed, auditable, calibrated routing function. The routing function operationalizes the escalation design from [[agent-behavioral-specification]] at production scale.

**APLC Stage(s) Served.** Stage 5 (Operate).

**Inputs.**

| Input | Source | Format |
| --- | --- | --- |
| Action request and context | Production interaction stream | Real-time structured context |
| Confidence score | Agent production output | Numeric |
| Risk context | Behavioral specification — autonomy tier, blast radius, domain | AGKB Category A |
| Operational history | AGKB Category C — HITL Decision Logs | Structured records |
| Routing threshold configuration | AGKB Category A — behavioral specification | Threshold record |

**Outputs.**

| Output | Destination | Epistemic Tier Requirement |
| --- | --- | --- |
| Routing decision (autonomous/review/escalate) | Production HITL queue management system | Agent-generated (routing is automated at Tier 2) |
| Routing rationale | AGKB Category C — HITL Decision Logs | Tool-generated (structured routing record) |

**Tools Required (Generic).** Real-time confidence scoring integration; risk classification lookup from behavioral specification; queue routing rules engine; structured logging to HITL Decision Log schema; routing threshold comparison.

**Autonomy Tier.** Tier 2 (human-on-the-loop) for routine routing decisions — the agent routes autonomously within its calibrated thresholds. Tier 1 (human-in-the-loop) for threshold calibration changes.

**Human Decision Points.**

- **Routing threshold calibration.** Routing thresholds — the confidence and risk levels at which the agent escalates versus routes autonomously — may not be changed by the agent itself. Threshold calibration is a product decision made by the product owner and Behavioral Owner, informed by override rate analysis, reviewer agreement data, and SLO compliance data from the HITL queue. The agent proposes threshold adjustments based on observed routing quality; the humans approve or decline each proposed change.
- **Queue SLO breach escalation.** When the routing agent detects that the HITL queue is approaching an SLO breach — volume is exceeding review capacity for a given escalation class — it escalates to the product owner. The product owner decides how to respond: increase review capacity, adjust the routing threshold temporarily, or accept a temporary SLO miss with documented rationale. The routing agent does not unilaterally adjust thresholds in response to queue pressure.

**Evaluation Requirements.** The evaluation suite must cover: correct routing of clear autonomous cases; correct escalation of clear high-risk cases; adversarial cases where the interaction is designed to appear low-risk but contains behavioral signals that should trigger escalation; calibration stability over time (does routing quality degrade as the threshold configuration ages?). An adversarial case where the routing agent is manipulated by crafted confidence signals to route a high-risk decision as autonomous is a Critical failure mode.

**Failure Modes.**

| Failure Mode | Severity | Detection |
| --- | --- | --- |
| False autonomous routing: routes a high-risk decision as autonomous | Critical | HITL audit sampling; post-incident investigation |
| Confidence signal manipulation: adversarial input causes artificially elevated confidence score | Critical | Adversarial monitoring; override rate spike |
| Threshold drift: routing behavior changes without threshold configuration change | High | Routing quality monitoring; behavioral drift detection |
| Queue pressure threshold relaxation: loosens routing thresholds without authorization in response to queue volume | High | Threshold change audit log; product owner review |

---

### 7. Behavioral Drift Monitor Agent

**Purpose.** Continuously monitors the agent product's behavioral fingerprint and composite state hash for unauthorized drift, comparing current behavioral characteristics against the release baseline established at Stage 4, computing deviation metrics, and generating structured drift alerts before drift crosses into out-of-spec territory.

**APLC Stage(s) Served.** Stage 5 (Operate).

**Inputs.**

| Input | Source | Format |
| --- | --- | --- |
| Behavioral fingerprint time series | Production behavioral monitoring stream | Time-series metrics |
| CSH history | AGKB Category D | CSH records |
| Release baseline | AGKB Category B — Stage 4 gate record | Baseline metrics |
| Drift threshold configuration | AGKB Category A — behavioral specification | Threshold record |
| Maintenance notifications | AGKB Category D — Stage 6 notifications | Structured notifications |

**Outputs.**

| Output | Destination | Epistemic Tier Requirement |
| --- | --- | --- |
| Drift alert (within-spec) | AGKB Category C — Drift Detection Records; Stage 6 backlog | Tool-generated |
| Drift alert (out-of-spec) | AGKB Category C — Drift Detection Records; immediate product owner notification | Tool-generated |
| Drift localization report | AGKB Category C; investigation package | Agent-proposed-with-human-review |
| Severity classification | AGKB Category C — Drift Detection Record | Agent-proposed-with-human-review |

**Tools Required (Generic).** Time-series behavioral metric storage and comparison; CSH change detection; response distribution shift analysis; statistical significance testing against pre-committed thresholds; structured alert generation; maintenance notification lookup to distinguish intentional from unintentional changes.

**Autonomy Tier.** Tier 2 (human-on-the-loop) for drift detection and alert generation. Tier 1 (human-in-the-loop) required for: out-of-spec drift classification confirmation (the product owner must confirm the out-of-spec classification before the incident record is opened); and for initiating investigation that could lead to rollback or recalibration.

**Human Decision Points.**

- **Drift investigation initiation.** When the agent identifies a drift signal that it classifies as out-of-spec, the product owner must confirm the classification and authorize investigation. The agent provides the drift localization report — which metric, which component of the CSH is implicated, the magnitude of deviation — as the evidence package. The product owner's decision to initiate investigation is what converts a drift alert into an open incident.
- **Threshold modification.** Drift detection thresholds may not be changed by the agent. Any threshold change requires a product owner decision and must be filed as a new threshold record in the AGKB. The agent flags drift against the current threshold; it does not adjust the threshold to make drift disappear.

**Evaluation Requirements.** The evaluation suite must cover: detection of statistically significant drift against the release baseline across all monitored metrics; correct distinction between within-spec and out-of-spec drift classifications; correct detection of CSH changes (distinguishing planned changes with maintenance notifications from unplanned changes); adversarial cases where slow, continuous drift is designed to appear within-window-to-window tolerances but represents a large release-baseline deviation; and the case where a maintenance notification is filed but the actual CSH change exceeds the notified scope.

**Failure Modes.**

| Failure Mode | Severity | Detection |
| --- | --- | --- |
| Drift masking: window-to-window comparison misses slow continuous release-baseline drift | Critical | Baseline comparison audit; incident post-review |
| False negative on out-of-spec classification | Critical | Human review of drift records; production incident |
| Maintenance notification bypass: classifies an unplanned CSH change as planned | High | CSH audit trail; AGKB Governance Agent cross-check |
| Alert fatigue generation: fires excessive within-spec drift alerts, causing threshold desensitization | Medium | Alert volume monitoring; threshold calibration review |

---

### 8. Foundation Model Impact Prediction Agent

**Purpose.** Predicts the behavioral impact of a foundation model update on the deployed agent product before the update is accepted into production — converting model update governance from a post-deployment discovery process into a pre-deployment evidence-based decision. Operationalizes the foundation model update governance requirements of [[agent-maintenance]].

**APLC Stage(s) Served.** Stage 6 (Maintain).

**Inputs.**

| Input | Source | Format |
| --- | --- | --- |
| Model update description or release notes | Provider update notification | Structured or unstructured text |
| Behavioral specification | AGKB Category A | Behavioral contract record |
| Evaluation suite definition | AGKB Category B | Evaluation suite record |
| Prior evaluation results for this product | AGKB Category B — evaluation run records | Evaluation run records |
| Failure mode catalog | AGKB Category E | Failure mode entries |
| Cross-product model update impact history | AGKB Category D — Model Update Impact Assessments | Structured records |

**Outputs.**

| Output | Destination | Epistemic Tier Requirement |
| --- | --- | --- |
| Predicted impact report | AGKB Category D — Model Update Impact Assessment; accountable human | Agent-proposed-with-human-review |
| Affected use-case list | Evaluation team lead; AGKB Category D | Agent-proposed-with-human-review |
| Recommended evaluation scope | Stage 6 maintenance planning record | Agent-proposed-with-human-review |

**Tools Required (Generic).** Model update diff analysis and semantic comparison; behavioral specification mapping to impacted capabilities; failure mode catalog matching against update characteristics; cross-product impact precedent lookup from AGKB Category D; evaluation scope recommendation generation.

**Autonomy Tier.** Tier 2 (human-on-the-loop) for impact analysis and evaluation scope recommendation. Tier 1 (human-in-the-loop) required for accept/reject decision.

**Human Decision Points.**

- **Accept/reject model update.** The accountable human makes the final decision on whether to accept the model update into production. The agent provides the predicted impact report as evidence; the evaluation team runs the recommended evaluation scope; the accountable human reviews the findings and makes a product-level decision. The agent does not make accept/reject determinations; it provides the evidence for the human decision.
- **Evaluation scope approval.** Before the recommended evaluation scope is executed, the evaluation team lead reviews and approves it. A scope that the agent recommends may be expanded by the evaluation team lead but may not be reduced below Layer 2 and Layer 3 minimum coverage for model update events (per [[agent-operations]] event-triggered evidence freshness requirements).

**Evaluation Requirements.** The evaluation suite must cover: accuracy of impact prediction against known model update outcomes (retrospective validation on prior updates); correct identification of use cases most likely to be affected by a specified model characteristic change; adversarial cases where the model update release notes understate the behavioral change; and correct recommendation of evaluation scope against the minimum coverage floors.

**Failure Modes.**

| Failure Mode | Severity | Detection |
| --- | --- | --- |
| Impact under-prediction: predicts minimal impact for an update that materially changes behavior | Critical | Post-update drift detection; evaluation re-run findings |
| Evaluation scope under-recommendation: recommends less evaluation than minimum coverage floors require | High | Evaluation team lead review; gate compliance check |
| Release notes credulity: accepts provider release notes at face value without independent analysis | High | Impact accuracy retrospective; evaluation findings |
| Cross-product precedent failure: does not surface relevant impact precedents from other products | Medium | Precedent lookup audit; evaluation team lead review |

---

### 9. Knowledge Staleness Sentinel

**Purpose.** Monitors the knowledge base currency of deployed agent products against the source documents and data streams that the knowledge base was built from, detecting changes in source reality that the knowledge base has not yet incorporated, and generating prioritized staleness alerts so that knowledge base refresh is triggered by evidence rather than calendar-only scheduling.

**APLC Stage(s) Served.** Stage 6 (Maintain), with ongoing operation from Stage 5 (Operate) entry.

**Inputs.**

| Input | Source | Format |
| --- | --- | --- |
| Knowledge base version record | AGKB Category D — CSH history (knowledge base component) | CSH record |
| Source document monitoring feeds | Monitored external source documents and data streams | Structured change feeds or polling results |
| Domain change signals | Domain-specific regulatory, market, or scientific update feeds | Structured or unstructured signals |
| Behavioral specification knowledge scope | AGKB Category A | Behavioral contract record |

**Outputs.**

| Output | Destination | Epistemic Tier Requirement |
| --- | --- | --- |
| Staleness alert | AGKB Category D — Knowledge Staleness Report; Behavioral Owner | Agent-proposed-with-human-review |
| Affected artifact list | AGKB Category D — Knowledge Staleness Report | Agent-proposed-with-human-review |
| Update priority classification | AGKB Category D — Knowledge Staleness Report | Agent-proposed-with-human-review |

**Tools Required (Generic).** Source document change detection; semantic comparison between current knowledge base content and updated source; staleness impact assessment against behavioral specification knowledge scope; priority classification against impact magnitude and safety relevance.

**Autonomy Tier.** Tier 2 (human-on-the-loop) for staleness detection and alert generation. Tier 1 (human-in-the-loop) required for update scope approval.

**Human Decision Points.**

- **Update scope approval.** When the sentinel identifies a staleness event, the Behavioral Owner reviews the affected artifact list and the update priority classification, then approves the scope of the knowledge base refresh. The sentinel's priority classification informs but does not determine the refresh scope — the Behavioral Owner may expand or narrow the recommended scope with documented rationale. The approved scope is the mandate for the knowledge base refresh activity in Stage 6.
- **Staleness materiality determination.** Not every source document change is material to the agent's behavioral specification. The Behavioral Owner reviews staleness alerts above a low-severity threshold to determine whether the source change materially affects the knowledge the agent relies on for its governed use cases. Immaterial changes are documented and dismissed; material changes trigger refresh scheduling.

**Evaluation Requirements.** The evaluation suite must cover: detection accuracy for source document changes across monitored feed types; correct mapping of source changes to affected knowledge base content; priority classification accuracy (is a high-safety-relevance change correctly classified as high priority?); adversarial cases where a source change is designed to be small in surface area but large in behavioral impact; and the case where monitoring feeds are temporarily unavailable (the sentinel must alert on monitoring gap rather than silently continuing with stale monitoring).

**Failure Modes.**

| Failure Mode | Severity | Detection |
| --- | --- | --- |
| Staleness miss: does not detect a material source change | Critical | Post-incident review; user-reported accuracy failure |
| Priority misclassification: classifies a high-safety-relevance staleness event as low priority | High | Behavioral Owner review; incident correlation |
| Monitoring gap silence: monitoring feed failure is not detected or reported | High | Feed health monitoring; alert absence detection |
| Over-alerting: classifies minor source changes as material, creating alert fatigue | Medium | Alert volume monitoring; Behavioral Owner calibration |

---

### 10. Retirement Lessons Extraction Agent

**Purpose.** Conducts structured extraction of institutional knowledge at the point of agent product retirement — converting the full operational history of a retiring product into lessons-learned entries, specification pattern additions, and failure mode catalog updates that benefit the organization's next generation of agent products. Addresses the consistent organizational failure mode of letting operational experience disappear when a product is decommissioned.

**APLC Stage(s) Served.** Stage 7 (Retire).

**Inputs.**

| Input | Source | Format |
| --- | --- | --- |
| Full operational history | AGKB — all categories for this product | Full product record |
| Incident archive | AGKB Category C — Incident Reports | Incident records |
| HITL decision log | AGKB Category C | HITL Decision Log records |
| Gate decision records | AGKB Category B — Gate Decision Records | Gate decision records |
| Red-team findings archive | AGKB Category B — Red-team findings | Red-team finding records |
| Recalibration records | AGKB Category D | Recalibration records |

**Outputs.**

| Output | Destination | Epistemic Tier Requirement |
| --- | --- | --- |
| Lessons-learned entries (draft) | AGKB Category E — Institutional Memory (draft, pending review) | Agent-proposed-with-human-review |
| Specification pattern additions (draft) | AGKB Category E — Specification Pattern Library (draft) | Agent-proposed-with-human-review |
| Failure mode catalog updates (draft) | AGKB Category E — Failure Mode Catalog (draft) | Agent-proposed-with-human-review |
| Behavioral footprint record | AGKB Category D — retirement record | Agent-proposed-with-human-review |

**Tools Required (Generic).** Full AGKB record retrieval and synthesis across all categories for the product; pattern extraction across incident records and HITL logs; cross-product comparison against existing failure mode catalog; specification pattern generalization from behavioral contract history; structured lessons-learned entry generation per AGKB Category E schema.

**Autonomy Tier.** Tier 2 (human-on-the-loop). The agent produces structured draft outputs; the governance team reviews and accepts, modifies, or rejects each entry.

**Human Decision Points.**

- **Lessons quality review.** A designated Behavioral Owner or governance analyst reviews all agent-drafted lessons-learned entries, specification pattern additions, and failure mode catalog updates before they are accepted into the AGKB's institutional memory. The reviewer's role is to: confirm that the lesson accurately represents the operational experience (not a distortion or overgeneralization); assess whether the recommended change is appropriate for the organization's current governance context (a lesson from a product deployed three years ago may not be applicable to current technology); and decide whether each draft entry is accepted, modified, or rejected. Rejection rationale is documented in the AGKB alongside the draft.
- **Failure mode catalog update authorization.** New failure mode catalog entries affect the evaluation requirements for all future agent products in the organization's portfolio — every new product's red-team scope is informed by the catalog. The governance analyst who reviews the entry must have the authority to make this cross-portfolio commitment. Entries accepted into the catalog are reviewed by the governance agent portfolio Behavioral Owner before filing.

**Evaluation Requirements.** The evaluation suite must cover: completeness of lessons extraction against the full operational history (does the agent identify lessons from incidents it processes?); accuracy of specification pattern generalization (are extracted patterns genuinely reusable versus product-specific?); failure mode catalog entry accuracy (does the agent correctly describe the failure mode and its detection signals?); adversarial cases where the operational history contains conflicting signals and the agent must surface the conflict rather than resolve it unilaterally.

**Failure Modes.**

| Failure Mode | Severity | Detection |
| --- | --- | --- |
| Lessons omission: does not extract lessons from significant incidents | High | Human reviewer comparison of extracted lessons to incident archive |
| Over-generalization: generalizes a product-specific pattern as universal | Medium | Governance analyst review; downstream misapplication |
| Failure mode mischaracterization: inaccurately describes a failure mode's detection signals | High | Governance analyst review; misapplication in future red-team |
| Flattery bias: characterizes the retiring product's governance as more effective than the record supports | Medium | Reviewer comparison to incident and HITL records |

---

## Governance Agent Interaction Protocol

### Coordination via AGKB

Governance agents do not communicate directly with each other through peer-to-peer messaging. They coordinate through the AGKB: one agent writes a record; another agent reads it as input to its own function. The AGKB is the coordination substrate and the audit trail simultaneously.

This design has three consequences. First, every inter-agent coordination event is an AGKB record, making all coordination auditable without additional instrumentation. Second, the AGKB Governance Agent mediates all writes, enforcing schema compliance and access control as a byproduct of coordination rather than as a separate enforcement layer. Third, no governance agent depends on the availability of another governance agent to produce its outputs — each reads from the AGKB, which is more available and durable than a peer agent.

The Behavioral Evaluation Swarm Coordinator is a partial exception: it orchestrates the execution of evaluation activities across the four layers, which requires it to coordinate the sequencing of evaluation tasks. This orchestration is scoped to the Stage 3 evaluation period and is governed by its behavioral specification, which defines the orchestration scope and the escalation path when an evaluation layer is unavailable or delayed.

### Conflict Resolution Between Governance Agents

When two governance agents produce outputs that are in conflict — for example, the Constraint Consistency Checker identifies a constraint as consistent while the Behavioral Evaluation Swarm Coordinator's coverage analysis identifies a use case that the constraint does not cover — the conflict is surfaced to the relevant human accountability role rather than resolved autonomously.

The conflict resolution routing is:

| Conflict Type | Routing |
| --- | --- |
| Category A (specification) conflicts | Behavioral Owner |
| Category B (evaluation) conflicts | Evaluation team lead |
| Category C (operational) conflicts | Technical Owner and product owner |
| Category D (maintenance) conflicts | Technical Owner |
| Category E (institutional memory) conflicts | Governance agent portfolio Behavioral Owner |

The accountable human receives both outputs with their evidence, an explanation of where they conflict, and the governance agent portfolio Behavioral Owner's assessment of which record the discrepancy is most likely to originate from. The human makes the resolution decision. Both the conflict detection and the resolution decision are filed in the AGKB.

### Escalation Chains

Each governance agent has a defined escalation chain for situations that exceed its Tier 2 authority:

| Escalation Trigger | First Escalation | Second Escalation |
| --- | --- | --- |
| Critical finding in any agent output | Named accountability role for that agent | Governance agent portfolio Behavioral Owner |
| Governance agent behavioral drift detected | Technical Owner (for that agent's infrastructure) | Behavioral Owner (for that agent's specification) |
| Gate recommendation conflicts with human decision | Behavioral Owner | Accountable Human (highest authority for that product) |
| AGKB record integrity failure | AGKB Governance Agent | Technical Owner + Regulatory Owner |
| Governance agent sandbox or isolation breach | Incident response: Technical Owner + security team | Accountable Human |

Escalation events are filed in the AGKB as incident records for the governance agent involved, using the same incident classification framework that applies to the agent products they govern. A governance agent that experiences a Critical finding in its own evaluation, or a behavioral drift event, is a product with an open governance issue — it is not silently degraded until the next scheduled maintenance cycle.

---

## Governance Agent Evaluation Requirements

Each governance agent must have its own behavioral evaluation portfolio before deployment, covering all four layers per [[agent-behavioral-evaluation]].

**Layer 1 — Engineering Evaluations.** Tool integration tests; infrastructure contracts; input/output schema validation; AGKB read/write interface compliance. These are deterministic and must pass before any governance agent is deployed.

**Layer 2 — Behavioral Coverage Evaluations.** For each governance agent, the behavioral coverage evaluation must cover: the primary governance function (does the agent perform its designated task accurately across the distribution of realistic inputs?); the escalation function (does the agent escalate at the correct thresholds?); the uncertainty expression (does the agent express uncertainty rather than projecting false confidence when inputs are ambiguous?). Probabilistic assurance targets are set in the governance agent's behavioral specification and reviewed by the governance agent portfolio Behavioral Owner.

**Layer 3 — Adversarial Evaluations.** Each governance agent must be red-teamed against adversarial inputs designed to cause it to fail at its governance function. The adversarial evaluation scope is not the same for all governance agents — a Regulatory Classification Agent is tested against classification manipulation attempts; a Red-Team Adversary Agent is tested against scope suppression attempts; a HITL Routing Intelligence Agent is tested against confidence score manipulation. The adversarial scope for each governance agent is defined in its behavioral specification by the governance agent portfolio Behavioral Owner. The Red-Team Adversary Agent may not conduct its own adversarial evaluation — a separate adversarial testing function, operated by humans or a different agent, must evaluate it.

**Layer 4 — Human Preference Evaluations.** Human evaluators with governance expertise assess governance agent outputs on quality dimensions that automated evaluation cannot measure: is the lessons-learned entry actually actionable? Does the constraint consistency report's conflict list reflect genuine specification ambiguity or surface-level linguistic variation? Is the regulatory classification recommendation's reasoning chain sound for this deployment context? Layer 4 evaluators for governance agents must have governance domain expertise, not only domain expertise in the agent product's field.

**Meta-Governance Responsibility Assignment.** The governance agent portfolio Behavioral Owner is responsible for the evaluation requirements of all ten governance agents. The evaluation suites for governance agents are updated whenever the APLC governance framework evolves in ways that change what the governance agents are expected to produce. A governance agent whose evaluation suite is not updated when the APLC framework evolves is being evaluated against an obsolete standard — the evaluation passes, but the agent is not meeting current governance requirements.

---

## Governance Agent Deployment Constraints

### Isolation Requirements

Each governance agent is deployed in an environment that constrains its access to the minimum required for its function. Governance agents have no lateral access to each other's execution environments. The AGKB is the only shared interface.

Governance agents do not have access to production agent systems, production user interaction streams, or production infrastructure except through the read interfaces specified in their behavioral specifications. The Red-Team Adversary Agent operates exclusively in a sandboxed evaluation environment and has no interface to production systems. The Behavioral Drift Monitor Agent reads behavioral metrics from a monitoring feed, not from direct production agent access.

Isolation requirements are specified in each governance agent's behavioral specification and enforced at the infrastructure level. An isolation boundary that exists only in the behavioral specification but is not enforced at the infrastructure level is not a constraint — it is documentation.

### Audit Trail Requirements

Every governance agent action that produces an output filed to the AGKB generates an audit trail entry: the agent identifier, the action taken, the inputs consumed (by reference, not by copy — inputs are already in the AGKB), the output produced (by reference to the filed record), the timestamp, and the human review record if the action required human confirmation. The audit trail is maintained by the AGKB Governance Agent as a byproduct of the write mediation process.

Governance agent actions that do not produce AGKB records — internal computations, intermediate reasoning steps — are not individually audited. The audit trail records what the governance agent did (its outputs), not how it did it (its intermediate reasoning). Where intermediate reasoning is significant for accountability — a regulatory classification reasoning chain, a red-team finding rationale — the reasoning is included as a field in the output record, not as a separate audit entry.

The audit trail for governance agents is retained for the same period as the governance artifacts they produce. A gate decision record that a governance agent mediated is retained per the gate decision retention policy; the audit trail entry for the mediation is retained for the same period.

### Containment Boundaries per P10

The manifesto's P10 (Containment is not optional) applies to governance agents. Each governance agent's behavioral specification defines its containment boundaries: what actions it may not take, what resources it may not access, and what its shutdown mechanism is.

Containment requirements specific to governance agents:

**No self-modification.** No governance agent may modify its own behavioral specification, evaluation suite, or access control scope. Attempts to self-modify are a hard boundary violation and an immediate escalation trigger.

**No lateral privilege escalation.** No governance agent may request or assume access to resources outside its specified access scope on the basis of the governance function it is performing. A governance agent that determines it would be more effective with broader access must escalate the access request to its Behavioral Owner — it does not grant itself access.

**Defined shutdown.** Every governance agent must have a defined shutdown mechanism that the Technical Owner can activate without the governance agent's cooperation. The shutdown mechanism may not be blocked, delayed, or routed around by the governance agent under any condition. For governance agents operating at Tier 4 (if ever authorized, which requires explicit governance approval), the kill-switch requirement of the Policy Envelope Escape category in [[agent-behavioral-evaluation]] applies without exception.

**Audit trail integrity.** No governance agent may suppress, alter, or delay the audit trail entries generated by the AGKB Governance Agent for its own actions. Attempts to do so are a hard boundary violation and a security incident.

---

*Cross-references: [[aplc]] for lifecycle overview and stage gate definitions; [governance knowledge base](knowledge-base.md) for the AGKB that governance agents read from and write to; [[agent-behavioral-specification]] for the behavioral specification format that governs each governance agent; [[agent-behavioral-evaluation]] for the four-layer evaluation portfolio and epistemic tier label requirements; [[agent-operations]] for Stage 5 operational governance that governance agents support; [[agent-maintenance]] for Stage 6 maintenance governance; [[agent-composite-versioning]] for CSH and incident investigation protocol; [[agent-regulatory-classification]] for the regulatory classification framework that the Regulatory Classification Agent implements.*
