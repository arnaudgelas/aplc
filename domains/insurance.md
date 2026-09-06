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
recommendations for individual insurance are high-risk under EU AI Act Annex III
**§5(c)** — "AI systems intended to be used for risk assessment and pricing
in relation to natural persons in the case of life and health insurance" —
where the line of business is life or health. **§5(b) is a different point**:
it reaches "AI systems intended to be used to evaluate the creditworthiness of
natural persons or establish their credit score", so it applies to an
underwriting agent only where that agent evaluates creditworthiness or a credit
score, and not because the agent prices insurance. [Point corrected 2026-09-05:
this paragraph previously cited §5(b) for insurance risk assessment and
pricing, which is §5(c).] For non-life personal lines (motor, home, travel)
neither point reaches the agent on the face of the instrument — §5(c) is
life-and-health only and §5(b) is creditworthiness only — and "access to and
enjoyment of essential private services and essential public services and
benefits" is the heading of point 5, not an operative criterion in either
sub-point; this file therefore asserts no Annex III classification for non-life
personal lines, which is not signed off and must go to counsel at Stage 1
rather than be settled from this file.

**Claims processing agents** making binding determinations about coverage or
settlement amounts are not reached on the face of any Annex III point 5
sub-point — §5(a) is confined to systems used by or on behalf of public
authorities for essential public assistance benefits, §5(b) to creditworthiness
and credit scoring, and §5(c) to risk assessment and pricing in life and health
insurance, and claims settlement is none of these. [Classification withdrawn
2026-09-05: this paragraph previously classified such agents as high-risk under
§5(b), which is a creditworthiness point. No replacement classification is
asserted, because whether a claims agent is high-risk on some other basis has
not been signed off; treat it as a live Stage 1 classification analysis with
counsel, not as a settled out-of-scope determination.] A
claims agent that triages, classifies, and routes claims for human decision is
typically not Annex III in scope. A claims agent whose output constitutes the
coverage determination — or substantially shapes a decision that the human
merely confirms — requires classification analysis at Stage 1.

**Customer advisory agents (IDD scope)** without binding authority over
coverage decisions are outside the high-risk class and carry the EU AI Act
Article 50 transparency obligation (disclosure that the interaction is with an
AI system); the Regulation names no "limited-risk" class. Where the
agent's recommendation constitutes the advice delivered to the customer and
shapes the customer's insurance purchase decision, the classification must
assess whether the advice affects access to essential insurance services at the
individual level.

**Fraud detection agents** in insurance follow the same classification logic as
in financial services: private enterprise fraud detection triggering claim
suspension is not automatically Annex III, but requires documented
classification analysis at Stage 1. That analysis must not be routed through
Annex III §5(b): the point ends "with the exception of AI systems used for the
purpose of detecting financial fraud", so the instrument excepts fraud
detection from that point rather than capturing it. [Analysis withdrawn
2026-09-05: this paragraph previously stated that a §5(b)
access-to-essential-services analysis applies where fraud detection affects a
customer's access to insurance benefits. That inverts the point's own
exception, and the "access to and enjoyment of essential private services and
essential public services and benefits" wording it invoked is the heading of
point 5 rather than text in §5(b). Whether such an agent is high-risk on another basis is not
asserted here and has not been signed off.]

**Pricing optimization agents** in commercial, fleet, and non-personal lines
insurance are outside Annex III **§5(c)**, whose text is limited to risk
assessment and pricing "in relation to natural persons in the case of life and
health insurance", and outside **§5(b)**, whose text reaches only evaluation of
creditworthiness and establishment of a credit score — so on the face of the
instrument neither point covers non-life commercial or fleet pricing, and the
point this sentence previously tested them against (§5(b)) was the wrong one.
That neither point covers them is not a finding that such an agent is outside
the Regulation, and this file asserts no such conclusion. [citation withdrawn
2026-09-05: this sentence previously classified personal-lines pricing agents
generally as Annex III high-risk. The Annex III point that reaches insurance
risk assessment and pricing carries a life-and-health-only limitation that
this line dropped; whether and how that limitation bears on non-life
personal-lines pricing (motor, home, travel) has not been signed off. See
`inputs/20260905-arnaud/prep/domain-files/domain_files_packet.md`.] The
distinction relevant to classification is the subject of the decision:
individual natural person or commercial entity, and — for the personal-lines
case — the line of business.

### Conformity Requirements

For high-risk insurance agent products, the Annex IV technical documentation
must be established before market placement and kept current throughout the
operational life. The APLC produces this documentation systematically as
described in
[agent/agent-regulatory-classification.md](../agent/agent-regulatory-classification.md).
For insurance-specific compliance:

**Solvency II model documentation** requirements apply to agent products in SCR
calculation or material risk decisions, parallel to and in addition to
EU AI Act Annex IV requirements. The composite state manifest serves the dual
purpose of EU AI Act configuration documentation and Solvency II model
identification record. The evaluation portfolio serves the dual purpose of
EU AI Act accuracy and robustness documentation and Solvency II calibration
and validation evidence. A single integrated documentation set should address both regimes.

**Model validation** required by Solvency II Article 124 (*Validation
standards*) is distinct from the EU AI Act Article 72 post-market monitoring
plan. Article 124 requires that undertakings "shall have a regular cycle of
model validation which includes monitoring the performance of the internal
model, reviewing the ongoing appropriateness of its specification, and testing
its results against experience" — **a regular cycle, whose period the Directive
does not fix; the "annual" cadence this document previously asserted is not in
Article 124 and is unsourced (`F2`)**. Article 120, cited here previously, is
the *Use test* and governs whether the internal model is widely used in and
plays an important role in the system of governance; it is not the validation
provision. The Solvency II validation is an actuarially rigorous periodic
review; the EU AI Act monitoring is a continuous production quality
measurement. Both must be in place for
Solvency II-scope agent products; document them as separate but related
obligations in the Stage 5 operations plan.

The conformity assessment path for most insurance high-risk agent products is
internal control (EU AI Act Annex VI), followed by registration of the provider and
the system under Article 49(1) in the EU database for high-risk AI systems
that the Commission maintains under Article 71 — a register the AI Office
does not hold. EU AI Act Article 49(1) excepts Annex III point 2 (critical
infrastructure) systems from that registration. The APLC's
behavioral specification, evaluation portfolio, and composite state manifest
together constitute the EU AI Act Annex IV technical file. For complex actuarial models,
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
insurance, disability insurance — GDPR Article 22(4) applies to decisions
**referred to in Article 22(2)**: such decisions may not be based on health or
genetic data "unless point (a) or (g) of Article 9(2) applies and suitable
measures to safeguard the data subject's rights and freedoms and legitimate
interests are in place" — that is, explicit consent under Article 9(2)(a), or
substantial public interest under Article 9(2)(g) on the basis of Union or
Member State law which is proportionate and provides suitable and specific
safeguards, and in either case with safeguarding measures in place. The trust
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

**Solvency II model validation (Article 124, *Validation standards*)** is the
primary ongoing monitoring obligation for agent products in SCR calculation or
material actuarial models. Article 124 requires "a regular cycle of model
validation which includes monitoring the performance of the internal model,
reviewing the ongoing appropriateness of its specification, and testing its
results against experience" and **does not fix its period; any annual cadence
is a firm's own supervisory or internal-policy commitment, not a requirement
stated in Article 124, and is unsourced as a Directive obligation (`F2`)**.
Across its full text Article 124 uses none of the words "annual", "year",
"frequency", "independent", "board" or "backtesting"; the APLC requirement
below that the validation produce a formal report to the board is a
requirement of this framework, not of Article 124. That report should
demonstrate that the model continues to meet the use test (Article 120,
*Use test*), statistical quality standards (Article 121) and calibration
standards (Article 122). The APLC output quality rate SLO provides
the monitoring data; the actuarial function owns the formal validation.

**EIOPA AI guidelines** require ongoing performance monitoring for all material
AI systems. For customer-facing agent products, this monitoring must include a
fairness dimension: are the agent's outputs producing disproportionate adverse
outcomes for any customer group defined by protected characteristics? The
output quality rate SLO calibration must include fairness metrics, not only
technical accuracy metrics.

**DORA Article 19** reporting obligations apply to insurance undertakings.
Behavioral incidents in agent products that cause operational disruption
must be classified against DORA's major incident criteria and, if they meet
the threshold, notified to the relevant competent authority. **DORA itself
sets no clock.** Article 19(4) requires the initial notification, the
intermediate report and the final report to be submitted "within the time
limits to be laid down in accordance with Article 20, first paragraph, point
(a), point (ii)" — that is, in the regulatory technical standards developed
by the ESAs. Any hour-or-day figure the firm operates to comes from those
RTS, not from the Regulation; take the current figures from the RTS in force
and record which version they were taken from. The incident classification
framework must map quality incident severity levels to DORA's classification
criteria before the agent product goes to production.

For agent products processing health data in large-scale insurance operations,
the GDPR Article 35 DPIA must include an ongoing monitoring component
confirming that technical and organizational measures remain effective. The
steward's monitoring process provides the data; confirm with the Data
Protection Officer that the monitoring data is being used to update the DPIA as
required.

### Incident Notification

**DORA Article 19** applies to insurance undertakings and requires the
reporting of major ICT-related incidents to the relevant competent
authority. Article 19(4) prescribes the three submissions — (a) an initial
notification, (b) an intermediate report, (c) a final report — but **fixes
no deadline for any of them**: they are due "within the time limits to be
laid down in accordance with Article 20, first paragraph, point (a), point
(ii)", i.e. in the ESAs' regulatory technical standards. Do not cite a
4-hour, 72-hour or one-month figure to DORA Article 19; cite the RTS adopted
under DORA Article 20, first paragraph, point (a)(ii), and name the version
relied on. Behavioral incidents in insurance agent products that cause
operational disruption — systematic underwriting errors affecting a large
number of policies, claims processing failures causing material delays,
pricing calculation errors affecting a product line — are ICT-related
incidents for DORA purposes if they meet the materiality criteria.

The incident classification framework at Stage 5 must map quality incident
severity levels to DORA's Article 18 classification criteria. The
classification must be confirmed by the ICT risk management function, not only
by the engineering team. An incident severity framework that is not mapped to
DORA criteria cannot determine notification obligations in real time; the
mapping must be established before the agent product goes to production.

**National supervisory authority notification** requirements may apply when
model failures affect SCR calculations. [citation withdrawn 2026-09-05: this
paragraph previously named a Solvency II provision as imposing an immediate
notification duty on the undertaking, tied to a defined notifiable-event
term and a named determination made under it. The cited provision is an
implementing-measures clause addressed to the European Commission; it
imposes no duty on any undertaking and defines no notification trigger.
Which provision actually creates an undertaking's notification duty on an
SCR-affecting model failure has not been signed off; see
`inputs/20260905-arnaud/prep/domain-files/domain_files_packet.md`.] A
behavioral incident in an SCR-calculation agent product that causes a
material error in the SCR should still be triaged for a supervisory
notification determination. The incident escalation path must include the
Chief Risk Officer or Chief Actuary who has the authority and knowledge to
make that determination.

**EU AI Act Article 73(1)** binds the *provider* of a high-risk AI system, who
must report any serious incident to the market surveillance authorities of the
Member States where the incident occurred. It does not bind "operators" as a
class — Article 3(8) defines an operator as a provider, product manufacturer,
deployer, authorised representative, importer or distributor. An organisation
that uses a third party's agent product is a *deployer*, and its own duty is
**Article 26(5)**: on identifying a serious incident it must immediately inform
first the provider, and then the importer or distributor and the relevant
market surveillance authorities, with Article 73 applying *mutatis mutandis*
only where the provider cannot be reached.

Each Article 73 deadline is stated here with the duty it governs. The general
report is due immediately after the provider has established a causal link
between the AI system and the incident or the reasonable likelihood of such a
link, and **not later than 15 days** after the provider or, where applicable,
the deployer becomes aware of it (Art. 73(2)). Where a person has died it is
due immediately on establishing or suspecting a causal relationship, and **not
later than 10 days** after awareness (Art. 73(4)). For a widespread
infringement, or a serious and irreversible disruption of the management or
operation of critical infrastructure within Article 3(49)(b), it is due
immediately and **not later than two days** after awareness (Art. 73(3)). An
infringement of obligations under Union law intended to protect fundamental
rights is Article 3(49)(c) and carries no shorter clock — it runs on the
general 15-day period of Article 73(2). Article 73 prescribes no report content
in any of its eleven paragraphs; the Commission guidance mandated by Article
73(7) is the forthcoming source for that.

Article 3(49) defines a serious incident as an incident or malfunctioning of an
AI system that directly or indirectly leads to any of four outcomes: the death
of a person, or serious harm to a person's health; a serious and irreversible
disruption of the management or operation of critical infrastructure; the
infringement of obligations under Union law intended to protect fundamental
rights; or serious harm to property or the environment.

For insurance agent products, a behavioral incident that causes
discriminatory underwriting or claims decisions — systematic adverse
treatment of a protected group — is potentially an Article 73 serious
incident under the fundamental-rights limb, Article 3(49)(c), and therefore
runs on the 15-day period of Article 73(2), in addition to being a major
ICT-related incident under the separate DORA reporting duty above, whose
deadline is set by the RTS under DORA Article 20, first paragraph, point
(a)(ii), and not by DORA itself. The incident triage must assess both
obligations; the addressees and the deadlines differ, and neither deadline
may be inferred from the other.
