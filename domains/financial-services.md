# APLC Domain Guidance — Financial Services

*Financial services-specific regulatory guidance for agent products deployed in financial services.*

See the Financial Services manifesto alignment for manifesto principle mappings.
See the [APLC Overview](../aplc.md) for the full agent product lifecycle framework.

---

## APLC Regulatory Guidance

*This section addresses product-level AI regulatory requirements that apply to
deployed agent products in financial services — distinct from the ASDLC
process-level requirements covered in the sections above. The question answered
here is: when you deploy an agent product in financial services, what applies
to the agent itself?*

See
[agent/agent-regulatory-classification.md](../agent/agent-regulatory-classification.md)
for the full EU AI Act classification workflow and Annex IV technical
documentation requirements. See
[agent/agent-conception.md](../agent/agent-conception.md) for trust architecture
design and the Stage 1 Conception Gate.

### AI System Classification

Common agent product types in financial services and their EU AI Act Annex III
classifications:

**Credit decisioning agents** are high-risk under Annex III §5(b) — "AI systems
intended to be used to evaluate the creditworthiness of natural persons or
establish their credit score, with the exception of AI systems used for the
purpose of detecting financial fraud". [Point corrected 2026-09-05: this
paragraph previously placed insurance risk assessment and pricing, and claims
processing, inside §5(b). Insurance risk assessment and pricing is §5(c) and is
limited on its face to "life and health insurance"; claims processing is in
neither point. No Annex III classification is asserted here for claims
processing agents — see `domains/insurance.md`, where the same withdrawal is
recorded.] Agent products that are high-risk under §5(b) require full high-risk
conformity documentation and EU database registration before market
placement.

**Customer advisory agents** require classification analysis at Stage 1. An
agent that provides analysis for a human advisor to act upon is not necessarily
Annex III. An agent whose output constitutes the recommendation delivered to
the customer — without meaningful human intervention in the recommendation
itself — is a candidate for Annex III §5(b) only if the recommendation
evaluates the creditworthiness of a natural person or establishes a credit
score, which is the whole of what §5(b) reaches; "essential financial services"
is not a criterion in that point's text, and "access to and enjoyment of
essential private services and essential public services and benefits" is the
heading of point 5 rather than an operative test. Binding recommendations
evaluating creditworthiness are high-risk under §5(b); binding recommendations
on insurance risk are high-risk under §5(c) only for life and health insurance;
informational responses that do neither require case-by-case analysis.

**Fraud detection agents** do not fall under Annex III §5(b): that point ends
"with the exception of AI systems used for the purpose of detecting financial
fraud", so the instrument excepts them from it expressly. [Classification
withdrawn 2026-09-05: this paragraph previously stated that fraud detection
agents may fall under §5(b) where fraud decisions affect customer account
access, which inverts the point's own exception.] They may fall under Annex III
§6 where deployed by public-authority partners in law enforcement contexts.
Private enterprise fraud detection that triggers account restriction without
binding legal effect is not automatically Annex III, but it requires documented
classification analysis at Stage 1 — an analysis that does not route through
§5(b).

**Trading agents** and **AML monitoring agents** do not fit cleanly into
Annex III categories designed for individual access decisions. Trading agents may
affect individuals indirectly through market impacts, but §5(b) reaches only
the evaluation of a natural person's creditworthiness or the establishment of
their credit score, which a trading agent does not perform. AML agents
producing SAR filing recommendations do not perform creditworthiness evaluation
either, so §5(b) is not the point to analyse them against. [Analysis withdrawn
2026-09-05: this paragraph previously characterised §5(b) as "focused on
individual access to essential services" — that is the heading of point 5, not
the text of §5(b) — and directed AML agents to be analysed against §5(b).
Whether either agent type is high-risk on another basis is not asserted here.]
Document the classification analysis; do not assume out-of-scope.

**Regulatory reporting agents** are typically out of Annex III scope when they
produce documentation for institutional use, not decisions about individuals.
Minimal-risk classification is appropriate for agents that draft, cross-check,
or format regulatory reports, subject to the downstream duties by role
described in
[agent/agent-regulatory-classification.md](../agent/agent-regulatory-classification.md).

### Conformity Requirements

For high-risk agent products, the technical documentation requirements under EU
AI Act Annex IV are non-negotiable. The APLC produces this documentation
systematically: the Agent Product Brief (Stage 1) satisfies general system
description requirements; the behavioral specification (Stage 2) satisfies
design choice and human oversight documentation; the evaluation portfolio
(Stage 3) satisfies accuracy, robustness, and fairness assessment
documentation; the composite state manifest (Stage 4) satisfies configuration
and change documentation; and the operations plan (Stage 5) satisfies
post-market monitoring documentation.

**SR 11-7 model documentation** applies to agent products meeting the SR 11-7
model definition — any quantitative method producing estimates used in
financial decisions. The APLC's behavioral baseline, evaluation portfolio, and
composite state manifest together satisfy SR 11-7's conceptual soundness,
validation, and model change governance requirements. The independent
validation gate (Stage 3) maps to SR 11-7's independent validation requirement:
the validation function must be organizationally separate from the development
team for high-materiality models.

**MiFID II appropriateness and suitability documentation** applies to customer
advisory agent products providing investment-related recommendations. The
behavioral specification must document how the agent assesses and satisfies
MiFID II appropriateness criteria; this documentation is an EU AI Act Annex IV input. For
robo-advice agent products, the MiFID II disclosure requirements apply to the
agent product's user interface and output format, not only its internal logic.

**FCA Consumer Duty** requires demonstrable evidence that retail-facing agent
products deliver good outcomes for customers. The APLC's output quality rate
SLO and the ongoing monitoring plan (Stage 5) constitute the Consumer Duty
monitoring evidence. The SLO must be calibrated against customer outcome
metrics, not only technical accuracy metrics.

The conformity assessment path for most financial services high-risk agent
products is internal control (EU AI Act Annex VI), followed by registration of the
provider and the system under Article 49(1) in the EU database for high-risk
AI systems that the Commission maintains under Article 71 — a register the
AI Office does not hold. EU AI Act Article 49(1) excepts Annex III point 2 (critical
infrastructure) systems from that registration. Under the
EU AI Act, third-party conformity assessment (Annex VII) is not required for
Annex III §5(b) systems. However, several financial services firms elect third-party
review to satisfy concurrent FCA or PRA expectations for AI systems in
regulated financial services. Document the election rationale at Stage 1.

### Automated Decision-Making Governance

GDPR Article 22 applies to agent products whose decisions are solely automated,
produce legal or similarly significant effects, and concern individual data
subjects. In financial services, this covers:

- Credit decisions, limit-setting, and loan approvals made or substantially
  shaped by the agent without meaningful human involvement
- Insurance risk assessments and premium determinations that significantly
  affect individual policyholders
- Financial advice that, taken as a whole, constitutes the advice delivered to
  the customer rather than an input to a human advisor's decision

For each decision type within scope, the trust architecture defined at Stage 1
must provide: (1) a meaningful human review path — not a nominal override
button, but an accessible and functioning process through which the individual
can obtain human involvement; (2) an explanation generation capability that can
produce, in plain language, the reasoning behind the decision; and (3) a
contestation workflow that routes the individual's challenge to a human
reviewer with the authority and the HITL queue visibility to re-examine the
decision.

GDPR Article 22(4) provides that decisions **referred to in Article 22(2)**
shall not be based on special category data — health data, genetic data, racial
or ethnic origin, political opinions, religious beliefs, sexual orientation —
"unless point (a) or (g) of Article 9(2) applies and suitable measures to
safeguard the data subject's rights and freedoms and legitimate interests are in
place". The two gateways are Article 9(2)(a) (explicit consent) and Article
9(2)(g) (necessary for reasons of substantial public interest, on the basis of
**Union or Member State law** which is proportionate, respects the essence of
the right and provides suitable and specific safeguards) — not any Member State
law that "provides for it" — and the safeguards condition applies in addition to
whichever gateway is relied on. For life and
health insurance agent products processing health data, this prohibition is the
binding design constraint: the trust architecture must route every decision
based on special category data through a human in the decision loop, not merely
make human review available on request.

The hard autonomy caps table in this document reflects these constraints for
key financial services use cases. Those caps are regulatory floors; they do not
change with organizational maturity phase.

### Ongoing Monitoring Requirements

For high-risk agent products under EU AI Act Article 72, a post-market
monitoring plan is a mandatory technical documentation element. The APLC's
operations plan (Stage 5) constitutes this plan when it addresses: the output
quality rate SLO and its measurement methodology, behavioral drift detection
and its thresholds, data distribution shift monitoring, and the escalation path
from monitoring anomaly to human review.

**SR 11-7 ongoing monitoring** requires that the monitoring is genuinely
continuous in production — not periodic reporting on a quarterly basis. The
output quality rate SLO must be measured in production, with alerting that
fires within an operationally meaningful interval when the SLO is breached. A
quarterly review that relies on aggregated metrics rather than ongoing
production measurement does not satisfy SR 11-7's ongoing monitoring
requirement.

**FCA Consumer Duty** requires periodic review of whether the agent product is
delivering good customer outcomes. This must be a distinct review from
technical accuracy monitoring: it must assess whether the agent's decisions are
producing outcomes that a reasonable person would consider fair, and whether
the agent's behavior toward vulnerable customers is appropriate. The steward's
value realisation monitoring at Stage 5 must include consumer outcome review
for retail-facing agent products.

**Solvency II** model monitoring and validation requirements apply to agent
products used in SCR calculation or underwriting decisions feeding technical
provisions. Model validation by an independent validation function is
required: Solvency II Article 124 requires "a regular cycle of model
validation" and **does not prescribe an annual period; the annual cadence this
document previously asserted is not stated in Article 124 and is unsourced as
a Directive obligation (`F2`)**. The APLC evaluation portfolio, when structured
to satisfy Solvency II model documentation requirements, constitutes the
validation evidence base.

For agent products processing special category data under GDPR, the data
protection impact assessment (DPIA) required under GDPR Article 35 must include
an ongoing monitoring component confirming that the technical and
organizational measures implemented at Stage 1 remain effective throughout the
operational life of the agent product.

### Incident Notification

**DORA Article 19** requires financial entities to report major ICT-related
incidents to the relevant competent authority. Article 19(4) prescribes three
submissions — (a) an initial notification, (b) an intermediate report, (c) a
final report — but **sets no deadline for any of them**: they are due "within
the time limits to be laid down in accordance with Article 20, first
paragraph, point (a), point (ii)", i.e. in the ESAs' regulatory technical
standards. Take the operative hour and day figures from the RTS adopted under
DORA Article 20, first paragraph, point (a)(ii), and record the version relied
on; do not attribute them to Article 19. Behavioral
incidents in agent products qualify as ICT-related incidents for DORA purposes.
An agent product that produces systematically incorrect outputs affecting
customer accounts, market positions, or regulatory submissions is a major ICT
incident if it meets DORA's classification criteria.

The DORA major incident classification criteria relevant to agent products
include: impact on the availability, authenticity, integrity, or
confidentiality of network and information systems; impact on the reputational,
financial, or other position of the financial entity; number of customers
affected; and duration of the incident. A behavioral drift event that goes
undetected for a significant period before alerting — affecting many customer
decisions — is likely a major incident under these criteria.

The incident classification framework at Stage 5 must map quality incident
severity levels to DORA incident classification criteria before the agent
product goes to production. An incident severity framework that is not mapped
to DORA's Article 18 classification criteria does not satisfy DORA's
notification obligations: the financial entity cannot determine whether
notification is required if it has not established the mapping.

For SR 11-7 purposes, behavioral incidents that constitute model performance
failures must be reported through the model risk governance process — including
escalation to the model risk committee if the incident indicates a model risk
limit breach. The APLC escalation path (quality incident → accountable human →
model risk governance) is the SR 11-7 incident management workflow for agent
products classified as models.

**EU AI Act Article 73(1)** requires the *provider* of a high-risk AI system
placed on the Union market to report any serious incident to the market
surveillance authorities of the Member States where that incident occurred. It
binds providers, not "operators": Article 3(8) defines an operator as a
provider, product manufacturer, deployer, authorised representative, importer
or distributor, a class far broader than the one Article 73(1) addresses. A
financial entity that uses a third party's agent product is a *deployer*, and
its own reporting duty is **Article 26(5)**, which requires it, on identifying
a serious incident, to immediately inform first the provider and then the
importer or distributor and the relevant market surveillance authorities — and
applies Article 73 *mutatis mutandis* only where the deployer cannot reach the
provider. Naming the wrong duty-holder here tells the wrong person to file.

The Article 73 reporting deadlines differ by incident type, and each is stated
here alongside the duty it governs rather than in a table elsewhere. The
general report is due immediately after the provider has established a causal
link between the AI system and the serious incident or the reasonable
likelihood of such a link, and **in any event not later than 15 days** after
the provider or, where applicable, the deployer becomes aware of the incident
(Art. 73(2)). Where a person has died, the report is due immediately after a
causal relationship is established or as soon as it is suspected, and **not
later than 10 days** after awareness (Art. 73(4)). For a widespread
infringement, or a serious incident within Article 3(49)(b) — a serious and
irreversible disruption of the management or operation of critical
infrastructure — the report is due immediately and **not later than two days**
after awareness (Art. 73(3)). An infringement of obligations under Union law
intended to protect fundamental rights is Article 3(49)(c); it is **not** in
the Article 73(3) carve-out and therefore carries **no shorter clock** than the
general 15-day period of Article 73(2). This matters directly here: the
discriminatory-decision case below is a fundamental-rights incident, and
treating it as a two-day filing, or a death as a two-day filing, misstates the
Act in opposite directions.

Article 3(49) defines a serious incident as an incident or malfunctioning of an
AI system that directly or indirectly leads to any of four outcomes: the death
of a person, or serious harm to a person's health; a serious and irreversible
disruption of the management or operation of critical infrastructure; the
infringement of obligations under Union law intended to protect fundamental
rights; or serious harm to property or the environment. For financial services
agent products, a behavioral incident that causes a discriminatory credit or
insurance decision is potentially an Article 73 serious incident under the
fundamental-rights limb, and one that causes significant financial harm to a
consumer must be assessed against the property limb. The incident triage
process at Stage 5 must include assessment of whether a quality incident meets
the Article 73 serious incident threshold, and the escalation path must reach a
person with the authority and knowledge to make that determination within the
applicable period above — the clock runs from awareness of the incident, not
from the completion of the internal triage.

Article 73 prescribes no report content in any of its eleven paragraphs. The
Commission guidance mandated by **Article 73(7)**, due 2 August 2025, is the
forthcoming source for report content; until it is available, any content
checklist an organisation uses is its own construction and should be marked as
such rather than attributed to Article 73.
