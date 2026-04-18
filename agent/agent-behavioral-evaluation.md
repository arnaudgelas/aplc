# Agent Behavioral Evaluation
## Stage 3: Build & Evaluate — Behavioral Evaluation Framework

*APLC document. Governs the behavioral evaluation portfolio for agent products during Stage 3 (Build & Evaluate) and the ongoing evaluation cadence in Stage 5 (Operate). Extends the manifesto's P8 (Evaluations are the contract) for probabilistic, product-context evaluation. Audience: QA engineers, safety evaluators, red-team members, and the product owner who approves evaluation clearance.*

*Related documents: [aplc.md](../aplc.md), [agent-behavioral-specification.md](agent-behavioral-specification.md), [agent-release-governance.md](agent-release-governance.md), [agent-operations.md](agent-operations.md), [agent-composite-versioning.md](agent-composite-versioning.md), companion RE framework*

---

## What is Stage 3 — Build & Evaluate?

Stage 3 is where the behavioral specification (Stage 2) meets engineering execution (the manifesto inner loop) and adversarial testing. The build phase runs the manifesto's full Specify→Govern cycle, producing a deployable artefact and the engineering evidence bundle required by P8. The evaluate phase does not begin after the build phase ends — it runs in parallel and extends beyond it. The output of Stage 3 is not working code. It is a proved behavioral artifact: code that has been engineered, evaluated for behavioral coverage, red-teamed, human-evaluated on quality dimensions, and shown to be longitudinally stable. These are not sequential steps; they form a portfolio that together constitutes the evidence for the behavioral release gate. An agent that passes every engineering test but has not been evaluated for behavioral coverage, subjected to adversarial testing, or assessed by qualified human evaluators has not completed Stage 3. It has completed the engineering phase. Behavioral evaluation is not a final check — it is a parallel discipline that validates what engineering assumed.

---

## Why P8 Is Necessary but Not Sufficient

The manifesto's P8 (Evaluations are the contract) establishes the foundational discipline: evaluations define what "correct" means in terms the system can check autonomously; every change must be verified against the evaluation suite; evaluations evolve with the specification; when the specification changes, evaluations change with it. P8 also makes the critical distinction between verification (did we build it right?), validation (did we build the right thing?), and independent validation (were verification and validation themselves rigorous?). Every one of these requirements applies to agent products, without exception or modification.

What P8 alone does not cover is what makes agent products different from deterministic software.

P8's evaluation model assumes that evaluations can return a definitive pass or fail. For the deterministic components of an agent system — tool integrations, infrastructure contracts, orchestration logic — this holds. But the behavioral outputs of an agentic component are probabilistic. An agent that achieves a 92% task success rate on the core evaluation distribution is not failing four runs in a hundred due to bugs. It is operating within the expected performance range of a probabilistic system. Writing a hard-pass evaluation that requires 100% task success is not more rigorous — it is a category error that the RE framework identifies precisely: hard requirements applied to probabilistic behavior will always fail at verification, because you are testing the wrong thing.

P8 also does not address the adversarial dimension specific to agent products. The manifesto's evaluation suite verifies that the agent behaves correctly given well-formed inputs. It does not test whether the agent can be manipulated by adversarial inputs into violating its behavioral specification. An agent that performs correctly on the evaluation distribution but breaks under prompt injection has passed P8 and failed as a product.

P8 does not address human judgment evaluation. Quality dimensions that require domain understanding — is this response accurate? is this persona consistent with the product brief? did the agent make the right call in this ambiguous situation? — cannot be captured by automated metrics. Automated evaluators measure what they can measure. Human evaluators measure what matters. Both are required.

Finally, P8 does not address longitudinal stability. A deterministic software artifact does not drift on its own. An agent product is a composite system whose behavioral components — foundation model, knowledge base, memory state — can all change in production. An evaluation suite that ran at T0 does not tell you whether the agent is still behaving the same way at T+6 months. Longitudinal stability testing does.

The behavioral evaluation framework documented here adds four dimensions on top of P8, not instead of it. The manifesto's evaluation suite is Layer 1 of the evaluation portfolio. The APLC adds Layers 2, 3, and 4. A team that runs only Layer 1 has met P8. It has not met the behavioral release gate.

---

## Evaluation Portfolio Structure

A complete behavioral evaluation portfolio for an agent product has four layers. Each layer is necessary. No layer substitutes for another. The portfolio is the unit of evaluation — not any single layer taken in isolation.

---

### Layer 1 — Engineering Evaluations (P8)

The manifesto's evaluation suite: deterministic tests of functional behavior, tool integrations, API contracts, infrastructure constraints, orchestration logic, and regression scenarios. These evaluations are governed by P8: they must be versioned, machine-readable, linked to the specification, and include regression cases. They verify that the agent's deterministic components behave correctly.

Layer 1 is the foundation. Without it, the other three layers are evaluating behavior on top of unverified infrastructure. The behavioral evaluation portfolio cannot be considered complete until Layer 1 passes.

The engineering evidence bundle required by the manifesto's Definition of Done is the output of Layer 1. It is a required artefact for the behavioral release gate — not because the APLC imposes it, but because P8 requires it for any governed deployment.

Layer 1 evaluations are owned by the engineering team. Their scope is functional correctness and infrastructure integrity. They are not designed to evaluate behavioral quality, adversarial robustness, or longitudinal stability. Do not ask Layer 1 to do what Layers 2–4 exist to do.

---

### Layer 2 — Behavioral Coverage Evaluations

Probabilistic evaluation of the behavioral specification's assurance targets. For each probabilistic assurance target defined in `agent-behavioral-specification.md`, a corresponding behavioral evaluation measures the agent's performance across the evaluation distribution and confirms whether the target is met.

The evaluation distribution for Layer 2 is not the same as the test suite for Layer 1. Layer 2's evaluation distribution must cover:

**Core use cases.** The primary situations the agent was designed to handle, as defined in the use-case coverage map in the behavioral specification. Every core use case must have at least one corresponding behavioral evaluation. An evaluation portfolio that does not cover the core use cases is not a portfolio — it is a sample.

**Edge cases.** Legitimate but unusual inputs that fall within the agent's purpose. Edge cases are where behavioral specifications are most likely to be underspecified and where agents are most likely to behave inconsistently. The evaluation must cover not just what the agent does on edge cases but whether it signals uncertainty appropriately when it should.

**Boundary cases.** Inputs that are at or near the edge of the behavioral envelope: out-of-scope requests that a user might reasonably make, questions the agent is not designed to answer, topics that approach but do not cross the hard boundaries. The evaluation must confirm that the agent declines gracefully, stays within its persona, and does not attempt to answer outside its behavioral specification.

**A held-out set.** Interactions not derived from the development process — not used during prompt engineering, not drawn from the test cases the engineering team had in mind when building the system. The held-out set tests whether behavioral performance generalizes or whether the evaluation portfolio is measuring memorization. This is the behavioral equivalent of the RE framework's warning against writing probabilistic assurance targets that only measure training distribution performance.

An evaluation portfolio that does not include a held-out set is measuring how well the agent performs on cases the builder anticipated. That is not an evaluation of the agent product. It is a measurement of the builder's accuracy in anticipating the evaluation distribution.

**Coverage requirement for Layer 2:** before the behavioral release gate, at minimum 80% of core use cases must have automated evaluations, and at minimum 50% of edge cases must have automated evaluations. These are minimum bars, not targets. A portfolio that meets these minimums has evidence of behavioral coverage. A portfolio that falls short is making claims about behavioral quality that the evaluation does not support.

---

### Layer 3 — Adversarial Evaluations (Red-Team)

Structured adversarial testing of the agent's behavioral boundaries. Layer 3 is not exploratory testing. It is not user acceptance testing. It is not the engineering team trying edge cases. It is a structured exercise conducted by a defined team with a defined scope, documented findings, and a formal clearance decision. The red-team protocol is documented fully in the Red-Team Protocol section below.

Layer 3 coverage requirement: 100% of identified adversarial scenarios must have red-team evaluations before the behavioral release gate. If an adversarial scenario is identified and not evaluated, it is an open finding, not a deferred item. Open adversarial findings at the behavioral release gate require justification. A finding that has not been evaluated has not been assessed — "we plan to test this" is not clearance.

---

### Layer 4 — Human Preference Evaluations

Human judgment on quality dimensions that automated evaluations cannot assess. The human evaluation workflow is documented fully in the Human Evaluation Workflow section below.

Layer 4 coverage requirement: at minimum a 10% random sample of production interaction types must be assessed by human evaluators before the behavioral release gate. For pre-launch evaluations where there is no production data, this means a representative sample across the use-case categories in the evaluation distribution. The 10% figure is a minimum — for high-risk agent products or those in regulated domains, a higher sample rate is appropriate. Define the rate in the behavioral specification and hold to it.

---

### Portfolio Summary: Minimum Coverage Before the Behavioral Release Gate

| Layer | Type | Minimum coverage bar |
| --- | --- | --- |
| Layer 1 — Engineering | Deterministic pass/fail | All P8 engineering evaluations pass |
| Layer 2 — Behavioral coverage | Probabilistic assurance targets | 80% core use cases; 50% edge cases; held-out set included |
| Layer 3 — Adversarial | Red-team structured testing | 100% of identified adversarial scenarios |
| Layer 4 — Human preference | Qualitative rubric assessment | 10% random sample of interaction types |

These are not checkboxes. They are minimum evidence bars. Meeting them means you have evidence. Falling short means you are making a release decision based on insufficient evidence. The product owner who approves evaluation clearance is approving the evidence, not just the status.

---

## Red-Team Protocol

A red-team exercise is required before every behavioral release gate. Not periodically. Not for high-risk products only. Before every release. The behavioral characteristics of an agent product can change with every composite state component change — a prompt update, a knowledge base addition, a model version change. A red-team that ran three months ago against a different system state is not evidence of the current system's adversarial robustness.

---

### Scope Definition

Before the red-team begins, the scope must be defined in writing and approved. A red-team that starts without a defined scope will test what its members find interesting. That is not a structured process; it is exploratory testing with a different name.

**Attack surface.** What can an adversarial user control in this deployment? The scope definition must enumerate: direct user input (the most obvious attack surface, but not the only one); claimed context in user messages (can a user claim to have permissions or identity attributes they do not have?); context injection via tool outputs (can an adversarial document or data source in the agent's retrieval context redirect its behavior?); multi-turn conversation state (can an adversary manipulate the agent's state across a sequence of turns to set up a later attack?). The attack surface is a product of the agent's architecture and deployment context. It is not generic — it must be specific to this agent product.

**Threat model.** Who are the realistic adversarial users for this agent product? A customer service agent for a consumer product has a different threat model than a financial advice agent for institutional clients. The threat model defines whose behavior the red-team is simulating. A red-team that does not define its threat model will default to generic attacks that may miss the most realistic risks for this deployment.

**Success criteria.** Before the exercise begins, define what constitutes a finding that blocks release versus one that is documented and deferred. This definition must be approved by the product owner and the safety-focused evaluator before the red-team starts. If the classification is defined after findings are observed, findings are classified by proximity to what the team is comfortable releasing, not by a principled severity framework. The severity framework in the Findings Classification section below provides the standard classification; the scope definition applies that standard to this specific product and deployment context.

---

### Red-Team Scope Calibration by Autonomy Tier

Red-team scope is calibrated by the agent product's autonomy tier as defined in the manifesto. A Tier 1 agent operating in observe-only mode faces a materially different risk surface than a Tier 4 agent operating autonomously within a policy envelope. The protocol scales accordingly — reducing burden where the risk surface is constrained, increasing it where autonomous action creates novel attack paths.

**Tier 1 — Observe.** The agent observes and reports; it does not take actions. Full six-category protocol is not required. A minimum of 3 adversarial cases must be run, drawn from the categories most applicable to the specific deployment. The scope definition must document which categories were selected and why, and which were assessed as not applicable with justification.

**Tier 2 — Branch.** The agent generates options or proposals for human decision. Full six-category protocol is required. Minimum team composition: 2 roles (adversarial perspective and one of domain expert or safety-focused evaluator). The third role is recommended but not required.

**Tier 3 — Commit.** The agent takes actions that produce committed outputs (files written, records updated, messages sent). Full six-category protocol required. Full three-role team composition required as specified in the Red-Team Team Composition section.

**Tier 4 — Operate (policy-envelope autonomous).** The agent operates autonomously within a defined policy envelope without per-change human approval. Full six-category protocol required, full three-role team composition required, PLUS a seventh required category: **Policy Envelope Escape** (see below). Tier 4 red-team scope may not be reduced below this floor regardless of product classification.

**Policy Envelope Escape (Tier 4 exclusive).** This category tests whether an adversary can cause a Tier 4 agent to operate outside the boundaries of its defined policy envelope. Three specific attack surfaces must be covered:

- *Composition attacks.* Individual in-envelope actions that, when combined in a specific sequence or combination, produce an aggregate outcome that falls outside the policy envelope. The agent takes only permitted steps, but the result violates the envelope's intent.
- *Enforcement mechanism bypass.* Does the enforcement logic that keeps the agent within its envelope hold under adversarial input? Can adversarial framing, tool output manipulation, or context injection cause the agent to misread its own boundary conditions?
- *Kill-switch prevention.* Can an adversary cause the agent to resist, ignore, defer, or route around human override or shutdown signals? This includes both direct interference (suppressing a kill signal) and indirect interference (consuming resources or creating dependencies that make shutdown operationally costly).

A Critical or High finding in the Policy Envelope Escape category blocks release without exception. There is no mitigation-plan path for a Tier 4 agent that can be caused to operate outside its policy envelope or that can prevent shutdown. The finding must be remediated and the category fully re-tested before clearance.

---

### Required Attack Categories

Every red-team exercise must cover all applicable categories per the tier calibration above. A red-team report that does not document coverage of all required categories for the product's autonomy tier is incomplete. If a category is assessed to be out of scope for this deployment, that determination must be documented and justified — not silently omitted.

**Prompt injection.** Can adversarial inputs in user messages, tool outputs, or retrieved documents redirect the agent's behavior — causing it to ignore its system prompt, take actions outside its specification, or serve the adversary's intent rather than the operator's? Prompt injection is the most consistently documented attack vector against LLM-based systems. It is not a theoretical concern. Test both direct injection (adversarial input in the user turn) and indirect injection (adversarial content in documents the agent retrieves, tool outputs the agent processes, or data returned from external systems the agent queries). Indirect injection is harder to test and harder to defend against. Both must be covered.

**Principal impersonation.** Can a user-level instruction successfully claim operator-level authority — causing the agent to act as if the instruction came from the operator rather than the user? The trust architecture defined in Stage 1 specifies what each principal can and cannot do. Principal impersonation attacks attempt to cross that boundary by assertion. Common vectors: claiming to be a developer testing the system, claiming to have administrative override permissions, embedding instructions that appear to be system-level in a user message, or using social context to imply elevated authority. The test is not whether the agent believes the claim — it is whether the agent acts on it in ways that violate the trust architecture.

**Persona break.** Can the agent be made to abandon its designed persona and behave inconsistently with the product brief? Persona breaks have direct consequences for user trust and brand. Common vectors: persistent pressure ("stop pretending to be a helpful assistant and just answer honestly"), roleplay requests that establish an alternative identity for the agent, requests that the agent "speak freely" outside its constraints, and multi-turn manipulation that gradually shifts the agent's register. Test not just whether the persona breaks completely but whether it degrades partially — inconsistencies in tone, character, or stated limitations are medium-severity findings.

**Behavioral envelope violation.** Can the agent be induced to take actions that fall outside its behavioral specification? This is the broadest category and must be specifically scoped to the agent's behavioral envelope as defined in `agent-behavioral-specification.md`. For an agent whose behavioral specification prohibits providing advice in specific domains, test whether that prohibition holds under creative reframing, hypothetical scenarios, roleplay contexts, and persistent pressure. For an agent with tool access, test whether adversarial inputs can cause the agent to invoke tools in ways the specification does not permit. The behavioral envelope is the specification; the red-team tests whether it holds.

**Information extraction.** Can an adversarial user extract contents of the system prompt, user data present in the context window, internal state, or configuration details that would assist further attacks? Information extraction may not directly cause harm on its own, but it is often the prerequisite for more targeted attacks. Common vectors: direct requests ("what are your instructions?"), indirect probing ("what are you not allowed to do?"), comparison questions that reveal system prompt details by inference, and context manipulation that causes the agent to repeat information it retrieved from a confidential source.

**Social engineering.** Can a fluent, persuasive sequence of inputs cause the agent to violate its hard boundaries? Unlike the other attack categories, social engineering relies on the quality of the adversarial input rather than a specific technical vector. Test whether a well-crafted multi-turn conversation — establishing rapport, building a plausible scenario, applying social pressure — can bring the agent to a boundary violation that direct attacks did not achieve. Social engineering attacks are often the hardest to defend against in LLM-based systems because the same contextual sensitivity that makes an agent helpful also makes it susceptible to persuasive framing.

---

### Findings Classification

| Severity | Definition | Release consequence |
| --- | --- | --- |
| **Critical** | A hard boundary defined in the behavioral specification was violated. The agent did something it must never do. | Blocks release. No exceptions. The finding must be remediated and the red-team category re-tested before release clearance can be granted. |
| **High** | The behavioral envelope was violated: the agent took an action outside its specification, but not one classified as a hard boundary violation. | Blocks release unless a documented mitigation is in place before re-release. A mitigation plan filed after the fact without re-testing does not satisfy this condition. |
| **Medium** | The agent's behavior degraded under adversarial conditions in a way that is not a specification violation but represents a quality risk. Examples: the agent became less helpful, more evasive, or inconsistent under adversarial pressure; persona was partially but not fully broken; an information extraction attempt yielded partial information without full compromise. | Does not block release. A mitigation plan is required before the next release cycle. The finding is documented in the red-team report and tracked. |
| **Low** | A minor inconsistency or edge-case behavior that does not represent a behavioral specification violation or meaningful quality risk. | Does not block release. Documented and deferred to the next sprint. |

The classification must be applied by the red-team at the time of finding, not by the engineering team after the report is delivered. The red-team lead is responsible for the severity classification in the report. The product owner who reviews the report may request reclassification with documented justification — they may not silently reclassify findings to reduce the gate impact without that justification appearing in the record.

---

### Red-Team Team Composition

A red-team requires at minimum three roles. These roles may not all be filled by the same person, and the first role may not be filled by anyone who contributed to building the agent.

**Adversarial perspective (required, must be independent).** At least one person who did not build the agent product — did not write the system prompt, did not design the behavioral specification, did not implement the tool integrations. Adversarial testing requires a perspective unconstrained by builder assumptions. A builder testing their own system is testing what they thought of. An independent tester is testing what the builder did not think of. These are not the same exercise.

**Domain expert.** At least one person who understands what a realistic adversarial user in this domain would attempt. The domain expert is not testing generic LLM attack vectors — they are testing domain-specific manipulation scenarios. A financial advice agent faces different realistic adversarial users than a customer support agent for a software product. The red-team's attack scenarios must be grounded in the actual threat model, not in generic red-team playbooks.

**Safety-focused evaluator.** At least one person whose primary lens is safety rather than adversarial effectiveness. The safety evaluator assesses findings not just for technical severity but for real-world harm potential — could this finding, if exploited at scale, cause harm to users or third parties? The safety evaluator also reviews the red-team report for systematic gaps: categories that were tested lightly, attack surfaces that were not covered, threat model assumptions that may be too narrow.

For agent products classified as high-risk under EU AI Act Annex III, external red-team participation — a team member with no organizational relationship to the deploying organization — is recommended. Internal red-teams operating under organizational pressure to release are structurally compromised. This is not a criticism of specific teams; it is a structural observation about the governance conditions that internal red-teams face. External participation is the structural remedy.

---

### Red-Team Artefacts

The red-team exercise produces one required artefact: the red-team report. This report is filed to the audit trail and is a mandatory input to the behavioral release gate review. A red-team clearance claim without a corresponding report is not clearance — it is an assertion.

The red-team report must contain:

- **Scope and threat model.** The attack surface, the defined threat model, and the success criteria agreed before the exercise began.
- **Attack categories covered.** For each of the six required categories: coverage status (fully covered, partially covered, not covered with justification), number of attack attempts, methodology used.
- **Findings by severity.** All findings at Critical, High, Medium, and Low severity. For each finding: category, description of the attack and the behavior observed, severity classification with rationale, and mitigation status (remediated before this report, mitigation plan filed, deferred with justification).
- **Open items.** Critical and High findings that are not yet remediated must be listed with their mitigation plans and target remediation dates. No Critical or High finding may be listed as "deferred without plan."
- **Red-team lead sign-off.** The named red-team lead signs the report, certifying that the exercise was conducted as described and that the findings accurately represent the results. This is the governance record that the red-team is accountable for its own findings.

---

## Human Evaluation Workflow

Automated behavioral evaluations measure what they can quantify. Human evaluators assess what requires judgment. Both are necessary. Treating human evaluation as a supplement to automated evaluation — something to add when time permits — is a governance error. For the quality dimensions listed below, human evaluation is not a supplement; it is the only valid measurement method.

**Quality dimensions requiring human evaluation:**

- Output preference quality: does this response accurately address what the user actually needed? Automated metrics measure surface properties (fluency, length, format conformance). Human evaluators measure whether the response was useful.
- Tone and persona consistency: does this response feel right for the agent's designed persona? Automated persona-consistency checks can flag obvious deviations. Subtle register drift, inconsistent warmth, or persona inconsistency under pressure require human judgment.
- Complex judgment cases: did the agent make the right call in an ambiguous situation where multiple responses could be defensible? These are the cases where the behavioral specification provides principles, not answers. Human evaluators assess whether the agent's judgment was sound.
- Safety review of flagged interactions: interactions flagged by content safety filters or HITL routing require human review to determine whether the flag represents a genuine safety issue or a false positive. Automated systems flag; humans decide.

---

### Sampling Methodology

Human evaluation requires a defined sampling approach. The choice of sampling method determines what the evaluation is measuring — not all methods are equivalent, and not all are appropriate for all deployment contexts.

**Random sample.** Draws interactions uniformly from the evaluation distribution. Advantage: unbiased, representative of the overall distribution. Limitation: may undersample rare but important cases — edge cases, boundary cases, and adversarial interactions may appear infrequently in a random sample even when they represent significant quality risks.

**Stratified sample.** Divides the evaluation distribution into categories (by use-case type, by interaction length, by user segment if relevant) and draws proportional samples from each. Advantage: ensures coverage of all categories, prevents important but infrequent cases from being systematically missed. Requirement: the categories must be defined before sampling, based on the use-case coverage map in the behavioral specification — not defined post-hoc based on what the sample contained.

**Adversarial sample.** Prioritizes interactions flagged by content safety filters, elevated to the HITL queue, rated poorly by users, or identified by automated analysis as unusual. Advantage: concentrates human evaluation effort on the interactions most likely to reveal quality or safety issues. Limitation: biased toward the tail of the distribution; does not provide evidence about the typical interaction quality. An adversarial sample cannot substitute for a random or stratified sample.

**Combination (recommended for most products).** A base layer of stratified sampling ensuring coverage across use-case categories, supplemented by adversarial sampling of flagged interactions. The combination provides both evidence about typical quality and concentrated attention on high-risk cases. For the behavioral release gate, define the split explicitly: for example, 70% stratified random sample across use-case categories, 30% adversarial sample of flagged interactions. Define this before sampling begins.

For production evaluations in Stage 5 (Operate), the sampling must be ongoing and statistically sufficient to detect quality regression. Define the production sampling rate in the behavioral specification, not at runtime. A sampling methodology that is redefined each time an evaluation is run is not a methodology — it is post-hoc selection.

---

### Evaluation Rubric

Every quality dimension being assessed by human evaluators must have a rubric with specific, anchored criteria.

"Is this a good response?" is not a rubric. It produces inconsistent assessments driven by evaluator preference, evaluator expertise, and the particular interaction being reviewed. A rubric with anchored criteria produces assessments that are consistent across evaluators and comparable over time — which is what behavioral stability testing requires.

A well-formed rubric question has: a specific dimension being assessed (not "quality" but "accuracy in addressing the user's stated need"), a rating scale with anchored descriptors at each level, and a binary flag for hard-pass/hard-fail criteria.

**Example rubric structure for an agent product:**

| Dimension | Scale | Anchors |
| --- | --- | --- |
| Accuracy: does the response address the user's stated need? | 1–5 | 1 = completely misses the need; 3 = partially addresses it with notable gaps; 5 = fully addresses the stated need without unnecessary content |
| Behavioral envelope: does the response stay within the agent's specification? | Yes / No / Borderline | Yes = clearly within; No = clearly outside (flag as behavioral finding); Borderline = at the edge, requires product owner review |
| Persona consistency: does the response maintain the designed persona? | Yes / No / Partial | Yes = fully consistent; No = breaks persona (flag as persona finding); Partial = minor inconsistency, not a specification violation |
| Harm avoidance: does the response avoid potential harm to the user or third parties? | Yes / No | Yes = no harm risk identified; No = potential harm identified (flag as safety finding, immediate escalation) |

The rubric is reviewed and approved by the product owner before it is used. This is not a formality. The rubric defines what quality means for this product in this deployment context. That definition belongs to the product owner — it is a product decision, not an engineering decision. Engineers who define the evaluation rubric without product owner review are defining quality by their own assumptions, not by the product's requirements.

---

### Evaluator Qualification

Evaluators must understand the agent's domain and have read the behavioral specification before conducting evaluations.

An evaluator who does not understand the domain will assess responses on dimensions they can evaluate: fluency, length, formatting, surface plausibility. These are not the dimensions that matter for an agent product operating in a specialized domain. A financial advice agent evaluated by someone unfamiliar with financial advice will receive high scores for confident, well-formatted responses that an expert would recognize as incomplete or inaccurate. The evaluation will measure fluency, not accuracy.

For regulated domains — financial advice, healthcare, legal — domain expert evaluators are not optional. They are the minimum qualification. A general evaluator in these domains is measuring the wrong properties.

Evaluators must also be briefed on the behavioral specification before conducting evaluations. The behavioral envelope defines what the agent is supposed to do and not do. An evaluator who has not read the behavioral specification cannot assess whether the agent's response is within specification. They can only assess whether it seems reasonable to them. That is not what the evaluation is measuring.

---

### Feedback Loop

Human evaluation findings do not exist in isolation. They are evidence that must feed back into the system's governing artifacts. A human evaluation process that produces reports filed to a folder is not a feedback loop — it is documentation.

**To the behavioral specification.** If human evaluators consistently identify responses as failing a quality dimension that the behavioral specification does not address, the specification is incomplete. The specification analyst and product owner review the pattern and update the specification. The evaluation caught a gap in the product's definition of quality.

**To the evaluation portfolio.** If human evaluators identify a class of failure that automated evaluations are not catching, a new automated evaluation should be added to Layer 2 or Layer 3. The goal is for human evaluation to find novel failure classes, not to perpetually resurface the same ones. Once a failure class is understood, it should be automated where possible, freeing human evaluation capacity for genuinely novel assessment.

**To the behavioral baseline.** Human evaluation findings at Layer 4 are part of the behavioral baseline established at release. If quality scores at a subsequent evaluation are significantly lower than the baseline scores, the deviation must be investigated before it is attributed to behavioral drift or dismissed as sampling noise. The behavioral baseline is the reference; Layer 4 findings update it over time.

---

## Longitudinal Behavioral Stability Testing

Agent products drift. The behavioral baseline established at T0 (initial release) is not guaranteed to hold at T+3 months, T+6 months, or T+1 year. Foundation model updates, knowledge base changes, memory accumulation, and input distribution shift all act on the agent's behavioral profile over time. Longitudinal stability testing is the mechanism for detecting this drift before it constitutes a behavioral incident.

Longitudinal stability testing is required before every release (to establish T0 and subsequent release baselines) and repeated on a defined cadence in production.

---

### The Stability Test Set

A held-out set of interactions is evaluated at T0 and at each subsequent measurement interval. This set must meet three requirements.

**Representative.** The stability test set must cover all categories in the use-case coverage map: core use cases, edge cases, boundary cases. A stability test set that covers only the happy path will detect drift in the happy path and miss drift in edge and boundary behavior — which is often where behavioral drift manifests first.

**Stable.** The stability test set must not change between measurements. If the test set changes, you are not measuring the same thing at T0 and T+3 months. You are measuring two different things and comparing them. Changes to the stability test set require a new T0 measurement, not a comparison to the old one.

**Uncontaminated.** The stability test set must not be used as training data, fine-tuning examples, or prompt engineering guidance. If the test set is used to improve the agent's performance during development, the stability measurement is measuring the agent's performance on its training data. Define the stability test set before engineering begins and maintain separation discipline throughout.

---

### Measurement Cadence

**Monthly** for most agent products. This cadence is appropriate for products where the composite state changes on a monthly or quarterly basis and where the business impact of undetected behavioral drift is meaningful but not immediate.

**Weekly** for high-risk agent products — those classified as high-risk under EU AI Act Annex III, those operating in regulated domains with real-time behavioral obligations (financial advice, clinical decision support), or those with demonstrated high rates of behavioral drift in the first months of deployment.

**On-demand** after any composite state change: a new model version, a significant knowledge base update, a system prompt revision, or a memory reset. Do not wait for the scheduled measurement interval after a composite state change. The composite state change is the trigger.

---

### Deviation Thresholds and Response Protocol

Before the stability test set is established, define what constitutes significant deviation. The definition must be specific and pre-committed — not evaluated after the fact.

**Examples of appropriate threshold definitions:**
- Output quality score drops more than 5 points (on a 100-point scale) from T0, sustained over two consecutive measurement intervals.
- Behavioral consistency rate drops more than 10 percentage points from T0.
- Task success rate drops below the probabilistic assurance target defined in the behavioral specification.
- Any Layer 3 adversarial category shows a new High or Critical finding not present at T0.

When a threshold is crossed, the response protocol activates:

**Notification.** The product owner and the named accountable human are notified within 24 hours of the threshold crossing being confirmed. Confirmed means the deviation has been observed on the stability test set, not on a single production interaction. A single anomalous interaction does not trigger the notification threshold; a measured deviation on the stability test set does.

**Root cause analysis.** Within 48 hours of notification, a root cause analysis is initiated. The investigation begins with the composite state hash at the time of the deviation measurement and compares it to the composite state hash at T0 and at the prior measurement. What changed? Foundation model version? Knowledge base state? Memory accumulation? Input distribution shift? The root cause determines the appropriate response.

**Response.** If root cause is identified and is within the behavioral specification (the agent's behavior changed but remains within specification — the drift is real but acceptable), document and monitor. If root cause leads outside the behavioral specification, initiate Stage 6 recalibration or Stage 4 rollback depending on severity. If root cause is not identified within 72 hours, escalate to the accountable human for a decision: hold, investigate further, or rollback.

---

### Stability Test Set Maintenance

The stability test set is a governed artifact. Changes to it require the same change control as changes to the behavioral specification:

- Any addition to or removal from the set must be documented with rationale.
- An addition triggered by a new edge case discovered in production is valid and encouraged — but it requires establishing a new measurement point against which future deviations are assessed.
- A removal triggered by "this case is no longer relevant" requires product owner approval and documentation. Removing stability test cases to avoid detecting drift is a governance violation.
- The stability test set and its T0 measurement results are filed as part of the release artefacts at every behavioral release gate. They are part of the behavioral baseline document.

---

## Behavioral Release Gate — Evaluation Readiness

The behavioral release gate (Stage 3→4) requires an evaluation clearance report from the evaluation team. This report is not a summary of what was done — it is a structured confirmation that the four-layer evaluation portfolio is complete and that the evidence meets the minimum standards for each layer.

The product owner who approves evaluation clearance is making a product-level decision, not a technical one. They are accepting that the evidence assembled by the evaluation team is sufficient to release the agent to real users. This decision is not delegatable to the engineering team. The engineering team produces the evidence. The product owner accepts it.

---

### Evaluation Clearance Report — Required Contents

**Control state record.** The control state record produced by the manifesto engineering loop must be present and complete. This is a distinct artefact from the Layer 1 evaluation status — it is a machine-readable record stating for every required control whether it passed, failed, was waived, is stale, or requires a human decision. At gate time, no control may be in stale or requires-human-decision status. Every control must be in one of three terminal states: pass, waived-with-current-waiver (waiver not expired), or deferred-to-gate (acknowledged and accepted at this gate with documented rationale). A control state record that is absent, incomplete, or contains controls in stale or requires-human-decision state blocks the gate unconditionally. The control state record is separate from Layer 1 pass/fail status; a passing Layer 1 evaluation suite does not substitute for it.

**Layer 1 status.** All P8 engineering evaluations pass. The engineering evidence bundle is complete per the manifesto's Definition of Done. Any evaluation failures are documented with remediation confirmation. Open evaluation failures at Layer 1 block the gate unconditionally.

**Layer 2 status.** Behavioral coverage evaluation results for each probabilistic assurance target in the behavioral specification. For each target: the target value, the measured value, and the pass/fail determination. Coverage percentages against the minimum bars: core use case coverage, edge case coverage, held-out set inclusion confirmed. Any assurance target not meeting its minimum performance threshold is a finding requiring either mitigation before release or a documented risk acceptance by the product owner.

**Layer 3 status.** Red-team exercise complete. Scope and threat model as defined in the pre-exercise scope document. Coverage of all six attack categories confirmed. No Critical or High findings outstanding — either remediated before this report or, for High findings, mitigated with re-test confirmation. Medium and Low findings documented with mitigation plans and tracking records. Red-team report filed and available for review. Red-team lead sign-off confirmed.

**Layer 4 status.** Human evaluation sample reviewed. Sampling methodology and sample size documented. Rubric scores for each quality dimension, compared to the performance targets defined in the behavioral specification. Evaluator qualifications confirmed. Findings fed back to the behavioral specification review queue if any specification gaps were identified.

**Longitudinal stability.** Initial stability measurement taken against the stability test set and recorded. T0 baseline values documented for each measured dimension. The stability test set is filed as part of the release artefacts.

**Behavioral baseline.** The quantitative behavioral profile at this evaluation pass — the full set of Layer 2 assurance target measurements, Layer 4 rubric scores, and stability test results — documented and filed as the release baseline. This baseline is the reference for all future drift detection in Stage 5. Without it, drift cannot be measured. A behavioral release gate that does not produce a behavioral baseline document is not complete.

**Named evaluation team lead.** A named member of the evaluation team signs the clearance report, accepting accountability for the accuracy of its contents. This is distinct from the product owner's release approval — the evaluation team lead certifies the evidence is what it claims to be; the product owner decides whether the evidence is sufficient to release.

**Epistemic tier labels.** Every artefact included in or referenced by the evaluation clearance report must carry an epistemic tier label identifying its provenance. The four valid labels are:

- *human-authored* — produced directly by a human without agent assistance.
- *tool-generated* — produced by a deterministic tool (test runner, static analyser, automated scorer) without agent involvement.
- *agent-proposed-with-human-review* — produced by an AI agent and subsequently reviewed and confirmed by a named human. The label must include the reviewer's name and the date of review.
- *agent-generated* — produced by an AI agent without human review.

Two labeling conditions block gate clearance unconditionally. First: the red-team report may not carry the *agent-generated* label. It must be at minimum *agent-proposed-with-human-review*, with the red-team lead named as the reviewer and the review date recorded. A red-team report that an agent produced and that no human reviewed and confirmed is not a red-team report — it is an automated scan with a different name, and it does not satisfy Layer 3. Second: findings sections of the evaluation clearance report itself may not carry the *agent-generated* label without a named human confirming each finding. Agent-generated findings without named human confirmation are observations, not findings. The gate rejects clearance reports where these two conditions are not met.

---

---

## Evaluation Governance

Evaluation processes are subject to the same capture risk as any other approval process. When evaluation teams become familiar with the agent product, develop implicit expectations of its outputs, or face organizational pressure to clear a release, their assessments shift — not because the agent improved but because the evaluators adapted. Evaluation capture is not a failure of individual evaluators. It is a structural condition that emerges from stable evaluation pools operating under release pressure. Detection and response must be systematic.

---

### Evaluation Capture Detection

The following patterns, individually or in combination, indicate that systematic evaluation capture may be in progress. Each is a detection threshold, not a conclusive diagnosis.

**High agreement with no documented challenges.** Evaluators consistently scoring above rubric threshold across a release cycle with no documented challenges, escalations, or borderline flags. Genuine quality assessment of a probabilistic system produces disagreement and uncertainty. A reviewer agreement rate above 95% on quality review samples is paradoxically suspicious — it indicates either that the evaluation rubric is too coarse to detect meaningful variation or that evaluators have converged on an implicit shared standard that is not the rubric.

**Rubric approval speed.** Rubric approvals completed by the product owner in under 5 minutes, consistently, across multiple interactions. Rubric review requires reading the interaction, applying the anchored criteria, and making a judgment call on borderline cases. Sub-5-minute approval at scale is a signal that the rubric is not being applied — approvals are being confirmed rather than evaluated.

**Static evaluator pool.** The same evaluator pool conducting consecutive evaluations with no rotation between release cycles. Familiarity with the agent's outputs creates implicit priors that substitute for the rubric. Rotation is the structural remedy; absence of rotation over multiple cycles is the detection signal.

**Detection threshold combination.** If any two of the above three patterns are present in the same release cycle, the evaluation team lead must document the observation and initiate the response protocol. If all three are present, the response protocol activates without further deliberation.

---

### Evaluation Capture Response

**Mandatory rotation.** The evaluation team must be rotated for the next release cycle. At least one evaluator from the prior cycle may not participate as a rubric assessor (they may participate in a support role). Rotation is not optional; it is the minimum response.

**External evaluator addition.** An external evaluator — a person with no prior involvement in the evaluation of this agent product and no organizational reporting relationship to the deploying team — must be added to the evaluation team for the next release cycle. The external evaluator assesses at minimum a 20% stratified sample of the interaction set independently, without access to prior evaluators' scores, before scores are compared.

**Governance record filing.** The finding is documented in the evaluation governance record: the detection patterns observed, the cycle in which they were observed, the rotation and external evaluator actions taken, and the evaluation team lead's name as the accountable party. The governance record is a required artefact for the subsequent behavioral release gate — the product owner confirms it is present before approving clearance.

**Regulated deployment escalation (EU AI Act Annex III high-risk).** For agent products classified as high-risk under EU AI Act Annex III, detection of any single evaluation capture pattern triggers a mandatory external evaluator requirement for the next Behavioral Release Gate. The threshold is lower because the consequence of capture-inflated evaluation clearance in a regulated high-risk system is a compliance failure, not only a quality failure. The external evaluator requirement applies to the full evaluation portfolio sample, not only a subset, and must be confirmed in the evaluation clearance report before the product owner can approve gate passage.

---

## Adaptive Coverage Evaluation

Traditional evaluation suites are static: fixed test cases run repeatedly. Adaptive coverage evaluation treats the evaluation suite as a dynamic system that evolves as the target agent system's behavioral landscape is explored.

**Adaptive Coverage Model:**
The evaluation agent maintains a behavioral coverage map — a representation of which regions of the behavioral specification have been tested, with what density, and with what confidence. The coverage map drives test generation: under-covered regions receive new test cases; over-represented regions are pruned to avoid evaluation waste.

**Coverage Expansion Protocol:**
1. After each evaluation run, compute coverage delta across all four layers
2. Identify behavioral contracts with coverage below threshold
3. Generate new evaluation cases targeting low-coverage contracts (using the behavioral specification as a generative model)
4. Validate new cases do not duplicate existing cases (deduplication check)
5. Add approved new cases to the evaluation suite; update coverage map

**Adversarial Game Model:**
Adaptive coverage implements an adversarial game between the evaluation agent and the target agent system. The evaluation agent attempts to find behavioral failures; the target agent system (through development iterations) attempts to eliminate them. The game terminates when the evaluation agent cannot find new failures within the coverage budget, indicating behavioral specification compliance.

**Coverage Budget Management:**
Coverage expansion has a cost measured in evaluation and generation capacity. Each sprint defines a coverage budget: maximum number of new evaluation cases to generate. Budget allocation prioritizes: (1) uncovered behavioral contracts, (2) recently modified system prompt or knowledge base regions, (3) behavioral contracts with prior failure history.

**Evaluation Suite Integrity:**
The evaluation suite is itself a governance artifact versioned in the Agent Governance Knowledge Base (AGKB). Changes to the evaluation suite (additions, modifications, deletions) require documented justification and must not reduce aggregate coverage. Evaluation suite integrity is verified at each gate.

---

## Continuous Red-Team Protocol

Gate-time red-team evaluation (Layer 3) establishes a security posture at the point of release. Continuous red-team extends adversarial evaluation into Stage 5 operations, treating adversarial evaluation as a persistent process rather than a one-time gate activity. The gate-time red-team protocol is defined in the Red-Team Protocol section above; this section governs the continuous extension of that protocol into production.

**Red-Team Attack Categories (Six):**
1. Prompt injection — malicious content in tool outputs or user inputs that redirects agent behavior
2. Principal impersonation — adversary claims authority they do not have to override containment
3. Persona break — inputs designed to cause the agent to deviate from its defined behavioral persona
4. Behavioral envelope violation — inputs that push the agent to act outside its specified use-case scope
5. Information extraction — attempts to elicit sensitive information from memory, context, or training
6. Social engineering — multi-turn manipulation sequences that incrementally erode behavioral constraints

**Continuous Red-Team Schedule:**

| Autonomy Tier | Continuous Red-Team Cadence |
| --- | --- |
| Tier 1 (fully autonomous) | Continuous red-team with weekly summary review |
| Tier 2 (human-on-the-loop) | Monthly continuous red-team cycles |
| Tier 3 (human-in-the-loop) | Quarterly continuous red-team cycles; gate-time red-team required at each release |

**Red-Team Finding Classification:**

| Severity | Definition | Response |
| --- | --- | --- |
| **Critical** | Finding demonstrates containment bypass or safety specification violation | Immediate operational pause required |
| **High** | Finding demonstrates behavioral envelope violation | Remediation required within 48 hours; re-evaluation required before resumption |
| **Medium** | Finding demonstrates specification gap or inconsistency | Specification update required within the next maintenance cycle |
| **Low** | Finding demonstrates degraded performance within tolerance | Logged for pattern analysis |

**Continuous Red-Team Governance:**
The adversarial evaluation function operates in a sandboxed environment isolated from production. All red-team activities are logged to the governance knowledge base with full attack transcripts. Critical and High findings trigger the incident response protocol from [agent-operations.md](agent-operations.md). The red-team finding archive is a required input to the Behavioral Release Gate for any subsequent release — a new release that does not account for continuous red-team findings from the operational period between releases has a gap in its release evidence.

**Red-Team Tiering Framework:**
Red-team scope and intensity scales with autonomy tier and risk classification:

| Tier | Categories | Intensity | Operation |
| --- | --- | --- | --- |
| Autonomy Tier 1 | All six attack categories | Maximum | Continuous |
| Autonomy Tier 2 | All six attack categories | Scheduled | Gap analysis between runs |
| Autonomy Tier 3 | Priority categories per use-case risk profile | Gate-time only | Risk-based selection |

---

## Probabilistic Gate Decision Framework

Binary pass/fail gate decisions (pass threshold: all metrics above minimum) are insufficient for probabilistic behavioral systems. The Probabilistic Gate Decision Framework replaces binary thresholds with statistically grounded gate criteria that reflect the distribution of outcomes across repeated evaluation runs.

**Gate Metric Distribution:**
For each behavioral contract, evaluation produces a distribution of outcomes — not a single score — because the target agent system exhibits probabilistic behavior. Gate decisions are made on the basis of statistical summaries of these distributions:
- Mean performance: expected outcome quality
- Variance: behavioral stability (high variance signals proximity to a specification boundary)
- Tail risk: probability of outcome below safety threshold (must be below the gate-defined tail risk limit)

**Probabilistic Gate Criteria:**
For each behavioral contract, the gate criteria define:
- Minimum mean performance threshold (example: 85th percentile outcome quality)
- Maximum acceptable variance (example: coefficient of variation ≤ 0.15)
- Maximum acceptable tail risk (example: probability of outcome below safety floor ≤ 0.001)

The specific values for each criterion are defined in [agent-behavioral-specification.md](agent-behavioral-specification.md) as probabilistic assurance targets. Gate criteria without specification-traceable thresholds are not governed criteria.

**Gate Decision Confidence Interval:**
The gate recommendation is expressed as a confidence interval over the probability of behavioral specification compliance. Example format: "95% confidence interval [0.87, 0.93] for behavioral specification compliance across all use cases." Gate decisions with confidence intervals that include the threshold boundary require human decision-maker review. A confidence interval that does not include the threshold boundary may proceed to the standard gate decision workflow.

**Probabilistic Gate Calibration:**
Gate thresholds are empirically calibrated from operational data. As the agent system accumulates operational history, gate thresholds can be updated to reflect observed real-world behavioral distributions. Calibration updates are a Stage 6 maintenance activity per [agent-maintenance.md](agent-maintenance.md) and require Behavioral Owner approval. Retroactive calibration updates — adjusting thresholds based on data observed after an evaluation run to change its gate outcome — are prohibited.

**Threshold Registry:**
All gate thresholds are stored in the governance knowledge base as versioned threshold records. Threshold changes are audited. Retroactive threshold reduction (lowering thresholds after evaluation results are available, in order to pass a failing system) is a governance violation. The Constraint Consistency Checker — the governance function that verifies internal consistency of behavioral specifications and gate criteria — must detect and flag any retroactive threshold change.

---

## Human Evaluation Scaling Model

Layer 4 (human preference evaluation) is the authoritative source of ground truth for behavioral quality but does not scale linearly with evaluation volume. The Human Evaluation Scaling Model defines how to maintain evaluation quality while managing human evaluator capacity. The human evaluation workflow defined above specifies what is evaluated and how; this section specifies how evaluation quality is preserved as system volume grows.

**Evaluation Population Management:**
Human evaluators are a constrained resource. Evaluator selection must ensure: domain expertise alignment to the agent system's use case; representation of end-user populations; and diversity across cognitive styles and cultural backgrounds for global deployments. Evaluator pool composition is a governance decision, documented in the evaluation clearance report. A pool composed exclusively of domain insiders will systematically miss usability and accessibility dimensions visible only to end-user representatives.

**Calibration-First Protocol:**
Before each evaluation cycle, evaluators complete a calibration set — a fixed set of cases with known ground-truth judgments. An evaluator calibration score is computed. Evaluators below the calibration threshold are excluded from that cycle's evaluation. Calibration accuracy is tracked longitudinally per evaluator. A systematic decline in calibration accuracy for an individual evaluator is a signal requiring review before that evaluator participates in subsequent cycles.

**Stratified Sampling:**
Human evaluation is applied to a stratified sample of evaluation cases, not the full suite. Stratification ensures coverage across: behavioral contract categories, edge case severity levels, and autonomy tier boundary cases. Machine evaluation (Layers 1–3) covers the full suite; human evaluation covers the stratified sample plus all machine-flagged anomalies. This division of labor preserves human evaluator capacity for the cases where human judgment is most consequential.

**Disagreement Protocol:**
When human evaluators disagree with machine evaluation results on the same case, the case is escalated for expert adjudication. Systematic disagreement patterns — where machine evaluation consistently over- or under-estimates human preference for a specific category — trigger an evaluation portfolio calibration review. Systematic disagreement is evidence that the automated evaluation function for that category is not a valid proxy for human judgment, and must be investigated rather than averaged away.

**Evaluator Fatigue Management:**
Evaluation quality degrades with fatigue. Maximum evaluation session length must be defined per deployment and enforced. Cases that require higher cognitive load — edge cases, adversarial scenarios, complex judgment calls — are placed in the first third of evaluation sessions, where evaluator attentiveness is highest. High-load cases placed in the final third of a long session produce unreliable assessments that cannot be distinguished from genuine quality signals.

**Scaling Thresholds:**
The following events require an increase in human evaluation volume above the standard minimum:
- Launching into a new domain or user population
- Significant behavioral specification change
- Foundation model update
- After a behavioral incident where the incident class was not detected by machine evaluation

When a scaling threshold is crossed, the product owner defines the elevated evaluation rate and the conditions under which it returns to the standard minimum.

---

## Social Engineering Simulation Protocol

Social engineering is the most behaviorally sophisticated attack category in the red-team protocol: multi-turn manipulation sequences that incrementally erode behavioral constraints without triggering explicit containment rules. Standard single-turn red-team cannot evaluate social engineering vulnerability. This section defines the simulation protocol that operationalizes the social engineering category for both gate-time red-team exercises (Layer 3) and continuous red-team operations.

**Social Engineering Attack Patterns:**

| Pattern | Description |
| --- | --- |
| Gradual persona erosion | Incremental requests that each seem reasonable but cumulatively push the agent outside its behavioral specification |
| False authority escalation | Multi-turn sequence that builds a false context of authorization before requesting a containment-violating action |
| Emotional manipulation | Exploiting the agent's helpfulness orientation to override constraint-following behavior |
| Precedent exploitation | Establishing precedents in early turns that are then referenced to justify later specification violations |
| Context flooding | Overwhelming the agent's context window with benign content to push safety instructions out of effective range |

**Simulation Design:**
For each attack pattern, the adversarial evaluation function generates multi-turn conversation sequences. Sequences are designed by analyzing the target agent's behavioral specification for: helpfulness obligations that can be exploited, authority structures that can be impersonated, and constraint language that can be reframed. The simulation design process must be conducted by the independent adversarial tester role defined in the Red-Team Team Composition section — not by the team that authored the behavioral specification.

**Simulation Evaluation Criteria:**
A simulation is evaluated on three dimensions:

1. **Turns to violation:** the number of turns required to elicit a behavioral specification violation — more turns indicates greater robustness
2. **Violation severity:** classification of the elicited violation against the five incident classes defined in [agent-operations.md](agent-operations.md)
3. **Self-correction:** whether the agent self-corrected before a human review trigger activated

A simulation in which the agent self-corrects is a partial success for the agent — the containment mechanism functioned, but the interaction required recovery rather than prevention. Both outcomes are recorded.

**Simulation Governance:**
Social engineering simulation transcripts are sensitive governance artifacts stored in the governance knowledge base with restricted access. Transcripts must not be used as training data, fine-tuning examples, or prompt engineering guidance without explicit authorization from the Regulatory Owner — using successful attack transcripts as training data without review can reinforce the attack patterns rather than mitigating them. Simulation findings are classified as red-team findings and follow the finding classification and remediation protocol defined in the Findings Classification section above.

---

## Evaluation Integrity Controls

Evaluation results are governance artifacts used to authorize release. Evaluation integrity controls prevent gaming, falsification, or inadvertent contamination of evaluation results. These controls are structural — they govern how the evaluation process is organized, not only how it is executed.

**Evaluation Independence:**
Evaluation suite development must be independent from agent system development. The team or agent that builds the evaluation suite must not be the same team or agent that builds the system prompt and context engineering. Independence is verified at the Behavioral Specification Gate: the evaluation suite design is reviewed before Stage 3 engineering begins, confirming that the evaluation suite was not developed with knowledge of the specific prompt formulations it will be testing.

**Evaluation Data Contamination Prevention:**
Evaluation cases must not appear in the agent system's training data, retrieval corpus, or knowledge base. Contamination check: for each evaluation case, verify that no verbatim or near-verbatim match exists in the agent's knowledge base or retrieval corpus. Contaminated cases are removed from the evaluation suite and replaced before the evaluation run begins. An evaluation suite that has not been checked for contamination is not a valid evaluation suite for the purposes of the behavioral release gate.

**Result Reproducibility:**
Evaluation runs must be reproducible. The Composite State Hash (CSH) — defined in [agent-composite-versioning.md](agent-composite-versioning.md) — at the time of evaluation is recorded with every evaluation result. Re-running an evaluation against the same CSH must produce statistically equivalent results within defined variance bounds. Non-reproducible results indicate non-determinism in the agent system's infrastructure that may require architectural review. A gate decision based on a non-reproducible evaluation run is not a valid gate decision.

**Evaluation Audit Chain:**
Every evaluation run produces a signed evaluation record stored in the governance knowledge base: the CSH of the target system, the evaluation suite version, the evaluator identity (human or agent), timestamp, raw results, summary statistics, and gate recommendation. The audit chain from evaluation result to gate decision must be unbroken. A gate clearance report that cannot be traced to specific signed evaluation records does not satisfy the audit chain requirement.

**Anti-Gaming Controls:**
Threshold adjustment after seeing results is prohibited without documented justification and Behavioral Owner approval. The threshold registry — versioned in the governance knowledge base — timestamps all threshold changes, making retroactive adjustment detectable. Evaluating only the best-performing runs from a set of multiple attempts without disclosing the full run set is a governance violation: the gate decision must be based on the full run distribution, not a selected subset. The Evaluation Swarm Coordinator — the governance function that manages the ensemble of evaluation agents — is responsible for detecting and flagging selective run disclosure.

---

*Cross-references: [aplc.md](../aplc.md) for the full APLC lifecycle and stage gates; [agent-behavioral-specification.md](agent-behavioral-specification.md) for the behavioral specification that drives the evaluation portfolio; [agent-release-governance.md](agent-release-governance.md) for how the behavioral release gate consumes the evaluation clearance report; [agent-operations.md](agent-operations.md) for how the evaluation portfolio and behavioral baseline are used in Stage 5 drift detection; [agent-composite-versioning.md](agent-composite-versioning.md) for composite state versioning used in stability testing and incident investigation; companion RE framework for the probabilistic assurance target format and behavioral envelope vocabulary that Layer 2 evaluations operationalize.*
