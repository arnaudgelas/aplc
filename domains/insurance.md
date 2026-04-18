# APLC Domain Guidance — Insurance

*Insurance-specific regulatory guidance for agent products deployed in insurance contexts.*

See the Insurance manifesto alignment for manifesto principle mappings.
See the [APLC Overview](../aplc.md) for the full agent product lifecycle framework.

---

## APLC Regulatory Guidance

*This section addresses product-level AI regulatory requirements that apply to
deployed agent products in the insurance sector — distinct from the ASDLC
process-level requirements covered in the sections above. The question answered
here is: when you deploy an agent product in insurance, what applies to the
agent itself?*

See
[agent/agent-regulatory-classification.md](../agent/agent-regulatory-classification.md)
for the full EU AI Act classification workflow and Annex IV technical
documentation requirements. See
[agent/agent-conception.md](../agent/agent-conception.md) for trust architecture
design and the Stage 1 Conception Gate.

### AI System Classification

Common agent product types in insurance and their EU AI Act Annex III
classifications:

**Underwriting advisory agents** producing risk assessments and pricing
recommendations for individual insurance are high-risk under EU AI Act Annex
III §5(b): AI systems intended for risk assessment and pricing in life and
health insurance, and for evaluating creditworthiness. The Annex III text
explicitly names life and health insurance risk assessment; for general
insurance lines affecting individuals, the classification analysis must assess
whether the agent's output meets the Annex III §5(b) criteria for access to
essential private services.

**Claims processing agents** making binding determinations about coverage or
settlement amounts are high-risk under Annex III §5(b) where those
determinations affect individual policyholders' access to insurance benefits. A
claims agent that triages, classifies, and routes claims for human decision is
typically not Annex III in scope. A claims agent whose output constitutes the
coverage determination — or substantially shapes a decision that the human
merely confirms — requires classification analysis at Stage 1.

**Customer advisory agents (IDD scope)** without binding authority over
coverage decisions are limited-risk with transparency obligations (EU AI Act
Article 50 disclosure that the interaction is with an AI system). Where the
agent's recommendation constitutes the advice delivered to the customer and
shapes the customer's insurance purchase decision, the classification must
assess whether the advice affects access to essential insurance services at the
individual level.

**Fraud detection agents** in insurance follow the same classification logic as
in financial services: private enterprise fraud detection triggering claim
suspension is not automatically Annex III, but requires documented
classification analysis at Stage 1. Where fraud detection affects a customer's
access to insurance benefits, the Annex III §5(b) access-to-essential-services
analysis applies.

**Pricing optimization agents** in commercial, fleet, and non-personal lines
insurance are typically outside Annex III §5(b) when they do not affect
individual natural persons' access to essential services. For personal lines,
pricing agents are Annex III §5(b) high-risk. The distinction is the subject of
the decision: individual natural person or commercial entity.

### Conformity Requirements

For high-risk insurance agent products, the Annex IV technical documentation
must be established before market placement and kept current throughout the
operational life. The APLC produces this documentation systematically as
described in
[agent/agent-regulatory-classification.md](../agent/agent-regulatory-classification.md).
For insurance-specific compliance:

**Solvency II model documentation** requirements apply to agent products in SCR
calculation or material risk decisions, parallel to and in addition to EU AI
Act Annex IV requirements. The composite state manifest serves the dual purpose
of EU AI Act configuration documentation and Solvency II model identification
record. The evaluation portfolio serves the dual purpose of EU AI Act accuracy
and robustness documentation and Solvency II calibration and validation
evidence. A single integrated documentation set should address both regimes.

**Annual model validation** required by Solvency II Article 120 is distinct
from the EU AI Act Article 72 post-market monitoring plan. The Solvency II
validation is an actuarially rigorous annual review; the EU AI Act monitoring
is a continuous production quality measurement. Both must be in place for
Solvency II-scope agent products; document them as separate but related
obligations in the Stage 5 operations plan.

The conformity assessment path for most insurance high-risk agent products is
internal control with EU AI Office database registration (Annex VI). The APLC's
behavioral specification, evaluation portfolio, and composite state manifest
together constitute the Annex IV technical file. For complex actuarial models,
organizations may elect third-party conformity assessment to demonstrate
independence to supervisory authorities; document the rationale at Stage 1.

### Automated Decision-Making Governance

Insurance underwriting and claims decisions that significantly affect
individuals are covered by GDPR Article 22 where they are solely automated and
produce legal or similarly significant effects. The primary insurance contexts
are:

- Individual underwriting decisions (coverage acceptance, pricing, exclusions)
  based solely on automated processing where the decision has significant
financial effects on the individual
- Claims decisions (coverage determination, settlement amounts) that are solely
  automated and significantly affect the individual's financial recovery

For agent products processing health or genetic data — life insurance, health
insurance, disability insurance — GDPR Article 22(4) applies: solely automated
decisions based on health or genetic data are prohibited unless the individual
has given explicit consent or Member State law provides for it. The trust
architecture must route every individual underwriting or claims decision based
on health or genetic data through a human in the decision loop.

IDD requires that automated advice systems meet the same suitability
requirements as human advisors. This is not a GDPR Article 22 requirement — it
is a separate conduct obligation. An automated advisory agent product that
provides IDD-scope insurance advice must demonstrate that its suitability
assessment is equivalent in quality to what a qualified human advisor would
produce. This requires the behavioral specification at Stage 2 to encode the
suitability assessment methodology and the evaluation portfolio at Stage 3 to
test it against realistic customer profiles.

The right to contestation for automated decisions is a GDPR Article 22
obligation where Article 22 applies, and a best-practice conduct obligation
where it does not. For insurance agent products making material decisions about
individual customers, the trust architecture must include: an accessible human
review path; an explanation generation capability that can produce, in plain
language, why the decision was made; and a contestation workflow that routes
the individual's challenge to a human reviewer with the authority to change the
decision.

### Ongoing Monitoring Requirements

**Solvency II annual model validation** is the primary ongoing monitoring
obligation for agent products in SCR calculation or material actuarial models.
The annual validation must produce a formal report to the board demonstrating
that the model continues to meet the use test, statistical quality standards,
and calibration standards. The APLC output quality rate SLO provides the
monitoring data; the actuarial function owns the formal annual validation.

**EIOPA AI guidelines** require ongoing performance monitoring for all material
AI systems. For customer-facing agent products, this monitoring must include a
fairness dimension: are the agent's outputs producing disproportionate adverse
outcomes for any customer group defined by protected characteristics? The
output quality rate SLO calibration must include fairness metrics, not only
technical accuracy metrics.

**DORA Article 19** reporting timelines apply to insurance undertakings.
Behavioral incidents in agent products that cause operational disruption must
be classified against DORA's major incident criteria and, if they meet the
threshold, notified to the competent authority within 4 hours of
classification. The incident classification framework must map quality incident
severity levels to DORA's classification criteria before the agent product goes
to production.

For agent products processing health data in large-scale insurance operations,
the GDPR Article 35 DPIA must include an ongoing monitoring component
confirming that technical and organizational measures remain effective. The
steward's monitoring process provides the data; confirm with the Data
Protection Officer that the monitoring data is being used to update the DPIA as
required.

### Incident Notification

**DORA Article 19** applies to insurance undertakings and requires notification
of major ICT-related incidents within 4 hours of classification as major, with
an intermediate report within 72 hours and a final report within 1 month.
Behavioral incidents in insurance agent products that cause operational
disruption — systematic underwriting errors affecting a large number of
policies, claims processing failures causing material delays, pricing
calculation errors affecting a product line — are ICT-related incidents for
DORA purposes if they meet the materiality criteria.

The incident classification framework at Stage 5 must map quality incident
severity levels to DORA's Article 18 classification criteria. The
classification must be confirmed by the ICT risk management function, not only
by the engineering team. An incident severity framework that is not mapped to
DORA criteria cannot determine notification obligations in real time; the
mapping must be established before the agent product goes to production.

**National supervisory authority notification** requirements apply when model
failures affect SCR calculations. Solvency II Article 127 requires immediate
notification to the supervisory authority when the undertaking detects an
irregularity that may affect the calculation of its SCR using an internal
model. A behavioral incident in an SCR-calculation agent product that causes a
material error in the SCR is an Article 127 notifiable event. The incident
escalation path must include the Chief Risk Officer or Chief Actuary who has
the authority and knowledge to make the Article 127 determination.

**EU AI Act Article 73** serious incident reporting applies to high-risk
insurance agent products. An Article 73 serious incident is one that has led
to, or may have led to, harm to health, safety, or fundamental rights. For
insurance agent products, a behavioral incident that causes discriminatory
underwriting or claims decisions — systematic adverse treatment of a protected
group — is potentially an Article 73 serious incident in addition to a DORA
incident. The incident triage must assess both obligations; the addressees and
timelines differ.
