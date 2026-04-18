# Agent Regulatory Classification

*Cross-cutting governance for agent products. Produced at Stage 1; informs all subsequent stages.*

See [aplc.md](../aplc.md) for the lifecycle overview.
See [agent-conception.md](agent-conception.md) for Stage 1 inputs and the Agent Product Brief.
See [agent-behavioral-specification.md](agent-behavioral-specification.md) for Stage 2 design constraints that regulatory classification imposes.
See [agent-release-governance.md](agent-release-governance.md) for Stage 4 gate conditions — including the EU Declaration of Conformity — that depend on the outputs of this document.

---

## Why Regulatory Classification Must Happen at Stage 1

Regulatory classification is not a compliance exercise to complete before launch. It is a design constraint that shapes every stage of the lifecycle from Stage 1 forward. Organizations that treat regulatory classification as a late-stage checklist item discover its consequences at the worst possible time — when a high-risk finding requires reworking artifacts that have already been built and reviewed across multiple stages.

The consequences propagate through every stage:

The **behavioral specification** at Stage 2 must include human oversight measures, uncertainty protocols, and escalation design that satisfy the technical requirements for the risk class. A behavioral specification written without knowing the applicable conformity requirements will not contain these elements at the right level of depth. Adding them retroactively requires re-opening and re-reviewing the specification, which re-opens the evaluation portfolio that was built against it.

The **evaluation portfolio** at Stage 3 must cover mandatory evaluation categories specific to the risk class. For EU AI Act high-risk systems, these include accuracy and robustness across demographic groups, fairness assessments, and adversarial robustness testing. A Stage 3 evaluation plan built without knowing that these categories are mandatory will not include them. Discovering the gap at Stage 4 means extending the evaluation, which delays the release and may require re-running evaluations already completed against a specification that has since changed.

The **release gate** at Stage 4 has hard documentation conditions for high-risk AI systems under the EU AI Act: the EU Declaration of Conformity is a gate condition that cannot be filed without the technical documentation produced across Stages 2 and 3. If those stages did not produce conformity-ready documentation because the classification was not known, the release gate cannot be passed. The path forward is rework, not expedited documentation.

**Post-market surveillance** obligations at Stage 5 are specified by regulation for high-risk AI systems — monitoring frequency, serious incident reporting timelines, periodic conformity review requirements. An operations plan built without knowing these obligations will not be designed to satisfy them.

**Retention requirements** at Stage 7 are longer for high-risk AI systems and subject to specific format requirements in some jurisdictions. A retirement plan that did not account for extended retention will have made archive and deletion decisions that cannot be undone.

The cost of early classification is a few hours of structured analysis at Stage 1. The cost of late classification is measured in stages of rework. There is no scenario in which delaying classification is economical.

---

## EU AI Act Classification Workflow

Work through these four steps in order. Document the result of each step. The classification document is an artifact of [agent-conception.md](agent-conception.md) and must be referenced in the Agent Product Brief.

---

### Step 1 — Prohibited Practices Check (Article 5)

Article 5 of the EU AI Act establishes an absolute prohibition on certain AI practices in EU markets. These are not high-risk categories requiring conformity assessment — they are practices that cannot be deployed at all. No conformity documentation, no notified body, no Declaration of Conformity changes this. If a use case falls under Article 5, it cannot be deployed in the EU.

For agent products, the most relevant Article 5 prohibitions are:

**Subliminal manipulation** — AI systems that deploy subliminal techniques beyond a person's consciousness to materially distort behavior in a way that causes or is likely to cause harm. An agent product that is designed to influence user decisions through framing, urgency creation, or information asymmetry exploitation — rather than transparent information delivery — requires a careful Article 5 analysis. The test is not whether the agent uses persuasive language; the test is whether it operates below the threshold of conscious awareness to produce behavior harmful to the person.

**Exploitation of vulnerabilities** — AI systems that exploit specific characteristics of groups (age, disability, social or economic situation) to distort behavior in a harmful way. An agent product serving vulnerable populations (elderly users, minors, people in financial distress, people seeking mental health support) requires explicit analysis of whether its design could constitute exploitation under Article 5(1)(b).

**Social scoring** — AI systems used by public authorities or on their behalf for the evaluation or classification of individuals based on social behavior, leading to detrimental treatment in unrelated contexts. This prohibition applies to public authority use cases. A private enterprise agent product that performs behavioral scoring for internal purposes is not automatically covered, but borderline cases require regulatory counsel.

**Real-time remote biometric identification in publicly accessible spaces** — for law enforcement purposes, subject to narrow exceptions. An agent product that integrates with live video feeds or biometric sensors in public spaces for identification purposes requires direct legal analysis.

**Document the check result for each prohibition category.** The documentation must state: the category, the assessment (in-scope / out-of-scope / borderline), the reasoning, and the name of the person who performed the assessment. Borderline assessments require regulatory counsel before Stage 2 begins.

---

### Step 2 — Annex III High-Risk System Check

Annex III of the EU AI Act enumerates categories of AI systems classified as high-risk. The classification is binary: either the agent product's use case falls within a listed category, or it does not. Operators cannot negotiate their way to a lower risk classification through design choices — if the use case is in scope, the high-risk requirements apply regardless of how carefully the system is built.

For each Annex III category, assess: **in scope / out of scope / borderline (requires further analysis)**.

**1. Biometric identification and categorisation systems.** Systems intended for remote biometric identification of natural persons, and systems intended to categorise individuals by biometric data according to sensitive attributes. Agent products that process voice, face images, or behavioral biometrics to identify or profile users require direct Annex III analysis.

**2. Critical infrastructure.** AI systems intended to be used as safety components in the management of critical infrastructure: road traffic, rail, water supply, gas, heating, electricity grid. Agent products that interface with operational technology, SCADA systems, or infrastructure control planes in any of these sectors are in scope.

**3. Education and vocational training.** Systems intended for determining access to educational institutions, evaluating learners, assessing the level of education, and detecting prohibited behavior. An agent product used by an educational institution to score assessments, recommend or filter applicants, or monitor student behavior in examinations is in scope.

**4. Employment and worker management.** Systems intended for recruitment or selection, including screening applications, evaluating candidates, and making decisions affecting terms of employment. An agent product used in any part of the hiring pipeline — initial screening, resume ranking, interview scheduling, assessment scoring — is in scope. Agent products used for performance monitoring, task allocation, or evaluation of employee conduct may also be in scope depending on the materiality of the decisions.

**5. Access to essential private services and public services and benefits.** Systems intended for evaluating creditworthiness, establishing credit scores, assessing risk and pricing in life and health insurance, and evaluating and classifying emergency calls. This category covers a substantial portion of financial services and insurance agent use cases. An underwriting agent, a credit recommendation agent, a claims triage agent, or a benefits eligibility agent is likely in scope and must be assessed against the full Annex III requirements.

**6. Law enforcement.** Systems intended for individual risk assessment, polygraph-type tools, evaluation of the reliability of evidence, crime analytics, and prediction of criminal offenses. Applicable to public sector law enforcement deployments. Private sector agent products with fraud detection or risk-scoring functions are not automatically covered under this category but may overlap with Category 5 (creditworthiness and insurance pricing).

**7. Migration, asylum, and border control.** Systems used for risk assessment of individuals applying for asylum, visa, or residence permits; for detecting undeclared items; and for automated examination of visa and permit applications. Public sector use cases primarily.

**8. Administration of justice and democratic processes.** Systems intended to assist judicial authorities in researching and interpreting facts and law, applying the law to a specific set of facts, and influencing the outcome of elections and voting behavior. Legal research agent products that go beyond information retrieval to provide case outcome predictions or legal strategy recommendations require careful Annex III analysis.

**9. Democratic processes.** Systems intended to influence elections and voting behavior, including targeting voters. This is a distinct sub-category from Category 8. Political messaging agents, voter outreach agents, and political advertising optimization agents are in scope.

For each category, the borderline determination is not a judgment that the agent product is probably fine. It is a determination that regulatory counsel must review the specific use case before Stage 2 begins. The APLC does not proceed past Stage 1 on a borderline Annex III determination without that review.

---

### Step 3 — General-Purpose AI (GPAI) Assessment

Title VIII of the EU AI Act governs providers and operators of general-purpose AI models. A GPAI model is a model trained on broad data, at significant compute, that exhibits generality of function and can be used for a wide range of tasks. The foundation models underlying most agent products — GPT-4o, Claude, Gemini, Llama, Mistral, and their derivatives — are GPAI models.

The GPAI assessment has two distinct components:

**Component A — Provider obligations.** GPAI model providers have their own obligations under Title VIII. These obligations belong to the provider (e.g., Anthropic, OpenAI, Google) not to the operator deploying an agent product built on top of the model. Operators do not inherit provider obligations, but they must confirm that the provider is compliant — particularly for high-risk downstream deployments. Document the GPAI model provider and confirm whether they have published a compliance summary or policy classification document. For major providers, this information is typically available in their EU AI Act compliance statements.

**Component B — Systemic risk.** Certain GPAI models are classified as posing systemic risk (currently, models trained with compute exceeding 10^25 FLOPs). Operators using systemic-risk GPAI models have additional transparency and documentation obligations at the system level. Identify whether the foundation model underlying the agent product is classified as a systemic-risk GPAI model. If the provider's model classification is not publicly available, document the inquiry and the response received.

**Operator obligations at the system level.** Regardless of systemic risk classification, operators using GPAI models to build AI systems have obligations to:
- Implement appropriate technical and organizational measures to ensure their downstream AI system complies with applicable obligations
- Document the GPAI model used and its characteristics in the technical documentation
- Maintain the information necessary to demonstrate compliance

Document the GPAI model, its provider, its current compliance classification, and whether systemic risk requirements apply. This documentation feeds directly into the technical documentation requirements at Stage 3 and Stage 4.

---

### Step 4 — Conformity Assessment Path

Having completed Steps 1 through 3, the classification outcome is one of: prohibited (Article 5), high-risk (Annex III), minimal or no risk (not Annex III), with a GPAI overlay where applicable. For non-prohibited, high-risk systems, determine the conformity assessment path.

**Internal control with EU AI database registration (Annex VI):** The default conformity assessment path for most Annex III categories. The operator conducts an internal conformity assessment — verifying that the AI system satisfies all applicable requirements — and registers the system in the EU AI Office database before market placement. The technical documentation produced across the APLC stages is the basis for the internal assessment. No third party is involved except where explicitly required.

**Third-party conformity assessment (Annex VII):** Mandatory for high-risk AI systems in two categories: (1) biometric identification systems, and (2) AI systems used in critical infrastructure where the AI system is the safety component. For these categories, a notified body (an accredited third-party conformity assessment body) must review the technical documentation and issue a conformity assessment certificate. The notified body review is a gate condition: the EU Declaration of Conformity cannot be issued without it.

**Self-certification with notified body consultation:** Some organizations in regulated industries elect third-party review even when not required, to support regulatory filings in concurrent jurisdictions (e.g., a financial services firm seeking to satisfy both EU AI Act and FCA expectations for AI systems in financial services). This is a governance decision, not a legal requirement. Document the rationale if elected.

The conformity assessment path must be determined at Stage 1 and documented in [agent-conception.md](agent-conception.md). If the path requires a notified body, the engagement timeline must be incorporated into the Stage 4 release plan — notified body review has lead times that cannot be compressed at the last moment.

---

## Technical Documentation Requirements (Annex IV)

For high-risk AI systems, Article 11 of the EU AI Act requires technical documentation to be established before market placement and kept up to date throughout the lifecycle. Annex IV specifies the content. The APLC produces this documentation systematically across its stages — the table below maps each Annex IV requirement to the stage and document that satisfies it.

| Annex IV Requirement | APLC Stage | APLC Document |
| --- | --- | --- |
| General description of the AI system, intended purpose, the version, and how it interacts with hardware or software | Stage 1 | [agent-conception.md](agent-conception.md) — Agent Product Brief |
| Description of the development process, including design choices and technical solutions adopted | Stage 2–3 | [agent-behavioral-specification.md](agent-behavioral-specification.md), [agent-behavioral-evaluation.md](agent-behavioral-evaluation.md) |
| Detailed description of the system's components and the process for development, including data governance where training data is used | Stage 2–3 | [agent-behavioral-specification.md](agent-behavioral-specification.md), [agent-behavioral-evaluation.md](agent-behavioral-evaluation.md) |
| Assessment of human oversight measures and how they are implemented | Stage 2 | [agent-behavioral-specification.md](agent-behavioral-specification.md) — Escalation Design |
| Accuracy, robustness, and cybersecurity measures and their validation | Stage 2–3 | [agent-behavioral-specification.md](agent-behavioral-specification.md), [agent-behavioral-evaluation.md](agent-behavioral-evaluation.md) |
| Description of the risk management system | Stages 1–2 | [agent-conception.md](agent-conception.md), [agent-behavioral-specification.md](agent-behavioral-specification.md) |
| Monitoring, functioning, and control of the AI system | Stages 4–5 | [agent-release-governance.md](agent-release-governance.md), [agent-operations.md](agent-operations.md) |
| Changes to the system throughout the lifecycle, including post-market changes | Cross-cutting | [agent-composite-versioning.md](agent-composite-versioning.md) |
| List of standards applied and description of solutions adopted to comply with requirements where standards were not applied | Stages 1–4 | This document, [agent-behavioral-specification.md](agent-behavioral-specification.md), [agent-release-governance.md](agent-release-governance.md) |
| Copy of the EU Declaration of Conformity | Stage 4 | [agent-release-governance.md](agent-release-governance.md) — Stage 4 gate artifact |
| Post-market monitoring plan | Stage 5 | [agent-operations.md](agent-operations.md) |

The technical documentation must be in a language accepted by the relevant market surveillance authority of the member state. For operators placing AI systems in multiple EU member states, confirm language requirements at Stage 1 rather than at Stage 4.

Technical documentation must be retained for ten years after the AI system has been placed on the market or put into service. This retention period feeds directly into the Stage 7 retirement planning in [agent-retirement.md](agent-retirement.md). If the organization's standard document retention policy is shorter than ten years, an exception must be documented at Stage 1 and the archive plan built accordingly.

---

## GDPR Article 22

Article 22 of the GDPR grants individuals the right not to be subject to decisions based solely on automated processing that produce legal effects or similarly significant effects. For agent products that make or contribute to decisions affecting individuals — credit, employment, insurance, medical, benefits, educational outcomes — Article 22 is a direct design constraint, not a disclosure obligation.

The three Article 22 requirements map to specific APLC design obligations:

**Right to explanation.** The individual must be able to receive a meaningful explanation of the logic involved in any automated decision. An agent product that cannot explain in plain language why it reached a conclusion is non-compliant for decisions within Article 22 scope — regardless of how accurate the decisions are. This requirement must be incorporated into the behavioral specification at Stage 2 in [agent-behavioral-specification.md](agent-behavioral-specification.md): the agent's uncertainty protocol and reasoning exposition are not optional design features, they are Article 22 compliance requirements. At Stage 5, the HITL workflow in [agent-operations.md](agent-operations.md) must include an explanation generation step — human reviewers handling escalated cases must be able to produce the explanation the affected individual is entitled to receive.

**Right to human review.** The individual must be able to obtain human intervention and express their point of view. An escalation path that is theoretically available but practically inaccessible — hidden, slow, unadvertised, or routed to a queue that is never cleared — does not satisfy Article 22. The escalation design at Stage 2 must provide a functioning, reachable human review path. At Stage 5, the HITL queue must have defined service levels that make the right to human review real, not nominal.

**Prohibition on solely automated decisions in specific contexts.** Article 22(4) prohibits solely automated decisions based on special category data (genetic data, health data, racial or ethnic origin, political opinions, religious beliefs, sexual orientation, and related categories) except where the individual has given explicit consent or where Member State law provides for it. The prohibition is not limited to decisions that produce legal effects — it applies to any significant effect. For agent products in financial services, healthcare, insurance, and HR, this prohibition is the binding constraint: if the agent's decisions are based on special category data and the decision is significant, a human must be in the decision loop — not available on request, but actually in the loop for every decision of that type. This requirement must be encoded in the trust architecture defined at Stage 1 in [agent-conception.md](agent-conception.md). It cannot be added at Stage 5 without revisiting the trust architecture.

Document the Article 22 scope determination at Stage 1: which of the agent product's decisions are within Article 22 scope, which involve special category data, and what the mandated decision path is for each. These determinations are design inputs to Stage 2, not compliance footnotes added at Stage 4.

---

## Sector-Specific AI Regulatory Requirements

The EU AI Act and GDPR are jurisdiction-specific instruments. Agent products deployed in regulated sectors also operate under sector-specific regulatory frameworks that impose model governance, validation, and change control requirements independent of EU AI Act classification. The following summaries identify the primary frameworks for each sector. They are cross-references, not interpretations: each requires qualified regulatory counsel for the specific jurisdiction, entity type, and use case.

---

### Financial Services

**SR 11-7 (Federal Reserve Supervisory Guidance on Model Risk Management).** SR 11-7 governs model risk management for banking organizations supervised by the Federal Reserve and OCC. Its scope is broad: any quantitative method, computational algorithm, or approach that produces estimates or predictions used in business decisions. An agent product that produces recommendations or decisions in credit, trading, portfolio management, risk assessment, or regulatory capital calculation is a model under SR 11-7. The three SR 11-7 pillars — conceptual soundness, ongoing monitoring, and model change governance — map directly to APLC stages:

- Conceptual soundness: the theoretical basis and empirical support for the agent's behavioral logic. Established through the behavioral specification at Stage 2 and the evaluation portfolio at Stage 3. For SR 11-7 purposes, this includes documentation of the limitations and assumptions embedded in the agent's reasoning, which must be explicit in [agent-behavioral-specification.md](agent-behavioral-specification.md).
- Ongoing monitoring: performance monitoring, input data quality monitoring, and behavioral drift detection. Governed by Stage 5 in [agent-operations.md](agent-operations.md). SR 11-7 requires that monitoring is ongoing, not periodic — the Stage 5 monitoring plan must satisfy this requirement.
- Model change governance: SR 11-7 distinguishes material model changes (requiring full validation) from minor changes (requiring lighter review). The composite versioning model in [agent-composite-versioning.md](agent-composite-versioning.md) provides the audit trail that demonstrates which changes were made and which change governance tier was applied. For high-risk banking models, independent validation (organizationally separate from the development team) is required for material changes — this is the same requirement as the EU AI Act Annex IV independent review requirement, satisfied in the same way.

**FCA PS22/3 / FCA AI and Machine Learning in Financial Services.** The FCA's expectations for AI and ML systems in UK financial services firms. The FCA expects firms to be able to explain AI-driven decisions to customers, to monitor for model drift, to maintain governance records, and to subject material AI changes to the firm's model risk management framework. The APLC's complete artifact chain — from Stage 1 conception through Stage 6 recalibration — constitutes the governance record the FCA expects to see.

**MiFID II.** For agent products providing investment advice or portfolio management, MiFID II requirements on appropriateness and suitability apply to the agent's recommendations. The agent's recommendation logic must satisfy the same disclosure, client suitability, and conflict-of-interest requirements as human advisors providing equivalent recommendations. For robo-advice and hybrid-advice agent products, MiFID II is a concurrent regulatory constraint alongside the EU AI Act — the two frameworks must be satisfied simultaneously, not sequentially.

**Solvency II model governance (insurance).** Insurance undertakings operating under Solvency II must demonstrate that models used in the Solvency Capital Requirement calculation satisfy governance requirements: documentation, validation, independent review, and change control. An agent product used in SCR calculation or in underwriting decisions that feed the technical provisions is subject to Solvency II Article 48 model governance requirements. The conformity documentation produced by the APLC must address Solvency II requirements for these use cases, not only EU AI Act requirements.

---

### Healthcare and Medical Devices

**FDA Software as a Medical Device (SaMD) — US.** The FDA applies its SaMD framework to software that is intended to be used for a medical purpose without being part of a hardware medical device. The classification question for agent products is: does the agent's output (recommendation, diagnosis, treatment suggestion, risk score) constitute software intended to diagnose, prevent, monitor, treat, or cure disease or other conditions? If yes, the agent product is a medical device under 21 CFR Part 820, and the applicable regulatory pathway must be determined at Stage 1.

The three SaMD risk tiers (based on state of healthcare situation and significance of information provided) map to different regulatory pathways:
- SaMD providing information to drive clinical management in a critical situation: highest risk tier, most rigorous pathway
- SaMD providing information to inform clinical management in a serious situation: medium tier
- SaMD providing information for non-serious situations: lowest tier

The regulatory pathway determination — 510(k) clearance, De Novo classification, or PMA approval — affects the entire technical documentation structure, the clinical validation requirements at Stage 3, and the post-market surveillance requirements at Stage 5. An agent product that requires a 510(k) clearance cannot be released without it; building the entire APLC evidence chain before determining whether a 510(k) is required is a significant avoidable risk.

**MDR (EU Medical Device Regulation) Article 22 — EU.** The MDR treats standalone software that qualifies as a medical device as a software-based medical device (SBMD), subject to conformity assessment and CE marking. The MDR risk classification for SBMD uses the MEDDEV 2.1/6 guidelines: Rules 9–13 of the MDR risk classification rules apply. For AI-driven diagnostic or treatment support agent products, the MDR classification must be determined alongside the EU AI Act classification at Stage 1. The two frameworks have different technical documentation requirements and different conformity assessment paths; for agent products in scope of both, the technical documentation must satisfy both.

**Clinical validation.** For diagnostic or treatment-recommendation agent products, clinical validation is not an evaluation category within the APLC's standard evaluation portfolio — it is a distinct clinical evidence requirement with its own methodology, statistical power requirements, and regulatory review process. Clinical validation must be planned at Stage 1, designed at Stage 2, and completed before Stage 4 regardless of the APLC's internal evaluation timeline. If clinical validation requires randomized controlled trial data or real-world evidence studies, the timeline extends well beyond the software development cycle and must be incorporated into the product plan before Stage 2 begins.

---

### Insurance

**Solvency II and EIOPA guidelines.** As noted in the financial services section, Solvency II model governance applies to insurance undertakings. EIOPA has published guidelines specifically addressing the use of AI and ML in insurance (EIOPA Opinion on Artificial Intelligence Governance and Risk Management, 2021, and subsequent guidance), which expand on the Solvency II model governance requirements in the AI context. These guidelines apply to all material AI systems — not only those in the SCR calculation — including customer-facing systems used for pricing, underwriting, and claims.

**Claims agent.** A claims processing or settlement agent that produces coverage determinations affects individuals' rights to insurance benefits. This use case is in scope for EU AI Act Annex III Category 5 (access to essential private services) and for GDPR Article 22 if special category data (e.g., health information for a health insurance claim) is involved. The trust architecture at Stage 1 must account for both.

**Underwriting agent.** An underwriting agent that produces risk assessments and pricing recommendations is a pricing model under Solvency II and an Annex III system under the EU AI Act. For personal lines insurance, underwriting agents may also be subject to indirect discrimination obligations under applicable national law — the use of proxy variables correlated with protected characteristics in pricing models has been subject to regulatory scrutiny across multiple jurisdictions.

**Customer advisory agent.** An agent product that provides coverage advice to policyholders or prospects may be subject to insurance intermediary requirements under the IDD (Insurance Distribution Directive) — specifically, the requirements for suitability assessment, disclosure, and conflict-of-interest management. Whether the agent constitutes an insurance intermediary under the IDD depends on jurisdiction-specific analysis. This determination must be made at Stage 1.

---

### HR and Employment

**EU AI Act Annex III — employment and worker management.** As noted in the Annex III assessment step, recruitment, selection, and employment management AI systems are listed in Annex III. An agent product used in the hiring pipeline is a high-risk AI system under the EU AI Act regardless of the size of the deploying organization, the seniority of the role being filled, or the degree to which humans are involved in the final decision. The high-risk classification applies to the system, not to the final hiring decision.

**EEOC guidance on AI in hiring (US).** The US Equal Employment Opportunity Commission has published technical assistance guidance confirming that employers are responsible for unlawful employment discrimination even when the discriminatory output is produced by an AI system developed or administered by a third party. The legal exposure belongs to the employer, not to the AI vendor. This means that an agent product's evaluation portfolio at Stage 3 must include disparate impact analysis across protected classes as a mandatory evaluation category for employment-use deployments — not an optional one.

**Automated decision-making and the right to contestability.** In EU deployments, GDPR Article 22 applies to employment screening decisions. In US deployments, a growing number of state and city laws (New York City Local Law 144, Illinois AI Video Interview Act, Colorado employment AI law) impose disclosure, bias audit, and contestability requirements for automated employment decision tools. These requirements must be identified in the regulatory classification document at Stage 1 because they impose specific behavioral requirements — explainability of rankings, auditability of scoring criteria, availability of human review — that must be built into the behavioral specification at Stage 2. They cannot be bolted on after the fact.

**Indirect discrimination through proxy variables.** Agent products that use data correlated with protected characteristics — postal code, educational institution attended, time gaps in employment history, communication style features — may produce disparate impact outcomes on protected groups even when the agent's explicit logic does not reference protected characteristics. The evaluation portfolio at Stage 3 must include proxy variable analysis as a standard category for all employment-use agent products. This analysis must be documented and available for regulatory examination.

---

## EU Declaration of Conformity

For high-risk AI systems under the EU AI Act, a Declaration of Conformity (EU DoC) is required before the system is placed on the market or put into service. The EU DoC is a formal legal document — not a compliance summary, not an internal policy — that the operator signs and files in the EU AI Office database.

The EU DoC must state:
- The AI system's identity: name, type, version identifier, and description of intended purpose
- That the AI system conforms to the requirements of the EU AI Act applicable to it
- The conformity assessment procedure followed (Annex VI internal assessment, or Annex VII third-party assessment with notified body certificate reference)
- The notified body name, identification number, and certificate reference (if third-party assessment was required)
- The signatory's name, role, and the date and place of signature

The EU DoC must be updated whenever a material change is made to the AI system. A material change is one that affects the system's compliance with the applicable requirements or changes its intended purpose. The composite versioning model in [agent-composite-versioning.md](agent-composite-versioning.md) provides the change record that informs whether a material change has occurred and whether the EU DoC requires updating.

**Stage 4 gate condition.** For high-risk AI systems, the EU DoC is a Stage 4 gate condition per [agent-release-governance.md](agent-release-governance.md). The release gate does not open without a filed EU DoC. The EU DoC cannot be filed without the technical documentation that the APLC has produced across Stages 1 through 4. If the conformity assessment path requires a notified body, the notified body certificate is a prerequisite for the EU DoC and must be obtained before the Stage 4 gate review is scheduled.

For high-risk AI systems in the financial services sector, the EU DoC does not substitute for sector-specific regulatory filings (model validation documentation, change records under the firm's model risk management framework, DORA-required change records). Both the EU DoC and the sector-specific filings are required. Document the filing checklist at Stage 1 and confirm each filing is completed at Stage 4.

The EU DoC must be kept for ten years after the AI system is placed on the market, consistent with the Annex IV technical documentation retention requirement. The EU DoC retention requirement is a Stage 7 planning input per [agent-retirement.md](agent-retirement.md).

---

*Regulatory classification at Stage 1 is not risk management theater. It is the act of understanding what the agent product actually is — in the eyes of the applicable legal frameworks — before investing in building it. The frameworks do not care when you discover their requirements. They care that you satisfied them. Discovering them at Stage 1 gives you the entire lifecycle to satisfy them. Discovering them at Stage 4 gives you a rework problem and a delayed release. Discovering them after deployment gives you a compliance violation.*
