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

**Claims processing agents and credit decisioning agents** are high-risk under
Annex III §5(b): AI systems intended for evaluating creditworthiness,
establishing credit scores, or assessing risk and pricing in insurance. These
agent products require full high-risk conformity documentation and EU database
registration before market placement.

**Customer advisory agents** require classification analysis at Stage 1. An
agent that provides analysis for a human advisor to act upon is not necessarily
Annex III. An agent whose output constitutes the recommendation delivered to
the customer — without meaningful human intervention in the recommendation
itself — is a candidate for Annex III §5(b) if the recommendation concerns
essential financial services. Binding recommendations affecting
creditworthiness or insurance risk are high-risk; informational responses that
do not determine access to services require case-by-case analysis.

**Fraud detection agents** may fall under Annex III §5(b) where fraud decisions
affect customer account access, or Annex III §6 where deployed by
public-authority partners in law enforcement contexts. Private enterprise fraud
detection that triggers account restriction without binding legal effect is not
automatically Annex III, but it requires documented classification analysis at
Stage 1.

**Trading agents** and **AML monitoring agents** do not fit cleanly into Annex
III categories designed for individual access decisions. Trading agents may
affect individuals indirectly through market impacts, but Annex III §5(b) is
focused on individual access to essential services. AML agents that produce SAR
filing recommendations affecting individuals' account relationships require
analysis against §5(b). Document the classification analysis; do not assume
out-of-scope.

**Regulatory reporting agents** are typically out of Annex III scope when they
produce documentation for institutional use, not decisions about individuals.
Minimal-risk classification is appropriate for agents that draft, cross-check,
or format regulatory reports, subject to the GPAI operator obligations
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
MiFID II appropriateness criteria; this documentation is an Annex IV input. For
robo-advice agent products, the MiFID II disclosure requirements apply to the
agent product's user interface and output format, not only its internal logic.

**FCA Consumer Duty** requires demonstrable evidence that retail-facing agent
products deliver good outcomes for customers. The APLC's output quality rate
SLO and the ongoing monitoring plan (Stage 5) constitute the Consumer Duty
monitoring evidence. The SLO must be calibrated against customer outcome
metrics, not only technical accuracy metrics.

The conformity assessment path for most financial services high-risk agent
products is internal control with EU AI Office database registration (Annex
VI). Third-party conformity assessment (Annex VII) is not required for Annex
III §5(b) systems. However, several financial services firms elect third-party
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

GDPR Article 22(4) prohibits solely automated decisions based on special
category data — health data, genetic data, racial or ethnic origin, political
opinions, religious beliefs, sexual orientation — except where the individual
has given explicit consent or Member State law provides for it. For life and
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
provisions. Annual model validation by an independent validation function is
required. The APLC evaluation portfolio, when structured to satisfy Solvency II
model documentation requirements, constitutes the annual validation evidence
base.

For agent products processing special category data under GDPR, the data
protection impact assessment (DPIA) required under GDPR Article 35 must include
an ongoing monitoring component confirming that the technical and
organizational measures implemented at Stage 1 remain effective throughout the
operational life of the agent product.

### Incident Notification

**DORA Article 19** requires financial entities to notify their competent
authority of major ICT-related incidents. The notification timeline is: initial
notification within 4 hours of the incident being classified as major;
intermediate report within 72 hours; final report within 1 month. Behavioral
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

EU AI Act Article 73 requires providers and operators of high-risk AI systems
to report serious incidents to the market surveillance authority. A serious
incident is one that has led to, or may have led to, harm to health, safety, or
fundamental rights. For financial services agent products, a behavioral
incident that causes a discriminatory credit or insurance decision, or that
causes significant financial harm to a consumer, is potentially an Article 73
serious incident. The incident triage process at Stage 5 must include
assessment of whether a quality incident meets the Article 73 serious incident
threshold, and the escalation path must reach a person with the authority and
knowledge to make that determination.
