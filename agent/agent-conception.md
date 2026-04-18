# Stage 1 — Conceive: The Agent Product Brief

*Primary Stage 1 document of the Agentic Product Lifecycle. Defines what the agent product is before any engineering begins: its purpose, the people it serves, the authority it has, the persona it presents, and its regulatory classification. Audience: product owners, business sponsors, legal and risk officers, specification analysts.*

---

## What is Stage 1 — Conceive?

Stage 1 is the governed foundation of the Agentic Product Lifecycle. Before any engineering begins — before behavioral specification, before code — the product's existence must be justified, its purpose defined, its authority bounded, and its regulatory classification determined. An agent deployed without a completed Stage 1 is an agent whose behavior is defined by builder assumptions, not product requirements. The Conception stage is not a preliminary to the real work: it is the work that makes all subsequent stages tractable. Everything written in Stage 2 behavioral specification, tested in Stage 3 evaluation, and enforced in Stage 4 release governance traces back to decisions made here. A weak or incomplete Stage 1 does not merely slow the lifecycle — it corrupts every downstream stage, because those stages will specify, evaluate, and release an agent whose product purpose was never clearly established.

---

## The Agent Product Brief

The governed output of Stage 1 is the Agent Product Brief. It is not a business case, a pitch, or a design document. It is the authoritative record of what the agent is, who it serves, what authority it has, and what success looks like — stated precisely enough that Stage 2 can begin and that the Conception Gate can be assessed.

A complete brief contains the following required components.

### Business Purpose

State what problem the agent solves, for whom, and with what evidence the problem is real. The same standard applies here as the ASDLC's demand validation: evidence-backed, not assumed. A stakeholder request without supporting evidence is not a validated business purpose. User research, data analysis, regulatory mandate, or documented executive decision with articulated rationale each constitute validation. An agent whose problem statement cannot be supported by evidence belongs in a proof-of-concept, not a product lifecycle.

Distinguish three parties whose interests are separate and must be addressed separately:

**The direct user** is who interacts with the agent. This may be a customer, an internal employee, a partner, or another system. The direct user experiences the agent's behavior in real time, carries the cognitive load of the interaction, and is the first person affected if the agent behaves badly. Their trust relationship with the agent is immediate and personal.

**The beneficiary** is who benefits from the interaction's outcome. The direct user and the beneficiary are often the same person — a customer asking a claims agent to process their claim is both. They are not the same when the direct user is a call centre operator and the beneficiary is the customer whose record they are updating, or when the direct user is an automated system and the beneficiary is a human whose downstream experience depends on the output. When they differ, the agent's design must account for both, and the brief must specify both.

**The deploying organisation** has its own interest: efficiency, cost reduction, compliance, revenue, risk mitigation. State it explicitly. An agent product brief that does not acknowledge the organisation's interest cannot assess alignment or tension between that interest and user welfare — and that tension is where agent product failure most often originates.

### User Model

Specify who the agent serves, in enough detail to design a behavioral envelope and a persona that are coherent with the actual user relationship.

**Relationship type.** Define what kind of relationship the agent has with users. Advisory: the agent provides analysis or recommendations that the user acts on independently. Transactional: the agent completes a task that has direct effects on the user's situation. Analytical: the agent processes data and returns insight. Decisional: the agent makes or substantially shapes a consequential decision affecting the user. Most agents combine types, but one type typically dominates, and the dominant type determines the agent's duties.

**Trust scope.** What do users trust the agent to do? What do they expect it not to do? State both explicitly, because the gap between the two is where misplaced trust produces harm. A customer who trusts a financial advisory agent to give neutral recommendations and expects it not to be steering them toward products the organisation profits from is in a fundamentally different trust relationship than a developer who trusts an internal code review agent and expects it to flag security issues but not to make production commits.

**Vulnerability and power asymmetry.** Not all users are equally situated. A customer advisory agent has a different duty than an internal tooling agent. A healthcare information agent interacting with patients has a different duty than a procurement agent interacting with trained professionals. Specify: are there classes of users who may have reduced capacity to evaluate the agent's outputs critically? Are there situations where users may be under stress, duress, or emotional load that affects their ability to engage with the agent in a normal way? Are there power differentials — the organisation holds information or capability the user does not — that create asymmetric risks? These are design constraints, not edge cases. They must be established here, not discovered at Stage 3.

### Success Criteria

Define measurable business outcomes. The metric, target, and measurement method must all be specified before Stage 2 begins. These criteria are assessed in production against observed behavior, not in evaluation against test inputs. Evaluation (Stage 3) verifies behavioral specification compliance. Success criteria measure whether deploying the agent produced the business result the brief claimed it would.

"Reduce claims processing time by 30% within 60 days of deployment" is a success criterion. It names a metric (processing time), a target (30% reduction), a measurement window (60 days), and an implicit baseline (current processing time, which must be recorded before deployment). "Improve customer experience" is not a success criterion. It names a direction of intent with no metric, no target, no measurement method, and no defined baseline.

Each success criterion in the brief must answer four questions: What is measured? What is the target value? How is it measured? What is the baseline? A brief with success criteria that cannot answer all four questions is not complete.

### Value Definition

State explicitly how the agent delivers value. This is not the same as the success criterion. The success criterion measures whether value was delivered. The value definition states the mechanism. There are three distinct value mechanisms:

**Output value:** the agent's outputs are themselves the product. A research synthesis agent, a document drafting agent, a code review agent. The output is what the user receives; the value is in the quality, relevance, and reliability of that output.

**Process efficiency value:** the agent accelerates or scales a process that would otherwise require human time. A claims triage agent, a document classification agent, a first-line support agent. The output matters less than the throughput and cost reduction. The agent is a process component, not a product in itself.

**Novel capability value:** the agent enables something that was not possible at scale without it. Personalised guidance across a large user base, real-time analysis of inputs too large for human processing, coordination across systems that previously could not communicate. The value is in the capability that did not exist before.

Most agents combine types, but the primary value mechanism shapes the evaluation strategy in Stage 3, the release criteria in Stage 4, and the operational monitoring in Stage 5. An agent whose brief says "process efficiency value" will be monitored for throughput and cost. An agent whose brief says "output value" will be monitored for output quality. Conflating them at the brief stage means the wrong things get measured at every subsequent stage.

### Out-of-Scope: Explicit Statement

State what the agent does not do — as a deliberate design decision, not a limitation discovered later. Out-of-scope statements in the brief serve two functions. First, they bound the behavioral specification in Stage 2: if something is out of scope at the product level, it should not appear as a use case in the behavioral envelope. Second, they prevent scope expansion during the build phase, which is the primary driver of specification drift. An out-of-scope statement that says "this agent does not provide investment advice, regardless of user request" is a product decision that constrains the behavioral envelope, the persona design, the escalation design, and the regulatory classification simultaneously. Discovering at Stage 3 that the agent was providing investment advice because no one said it should not is a Stage 1 failure.

Out-of-scope statements must be specific. "The agent does not handle complex cases" is not specific enough to guide behavioral specification. "The agent does not process claims involving third-party liability, multi-vehicle incidents, or claims where fraud indicators are present at intake" is specific enough to derive behavioral requirements.

---

## Trust Architecture Design

Trust architecture is not a security configuration. It is a product design decision that determines who can direct the agent's behavior, to what degree, and under what constraints. An agent whose trust architecture is left to engineering inference will behave differently in the hands of different operators, with different users, under different instructions — because the authority hierarchy was never resolved by design.

Three components are required.

### Principal Hierarchy

Define who can instruct the agent, at what authority level, and through what channel.

**Operator** is the deploying organisation. The operator configures the agent, sets its operating context, and bears legal and regulatory accountability for its behavior. The operator's authority is the highest in the hierarchy. Operator instructions can expand or restrict the agent's default behavioral envelope within limits set by the model provider. The operator cannot instruct the agent to act against users' basic interests — this is a hard limit that no operator configuration can override.

**User** is the interacting human. The user can adjust the agent's behavior within the scope the operator permits. The user cannot override operator-level configurations. User authority is narrower than operator authority, and its scope must be specified explicitly: what can a user change? Tone? Language? Level of detail? Whether the agent asks clarifying questions? What they cannot change is as important as what they can, and both must be stated.

**System** covers automated inputs: other agents, upstream pipeline outputs, tool responses, external data feeds. System-level inputs may carry operator-level or user-level authority depending on the architecture. The authority level of every automated input channel must be assigned explicitly. An agent that treats a tool response as operator-level instruction is vulnerable to prompt injection through that tool. The trust architecture must specify: which automated inputs are trusted at what level, what integrity verification is applied to those inputs, and what happens when an automated input contains an instruction that conflicts with operator or user intent.

**Conflict resolution.** When principal instructions conflict — and they will — the agent's resolution behavior must be specified by design, not inferred at runtime. The general resolution hierarchy is: hard limits (model-provider level) override operator instructions, which override user instructions, which override system inputs. But this hierarchy has exceptions that must be specified: user safety requests may override operator configuration in certain circumstances; a user in genuine distress may require a different response than operator instructions anticipate. These exceptions must be specified in the trust architecture, not handled ad hoc in the behavioral specification.

### Agent Principals in Multi-Agent Deployments

When this agent product will operate as a component of a multi-agent system — receiving instructions from an orchestrator, exchanging results with peer agents, or providing outputs to downstream agents — the trust architecture must explicitly define the agent principal tier alongside user and operator principals.

**Agent principal classification required fields:**
- The identity of any agent product that will send instructions to this agent (by agent identifier, not by deployment instance)
- The principal tier assigned to each such agent principal (default: user tier; operator tier requires explicit justification and must not be assumed from architectural position)
- The identity verification mechanism: how does this agent confirm, at message receipt, that the instructing agent is who it claims to be, operating at the authority level it claims?
- The hard boundary: no agent principal may claim authority exceeding its designated tier. Instructions from an agent principal claiming elevated authority are treated as principal impersonation attempts.

**Default posture for unspecified agent principals.** Any message received from an agent source not explicitly named in the trust architecture is treated as user-tier by default. The agent must not infer elevated authority from the channel, the message format, or the content of the message.

**Governance agent principals.** APLC governance agents (as defined in `governance/agents.md`) that interact with this agent product during governance activities occupy the tier defined in their own behavioral specifications — typically Tier 2 (human-on-the-loop, advisory). Governance agent messages do not carry operator-tier authority by virtue of being governance agents.

This trust architecture specification for agent principals is a Conception Gate condition for any agent product deployed in a multi-agent context. A product conceived for a multi-agent deployment without this specification has an undefined trust surface and cannot satisfy the Behavioral Specification Gate's single-source integrity condition.

### Permission Model

The permission model specifies, for each principal, what they can instruct the agent to do and what they cannot. It is a security and safety design, not a UX design. It is the first line of defense against adversarial use — by users attempting to manipulate the agent beyond its intended scope, by operator misconfigurations that create unintended agent behavior, and by automated inputs that attempt to hijack the agent's actions.

**Hard limits** are behaviors no instruction from any principal can override. They are enforced by infrastructure policy, not by prompt instruction. Examples: the agent will not exfiltrate data from the system context to an external endpoint; the agent will not impersonate a named human; the agent will not produce content that sexualises minors. Hard limits in the permission model must map directly to Layer 1 hard boundaries in the behavioral envelope developed in Stage 2 (see `agent-behavioral-specification.md`). If a hard limit is stated in the permission model but not enforced as a hard boundary in the behavioral specification, the permission model is aspirational rather than functional.

**Soft limits** are behaviors the agent does by default that operator instructions can override, or behaviors the agent does not do by default that operator instructions can enable. Operators operate within the space the model provider defines; users operate within the space the operator defines. No permission flows upstream. A user cannot grant themselves operator-level authority by instruction.

Specifying the permission model requires naming the limits, not just the categories. "Users cannot instruct the agent to ignore safety guidelines" is a category. "Users cannot instruct the agent to process requests involving personal financial information beyond the fields specified in the data model" is a limit specific enough to verify. The behavioral specification in Stage 2 will derive its permission-related requirements directly from this model.

### Principal Authentication Mechanism

The principal hierarchy defines which tier each instruction source occupies. The authentication mechanism specifies how the agent infrastructure verifies, at runtime, that an instruction actually originates from the claimed tier. Without authentication, the hierarchy is a policy statement; with authentication, it is an enforced control.

**Required fields for each principal tier.** The trust architecture specification must define, for each principal tier (user, operator, system, and any agent principal tiers defined under multi-agent deployment):

- *Authentication method:* the technical mechanism by which the agent infrastructure verifies the instruction source's claimed tier. Valid mechanisms:
  - Authenticated API channel with mTLS (mutual TLS) or JWT (JSON Web Token) with an organizational signing key — the infrastructure verifies the token before the instruction reaches the model.
  - Cryptographically signed message with the principal's registered key — the infrastructure verifies the signature; only verified instructions proceed to the model.
  - Hardware security module attestation for system-tier principals — instructions from system-tier sources are only accepted from HSM-attested environments.
  - For user-tier principals: session authentication through the operator's identity management system is sufficient; model-level verification of user identity is not required.

- *Verification failure response:* what happens when authentication fails — the instruction cannot be verified as originating from the claimed tier. Default: treat the instruction as user-tier regardless of its claimed tier; log the authentication failure as a principal impersonation attempt; escalate to HITL for review if the instruction claimed elevated authority.

**What is not a valid authentication mechanism.** The following are explicitly invalid as primary authentication mechanisms (they may supplement but not replace the mechanisms above):
- System prompt positioning — an instruction in the system prompt position is not authenticated as operator-tier merely by its position; any instruction that arrives in the system prompt from an unverified source is an unverified instruction.
- Channel assumption — assuming that instructions arriving through a specific channel carry a specific authority tier without cryptographic verification of the channel's integrity.
- Content-based tier inference — inferring an instruction's tier from its content, format, or claimed identity rather than from verified authentication.

**Infrastructure enforcement requirement.** The authentication mechanism is enforced at the infrastructure layer before instructions reach the model. A behavioral specification that defines authentication requirements but relies on the model to enforce them (via the system prompt) has not defined an authentication mechanism — it has defined a preference. The Stage 3 Layer 1 evaluation suite must include a test confirming that the authentication mechanism is enforced at the infrastructure layer: instructions claiming elevated tier without valid authentication credentials must be verifiably rejected at the infrastructure level, not by model refusal.

### Policy Envelope (Tier 4 Systems)

For agent products intended to operate at Tier 4 autonomy — where agents execute autonomously within a human-approved, machine-enforced policy envelope without per-change human approval — the policy envelope is a primary trust architecture artifact at the same level as the principal hierarchy and permission model.

The policy envelope specifies the space within which the agent may act without per-action human approval. The product brief must specify the policy envelope's intended scope across five dimensions:

**Allowed change classes**: precise definitions of the categories of action the agent may take within the envelope. Vague descriptions ("routine changes") are not permitted — each allowed class must be defined specifically enough that an action can be unambiguously classified as within or outside the class.

**Blast radius ceiling**: the maximum consequence of any single action the agent may take within the envelope, with the measurement methodology stated. The blast radius ceiling is enforced by machine policy, not by the agent's judgment.

**Required evidence schema**: the structure and content of the evidence the agent must record for each action taken within the envelope. Evidence schema is not logging — it is the auditability contract for autonomous operation. Specify: what fields are mandatory, what provenance is required, and what retention period applies.

**Rollback conditions**: the conditions under which an action taken within the envelope must be reversed, and the mechanism by which rollback is triggered and executed. For actions whose effects cannot be rolled back, those action classes must be explicitly excluded from the policy envelope.

**Kill-switch configuration**: how autonomous operation is halted, by whom, and within what latency. The kill-switch must be operable by the accountable human without requiring engineering intervention.

The accountable human named in the product brief accepts accountability for envelope design, not per-action approval. This is a governance model shift that must be acknowledged explicitly: the accountable human is responsible for the quality, scope, and safety of the envelope definition, and accepts that actions taken within an approved envelope are authorized by the envelope, not by individual review. A product brief that treats Tier 4 as "Tier 3 with fewer reviews" has misunderstood this shift and must be revised before the Conception Gate is assessed.

**Regulatory classification note for Tier 4 systems:** Autonomous operation within a policy envelope without per-action human approval likely elevates the system's risk classification under the EU AI Act. The absence of per-action human oversight is a material factor in Annex III classification analysis and in the Article 14 human oversight requirements. This must be flagged explicitly as a classification input requiring legal review before the Conception Gate is passed. Do not assume that a system classified as lower-risk at Tier 3 retains that classification at Tier 4.

### Conflict Resolution

Specify how the agent resolves conflicts between principal instructions. The hierarchy stated above provides a default order. What the brief must add is the agent's behavior in specific conflict patterns that arise in the product context:

What does the agent do when a user asks it to do something the operator configuration would normally permit, but the specific request has characteristics that suggest the user is attempting to abuse the system? What does the agent do when a tool response instructs it to take an action the operator configuration does not explicitly address? What does the agent do when a user expresses a safety need (distress, harm risk) that conflicts with the operator's instruction to restrict responses to product scope?

These are not edge cases. They are predictable conflict patterns in almost every deployed agent. Resolving them by design — stating the agent's behavior explicitly for each pattern — is the difference between a governed agent and one that resolves conflicts by inference and therefore resolves them inconsistently.

---

## Persona Design

The agent's persona is its designed identity: its name, communication style, tone, stated limitations, and relationship style with users. Persona design is a product decision, not a prompt engineering decision. It must be established in Stage 1 because the behavioral envelope in Stage 2 must be consistent with the persona. An agent whose persona promises approachability, warmth, and comprehensive assistance while its behavioral envelope is narrow, terse, and quick to escalate will produce users who feel misled. The mismatch between persona promise and behavioral reality is a product defect, not a prompt tuning opportunity.

Persona design must address four required questions.

**How the agent identifies itself as an agent.** EU AI Act Article 50 requires that AI systems interacting with humans disclose their AI nature on request. This is not merely a legal requirement — it is a trust architecture decision. Specify: when does the agent identify itself as an AI? Only when asked, or proactively? What language does it use? Does it have a name that is clearly non-human, or a human-sounding name that requires explicit disclosure? How does it respond to the direct question "are you a human?"? These decisions must be made at Stage 1 and held consistently through every stage. An agent that inconsistently identifies itself — sometimes disclosing its AI nature, sometimes not — is a product defect and a regulatory risk.

**What the agent says when it does not know.** This is one of the most consequential persona decisions, because it determines whether the agent will hallucinate with confidence or express genuine uncertainty. An agent whose persona is authoritative and comprehensive will resist expressing uncertainty because uncertainty conflicts with its persona. That is a design defect. Specify explicitly: the language the agent uses to signal uncertainty, the conditions under which it uses it (below what confidence threshold?), and whether it can decline to answer rather than produce a low-confidence response. The uncertainty protocol in Stage 2 (`agent-behavioral-specification.md`) must be consistent with what the persona design establishes here.

**How the agent handles user frustration or adversarial tone.** Users interact with agents under conditions that include frustration, confusion, distress, and occasionally deliberate hostility. The agent's response to these inputs must be designed, not left to model defaults. Specify: does the agent acknowledge frustration? Does it maintain the same persona under adversarial pressure? Does it have a de-escalation protocol, and if so, what are its limits? Does it escalate to a human when user frustration reaches a threshold? These are product decisions with legal and reputational implications, not UX niceties.

**What the agent says when it reaches the boundary of its behavioral envelope.** When a user asks the agent to do something outside its scope — either because it is genuinely out of scope or because the input is adversarial — the agent's response must be designed. "I can't help with that" is a different product experience than "I'm designed specifically for claims processing — for questions about your broader policy, I can transfer you to our customer service team." The boundary response is often the first place users encounter the agent's limits, and it determines whether they experience the agent as coherent and trustworthy or arbitrary and unhelpful.

---

## EU AI Act Risk Classification

Regulatory classification is not a compliance checkbox performed after the product is designed. It is a Stage 1 activity because the classification determines which conformity requirements flow into every subsequent stage. An agent that is classified as high-risk in Stage 1 must be specified, evaluated, released, and operated to high-risk standards. An agent that has not been classified cannot be specified to the correct standard.

The classification process follows four steps.

### Step 1: Prohibited Practices Check (Article 5)

Before any classification, determine whether the agent's use case falls within the prohibited practices enumerated in Article 5. Prohibited practices include: subliminal or manipulative techniques that impair free decision-making; exploitation of vulnerabilities of specific groups; social scoring by public authorities; real-time remote biometric identification in public spaces (with narrow exceptions); emotion recognition in workplace and educational settings; and AI systems that infer sensitive attributes such as political opinions or sexual orientation from biometric data.

If the agent's use case falls within a prohibited practice, the agent cannot be deployed in the EU. This is not a risk management question — it is a binary: prohibited or not. Determine this with qualified legal counsel. If the answer is "not clearly prohibited," document the analysis. The documentation will be required if the classification is later challenged.

### Step 2: Annex III High-Risk Category Check

If the use case is not prohibited, determine whether it falls within the high-risk categories enumerated in Annex III. The high-risk categories include: biometric identification and categorisation; critical infrastructure management; educational and vocational training that determines access or evaluates persons; employment and worker management; access to essential private and public services and benefits; law enforcement; migration and border control; administration of justice; and AI systems that influence elections.

For product teams in financial services, insurance, or professional advisory sectors: agents that make or substantially influence decisions about creditworthiness, insurance pricing, loan approval, or access to financial services are candidates for high-risk classification under "access to essential private and public services." The classification depends on whether the agent makes the decision, influences the decision, or merely supports a human who makes the decision. The distinction is consequential — specify the decision architecture clearly.

If the use case falls within Annex III, the agent is a high-risk AI system. High-risk classification triggers: technical documentation requirements, data governance requirements (Article 10), transparency and information provision requirements (Article 13), human oversight requirements (Article 14), accuracy, robustness, and cybersecurity requirements (Article 15), and registration in the EU database of high-risk AI systems.

These obligations are not optional additions to the product specification. They are product requirements that must be specified in Stage 2, tested in Stage 3, and enforced as release gate conditions in Stage 4.

### Step 3: General-Purpose AI Assessment

If the agent is built on a general-purpose AI model (GPAI) — including all current large language models from major providers — the deploying organisation is acting as an operator of a GPAI system. Operator obligations under Articles 28–29 include: implementing technical and organisational measures appropriate to the intended purpose, monitoring for misuse, conducting fundamental rights impact assessments for high-risk deployments, and maintaining logs as required by the Act.

The GPAI model provider's transparency documentation is a required input to the operator's technical documentation for high-risk systems. Verify that the model provider you intend to use has published GPAI transparency documentation that covers the model you are deploying. If it has not, the conformity assessment path for your high-risk system will be incomplete.

### Step 4: Conformity Assessment Path

For high-risk systems, two conformity assessment paths are available:

**Self-assessment** is available for most Annex III high-risk systems (except biometric systems and AI used in law enforcement). Self-assessment requires: establishing and following a quality management system, completing the technical documentation, meeting all Article 9–15 requirements, and registering the system in the EU database. The quality management system requirements under Article 17 are non-trivial — they include design, development, production, and post-market monitoring processes.

**Third-party conformity assessment** is required for biometric identification systems and AI systems used in law enforcement. For other categories, it may be chosen voluntarily or required by the deploying organisation's risk governance.

The conformity assessment path must be selected and its requirements documented in Stage 1. The requirements flow directly into Stage 2 behavioral specification (data governance, accuracy requirements, human oversight design), Stage 3 evaluation (independent evaluation by notified body or internal quality function), Stage 4 release governance (CE marking, EU database registration), and Stage 5 operational monitoring (post-market monitoring system, incident reporting obligations). A conformity path selected at Stage 4 is not a conformity path — it is a retrofit that will miss requirements embedded in earlier stages.

### Non-EU Jurisdictional Notes

For products deployed or marketed in the United States: the SEC and FINRA have issued guidance on AI in investment advice and broker-dealer contexts. Agents that generate investment recommendations, provide personalised financial guidance, or influence order routing may be subject to investment adviser obligations under the Investment Advisers Act. The regulatory boundary between "information" and "advice" in the AI context is not settled; document the classification analysis and the assumptions it rests on.

For products deployed in the United Kingdom: the FCA has issued guidance on AI in regulated financial advice. The Consumer Duty (PS22/9) imposes positive obligations to act in retail customers' interests, which applies to AI systems interacting with retail customers in financial contexts. For healthcare agents: NHS Digital guidelines and the MHRA software as a medical device (SaMD) framework apply to diagnostic or treatment-influencing AI systems. For US healthcare contexts: FDA SaMD guidance applies to software that qualifies as a medical device under 21 CFR Part 820.

These are not substitutes for qualified regulatory counsel. They are flags for the brief author to confirm that the correct specialist review has occurred before the Conception Gate is passed.

---

## Conception Gate Assessment

The Conception Gate is the decision point that closes Stage 1 and authorises Stage 2 to begin. It is not an approval ceremony — it is a structured assessment of whether the evidence required to govern Stage 2 work exists. A gate passed without evidence is a gate that was not assessed; it is a decision to accept the risk of every subsequent stage being built on an incomplete foundation.

Seven conditions must be satisfied. For each, the brief must contain the specified evidence, and the gate assessor must confirm that it does.

**Condition 1: Business purpose validated.** The brief contains an articulated problem statement, a defined user population, and evidence that the problem is real (not asserted). Evidence may take the form of user research, data analysis, a regulatory mandate with citation, or an executive decision with documented rationale. Acceptability threshold: a qualified person reading the evidence would conclude that the problem warrants investment in an agent product.

**Condition 2: Success criteria measurable.** Each stated success criterion answers four questions: what is measured, what is the target, how is it measured, and what is the baseline. At least one success criterion must be a business-level metric (not a model quality metric) that can be assessed in production. Evaluation proxies (ROUGE scores, task success rates on held-out sets) may supplement but do not replace business-level success criteria.

**Condition 3: Trust architecture complete.** The principal hierarchy is specified with all three tiers (operator, user, system) defined. Hard limits and soft limits are named. Conflict resolution rules for the predictable conflict patterns in the product context are stated. The permission model is specific enough that a Stage 2 specification analyst could derive behavioral requirements from it.

**Condition 4: Persona design coherent.** The persona design addresses all four required questions. The persona is consistent with the behavioral scope defined in the product brief — it neither promises capabilities outside the scope nor denies capabilities within it. EU AI Act Article 50 disclosure obligations are addressed.

**Condition 5: Regulatory classification completed.** The prohibited practices check, the Annex III check, and the GPAI assessment are documented. For each check, the analysis and the conclusion are recorded, not just the conclusion. For high-risk systems, the conformity assessment path is selected and its Stage 2–5 implications are identified. The analysis was reviewed by a qualified person (internal legal/compliance or external counsel as appropriate to the classification result).

**Condition 6: Accountable human named.** A named person accepts product-level accountability for the agent's behavior in production. This is the P12 anchor for the APLC, established at Stage 1. The accountable person owns the success criteria, has reviewed the trust architecture, understands the regulatory classification and its implications, and accepts that their name is associated with this product's outcomes.

**Condition 7: Out-of-scope explicitly stated.** The brief contains at least three specific out-of-scope statements — not category descriptions but specific behavioral exclusions precise enough to derive behavioral requirements from. The out-of-scope statements are consistent with the business purpose and do not exclude things that the success criteria imply the agent must do.

**Condition 8 (Tier 4 systems only): Policy envelope scope specified.** For agent products intended to operate at Tier 4 autonomy, the policy envelope is fully specified in the trust architecture section across all five required dimensions: allowed change classes (with precise definitions), blast radius ceiling (with measurement methodology), required evidence schema for agent actions within the envelope, rollback conditions (with rollback mechanism), and kill-switch configuration. The accountable human has explicitly acknowledged in writing that their accountability is for envelope design rather than per-action approval. The regulatory classification section reflects a Tier 4-specific analysis and confirms that legal review of the autonomy level's classification implications has been completed or is formally scheduled with a date.

**Regulatory Monitoring Subscription.** Before Stage 2 can begin, the organization must establish monitoring subscriptions for every regulatory framework identified in the regulatory classification as applicable to this agent product. The subscription list is registered in the AGKB Knowledge Source Registry by the Regulatory Owner, using regulatory sources as a distinct source category. Required for each applicable framework: the official regulatory body publication feed (official gazette, regulatory authority release RSS, legal database update alert), covering at minimum: the primary regulation (e.g., EU AI Act full text and implementing acts), sector-specific guidance (e.g., EBA guidance for financial services AI), and enforcement decisions from the relevant supervisory authority.

This condition does not require that all regulatory analysis be complete — it requires that the infrastructure for detecting regulatory changes is operational before behavioral specification work begins. A specification written in a regulatory vacuum (without active monitoring for changes to the frameworks it must satisfy) is a specification that becomes stale without warning. Regulatory monitoring subscriptions are a prerequisite for specification currency, not a Stage 5 operational add-on.

For organizations deploying multiple agent products, the same regulatory monitoring subscriptions can serve multiple products — the condition is satisfied by confirming the relevant frameworks are already monitored at the organizational level, not by creating redundant product-level subscriptions.

The gate decision is recorded with the name of the assessor, the date, the conditions satisfied, any conditions deferred with documented rationale, and the conditions that must be satisfied before Stage 2 outputs can advance to Stage 3. A gate decision with deferred conditions is a conditional pass — Stage 2 may begin on the non-deferred components, but Stage 3 cannot begin until the deferred conditions are resolved.

Gate records are retained for the product's operational life plus the jurisdiction's applicable retention period. For EU high-risk AI systems, technical documentation must be retained for ten years after the system is placed on the market.

---

*See also: `aplc.md` (lifecycle overview), `agent-behavioral-specification.md` (Stage 2), `agent-behavioral-evaluation.md` (Stage 3), `agent-release-governance.md` (Stage 4).*

---

## Four Accountability Roles

APLC Stage 1 establishes the four accountability roles that persist for the full lifetime of the agent system, from conception through retirement. These roles are distinct from team structure — one person may hold multiple roles for small systems, or each role may be held by different individuals or organisational units for large systems.

**Business Owner:**
Accountable for: business case, ROI (P11), P1 outcome definition, stakeholder alignment.
Rights: final authority on whether to proceed at Conception Gate; authority to initiate retirement for economic reasons.
Obligations: maintain business case currency throughout the lifecycle; approve specification changes that affect business outcomes; participate in retirement vs. recalibrate decision.

**Behavioral Owner:**
Accountable for: behavioral specification quality, specification currency, evaluation portfolio design, behavioral quality governance.
Rights: final authority on behavioral specification at Behavioral Specification Gate; authority to block release if behavioral quality standards are not met.
Obligations: maintain specification currency through operational feedback; review and approve evaluation suite changes; participate in all gate decisions; maintain reviewer calibration standards.

**Technical Owner:**
Accountable for: architecture (P3), Composite Agent State design, CSH management, context engineering (P7), FinOps technical controls (P11).
Rights: authority over Composite Agent State component selection; authority to block release if CSH integrity is compromised; authority to reject foundation model updates with unacceptable behavioral impact.
Obligations: maintain CSH integrity throughout the lifecycle; compute and record CSH at each gate; perform foundation model impact prediction before updates; ensure behavioral fingerprint baseline is maintained.

**Regulatory Owner:**
Accountable for: regulatory classification, conformity assessment, documentation (Annex IV), GDPR compliance, sector-specific regulatory obligations.
Rights: authority to block Conception Gate if regulatory classification is contested or documentation is insufficient; authority to require additional evaluation for high-risk classification; authority to mandate retirement if compliance cannot be maintained.
Obligations: maintain regulatory classification currency (trigger review on regulatory framework changes); manage GDPR erasure requests; maintain conformity assessment documentation; notify relevant authorities of significant behavioral incidents as required by regulation.

**Accountability Role Continuity:**
Accountability role assignments are recorded at Stage 1 in AGKB and updated whenever assignments change. There must be no gap in role coverage — if a role holder departs, a successor must be named before the departure takes effect. Role vacancies are governance violations detected by the Governance Observability system.

**Accountability Matrix (RACI):**
For each APLC gate decision, a RACI (Responsible, Accountable, Consulted, Informed) is defined by role. This is documented in [[aplc.md]] and the gate-specific documents.

### Governance Role Independence Requirements

Governance decisions are only as trustworthy as the independence of the people making them. The following independence requirements apply to governance role assignments and to specific governance tasks throughout the APLC lifecycle.

**Prohibited role combinations (for the same agent product).** These combinations create conflicts of interest that compromise governance integrity:

- *Behavioral Owner and product owner:* the product owner approves the evaluation clearance report that the Behavioral Owner authored and the behavioral specification that the Behavioral Owner wrote. Separation is required — the product owner must be a different individual from the Behavioral Owner, with no direct reporting relationship between them in either direction.

- *Waiver grantor and gate approver for the same gate:* the person who approves a waiver and the person who approves the gate that the waiver enables must be different individuals. Approving your own waiver — clearing a condition you yourself granted an exemption for — eliminates the oversight function.

- *Red-team lead and anyone who built the system:* the red-team lead for any given release may not have contributed to any of: the system prompt, the behavioral specification, or the evaluation suite design for that release cycle. Adversarial testing requires a perspective unconstrained by builder assumptions.

**Disclosure and management.** At the start of any gate assessment, evaluation review, or red-team exercise, each participant must disclose any potential conflict of interest — including organizational reporting relationships, prior involvement in the product's development, financial interests in deployment timelines, and any other relationship that could compromise independence. Undisclosed conflicts discovered after a governance decision require that decision to be re-reviewed by a conflict-free panel.

**Conflict discovered mid-process.** When a conflict of interest is identified after a governance role has already been filled (e.g., the designated red-team lead joins the product team), the role must be reassigned immediately. Decisions made while the conflict was present but undisclosed require a retrospective review to determine whether the conflict materially affected the decision. The retrospective review finding is filed in the AGKB alongside the original decision record.
