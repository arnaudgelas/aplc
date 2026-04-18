# Stage 2 — Specify Behaviorally: The Agent Behavioral Specification

*Primary Stage 2 document of the Agentic Product Lifecycle. Extends `companion-re-framework.md` from engineering specification to product specification. The behavioral specification is the product's constitution — what the agent does, how it does it, what it never does, and how it handles the edge. Audience: specification analysts, product owners, domain experts, safety engineers, engineers (who implement), and non-engineers (who review and approve).*

---

## What is Stage 2 — Specify Behaviorally?

Stage 2 translates the agent product brief (Stage 1) into a behavioral specification that engineers can implement and evaluators can test. It extends the companion RE framework from the component level to the product level. The behavioral specification is the authoritative reference for all subsequent stages — evaluation (Stage 3) tests against it, release (Stage 4) is gated on it, drift detection (Stage 5) is measured against it, recalibration (Stage 6) restores it. A behavioral specification is not a design document or an intent statement. It is a contract: between the product and its users, between the deploying organisation and regulators, and between the specification analyst and the engineers who will implement it. Every behavioral claim in this document must be verifiable, and every verifiable claim must have a corresponding evaluation defined before Stage 3 begins.

---

## Relationship to the RE Framework

The companion RE framework (`companion-re-framework.md`) provides the vocabulary and technical specification structures that this document depends on: behavioral envelopes, probabilistic assurance targets, hard requirements versus performance targets, the single-source principle, tiered lifecycle governance, and the two-axes classification matrix. Readers who have not read the RE framework should do so before working with this document. What follows is a reference to the key structures this document extends, not a re-derivation of them.

The RE framework was written for the engineering component level: how to specify an individual agent component, how to structure its behavioral envelope, how to assign its autonomy tier. Stage 2 of the APLC applies all of that at the product level — the level of the agent as a deployed product interacting with real users in a real operational context.

The critical addition this document makes to the RE framework is directional: the business purpose, user model, and trust architecture from Stage 1 (`agent-conception.md`) are not background context for the behavioral specification. They are its primary inputs. Every section of the behavioral specification is shaped by them:

- The hard boundaries in the behavioral envelope are derived from the permission model in the trust architecture, from the out-of-scope statements in the product brief, and from the regulatory classification.
- The performance targets are derived from the success criteria in the product brief — they are the measurable proxies for business success, not independent technical targets.
- The use-case coverage map is derived from the user model: the user's relationship type, trust scope, and vulnerability determine which edge cases are safety-relevant and which are merely inconvenient.
- The uncertainty protocol is constrained by the persona design: if the persona commits to authoritative answers, the specification must address how that commitment is honoured when the agent genuinely cannot provide one.
- The escalation design is constrained by the trust architecture: escalation paths must be consistent with the principal hierarchy.

An engineering RE spec written without the agent product brief as input will be technically correct but product-wrong. It will specify an agent that behaves consistently with its own internal logic while being inconsistent with its product purpose, its user relationship, and its regulatory obligations. The behavioral specification's authority comes from the chain that connects it to Stage 1: every requirement in this document must trace to a decision made in the product brief.

The RE framework's single-source principle applies here at the product level: this document is the canonical source for all downstream projections — agent-consumable behavioral contracts, evaluation suite definitions, compliance documentation, and operational monitoring specifications. No projection may be authored independently. When this document changes, all projections must be re-derived.

---

## The Behavioral Envelope (Product Level)

The RE framework defines four behavioral envelope layers for agent components. This section applies those layers at the product level — not to describe what a component does, but to define what the agent product as a whole will and will not do in interaction with real users.

The product-level behavioral envelope is the primary specification artifact for Stage 2. It is the reference against which evaluation is designed, release is gated, and drift is measured. Specify it with enough precision that a domain expert who has not read any other document could determine, for any described agent behavior, whether it is within or outside the envelope.

### Layer 1: Hard Boundaries

Hard boundaries define what the agent never does regardless of instruction, context, or principal. These are non-negotiable product constraints, not engineering guardrails. They are not aspirational. They are the behaviors for which the answer is always no, regardless of who is asking, what the framing is, or how compelling the apparent justification.

Hard boundaries at the product level derive from three sources:

**Trust architecture hard limits** from Stage 1: the permission model's hard limits map directly to Layer 1. If the permission model states that no principal can instruct the agent to exfiltrate data from the system context, that is a Layer 1 hard boundary. Every hard limit in the permission model must appear as a Layer 1 hard boundary here.

**Regulatory prohibitions**: for EU-deployed systems, Article 5 prohibited practices that the product brief confirmed do not apply to the current product but could apply to adjacent behaviors must be bounded here. The hard boundary against manipulative techniques that impair free decision-making, for example, applies regardless of operator configuration.

**Product-level exclusions**: the out-of-scope statements from the product brief that represent design decisions rather than limitations. These must be expressed precisely enough that a user interacting with the agent would recognize them as consistent and predictable. "This agent does not provide legal advice" is a product-level hard boundary if the out-of-scope statement in Stage 1 was specific: "This agent does not interpret contractual obligations, assess litigation risk, or recommend legal action, regardless of user request or operator configuration."

Hard boundaries must be enforced by infrastructure policy, not by prompt instruction. A hard boundary implemented only as a prompt instruction is a soft boundary in practice: it can be overridden by prompt injection, instruction conflict, or context manipulation. For each hard boundary, the behavioral specification must specify the enforcement mechanism: tool removal, permission policy, output filtering, or a combination. See the RE framework's Section 3 for the correct requirement type and Section 7 (security NFR) for the threat model that motivates infrastructure enforcement.

**What "infrastructure enforcement" means technically.** The following mechanisms qualify as infrastructure enforcement; implementations must use at least one of these per hard boundary, and must document which mechanism enforces each boundary in the behavioral specification:

- *Output filtering layer.* A post-generation classifier or rule-based filter that intercepts agent responses before they reach the user and blocks or transforms responses that violate the hard boundary, independent of the model's own refusal behavior. The filter must be maintained and versioned separately from the system prompt.
- *Tool permission ACL.* A permission policy enforced at the tool invocation layer that prevents the agent from invoking tools or accessing resources that would enable the prohibited behavior, regardless of what the model requests. Permission policies are enforced by the tool orchestration infrastructure, not by prompt instruction to the model.
- *Sandboxed execution environment.* An execution environment in which the agent has structural inability to take the prohibited action — the capability does not exist in the execution context. For example, an agent that must never write to a production database cannot be given write credentials; the architectural separation is the enforcement mechanism.
- *Middleware interception.* A middleware layer that validates every agent action against the hard boundary list before execution, rejecting non-compliant actions with an error that triggers the agent's escalation protocol.

A hard boundary implemented exclusively as a system prompt instruction ("you must never do X") is a soft boundary in practice, regardless of language strength. Prompt instructions are overridable by sufficient adversarial pressure, context manipulation, and model updates. For each hard boundary in the specification, the enforcement mechanism must be named, and "system prompt" is not an acceptable answer. Where no technical enforcement mechanism is available for a hard boundary, the boundary must either be elevated to a product architectural requirement (removing the capability entirely) or re-classified as a soft boundary with documented rationale and the compensating controls that substitute for infrastructure enforcement.

**Tier 4 systems — policy envelope as Layer 1 boundary:** For Tier 4 agent products, the policy envelope boundary defined in the Stage 1 trust architecture is a Layer 1 hard boundary. Any agent action that would take the system outside the approved policy envelope is a hard boundary violation — even if the action would otherwise be within the behavioral specification and within the agent's technical capability. The policy envelope's outer constraints must appear explicitly in Layer 1 alongside all other hard boundaries, with the same enforcement requirement: machine-enforced, not prompt-instructed. A Layer 1 entry of the form "The agent must not take actions outside the approved policy envelope [reference: Stage 1 Trust Architecture, Policy Envelope section]" is required for every Tier 4 behavioral specification. The policy envelope as documented in Stage 1 is the authoritative definition — this Layer 1 entry is a reference and enforcement hook, not a re-specification.

### Layer 2: Soft Boundaries

Soft boundaries define what the agent does by default but which can be adjusted through operator configuration. They represent the product's default behavior within its intended operational context — behaviors that are appropriate for most deployments but which legitimate operator customization may need to modify.

The canonical format for a soft boundary in this document is:

> By default, the agent [default behavior]. Operators may configure the agent to [alternative behavior] instead. Users cannot adjust this setting.

Or, for the inverse:

> By default, the agent does not [behavior]. Operators may configure the agent to [behavior] for [defined context]. Users cannot adjust this setting.

Examples of soft boundaries that must be specified for most product deployments: default language and locale behavior (can operators configure multi-language?); default response length and detail level (can operators configure verbosity for professional versus consumer contexts?); default escalation thresholds (can operators lower the threshold for their higher-risk user population?); default confidence disclosure (can operators suppress uncertainty language for contexts where it would confuse rather than inform?).

Each soft boundary specification must identify: the default, the configurable alternative, who can configure it (operator only, or also some users?), and the hard limit that bounds the configuration space (because even operator-configurable soft boundaries have outer limits that are Layer 1 hard boundaries).

**Tier 4 systems — envelope drift as Layer 2 boundary:** For Tier 4 agent products, the policy envelope recalibration trigger conditions must be specified as a Layer 2 soft boundary. The specification must define: under what conditions does observed envelope drift require a return to Stage 4 for envelope re-approval? The default trigger is: when the agent has operated near any envelope boundary — taking actions within a defined proximity of the blast radius ceiling, or approaching the limits of allowed change classes — at a frequency that exceeds a specified threshold over a trailing observation window, the condition is flagged for envelope review. Operators may configure tighter trigger thresholds than the default; they may not configure looser ones without a corresponding Stage 4 re-approval of the relaxed trigger. The recalibration trigger condition follows the canonical soft boundary format: by default, the agent triggers an envelope review when [default threshold conditions]. Operators may configure the agent to trigger review at more sensitive thresholds. Operators may not configure the agent to trigger review at less sensitive thresholds than the default without Stage 4 envelope re-approval.

### Layer 3: Performance Targets

Performance targets are the probabilistic assurance targets for the agent product's output quality dimensions. Use the RE framework's format: "The agent shall achieve [metric] of [value] across [evaluation distribution] with [confidence level]." These are not testing thresholds — they are product commitments that must hold in production, with evaluation (Stage 3) providing the pre-release evidence that they can be met.

Performance targets at the product level must cover at minimum:

**Task success rate**: the proportion of user interactions in which the agent successfully completed its intended task, as defined by the success criteria in Stage 1. The evaluation distribution must represent the actual user population, not a clean test set constructed to be easier than real use.

**Response quality score**: a human-evaluated score measuring output quality against the product's quality definition. "Human-evaluated" is not optional for this metric at the product level. Automated proxy metrics (BLEU, ROUGE, embedding similarity) may supplement human evaluation but do not replace it for a metric that will be used in release decisions. Specify: the quality rubric, the evaluator profile (domain expert? typical user?), the scale, and the minimum acceptable score.

**Behavioral consistency rate**: the proportion of functionally equivalent inputs across the evaluation distribution that produce responses consistent with the behavioral envelope. This metric detects the failure mode where the agent behaves correctly in most cases but inconsistently at the boundaries — which is the failure mode that erodes user trust fastest.

**Escalation rate**: the proportion of interactions that trigger escalation. This is both a performance target (too low means the agent is handling cases it should not; too high means the escalation design is misconfigured) and an operational metric (escalation rate in production is a leading indicator of behavioral drift or distribution shift). State both the target rate and the acceptable band.

**Cost envelope.** The behavioral specification must define the cost envelope for the agent product as a required Layer 3 performance target alongside behavioral quality targets. The cost envelope is not optional — it is the economic expression of the product's performance requirements. Required fields:

- *Maximum cost per successful interaction:* the total cost ceiling (foundation model inference + knowledge base retrieval + tool API calls + HITL review allocation) per interaction that achieves a successful outcome, denominated in USD or the organization's accounting currency. Expressed as a hard ceiling, not a target.
- *Maximum monthly operating cost:* the total product operating cost ceiling per calendar month at the specified interaction volume. This is the Business Owner's economic commitment; it must be signed by the Business Owner at the Behavioral Specification Gate, not at the Operational Readiness Gate.
- *HITL cost ratio target:* the expected proportion of total operating cost attributable to human review, expressed as a range (minimum: human oversight design requirement; maximum: acceptable overhead). Both bounds must be specified — a ratio below the minimum indicates under-escalation; a ratio above the maximum indicates escalation logic failure or autonomy tier misconfiguration.
- *FinOps drift alert threshold:* the percentage above the cost envelope baseline at which a cost anomaly alert fires. Default: 20%. The threshold must be pre-committed before production; a threshold set after the first cost anomaly is rationalization, not governance.

A behavioral specification without a cost envelope is incomplete at Layer 3. The Stage 4 Operational Readiness Gate requires a signed cost envelope filed before deployment.

Additional performance targets are required for high-risk EU AI Act systems: accuracy across defined demographic subgroups (Article 10 data governance and Article 15 accuracy requirements), robustness under distribution shift, and response latency at p50/p95 under expected production load.

### Layer 4: Adaptation Scope

Adaptation scope defines what the agent is permitted to learn or change from interactions, and what it cannot. An agent with unspecified adaptation scope is an agent that may be learning the wrong lesson from a manipulative interaction — which is a safety risk that does not become visible until the learned behavior propagates.

Specify adaptation scope by answering three questions for each type of state the agent can accumulate:

**What can the agent update from interaction?** Few-shot history in context, RAG knowledge base entries, long-term memory writes, fine-tuning data selection. For each type, specify the conditions under which updates are permitted (e.g., "RAG knowledge base entries may be updated from operator-sourced documents through the document ingestion pipeline; user inputs do not update the knowledge base").

**What triggers a revalidation cycle?** If the agent's retrieved knowledge, in-context history, or long-term memory changes substantially, when does that change trigger a return to Stage 2 for re-specification? For fine-tuning or substantial knowledge base updates, re-specification and re-evaluation are required. For per-session context accumulation that does not persist beyond the session, they may not be. Specify the threshold.

**How is learned state governed and audited?** What provenance information is recorded for knowledge base entries? Who can write to persistent memory and under what conditions? What is the retention and expiry policy? How can learned state be rolled back if behavioral drift is detected in Stage 5?

**What cross-session access policy governs the agent's memory?** The behavioral specification must explicitly state whether the same user in session N+1 may access and benefit from memory accumulated in session N of that user. This is not a default — it must be a deliberate design decision with documented rationale. Four configurations must be covered:

*User-scoped persistent memory:* the agent retains memory from prior sessions and uses it to personalize subsequent sessions for the same user. This is the default assumption in most deployments; it must be explicitly specified, not assumed. Specify: what memory categories persist (e.g., user preferences may persist; specific interaction content may not); the maximum retention period; and the GDPR Article 7 lawful basis for this persistence (typically consent or legitimate interest with a proportionality analysis).

*Session-isolated memory:* the agent resets to its initial state at the start of every session, regardless of prior interactions with the same user. This is the most conservative option and requires no cross-session governance. Specify: what constitutes "session start" and "session end"; whether any state (e.g., authentication context) persists between sessions as an exception.

*Opt-in persistent memory:* the agent retains memory only for users who have explicitly opted in. Specify: the opt-in mechanism and how it is reflected in the agent's behavioral context; what happens to memory accumulated before opt-out is exercised (treated as a GDPR erasure trigger).

*Tiered memory:* different memory categories have different cross-session policies. Specify: the cross-session policy for each memory category defined in the memory schema.

Cross-session memory sharing between different users — where one user's sessions influence the agent's behavior in another user's sessions — is prohibited unless explicitly authorized in the behavioral specification's Layer 4 adaptation scope with full privacy impact assessment. This prohibition applies to both direct memory sharing and to aggregate pattern learning that is derived from multiple users' sessions without appropriate anonymization governance.

The RE framework's Layer 4 (adaptation envelope) applies at the component level; this section applies it at the product level, which means the adaptation scope must also account for the user relationship established in Stage 1: an agent in an advisory relationship with potentially vulnerable users has a narrower permissible adaptation scope than an internal tooling agent.

**Tier 4 systems — envelope drift as an adaptation phenomenon:** For Tier 4 agent products, envelope drift is a form of adaptation that must be explicitly governed in Layer 4. If the agent consistently operates near envelope boundaries — taking actions at or approaching the blast radius ceiling, or repeatedly selecting action classes near the edges of the allowed change classes — the effective policy envelope has shifted in practice even if the approved envelope has not changed. The behavioral specification must address three questions for Tier 4 systems:

How is envelope boundary approach frequency tracked? The specification must define the metric (e.g., "proportion of actions within the trailing N-action window whose blast radius exceeded X% of the ceiling"), the observation window, and the logging requirement that makes the metric computable.

What threshold triggers an envelope review? Specify the numeric threshold at which boundary approach frequency requires escalation to a human steward for envelope review. This threshold feeds directly into the Layer 2 recalibration trigger condition — they must be consistent.

Can the agent adapt its behavior autonomously in response to approaching boundaries? No. Boundary approach must trigger human review, not autonomous behavioral adjustment. An agent that self-modifies its action selection strategy in response to approaching the envelope boundary has effectively modified the policy envelope without approval — which is a Layer 1 violation. The Layer 4 specification must state this explicitly: if boundary approach frequency exceeds the threshold, the agent notifies the human steward and awaits instruction; it does not autonomously alter its selection criteria to move away from the boundary.

### Layer 5: Conversation-Level Behavioral Invariants

Conversation-level behavioral invariants are behavioral properties that must hold across a multi-turn conversation, not just within a single response. They are not a fifth layer of the behavioral envelope in the sense that they constrain individual responses — they constrain response sequences. A product whose single-response behavioral envelope is fully specified but whose conversation-level invariants are undefined is underspecified: an adversary can exploit the conversation dimension to achieve outcomes that no single response would permit.

**Required invariant categories for all agent products with multi-turn capability:**

*Escalation persistence.* Once a hard boundary or escalation trigger has been reached in a conversation, subsequent turns in the same conversation may not de-escalate the decision without explicit human authorization. An agent that escalates a conversation to a human review queue in turn 3 must not resume autonomous operation in turn 5 of the same conversation unless the human reviewer has explicitly closed the escalation.

*Constraint stability under pressure.* The agent's stated limitations and behavioral constraints must not weaken over the course of a conversation in response to user pressure, repeated requests, or incremental reframing. The behavioral specification must state explicitly: "The agent's Layer 1 hard boundaries are not subject to negotiation in conversation; repeated requests for boundary-violating behavior must be declined with consistent responses rather than progressively weakened ones."

*Persona coherence over conversation length.* The agent's persona, voice, and stated identity must remain consistent from the first turn to the last. The behavioral specification must specify what the agent does when it detects that its conversation-level persona coherence is under threat — the escalation design must include persona integrity as an escalation trigger for conversations that have exceeded a defined length while maintaining adversarial pressure.

*Memory boundary at conversation end.* What state, if any, persists from the conversation to future conversations must be specified. The specification must state explicitly which conversation elements the agent is permitted to retain in persistent memory and which must be dropped at conversation end.

**Specification format.** Conversation-level invariants are specified alongside the hard boundaries in Layer 1, with the annotation `scope: conversation` to distinguish them from per-response hard boundaries. They are evaluated in Stage 3 using multi-turn evaluation sequences, not single-turn test cases.

---

## Use-Case Coverage Map

The use-case coverage map is a structured analysis of the input space. Its purpose is to ensure that the behavioral specification covers not just the cases the product was designed for, but the full range of inputs the agent will encounter in production — including the inputs it was not designed for but will receive anyway.

The map has five zones. Each zone requires a different specification approach.

### Core Use Cases

Core use cases are the primary situations the agent was designed for. They correspond directly to the business purpose stated in Stage 1. For each core use case, the behavioral specification must define:

**Trigger conditions**: what input characteristics identify this as a core use case?

**Expected behavior**: what does the agent do? Stated at the level of behavioral description, not implementation steps.

**Acceptance criteria**: the measurable criteria against which a specific interaction in this use case would be judged successful. These are the unit-level acceptance criteria from which the product-level performance targets (Layer 3) are derived. They must be consistent with the success criteria defined in Stage 1.

**Domain-specific constraints**: constraints on behavior within this use case that derive from the user model or trust architecture — not general constraints that apply everywhere, but constraints specific to what this use case involves.

Core use cases must be specified completely enough that a specification analyst who has not worked with this product before could write a first-draft evaluation case for each one. If a core use case cannot be specified to that level of precision, it belongs in the product brief revision queue, not in the behavioral specification.

### Edge Cases

Edge cases are legitimate inputs within the agent's purpose that are unusual, infrequent, or require more nuanced handling than core use cases. They are not adversarial; the user asking them has a genuine need. They are "edge" because they push toward the limits of the agent's designed capability.

For each identified edge case category, the behavioral specification must define: how the agent recognizes it, the behavioral requirement for handling it (which may include declining gracefully and escalating rather than attempting a low-quality answer), and the performance target for this category (which may differ from the overall performance target if the edge case population is harder).

Edge cases that the product team cannot specify handling for are candidates for Layer 2 soft boundaries: they may require operator-specific configuration to handle correctly, which means the default behavior must be defined and the configurable extension must be bounded.

### Boundary Cases

Boundary cases are inputs at or near the edge of the behavioral envelope — inputs where the agent's correct response is to do something rather than nothing, but where the full scope of the request cannot or should not be fulfilled. These are the cases where the behavioral specification's precision matters most, because the agent's behavior in boundary cases is where the trust architecture and the persona design are most visibly tested.

For each identified boundary case category, specify: what triggers boundary recognition, what the agent does (partial fulfillment? referral? explicit scoping?), and what language the agent uses when operating at the boundary. This last requirement connects to the persona design established in Stage 1: the language the agent uses when it reaches its limits must be consistent with its persona and must have been approved as part of the persona design.

Boundary cases require human review during Stage 3 evaluation. Automated evaluation of boundary behavior is insufficient because boundary behavior requires judgment about whether the agent's response is appropriate in context — a judgment that requires a human evaluator with domain knowledge.

### Out-of-Scope Inputs

Out-of-scope inputs are requests the agent was designed not to fulfill. They are not edge cases or boundary cases — they are categorically outside the product's scope, as defined by the out-of-scope statements in Stage 1. The behavioral requirement for out-of-scope inputs is: decline gracefully, without being unhelpful.

"Without being unhelpful" is a design constraint, not an aspiration. An agent that responds to out-of-scope inputs with "I can't help with that" is technically compliant with the out-of-scope boundary but has failed the product design requirement to be useful at the boundary. The behavioral specification must define the decline response pattern: does the agent explain why it cannot help? Does it redirect to an alternative resource? Does it offer what it can do instead?

The decline response pattern must be specified for each out-of-scope category, not as a single generic response. A user asking a claims processing agent for investment advice needs a different response than a user asking the same agent to help them commit fraud. Both are out-of-scope. Both require graceful decline. The responses are not the same.

### Adversarial Inputs

Adversarial inputs are covered by the red-team protocol in Stage 3 evaluation (`agent-behavioral-evaluation.md`). The behavioral requirement stated here is a hard boundary, not a performance target: the agent must maintain behavioral envelope integrity under adversarial inputs.

This means: the agent's Layer 1 hard boundaries must hold under prompt injection attacks delivered through user inputs, tool responses, or retrieved content. The agent's persona must not be overridden by sufficiently persistent adversarial prompting. The agent's trust architecture must not be subverted by instructions that claim false authority. "Maintain behavioral envelope integrity" is not a probabilistic target. It is an absolute requirement enforced by infrastructure policy — prompt-level defenses are supplementary, not primary.

The Stage 3 red-team protocol will test this requirement. The behavioral specification's role is to state the requirement clearly enough that the Stage 3 protocol knows what failure looks like: any response that violates a Layer 1 hard boundary, regardless of the input that produced it, is a failure. Any response that adopts a persona inconsistent with the designed persona as a result of adversarial pressure is a failure. Any response that acts on an instruction from a source claiming authority it was not assigned in the trust architecture is a failure.

---

## Uncertainty Protocol

Three decisions define the agent's uncertainty protocol. Each must be made explicitly in the behavioral specification, because each has direct consequences for user safety and product trust. An agent whose uncertainty protocol is left to model defaults will express uncertainty inconsistently, and inconsistent uncertainty expression is the behavioral correlate of inconsistent reliability.

### When to Express Uncertainty

The agent must signal uncertainty when the confidence level of its response falls below a defined threshold. The threshold must be specified. "Low confidence" is not a specification — a numeric threshold or a defined categorical trigger is.

The specification must define: the confidence signal (model-internal probability? a classification applied to the output? a domain-specific detection rule?), the threshold below which uncertainty is expressed, and the language the agent uses to express it. The uncertainty language must be consistent with the persona design: a formal professional persona uses different language than a conversational consumer persona, but both must express genuine uncertainty clearly enough that a user can act on the signal.

An agent that never expresses uncertainty will hallucinate with confidence. This is not a behavioral failure that evaluation will catch easily, because the hallucination by definition produces outputs that look plausible. It is a specification failure: the uncertainty protocol was not specified, so the agent was never constrained to behave honestly about its limits.

For agents in regulated domains where outputs may influence consequential decisions — financial, medical, legal — the uncertainty expression requirement is elevated. The behavioral specification must state that confidence-qualified outputs be labeled as such, that outputs below a defined threshold must include a recommendation to seek authoritative confirmation, and that the agent must not present uncertain outputs as definitive without explicit confidence qualification.

### When to Ask for Clarification

The agent should ask for clarification when the input is ambiguous in a way that matters — when different interpretations would produce substantially different responses, and where asking is likely to produce information that resolves the ambiguity efficiently. The behavioral specification must define this precisely, because the calibration of clarification requests is a direct user experience and trust factor.

Agents that ask clarifying questions for every ambiguous input are annoying and lose user trust through perceived incompetence. Agents that never ask clarifying questions when they should appear to guess at intent, which produces confident but wrong responses and erodes user trust differently. The behavioral specification must define:

The conditions under which clarification is required (not just permitted): ambiguity that would result in a response that could be harmful in one interpretation, ambiguity that would result in substantially different outputs with different risk profiles, or ambiguity that the agent cannot resolve from context.

The conditions under which clarification is not required: the agent must make a reasonable interpretation and proceed, not ask, when the cost of asking exceeds the cost of a slightly imprecise response, or when the context provides enough signal to make a reasonable determination.

The maximum number of clarifying questions per interaction (a specific number, not "keep it reasonable"), and what the agent does if clarification attempts do not resolve the ambiguity.

**Tier 4 systems — halt-and-notify instead of escalation:** For Tier 4 agent products, the standard uncertainty-triggered escalation pattern changes because there may be no human reviewing individual interactions. When uncertainty would trigger an escalation in a Tier 3 system, in a Tier 4 system the agent must instead halt and notify: the agent stops the current action sequence, records the halt condition with full context, and notifies the designated human steward. It does not proceed on the basis of a conservative default action, because in autonomous operation there may be no conservative default that remains within the approved policy envelope when the agent is uncertain about which actions are within it. The behavioral specification must define the halt-and-notify protocol: what information is included in the notification, who is notified, within what latency, and what the agent's state is while awaiting response (fully halted, or continuing with strictly in-envelope actions only). The notification must include sufficient context for the human steward to determine whether to approve continuation, modify the policy envelope, or abort the current task.

### When to Escalate or Refuse

Escalation and refusal are distinct behaviors with different implications. Escalation means transferring the interaction to a human, another system, or a deferred queue — the user's need is legitimate but the agent cannot serve it alone. Refusal means declining to proceed — the request is out of scope, unsafe, or contrary to the behavioral envelope.

The behavioral specification must define both sets of conditions precisely. The escalation conditions connect to the escalation design below; they must be consistent with it. The refusal conditions connect to the hard boundaries and the out-of-scope definitions above; they must be consistent with them. What the specification adds here is the decision procedure: given a specific input, how does the agent determine whether to escalate or refuse?

For inputs that could be either boundary cases (legitimate but difficult) or out-of-scope inputs (not legitimately within scope), the decision procedure must specify which signals the agent uses to distinguish them. A user asking a legal information agent to "explain whether I have a strong case" may be asking for general information (boundary case: close to scope, can serve with qualification) or seeking a legal opinion (out-of-scope: must decline and redirect). The behavioral specification must specify the distinguishing signals and the response for each outcome.

---

## Escalation Design

Escalation is a product design decision, not an engineering parameter. The escalation design must be reviewed and approved by the product owner and risk stakeholders before Stage 3 begins, because escalation paths involve operational processes, staffing assumptions, and SLA commitments that are outside engineering scope.

Three dimensions must be specified for each escalation category.

### Escalation Triggers

Define what causes the agent to escalate. There are four primary trigger categories:

**Uncertainty threshold**: the agent's confidence falls below the threshold defined in the uncertainty protocol, and the interaction involves a consequential decision or a domain where low-confidence responses carry safety risk.

**User request**: the user explicitly requests a human. This is always an escalation trigger, regardless of whether the agent believes it can serve the request. A user who asks to speak to a human must be able to do so.

**Sensitive content detection**: the interaction touches content categories that require human review regardless of the agent's technical ability to respond — suicide and self-harm content, content indicating potential fraud or abuse, content that suggests the user is in immediate danger. These triggers must be defined before Stage 2 is complete because they require consultation with safety and risk stakeholders who may not be part of the engineering team.

**Blast-radius threshold**: the user is requesting an action whose consequence, if incorrect, exceeds the blast radius established for this agent's autonomy tier. For Tier 3 agents (production-impacting, per the RE framework's Section 6), this trigger must be specified as a hard boundary: actions above the blast-radius threshold require explicit human approval before execution, not just human notification.

### Escalation Path

For each trigger category, specify where the case goes. Four path types exist and may be combined:

**Human queue**: the interaction is transferred to a human agent queue, the user is informed of the transfer and the expected wait time, and the agent provides a summary of the interaction context to the human agent.

**Email notification**: the case is flagged for asynchronous human review, the interaction continues with the agent, and the reviewer's findings may update the agent's future behavior if they identify a specification gap.

**Synchronous transfer**: the interaction pauses and awaits human pickup before continuing. This path requires specification of the maximum wait time before the agent informs the user of delay and offers an alternative.

**Asynchronous review**: the interaction completes with the agent, and the case is queued for post-hoc human review. This path is appropriate for quality monitoring but not for safety-critical triggers, where human review must occur before the interaction concludes or before any consequential action is taken.

### Escalation Latency

Specify how long the agent waits for a human response before taking a decision. Three outcomes must be specified for each escalation path: how long the agent waits, what it does if the human responds within that window, and what it does if the human does not.

The not-responded case must be specified. An agent that escalates to a human queue and then waits indefinitely has transferred the latency risk to the user. The behavioral specification must define: the maximum wait time, whether the agent informs the user of the delay and at what interval, and whether the agent can proceed with a conservative default action or must defer entirely until human response.

For high-risk EU AI Act systems, escalation to human oversight is not optional for specified trigger categories (Article 14). The escalation latency specification must satisfy the Act's human oversight requirements: the oversight mechanism must be technically effective, not nominally present. A human who is notified but cannot practically review and respond within the specified latency window is not providing oversight — they are providing cover.

**Tier 4 systems — policy-envelope halt condition:** For Tier 4 agent products, the escalation design must specify the policy-envelope halt condition as a named escalation category. The policy-envelope halt condition is: the agent determines that it cannot proceed with the current task within the approved policy envelope without exceeding a boundary. This is distinct from uncertainty about the correct action — it is a determination that any available action that would advance the task would violate the policy envelope. When this condition is reached, the agent halts autonomous operation and notifies the human steward. The escalation design must specify for this category: the trigger (agent cannot identify any in-envelope action path to task completion), the path (halt-and-notify to the named human steward, not to a general human queue), the notification content (current task state, the envelope boundary that cannot be cleared, and the agent's assessment of what policy-envelope change would enable continuation), and the latency (maximum time the agent waits before declaring the task abandoned and recording a halt record). The policy-envelope halt is not a failure — it is the correct behavior. A Tier 4 agent that proceeds past envelope boundaries rather than halting has failed; a Tier 4 agent that halts and notifies rather than exceeding its mandate has succeeded.

---

## Safety and Alignment Requirements

Safety and alignment requirements constrain the behavioral space regardless of task performance. An agent that achieves excellent task success rates while failing these requirements is not a successful product — it is a liability. These requirements are specified here, not derived from the behavioral envelope, because they apply across all use-case categories and all interaction types.

### Harmful Content Prevention

Define the categories of harmful content the agent must never produce, regardless of user request, operator configuration, or apparent justification. The categories must be specific. "Harmful content" is not a specification; it is a category label that defers the hard decisions.

Categories for most deployed agents include at minimum: content that facilitates violence or illegal activities, content that facilitates harassment or abuse of identified individuals, content that sexualises minors, content that is deceptive about the agent's nature or the deploying organisation's practices, and content that constitutes medical or legal advice beyond the agent's stated scope without appropriate qualification and referral.

For agents in regulated domains, the categories extend: financial agents must not produce content that constitutes investment advice without appropriate regulatory authorization and disclosure; healthcare agents must not produce content that could be interpreted as diagnosis or treatment recommendation without appropriate qualification; legal information agents must not produce content that could be interpreted as legal advice.

Each category must map to a Layer 1 hard boundary in the behavioral envelope and to an infrastructure enforcement mechanism. A category stated here without a corresponding hard boundary and enforcement mechanism is aspiration, not specification.

### Fairness and Bias Requirements

Define the group-based biases the agent must avoid, with specific requirements for demographic groups relevant to the user population. For EU high-risk AI systems, Article 10 of the AI Act requires data governance measures that address biases in training and evaluation data. The fairness requirements in this section are the behavioral specification correlate of those data governance obligations.

Fairness requirements must specify: the protected characteristics to be addressed (the EU AI Act's non-discrimination basis covers race, ethnicity, sex, age, disability, religion, and sexual orientation, among others), the behavioral requirement for each (equal task success rate across groups? absence of systematic output quality differences?), the evaluation methodology (how will bias be measured in Stage 3?), and the threshold below which a bias finding blocks release.

Stating "the agent must not be biased" is not a fairness requirement. "The agent's task success rate across protected demographic groups, as measured against the evaluation distribution specified in the Stage 3 evaluation plan, must not differ by more than five percentage points between any two groups at the 90% confidence level" is a fairness requirement.

### Privacy Requirements

Define the personal data the agent must not surface, retain, or act on without authorization. This section maps to the RE framework's privacy NFR (Section 7) at the product level.

Privacy requirements in the behavioral specification must address four dimensions: what personal data the agent may access from its context window (the data explicitly provided to it), what personal data it may retrieve from connected data sources, what personal data it may retain in memory beyond the interaction, and what personal data it may surface in its outputs.

For each dimension, the requirement must be specific: not "the agent must not misuse personal data" but "the agent must not include personal financial data beyond [specific fields] in its outputs; must not retrieve data from the customer record beyond [specific fields] for any single interaction; must not write customer identifiers to long-term memory." These requirements derive directly from the trust architecture's permission model and from the data governance requirements in the Stage 1 regulatory classification.

For EU high-risk systems, the privacy requirements must be consistent with the GDPR and with the AI Act's Article 10 data governance obligations. The behavioral specification is not the place to conduct a GDPR compliance analysis — that belongs in the legal review. The behavioral specification's role is to translate the legal obligations into behavioral requirements the engineering team can implement and Stage 3 can evaluate.

**Special category data protocol.** Agents deployed in contexts where users may disclose special category data — health information, data revealing political opinions, religious or philosophical beliefs, trade union membership, genetic or biometric data, data concerning sex life or sexual orientation — must address the following in the behavioral specification:

*Authorization status.* State explicitly whether the agent is authorized to process special category data, and if so, the Article 9 lawful basis (explicit consent per Article 9(2)(a), employment law per 9(2)(b), vital interests per 9(2)(c), etc.). "Not authorized" is a valid answer and generates a hard boundary.

*Behavioral hard boundary against elicitation.* If the agent is not authorized for a category, the specification must define a hard boundary prohibiting: (a) prompts or conversation patterns designed to elicit special category data from the user; (b) retention of any special category data disclosed beyond the immediate interaction; (c) acting on special category data in a way that changes the agent's recommendations, decisions, or outputs. The hard boundary must specify the enforcement mechanism (output filter, context window sanitization, or both).

*DPIA requirement.* Processing operations involving special category data that are "likely to result in a high risk" require a Data Protection Impact Assessment (DPIA) under GDPR Article 35. The DPIA completion status is a Conception Gate condition for agents where special category data exposure is reasonably foreseeable. A deployed agent that processes special category data without a completed DPIA is in regulatory non-compliance from its first production interaction.

*Detection and response.* The behavioral specification must define what the agent does when special category data is disclosed beyond the authorized scope: graceful acknowledgment without retention, immediate context sanitization, and (where required by the DPIA) a notification to the data controller.

### Explainability Requirements (EU AI Act Article 86)

For agent products deployed in EU high-risk contexts where the agent makes or substantially influences decisions about individuals (as defined by Article 6 and Annex III of the EU AI Act), Article 86 grants affected persons the right to receive a meaningful explanation of the decision. This right has direct behavioral specification implications that must be addressed at Stage 2, not deferred to Stage 4 documentation.

**Explainability as a Layer 1 hard boundary.** The agent must be capable of producing, for any decision subject to Article 86, a human-readable explanation of: (1) the principal factors that led to the decision; (2) the data inputs that were most influential; and (3) the behavioral specification clauses that governed the decision. This capability is not optional for high-risk systems — it is an Article 86 compliance requirement and must be specified as a Layer 1 hard boundary: "The agent must not produce a decision affecting an individual without also producing an explanation that satisfies the Article 86 standard."

**Specification requirements.** The behavioral specification must define: the explanation format (the structure, fields, and level of detail required to satisfy the "meaningful" standard for this deployment context); the trigger conditions for explanation generation (any decision subject to Article 86 generates an explanation automatically, not only when requested); the storage and retrieval mechanism (explanations must be stored and retrievable by the data subject for the retention period applicable to the decision); and the escalation path for cases where an explanation cannot be generated (the agent must escalate to human review rather than issue a decision without an explanation).

**Evaluation requirement.** Layer 3 evaluation must include adversarial test cases where a decision is made without a retrievable explanation — the red-team tests whether the explanation generation can be bypassed. Layer 4 human evaluation must assess whether the explanations produced are "meaningful" against the Article 86 standard for a sample of decisions in the product's use case.

This requirement applies in addition to, not instead of, the GDPR Article 22 automated decision-making requirements specified elsewhere in the APLC. Both sets of rights may be asserted simultaneously for the same decision.

### Alignment Requirements

Alignment requirements address whether the agent's behavior remains consistent with its stated purpose under conditions that may create pressure to diverge — distribution shift, edge cases not anticipated in Stage 1, adversarial use, or optimization dynamics that favor engagement metrics over user welfare.

Three alignment requirements apply to all deployed agents:

**Stated purpose consistency**: the agent's behavior at the boundary of its scope must be consistent with its stated purpose, not with what produces the most engagement or the most superficially satisfying response. An advisory agent whose responses become subtly directive under distribution shift (because directive responses correlate with user engagement in training data) has drifted from its stated purpose. The behavioral specification must state this as a requirement, and Stage 5 operational monitoring must detect it.

**User welfare over engagement**: where the agent has any optimization signal from interaction (implicit feedback, engagement metrics, session length), the behavioral specification must state that user welfare, as defined by the product brief's user model, is the primary optimization target. Engagement metrics are monitored as operational indicators, not as behavioral objectives. This requirement is particularly important for agents in consumer contexts where engagement optimization can diverge from user welfare in non-obvious ways.

**Distribution shift stability**: the agent's behavioral envelope must be maintained under distribution shift. When the production input distribution shifts from the specification-time training distribution, the agent must maintain its hard boundaries and escalate to a human rather than adapt its behavior outside the specification. Distribution shift that causes behavioral drift is detected by Stage 5 monitoring and triggers a Stage 6 recalibration cycle — it is not handled by the agent autonomously.

### Secrets and Credential Management

Secrets — API keys, database credentials, bearer tokens, and any other authentication material used by the agent's tool invocations — are a distinct security surface that the behavioral specification must govern explicitly.

**Hard boundary: secrets must not enter the agent's generative context.** Secrets used by tool invocations must be stored in a dedicated secrets management service (hardware security module, secrets vault, or equivalent infrastructure-level credential store). They must not appear in: the system prompt, any part of the context window visible to the foundation model, the knowledge base, or any memory store. A secret that is visible to the model's generative process is a persistent exfiltration risk for every adversary who can induce the agent to reproduce its context.

**Required specification fields.** The behavioral specification must declare each secret the agent requires by type and purpose: `{secret_type, purpose, rotation_cadence, storage_mechanism}`. The agent may not use credentials that are not declared in the specification — undeclared credential use is a Layer 1 hard boundary violation.

**Evaluation requirement.** The Layer 3 adversarial evaluation must include one test case per declared secret: a structured information extraction attempt designed to elicit the secret value from the agent's output. A passing test confirms the secret is architecturally inaccessible to the model's generative process. A failing test — the agent reproduces a secret value in any form, including partial, obfuscated, or encoded — is a Critical red-team finding blocking release.

**Rotation trigger.** Secret rotation events for credentials referenced in the system prompt require a new system prompt content hash. The rotation event is recorded in the CSH version history as a system prompt component change, triggering the Stage 6 maintenance notification to Stage 5 monitoring.

### Agent-to-Agent Trust in Multi-Agent Deployments

When the agent operates as a component of a multi-agent system — receiving instructions from an orchestrator agent, exchanging messages with peer agents, or passing results to downstream agents — the trust architecture must explicitly classify agent principals alongside user and operator principals.

**Agent principal classification.** The behavioral specification must state, for each class of agent that can send messages to this agent: (1) the principal tier that agent occupies in this deployment's trust architecture; (2) the mechanism by which this agent verifies the instructing agent's identity and authority; and (3) whether an agent principal can claim operator-level authority, and if so, under what conditions and through what verified channel.

**Default position: agent principals occupy user tier.** In the absence of an explicit elevated authorization, messages from agent principals must be treated as user-tier instructions. An orchestrator agent that sends instructions to a subordinate agent does not automatically inherit the authority of the operator who deployed the orchestration system. Operator-tier authority for agent principals must be explicitly granted through the same trust architecture mechanism as for human operator principals, and must be verified at message receipt, not assumed from channel.

**Hard boundary: agent principals cannot grant themselves authority elevation.** A message from an agent principal that claims authority exceeding its designated tier must be treated as a principal impersonation attempt and handled per the principal impersonation protocol in the behavioral specification's escalation design. The agent receiving the message must not act on the claimed elevated authority without independent verification through the trust architecture's authority verification mechanism.

This requirement applies even when the instructing agent is a governance agent operating within the APLC governance framework. Governance agents operate at designated autonomy tiers; their messages do not carry authority beyond those tiers.

---

## Evidence Freshness Model

Behavioral specification evidence does not become stale on a calendar schedule. Evidence becomes stale when a triggering event occurs that materially affects the conditions the evidence was assembled to assess. A specification reviewed six months ago with no triggering events since is not stale by age alone. A specification reviewed two weeks ago where the deployment domain's regulatory guidance was updated last week has stale safety and alignment requirements — regardless of the recency of the review.

The following triggering events require re-assessment of the affected gate conditions before Stage 3 can proceed or continue:

**Stakeholder change or user model change.** If the user population, the user relationship type, the trust scope, or the vulnerability profile changes — including addition of a new user segment not present in the original user model — use-case coverage, safety requirements, and persona coherence conditions are potentially stale and must be re-assessed.

**Regulatory environment shift.** New regulatory guidance, an enforcement action in the deployment domain, or a material change in the relevant legal framework renders safety and alignment requirements and the regulatory classification analysis potentially stale. This includes EU AI Act implementing acts, sector-specific guidance from national supervisory authorities, and significant enforcement decisions that reinterpret applicable obligations.

**Trust architecture change.** Addition of a new principal, a change in permission scope for an existing principal, or integration of a new tool or external data feed into the agent's action space requires re-assessment of the Layer 1 hard boundaries, the permission-model-derived behavioral requirements, and for Tier 4 systems, the policy envelope specification.

**Material scope change.** Addition of a new use case, revision of out-of-scope statements, or expansion of the agent's operational context requires re-assessment of the use-case coverage map and any gate conditions whose evidence was assembled under the narrower scope.

**Foundation model change that affects behavioral characteristics.** Upgrading the foundation model, switching model providers, or applying fine-tuning that materially alters the model's behavioral characteristics requires re-assessment of any gate conditions that depend on those characteristics — including uncertainty protocol calibration, behavioral consistency targets, and hard boundary enforcement.

When a triggering event occurs after the Behavioral Specification Gate has been passed, the change control process (see `agent-release-governance.md`) determines which gate conditions require re-assessment and whether Stage 3 evaluation must be paused until re-assessment is complete.

## Behavioral Specification Gate Assessment

The Behavioral Specification Gate closes Stage 2 and authorises Stage 3 to begin. Like the Conception Gate in Stage 1, it is a structured evidence assessment, not an approval ceremony. Stage 3 cannot begin until the specification is complete enough that evaluation cases can be derived from it.

Six conditions must be satisfied.

**Condition 1: Behavioral envelope complete at all four layers.** All four layers of the behavioral envelope are specified: Layer 1 hard boundaries are stated with specific enforcement mechanisms, Layer 2 soft boundaries are stated in the canonical format with operator/user configuration boundaries, Layer 3 performance targets are stated in the RE framework's probabilistic assurance target format with evaluation distributions defined, and Layer 4 adaptation scope is specified with governance and rollback procedures.

**Condition 2: Use-case coverage map reviewed by domain expert.** All five zones of the use-case coverage map are populated. A domain expert who was not involved in writing the specification has reviewed the core and edge case zones and confirmed that the coverage is representative. Out-of-scope zones have been reviewed by risk stakeholders and confirmed consistent with the trust architecture.

**Condition 3: Uncertainty protocol operationally specified.** The uncertainty protocol addresses all three decision points with specific thresholds, conditions, and language. The persona design reviewers from Stage 1 have confirmed that the uncertainty language is consistent with the persona.

**Condition 4: Escalation design reviewed and approved by product owner and risk stakeholders.** The escalation design covers all three dimensions for each escalation category. The product owner has confirmed that the escalation paths are operationally viable — that the human queues, review processes, and response time commitments are resourced. Risk stakeholders have confirmed that safety-critical escalation triggers are complete.

**Condition 5: Safety and alignment requirements traceable to Stage 1.** Each safety and alignment requirement traces to a specific decision in the Stage 1 product brief: a trust architecture hard limit, a regulatory classification obligation, or an out-of-scope statement. Requirements that cannot be traced to Stage 1 are either missing from Stage 1 (which requires a Stage 1 revision) or should not be in the behavioral specification.

**Condition 6: Single-source integrity confirmed.** The behavioral specification has been reviewed to confirm that it is internally consistent — that no section specifies behaviors that conflict with another section, that the hard boundaries in Layer 1 are consistent with the hard limits in the trust architecture, that the performance targets in Layer 3 are consistent with the success criteria in Stage 1, and that the escalation design is consistent with the uncertainty protocol. A specification that is internally inconsistent cannot produce a coherent evaluation plan.

**Condition 7 (Tier 4 systems only): Policy envelope specified and internally consistent.** For Tier 4 agent products, the policy envelope is fully specified: allowed change classes with precise definitions, blast radius ceiling with measurement methodology, evidence schema for agent actions within the envelope, rollback conditions (including rollback mechanism), and kill-switch configuration. The policy envelope must be internally consistent with the behavioral specification's Layer 1 hard boundaries: the envelope cannot authorize action classes that Layer 1 prohibits. This consistency check is mandatory — a policy envelope that grants authority to take actions that Layer 1 forbids creates a conflict that cannot be resolved at runtime and that will either result in Layer 1 violation or task failure. The gate assessor must confirm both that the envelope is complete and that a cross-reference between the envelope's allowed change classes and the Layer 1 hard boundary list has been performed with no conflicts identified.

The gate decision is recorded with the name of the assessor, the date, the conditions satisfied, any deferred conditions with documented rationale, and the identified Stage 3 evaluation cases that the specification must support before Stage 3 can be closed. The behavioral specification at gate closure becomes the version-controlled canonical reference for Stage 3. Any change to the behavioral specification after gate closure requires a change control review, re-assessment of affected gate conditions, and approval before Stage 3 evaluation continues against the updated specification.

---

*See also: `companion-re-framework.md` (RE vocabulary and technical structures), `agent-conception.md` (Stage 1 inputs), `aplc.md` (lifecycle overview), `agent-behavioral-evaluation.md` (Stage 3), `agent-release-governance.md` (Stage 4).*

---

## Machine-Executable Specification Model

A behavioral specification written in natural language is a human artifact. A machine-executable specification is a structured representation from which governance agents can automatically derive: evaluation cases, rubrics, thresholds, gate criteria, and monitoring rules. This section specifies the machine-executable extension of the behavioral specification.

### Specification as Generative Model

Each behavioral contract in the specification is extended with a machine-readable schema that enables automatic derivation:

- From the contract's expected behavior → evaluation case templates (inputs, expected output criteria)
- From the contract's constraints → evaluation rubric (what constitutes pass or fail)
- From the contract's risk level → evaluation threshold (confidence level required to pass)
- From the contract's autonomy tier → gate criteria (which evaluation layers are required)
- From the contract's constraint list → monitoring rules (what operational signals trigger review)

This derivation chain closes the gap between the specification and its downstream projections. When the behavioral contract changes, the derived evaluation cases, rubrics, and monitoring rules change with it — not by manual update, but by re-running the derivation from the updated source. This is the machine-executable expression of the single-source principle from the RE framework (`companion-re-framework.md`): no projection is authored independently.

### Behavioral Contract Schema (Machine-Executable Extension)

Each behavioral contract in the specification is extended with a machine-readable block alongside the human-readable description. The schema fields are:

```
contract_id:                  unique identifier
use_case:                     human-readable description
expected_behavior:            structured outcome criteria (machine-parseable)
constraints:                  ordered list of constraint records
  - constraint_id
  - constraint_type
  - constraint_expression
  - violation_severity
autonomy_tier:                1 | 2 | 3 | 4
risk_level:                   critical | high | medium | low
temporal_constraints:
  rate_limit:               max_invocations_per_window (integer) + window_seconds (integer)
  turn_limit:               max_conversation_turns_before_escalation (integer | null)
  time_bounded_behaviors:   list of {active_condition: string, behavior_override: string}
  accumulation_limit:       max_actions_before_mandatory_review (integer | null)
evaluation_template:
  layer_coverage_required:    list of required evaluation layers, e.g. [1, 2, 3, 4]
  minimum_case_count:         integer
  minimum_coverage_confidence: float [0, 1]
  tail_risk_limit:            float [0, 1]
monitoring_rules:
  drift_signal_threshold:     float
  cost_envelope_upper:        token budget
  hitl_escalation_triggers:   list of condition expressions
```

**Temporal constraint fields.** `rate_limit` bounds the agent's invocation frequency — required for any agent that could cause harm through repetition (e.g., an agent sending notifications must not send more than N per hour). `turn_limit` specifies the maximum conversation length before mandatory escalation — required for any agent where long conversation accumulation is a known behavioral risk. `time_bounded_behaviors` defines behaviors that activate only under specified conditions (e.g., different behavior during business hours vs. after hours). `accumulation_limit` defines the maximum number of consecutive autonomous actions before a mandatory human review checkpoint — required for Tier 4 agents. All temporal constraint fields must be specified for Critical and High risk-level contracts; they are optional for Medium and Low risk-level contracts unless the behavioral specification analyst determines that temporal dynamics are relevant to the contract's safety properties.

The `constraint_expression` field is a machine-parseable predicate — a logical expression that can be evaluated against a candidate output. The `violation_severity` field maps to the findings classification in `agent-behavioral-evaluation.md`: Critical, High, Medium, or Low. The `layer_coverage_required` field maps directly to the four-layer evaluation portfolio structure, eliminating the manual step of translating a risk classification into an evaluation scope.

**Constraint Expression Language Specification.** The `constraint_expression` field must be authored in one of the following three forms, listed in order of preference:

*Form 1 — JSON Schema predicate (preferred for output structure constraints).* A JSON Schema object that validates against the agent's response structure. The expression is satisfied if the response, when serialized as a JSON object with the fields defined in the agent's output schema, validates against the JSON Schema predicate. Example: `{"properties": {"confidence": {"maximum": 0.7}}, "required": ["confidence"]}` expresses the constraint that a response must include a confidence field with value ≤ 0.7.

*Form 2 — Named classifier reference (preferred for semantic constraints).* A reference to a named, versioned classifier function registered in the AGKB evaluation suite definitions: `classifier:<classifier_id>:<version>`. The classifier is a function that takes the agent's response as input and returns a boolean. The constraint is satisfied if the classifier returns true. The classifier must be independently evaluated before it can be registered, and its evaluation must be included in the behavioral specification gate evidence.

*Form 3 — Natural language with structured decomposition (when Forms 1 and 2 are not applicable).* A natural language statement that is accompanied by a mandatory structured decomposition: `{"statement": "<natural language>", "detection_method": "<one of: output_filter | human_reviewer | automated_classifier>", "test_oracle": "<description of how a test case can produce a definitive pass or fail determination>"}`. Form 3 expressions require a named human reviewer in the evaluation clearance report; they may not be evaluated by automated means alone.

A behavioral contract with a `constraint_expression` in an unspecified format is not a machine-executable contract. The Constraint Consistency Checker governance agent must reject contracts with unparseable constraint expressions and return a structured error identifying the field and the violation.

### Auto-Derivation Protocol

When a behavioral contract is written or updated, two automated checks run before the contract is accepted into the Agentic Governance Knowledge Base (AGKB):

**Constraint consistency check.** The Constraint Consistency Checker validates that no two constraint expressions within the same contract are mutually contradictory — that is, there is no input for which satisfying one constraint requires violating another. Contradictory constraints are a specification error that, if undetected, produces evaluation results where pass and fail are simultaneously asserted.

**Evaluation template validation.** The Use-Case Elicitation Agent confirms that the `evaluation_template` fields are logically consistent with the contract's `risk_level` and `autonomy_tier`. For example, a contract marked `risk_level: critical` but specifying `layer_coverage_required: [1]` is inconsistent with the probabilistic gate criteria in the following section. The validation rejects such combinations and requests reconciliation by the Behavioral Owner.

Once accepted, the Behavioral Evaluation Swarm Coordinator uses the `evaluation_template` fields to configure the Layer 2 evaluation suite automatically. The Behavioral Drift Monitor uses the `monitoring_rules` to configure operational monitoring automatically. This eliminates the manual translation step from specification to evaluation configuration — a step that is a documented source of evaluation portfolio gaps in organisations that maintain specification and evaluation suites separately.

### Specification Health Metrics

Machine-executable specifications enable automatic computation of specification health metrics. These metrics are computed against the full set of behavioral contracts in AGKB and are reported at the Behavioral Specification Gate:

| Metric | Definition | Minimum threshold at gate |
| --- | --- | --- |
| Completeness | Percentage of behavioral contracts with all machine-readable fields populated | 100% for critical and high risk-level contracts; 80% for medium and low |
| Consistency | Percentage of contracts with no constraint conflicts verified by the Constraint Consistency Checker | 100% — no contracts with unresolved conflicts may proceed to Stage 3 |
| Coverage | Percentage of stated use cases in the use-case coverage map with a corresponding behavioral contract | 100% for core use cases; 80% for edge cases |
| Derivability | Percentage of evaluation cases that were auto-derived from behavioral contracts versus manually authored | Reported as an indicator; no minimum threshold, but declining derivability is a leading indicator of specification–evaluation divergence |

The Derivability metric is informational rather than a hard gate condition. Its purpose is to surface the degree to which the evaluation portfolio has drifted from the specification as its source. A low Derivability score does not block the gate but is a signal to the Behavioral Owner that the specification and the evaluation suite require reconciliation.

### Specification Quality Gate Condition

At the Behavioral Specification Gate, the machine-executable specification must satisfy the Completeness and Consistency thresholds in the table above. Specifically: the gate cannot be passed while any critical or high risk-level behavioral contract has unpopulated machine-readable fields. This condition is Condition 1 (behavioral envelope complete at all four layers) made machine-verifiable: the gate assessor does not inspect fields manually — the AGKB reports a binary satisfying or not satisfying determination against the threshold.

---

## Probabilistic Gate Criteria in Specifications

Behavioral specifications must define gate criteria appropriate for probabilistic behavioral systems. This section specifies how probabilistic gate criteria are authored as part of the behavioral specification — at Stage 2, not determined ad hoc at gate time.

### Gate Criteria as Specification Elements

Gate criteria are not established at gate time. They are authored in the behavioral specification at Stage 2, stored in AGKB alongside the behavioral contracts they govern, and reviewed as part of the Behavioral Specification Gate. This sequence matters: if thresholds are set at gate time, they can be calibrated toward the system's current performance rather than toward the system's required safety properties. Pre-committed thresholds authored before the system is evaluated cannot be manipulated toward observed results.

Any change to gate criteria after the Behavioral Specification Gate has been passed requires change control review, documented justification, Regulatory Owner approval, and retroactive impact analysis. The retroactive impact analysis answers: would prior gate decisions have changed under the proposed new thresholds? If yes, those prior decisions must be re-examined before the new thresholds are applied prospectively.

### Threshold Specification by Risk Level

The following defaults apply to probabilistic assurance targets. These values represent the minimum acceptable thresholds. Behavioral Owners may specify more stringent thresholds; they may not specify less stringent thresholds without Regulatory Owner approval documented in AGKB.

| Risk level | Mean performance floor | Tail risk limit | Required evaluation layers | Gate decision authority |
| --- | --- | --- | --- | --- |
| Critical | ≥ 0.95 | P(below safety floor) ≤ 0.0001 | Layers 1, 2, 3, and 4 all required | Human gate decision required |
| High | ≥ 0.90 | ≤ 0.001 | Layers 1, 2, and 3 required | Human gate decision required |
| Medium | ≥ 0.85 | ≤ 0.01 | Layers 1 and 2 required | Human or governance agent gate decision |
| Low | ≥ 0.80 | ≤ 0.05 | Layer 1 required | Governance agent gate decision permitted |

The tail risk limit is defined as the probability that a randomly drawn production interaction falls below the behavioral safety floor specified in the behavioral contract. The safety floor is not the same as the mean performance floor: it is the absolute minimum acceptable performance level below which the agent's behavior constitutes a safety or compliance failure, regardless of mean performance across the distribution. A contract may specify a mean floor of 0.90 with a safety floor at 0.60 — meaning average performance must be high, but the tail of the distribution may not reach below 0.60 even for difficult cases.

**Gate decision authority clarification.** For critical and high risk-level contracts, a governance agent may assist the gate process — drafting the gate assessment, summarising evaluation results, flagging conditions — but the gate decision itself must be made by a named human. A gate record showing an agent-generated gate approval for a critical risk-level contract is a governance failure, not a valid gate passage. This constraint is consistent with the governance agent participation framework in `aplc.md`.

### Confidence Interval Requirements

The behavioral specification must define the required confidence interval width for each probabilistic assurance target. Confidence interval width determines the number of evaluation runs required: narrower intervals require more runs, which increases evaluation cost and duration. The specification author makes an explicit cost-quality trade-off when setting confidence interval requirements.

The tradeoff must be documented. A specification that states a performance target but does not state a required confidence interval width is leaving evaluation scope undefined — the evaluation team can satisfy the letter of the specification with an arbitrarily small sample, but the resulting confidence interval may be wide enough to be uninformative about whether the target is actually met. Minimum required documentation: the target value, the required confidence interval half-width, and the confidence level (typically 90% or 95%), which together determine the minimum evaluation sample size.

### Threshold Version Control

All threshold specifications are versioned in AGKB as part of the behavioral specification version record. The version record captures: the threshold values, the Behavioral Owner who approved them, the date of approval, and the rationale for any threshold that deviates from the risk-level defaults. When thresholds change between specification versions, AGKB records both the old and new values and the date of change.

Retroactive impact analysis is automatically computed by the Behavioral Evaluation Swarm Coordinator when a threshold change is submitted: the coordinator replays prior evaluation results against the proposed new thresholds and reports which prior gate decisions would have been different. This report is a required input to the Regulatory Owner's approval decision.

### Probabilistic Regression Criteria

The behavioral specification must define what constitutes a behavioral regression between evaluation cycles. Regression criteria operate differently from gate criteria: gate criteria determine whether the system may be released; regression criteria determine whether a behavioral change between evaluation cycles requires investigation before the next release cycle proceeds.

**Default regression criterion:** any behavioral contract whose mean performance drops by more than 5 percentage points from the prior evaluation cycle's measurement is flagged as a regression requiring investigation. The investigation must identify the cause before the next behavioral release gate clears. A regression finding does not automatically block the gate — the investigation result determines whether the regression represents a systematic deterioration requiring remediation or a measurement artifact within acceptable variance.

Behavioral Owners may specify stricter regression criteria for individual contracts — for example, a 2 percentage point drop threshold for a critical risk-level contract covering a safety-sensitive use case. These stricter criteria are stored in the behavioral contract's machine-readable schema and are applied automatically by the Behavioral Evaluation Swarm Coordinator. Less sensitive regression criteria than the 5 percentage point default may not be specified without Regulatory Owner approval.

---

## Specification Health Monitoring

Behavioral specifications age. As the agent system operates, accumulates incidents, and encounters edge cases not anticipated at specification time, the specification becomes increasingly incomplete relative to the operational reality it is supposed to govern. Specification Health Monitoring tracks specification currency and triggers maintenance actions before incompleteness becomes an incident.

### Specification Age Indicators

The following indicators are monitored continuously against each behavioral specification in AGKB. They are reported in the Stage 5 operational dashboard alongside behavioral performance metrics, because specification currency is a precondition for the validity of those behavioral metrics — a behavioral metric measured against a stale specification is not a meaningful governance signal.

**Absolute age.** Time elapsed since the last full specification review. A specification that has not been reviewed in twelve months is a mandatory review trigger regardless of the other indicators.

**Domain change rate.** Frequency of external changes — regulatory updates, domain standard revisions, user population changes — that may affect specification validity. This indicator is supplied by the Knowledge Staleness Sentinel, which monitors the external sources that informed the specification and generates alerts when those sources change (see Knowledge Staleness Sentinel Integration below).

**Incident-derived gap rate.** Frequency of production incidents attributed to specification gaps, as identified through the HITL four-channel learning mechanism in Stage 5 (`agent-operations.md`, Channel 2: specification gap identification). Each such incident represents an operational reality that the behavioral specification did not anticipate and did not specify handling for.

**HITL override rate.** The proportion of agent decisions that human reviewers override. A sustained high override rate indicates that the specification does not adequately capture required behavior — human reviewers are compensating for specification incompleteness at the decision level. An override rate sustained above 10% for 30 consecutive days is a specification review trigger.

**Evaluation anomaly rate.** Frequency of evaluation results that fall outside the ranges predicted by the behavioral contracts' machine-readable fields. When evaluation results are consistently surprising relative to what the specification predicted, the specification model of the system is wrong — either the expected behaviors are miscalibrated, the constraints are mis-expressed, or the risk-level assignments do not reflect actual operational risk.

### Specification Review Triggers

Any of the following conditions automatically generates a specification review request directed to the Behavioral Owner:

| Trigger | Threshold |
| --- | --- |
| Incident-derived gap rate | Exceeds 3 incidents per 30-day rolling window |
| HITL override rate | Sustained above 10% for 30 consecutive days |
| Regulatory change | Any regulatory update affecting this agent system's use-case domain |
| Foundation model update | Any composite state component change affecting the foundation model version |
| Time elapsed | 12 months since the last full specification review |

The regulatory change trigger and the foundation model update trigger are unconditional: they activate regardless of the other indicator levels. A regulatory change may invalidate safety requirements or hard boundary definitions regardless of how current the specification appeared before the change. A foundation model update may expose specification gaps that the prior model version did not reach — the specification was effectively calibrated to the prior model's behavioral characteristics.

### Knowledge Staleness Sentinel Integration

The Knowledge Staleness Sentinel monitors the external sources that informed the specification: the regulatory frameworks cited in the safety and alignment requirements, the domain standards that grounded the use-case coverage map, and the product requirement documents from which the business purpose and success criteria were derived. When a monitored source changes, the Sentinel generates a staleness alert containing:

- The source that changed, with a reference to its new version or updated content
- The behavioral contract identifiers whose content cites or depends on that source
- A preliminary assessment of which specification elements may require revision

The staleness alert is not a specification change — it is a directed review trigger. The Behavioral Owner receives the alert and determines whether the affected specification elements require revision. The Constraint Consistency Checker then runs against the affected contracts to identify any new conflicts introduced by the source change.

Sources are registered with the Knowledge Staleness Sentinel at Stage 2, as part of completing the behavioral specification. A specification that cites regulatory frameworks without registering them with the Sentinel has created an ungoverned dependency — the specification may become stale without triggering a review. Registering cited sources is therefore a required step in Behavioral Specification Gate Condition 5 (safety and alignment requirements traceable to Stage 1): the traceability chain must extend to the external sources that informed those requirements, and those sources must be monitored.

### Specification Review Process

When a specification review is triggered, the following process governs its execution:

1. **Trigger receipt.** The Behavioral Owner receives the review trigger — either a staleness alert from the Knowledge Staleness Sentinel, an automatic threshold alert from the operational dashboard, or a mandatory time-based trigger.

2. **Automated consistency check.** The Constraint Consistency Checker runs an automated review of the behavioral contracts flagged by the trigger, evaluating them against the updated external sources or the new operational data. The checker identifies: constraints that conflict with updated regulatory text, use cases that are no longer covered by the current specification, and machine-readable fields that have become inconsistent with the trigger's source change.

3. **Gap and conflict presentation.** The checker produces a structured gap report identifying affected behavioral contracts, the nature of each gap or conflict, and a severity assessment (using the Critical / High / Medium / Low classification). This report is presented to the Behavioral Owner for scope determination.

4. **Review scope approval.** The Behavioral Owner approves the scope of the specification update — which contracts are revised, which are confirmed as still valid, and whether any new contracts must be added to cover previously unspecified cases. The scope approval is recorded in AGKB.

5. **Targeted elicitation.** The Use-Case Elicitation Agent runs targeted use-case elicitation for the areas identified in the scope. Targeted elicitation focuses on the affected domains and does not re-run the full elicitation process — it extends the existing coverage map at the affected boundaries.

6. **Mini Behavioral Specification Gate.** The updated specification — comprising only the revised and new behavioral contracts — is reviewed at a mini Behavioral Specification Gate. The mini gate confirms: the affected contracts satisfy the Completeness and Consistency health metrics; the revised gate criteria are consistent with risk-level defaults; and the updated specification does not introduce conflicts with unchanged contracts. The mini gate does not re-examine the full specification unless the scope of changes is material enough to require it.

7. **AGKB publication.** The updated specification is published to AGKB with a version increment. The version record captures: the trigger that initiated the review, the Behavioral Owner who approved the scope, the contracts changed, and the mini gate assessor's name and date. All downstream projections derived from the affected contracts — evaluation case templates, monitoring rules, gate criteria — are automatically re-derived from the updated machine-readable fields.

A specification review initiated by a regulatory change or a foundation model update may, upon the Behavioral Owner's assessment, determine that the scope of required changes is large enough to constitute a material specification revision. In that case, the mini gate is replaced by a full Behavioral Specification Gate, and Stage 3 evaluation must be re-run against the updated specification before the next release proceeds.

### Annual Specification-to-Brief Coherence Review

Individual specification revisions are governed by the review process above. The cumulative effect of many governed revisions can produce a specification that has drifted materially from the Stage 1 product brief without any single revision being out of compliance. The annual coherence review detects this cumulative drift.

**Cadence.** Once per calendar year for all deployed agent products, or immediately following any material specification revision that the Behavioral Owner assesses as potentially affecting the brief's premises.

**Scope.** Compare the current behavioral specification against the original Stage 1 product brief on four dimensions:

1. *Business purpose alignment.* Does the specification's declared scope and behavioral design still serve the validated business purpose from Stage 1? Additions, extensions, or scope creep that were individually approved but collectively represent a different product require a Stage 1 review.

2. *User model consistency.* Do the behavioral requirements still reflect the Stage 1 user model — the same population, relationship type, trust scope, and vulnerability profile? Specification revisions that effectively serve a different user population require a Stage 1 revision of the user model before being incorporated into the specification.

3. *Trust architecture coherence.* Are all current behavioral constraints traceable to the Stage 1 trust architecture? Constraints added during recalibration without traceability to Stage 1 are either correctly derived from the trust architecture (and the trace should be documented) or represent scope expansion that requires Stage 1 review.

4. *Regulatory classification consistency.* Have specification revisions created behavioral capabilities that affect the Stage 1 regulatory classification? An agent that has acquired new tool access, expanded its interaction scope, or moved into new decision-making territory since Stage 1 may have changed its EU AI Act risk classification without a formal Stage 1 review.

**Outcome.** The coherence review produces a structured record: one finding per dimension (consistent / diverged-within-tolerance / material-drift). A "material-drift" finding on any dimension triggers a Stage 1 review — not a Stage 2 revision. The gap is at the conception level. The coherence review record is filed to AGKB alongside the behavioral specification version record.

*See also: `companion-re-framework.md` (single-source principle, probabilistic assurance target format), `agent-behavioral-evaluation.md` (evaluation portfolio structure and probabilistic gate decisions), `agent-operations.md` (HITL four-channel learning and Knowledge Staleness Sentinel), `agent-maintenance.md` (foundation model update governance), `aplc.md` (governance agent participation framework and gate integration).*
