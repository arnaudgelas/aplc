# Agentic Product Lifecycle (APLC)

> *Governing agent products from the first idea to the last interaction — and the regulated retirement in between.*

---

Deploying an AI agent is not the same as deploying software. If you have ever experienced a chatbot that drifted in tone over time without anyone touching the code, an AI assistant that broke character when pushed, or a model provider update that silently changed a product's behavior overnight — you already know this. The question is whether your governance framework knows it too.

The **Agentic Product Lifecycle (APLC)** is a comprehensive governance framework designed specifically for agent products: systems where the AI agent *is* the product, not just a tool used to build it. It covers everything from the first conversation about what the agent should do, through behavioral specification, evaluation, and release, all the way to the moment the agent is retired — and what must happen at each point for the product to be trustworthy, auditable, and compliant.

It is rigorous where it needs to be. It is practical by design. And it is the missing governance layer that most organizations building AI agents don't know they're missing until something goes wrong.

---

## Why the APLC Exists

Software delivery has the ASDLC. AI model development has model governance frameworks. But agent products — systems that behave, that interact with users, that make decisions on their behalf — fall between those two worlds. They are neither pure software nor pure models. They are *composite systems* whose behavior is determined by five components simultaneously:

- the application code
- the system prompt
- the foundation model
- the knowledge base
- the memory state

Change any one of these — including changes made by the model provider without your team's intervention — and the behavioral identity of the product changes. The APLC governs that composite system throughout its operational life.

The paradigm shift is real, and it has governance implications at every level:

| Dimension | Software delivery | Agent product delivery |
| --- | --- | --- |
| What you specify | Functional acceptance criteria | Behavioral envelope and persona |
| What you test | Deterministic pass/fail | Probabilistic behavioral coverage + red-teaming |
| What drifts | Nothing (code doesn't change itself) | Everything (model updates, memory, knowledge staleness) |
| What incidents look like | Crashes, outages, bugs | Hallucinations, persona breaks, adversarial manipulation |
| What "version" means | A single artifact hash | A composite state hash across five components |
| Regulatory exposure | Process-level (how you built it) | Product-level (what it is and what it does) |

The APLC exists to make this paradigm shift governable.

---

## Five Values

The APLC is built on five product-level values. They are not aspirations — they are the reasoning behind every stage gate condition and every evaluation requirement in the framework.

| We value more | over | We also value |
| --- | --- | --- |
| Behavioral integrity | over | Deployment velocity |
| Measured behavioral coverage | over | "The demo worked" |
| Governed behavioral drift | over | Passive monitoring |
| Explicit trust architecture | over | Implicit defaults |
| Regulated retirement | over | Silent abandonment |

An agent product whose behavioral characteristics are not understood before deployment is not a product — it is an experiment conducted on users. The APLC ensures you understand what you are deploying before you deploy it, and that you continue to understand it for as long as it is running.

---

## The Seven-Stage Model

The APLC structures the agent product lifecycle into seven stages, each bounded by a governance gate:

```
Stage 1: Conceive          →  [Conception Gate]
Stage 2: Specify           →  [Behavioral Specification Gate]
Stage 3: Build & Evaluate  →  [Behavioral Release Gate]
Stage 4: Release           →  [Operational Readiness Gate]
Stage 5: Operate           ↕  (concurrent with Stage 6)
Stage 6: Maintain          ↕  (concurrent with Stage 5)
Stage 7: Retire
```

**Stage 1 — Conceive.** Define the agent product: what it is, who it serves, what authority it has, and what success looks like. Establish the trust architecture (who can instruct the agent and at what level), the persona design, and the EU AI Act regulatory classification. Nothing in Stage 2 can be correctly specified without a complete Stage 1 — every behavioral requirement traces back here.

**Stage 2 — Specify Behaviorally.** Translate the product brief into the behavioral specification: the authoritative contract from which engineers implement and evaluators test. Define the four-layer behavioral envelope (hard boundaries that infrastructure enforces, soft limits that configuration sets, performance targets, and adaptation scope), the use-case coverage map, the uncertainty protocol, and the escalation design.

**Stage 3 — Build and Evaluate.** Run the manifesto's full engineering inner loop and simultaneously execute the four-layer behavioral evaluation portfolio: Layer 1 engineering evaluations, Layer 2 probabilistic behavioral coverage, Layer 3 adversarial red-teaming across six attack categories, and Layer 4 human preference evaluation. All four layers must be complete before release.

**Stage 4 — Release.** Govern the transition from built-and-evaluated agent to deployed product. Establish the behavioral baseline, file the composite state manifest, complete EU AI Act conformity documentation for applicable systems, confirm monitoring infrastructure is live, and run a canary deployment for significant user bases before full rollout.

**Stage 5 — Operate.** Govern behavioral quality in production: output quality rate, behavioral envelope compliance, drift detection against the release baseline, HITL queue management, and incident classification across five incident classes (quality, behavioral, safety, persona, adversarial).

**Stage 6 — Maintain.** Govern planned behavioral maintenance: recalibration cycles, foundation model update governance (detect, test, accept or reject), knowledge base refresh, and memory governance. Runs concurrently with Stage 5 from deployment onward.

**Stage 7 — Retire.** Execute governed decommission: user migration, decision record preservation, composite state manifest archive, and regulated retirement confirmation. For EU high-risk AI systems, technical documentation must be retained for ten years. Silent abandonment — switching off the agent without migration or retention — is a governance failure, not an operational convenience.

The lifecycle is not linear. Persistent drift sends the product back to Stage 2. Quality incidents send it back to Stage 3. Business purpose misses trigger a return to Stage 1. Gate failures at Stage 4 return to Stage 3 for remediation. The loops are closed in both directions.

---

## Six Concepts That Change Everything

These concepts have no direct analog in software delivery governance. Understanding them is understanding what makes agent product governance different.

### 1. Composite Agent State and the CSH

An agent product's behavioral identity is determined by five components simultaneously: application code, system prompt, foundation model, knowledge base, and memory state. The **Composite State Hash (CSH)** is a hash over all five component identifiers. When *any* component changes — including a model update you did not initiate — the CSH changes, and a new composite state manifest must be filed. Every production interaction is associated with the CSH active at the time, so any behavioral deviation can be traced to exactly which component changed and when.

### 2. Behavioral Drift

Behavioral drift is a change in the agent's behavioral profile not caused by an intentional update. Sources: model provider updates, memory accumulation, knowledge staleness, input distribution shift. Drift is measured against the behavioral baseline established at release — not against last week's measurement, which masks slow continuous decline. Drift within the behavioral specification requires Stage 6 attention. Drift outside the specification is an incident requiring immediate response.

### 3. Foundation Model Update Governance

The foundation model is the one component of the composite state the engineering team does not directly control. Model providers update their models without necessarily notifying you that your product's behavior has changed. Foundation model update governance is the process for detecting those updates (via CSH monitoring), testing them against the behavioral evaluation portfolio, and making an explicit accept or reject decision before accepting the update into production. The default must be reject unless the regression suite passes — not accept unless something obviously breaks.

### 4. Red-Team Protocol

Red-teaming for an agent product is not exploratory testing. It is a structured adversarial exercise required before every behavioral release gate, covering six mandatory attack categories: prompt injection, principal impersonation, persona break, behavioral envelope violation, information extraction, and social engineering. Every composite state change can change the adversarial robustness profile. Critical findings block release without exception. This is not periodic or optional — it is before every release.

### 5. Human Evaluation Workflow

Automated evaluations measure what they can quantify. Human evaluators assess what requires judgment: output preference quality, tone and persona consistency, complex judgment cases, safety review of flagged interactions. For these four quality dimensions, human evaluation is not a supplement to automated evaluation — it is the only valid measurement method. For agents in regulated domains, domain expert evaluators are not optional. Evaluator qualification is a gate condition.

### 6. Agent Incident Classification

Agent products experience five classes of incident: **quality** (available but outputs below quality SLO), **behavioral** (operating outside the behavioral specification), **safety** (harm caused or credibly imminent), **persona** (character broken, AI identity denied), **adversarial** (confirmed malicious manipulation — jailbreak, injection, impersonation). Each class has a distinct detection methodology, escalation path, and response protocol. Treating all five as "bugs" produces the wrong response to four of them.

---

## The Governance Agent Framework

APLC governance is partially automated through ten specialized governance agents that execute governance functions across the lifecycle. Each is itself governed under APLC — it has a behavioral specification, an evaluation suite, and human decision points. Governance agents prepare gate packages and produce recommendations; decision authority for critical and high-risk systems always remains with the appropriate human accountability role holder.

The ten agents cover: regulatory classification, use-case elicitation, constraint consistency checking, evaluation swarm coordination, adversarial red-teaming, HITL routing intelligence, behavioral drift monitoring, foundation model impact prediction, knowledge staleness detection, and retirement lessons extraction.

All governance agent actions and all lifecycle artifacts are stored in the **APLC Governance Knowledge Base (AGKB)** — the authoritative source of record for every governance decision, behavioral specification, evaluation result, and operational governance artifact from conception through retirement.

---

## Getting Started

**New to the APLC?** Start with [`aplc.md`](aplc.md) for the full lifecycle architecture, then [`aplc-guide.md`](aplc-guide.md) for implementation guidance including minimum viable governance at each stage and the five APLC maturity levels.

**Already have an agent in production without APLC governance?** Start at Stage 5. Establish a behavioral baseline retrospectively, derive a behavioral specification from observed behavior, conduct a retrospective red-team, and file a composite state manifest for the current deployment. Then work forward from there.

**Deploying in a regulated industry?** Start with [`agent-regulatory-classification.md`](agent/agent-regulatory-classification.md). Determine the EU AI Act risk class before anything else — regulatory requirements are design constraints from conception onward, not a documentation exercise at release.

The APLC is not all-or-nothing. The guide defines minimum viable governance at each stage, and each stage's minimum bar can be reached without waiting for perfection at the previous one.

---

## What's in This Directory

### Core Documents

| Document | What it covers |
| --- | --- |
| [`aplc.md`](aplc.md) | Lifecycle overview: the seven stages, four gates, six concepts, APLC values, and relationship to the manifesto and ASDLC |
| [`aplc-guide.md`](aplc-guide.md) | Practitioner implementation guide: minimum viable governance, common failure modes, five maturity levels, EU AI Act / ISO 42001 / SR 11-7 / GDPR integration |

### Stage Documents

| Document | Stage | What it covers |
| --- | --- | --- |
| [`agent-conception.md`](agent/agent-conception.md) | Stage 1 | Agent product brief, trust architecture, persona design, accountability roles |
| [`agent-regulatory-classification.md`](agent/agent-regulatory-classification.md) | Stage 1 | EU AI Act classification walkthrough, conformity assessment path selection |
| [`agent-behavioral-specification.md`](agent/agent-behavioral-specification.md) | Stage 2 | Four-layer behavioral envelope, use-case coverage map, uncertainty protocol, machine-executable specification model |
| [`agent-behavioral-evaluation.md`](agent/agent-behavioral-evaluation.md) | Stage 3 | Four-layer evaluation portfolio, red-team protocol, human evaluation workflow, adaptive coverage, continuous red-team |
| [`aplc-stage3-inner-loop.md`](aplc-stage3-inner-loop.md) | Stage 3 | Stage 3 inner loop behavioral interpretation, Agentic Definition of Done |
| [`agent-release-governance.md`](agent/agent-release-governance.md) | Stage 4 | Seven behavioral release gate conditions, composite state manifest, canary deployment, rollback governance |
| [`agent-operations.md`](agent/agent-operations.md) | Stage 5 | Behavioral observability, drift detection, HITL management, incident classification, HITL four-channel learning |
| [`agent-maintenance.md`](agent/agent-maintenance.md) | Stage 6 | Recalibration cycles, foundation model update governance, knowledge base governance, GDPR memory erasure |
| [`agent-retirement.md`](agent/agent-retirement.md) | Stage 7 | Retirement triggers, user migration, lessons extraction, retirement vs. recalibrate decision framework |

### Cross-Lifecycle Documents

| Document | What it covers |
| --- | --- |
| [`agent-composite-versioning.md`](agent/agent-composite-versioning.md) | Composite State Hash, manifest format, behavioral fingerprint, memory state snapshot policy |
| [`agent-portfolio-governance.md`](agent/agent-portfolio-governance.md) | Portfolio-level governance: registry, foundation model epidemic surveillance, multi-agent interaction governance |
| [`agent-finops-governance.md`](agent/agent-finops-governance.md) | APLC FinOps governance: cost attribution, FinOps metrics, stage-by-stage economics |
| [`waiver-governance.md`](waiver-governance.md) | Governance waiver process for gate condition exceptions |

### Governance Agent Framework

| Document | What it covers |
| --- | --- |
| [`governance/knowledge-base.md`](governance/knowledge-base.md) | APLC Governance Knowledge Base architecture, schemas, access control, retrieval interface |
| [`governance/agents.md`](governance/agents.md) | Ten APLC Governance Agents with full specifications, autonomy tiers, and evaluation requirements |
| [`governance/tool-stack.md`](governance/tool-stack.md) | Twelve governance tools with per-agent access control matrix |
| [`governance/observability.md`](governance/observability.md) | Governance process observability: health metrics, anomaly detection, SLAs, audit trail |
| [`governance/queries.md`](governance/queries.md) | Canonical governance query library: 25 structured queries (GQ-01 through GQ-25) across all lifecycle stages |

---

## Who This Is For

The APLC is written for everyone involved in building and governing agent products:

- **Product owners and business sponsors** who need to understand what they are accountable for and what governance evidence they need to provide
- **Engineering leads** who need to understand how the manifesto's inner loop integrates with lifecycle governance — and what the behavioral release gate actually requires
- **Risk officers and compliance leads** who need a lifecycle framework that maps to EU AI Act, ISO 42001, SR 11-7, and GDPR obligations
- **Enterprise architects** who need to understand how APLC and ASDLC work together without replacing each other
- **Governance officers** who need to understand what minimum viable governance looks like at each stage and how to get from Level 1 (unstructured) to Level 5 (regulated)

The APLC does not assume a large team or a mature organization. It defines minimum viable governance at each stage precisely so that teams of any size can start somewhere, build the governance muscle incrementally, and reach the level their risk profile and regulatory obligations require.

---

## The Relationship to the Manifesto and ASDLC

The **manifesto** is the engineering execution engine for Stage 3. Every manifesto principle applies inside Stage 3, unchanged. The manifesto's P8 (Evaluations are the contract) is the foundation of the APLC's Layer 1 behavioral evaluation. P9 (Observability is accountability) is the foundation of Stage 5. P12 (A named human is accountable) runs through every stage gate from Conception to Retirement.

The **ASDLC** governs software delivery. The APLC governs agent product delivery. They run in parallel, not in competition. The ASDLC governs the infrastructure and platform that hosts the agent; the APLC governs the agent product itself. The APLC's Stage 4 extends the ASDLC's release gate rather than replacing it. Stage 5 extends ASDLC operations governance. Stage 6 extends ASDLC maintenance governance. Both reference the manifesto as the engineering execution standard.

"Extends" has a precise meaning here: ASDLC conditions are required, and the APLC adds additional conditions on top. An agent product that satisfies only APLC conditions without satisfying ASDLC conditions is not fully governed.

---

*The APLC is part of the Agentic Engineering Manifesto ecosystem. See also: manifesto (engineering principles), ASDLC (software delivery lifecycle), [`aplc.md`](aplc.md) (full lifecycle architecture).*
