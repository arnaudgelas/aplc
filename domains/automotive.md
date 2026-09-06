# APLC Domain Guidance — Automotive

*Automotive-specific regulatory guidance for agent products deployed in automotive contexts.*

See the Automotive manifesto alignment for manifesto principle mappings.
See the [APLC Overview](../aplc.md) for the full agent product lifecycle framework.

---

## APLC Regulatory Guidance

*This section addresses product-level AI regulatory requirements that apply to
deployed agent products in the automotive sector — distinct from the ASDLC
process-level requirements covered in the sections above. The question answered
here is: when you deploy an agent product in automotive, what applies to the
agent itself?*

See
[agent/agent-regulatory-classification.md](../agent/agent-regulatory-classification.md)
for the full EU AI Act classification workflow and Annex IV technical
documentation requirements. See
[agent/agent-conception.md](../agent/agent-conception.md) for trust architecture
design and the Stage 1 Conception Gate.

### AI System Classification

**Road traffic — not transport — is the sector EU AI Act Annex III §2 names.**
Point 2 reaches AI systems "intended to be used as safety components in the
management and operation of critical digital infrastructure, road traffic, or
in the supply of water, gas, heating or electricity". "Transport" is broader
than "road traffic" and would sweep in rail, air and maritime, none of which is
in the point, and the difference decides classification. [Corrected 2026-09-06:
this section previously opened by calling transport a critical infrastructure
sector under EU AI Act Annex III §2, and scoped the paragraphs below from that
reading.] Two limits are operative in the same sentence as any §2 claim: the
system must be a **safety component**, and it must be in the **management and
operation of road traffic** — that is, of the traffic system, which is where
traffic-signal control, traffic management centres and roadside infrastructure
agents sit. An AI system inside a single vehicle is not managing or operating
road traffic, so §2 is not the route for it.

**In-vehicle agent products go through Article 6(1)/Annex I, not Annex III §2.**
Article 6(1) makes a system high-risk where it "is intended to be used as a
safety component of a product, or the AI system is itself a product, covered by
the Union harmonisation legislation listed in Annex I" and that product "is
required to undergo a third-party conformity assessment" under that
legislation. Annex I Section B lists Regulation (EU) 2018/858 (approval and
market surveillance of motor vehicles) and Regulation (EU) 2019/2144 (general
safety type-approval requirements), which is the type-approval regime ADAS and
autonomous driving functions already sit inside. Article 2(2) then limits what
this Regulation adds: "For AI systems classified as high-risk AI systems in
accordance with Article 6(1) related to products covered by the Union
harmonisation legislation listed in Section B of Annex I, only Article 6(1),
Articles 102 to 109 and Article 112 apply. Article 57 applies only in so far as
the requirements for high-risk AI systems under this Regulation have been
integrated in that Union harmonisation legislation." — so the Chapter III
requirements and the Annex VI/VII conformity paths of this Regulation do not
apply to them,
and the substantive requirements come from the type-approval framework.

**ADAS advisory agents and autonomous driving monitoring agents** deployed in
operational vehicles are **not** Annex III §2 systems — an in-vehicle function
is not a safety component in the management and operation of road traffic —
and are to be assessed under Article 6(1) against the Annex I Section B
type-approval entries above. [Corrected 2026-09-06: this paragraph previously
called them unambiguously Annex III §2 high-risk regardless of ASIL
assignment; the §2 route rested on the withdrawn "transport" reading.] The
ASIL determination under ISO 26262 must still be conducted at Stage 1 alongside
the EU AI Act classification, and both frameworks impose concurrent
obligations: the AI Act addresses the deployed agent product and its conformity
route, ISO 26262 the software development process and the product's functional
safety assurance. ASIL assignment does not determine the AI Act route in either
direction — Article 6(1) turns on the Annex I product and its third-party
conformity assessment requirement, not on the ASIL.

**Vehicle diagnostics agents** deployed in production vehicles or in workshop
diagnostic systems must be assessed based on what decisions their outputs
enable. A diagnostics agent whose output determines whether a vehicle is
cleared for continued operation is contributing to a safety-critical decision —
but that does not make it Annex III §2, which reaches only safety components in
the management and operation of road traffic and not systems inside a single
vehicle or a workshop; assess it under Article 6(1) against the Annex I Section B
type-approval entries instead. [Corrected 2026-09-06: previously read likely
Annex III §2 in scope.] A diagnostics agent whose output is a workshop
recommendation reviewed by a trained technician before any action is taken is
outside both routes on the face of the instrument; the Regulation names no
"limited-risk" class, so what remains is the Article 50 transparency
obligations where they are triggered, and no high-risk obligation. The Act
imposes no GPAI obligation on an "operator" (Article 3(8) defines that term as
"a provider, product manufacturer, deployer, authorised representative, importer
or distributor"): Chapter V binds the provider of the model, and the deploying
organisation's own duties follow from whether it is the provider of the
downstream system (Article 16) or its deployer (Article 26), plus Article 50
transparency and Article 4 AI literacy at any risk class.

**Fleet management agents** and **warranty claim agents** do not typically
involve safety-critical vehicle functions and are not automatically Annex III
§2. Annex III §5(b) reaches only "AI systems intended to be used to evaluate
the creditworthiness of natural persons or establish their credit score", so it
covers such an agent only where the agent does that; insurance-linked fleet
scoring and warranty eligibility determinations are not creditworthiness
evaluation on the face of the point, and insurance risk assessment and pricing
is §5(c), limited to life and health insurance, so that point does not reach
them either. [Classification corrected 2026-09-05: this paragraph previously
offered §5(b) as the point these agents may fall under if they "make access
decisions affecting individuals" — that phrase paraphrases the heading of point
5, not the text of §5(b). No replacement Annex III classification is asserted;
it has not been signed off.] Classify each agent product type at Stage 1 based
on the specific decision structure, not the general automotive context.

**ASIL determination at Stage 1** is the single most consequential
classification decision for automotive agent products, and it must be completed
before the behavioral specification work begins. The ASIL drives the autonomy
tier ceiling, the verification depth, the tool confidence level requirements,
and the conformity assessment path. A specification written without a confirmed
ASIL has no governing constraint, and discovering the correct ASIL assignment
after the evaluation portfolio has been built means rebuilding the evaluation
suite to the correct ASIL requirements.

### Conformity Requirements

For agent products this document previously classified as high-risk under EU AI
Act Annex III §2 — a classification withdrawn in the AI System Classification
section above, so this section's premise no longer holds and its content is
retained as a record and as a governance requirement of this framework, not as
an asserted legal path — this document states that the conformity assessment
path is Annex VII (third-party assessment) — the same Annex VII reading that `domains/aviation.md` applies to
aviation critical infrastructure safety components, and one that contradicts
Art. 43(2), under which providers of the high-risk systems "referred to in
points 2 to 8 of Annex III" follow the internal-control procedure of Annex VI,
"which does not provide for the involvement of a notified body"; it has
therefore not been verified and must not be relied on until reconciled. On that
same unreconciled reading a notified body would have to review the Annex IV
technical documentation before the EU Declaration of Conformity can be issued.
The Stage 4 release gate accordingly carries notified body certification as a
gate condition for agent products within vehicle safety functions — a gate
condition resting on that same contradicted reading, which must not be relied
on as a legal requirement until Art. 43(2) is reconciled, and which is retained
rather than removed because an undefined gate was judged worse than a marked
contradiction. The flag below records the full analysis.

> **Flagged 2026-09-05, not resolved — read before relying on this gate
> condition.** EU AI Act Art. 43(2) states that for the high-risk systems
> referred to in points 2 to 8 of Annex III, providers follow the conformity
> assessment procedure based on internal control (Annex VI), which does not provide for the involvement of a notified body.
> Annex III §2 is point 2.
> The paragraph above states the opposite of that for the same point, and it
> cites `aplc/domains/aviation.md` as its authority for that reading — see
> that file's own flag on the same point. This is load-bearing on a release
> gate, so the paragraph is left as written rather than withdrawn outright —
> an undefined gate is worse than a marked contradiction — but the
> conformity-assessment path and the notified-body gate condition above
> have not been verified and must not be relied on until reconciled against
> Art. 43(2). No replacement route is asserted here. **Scope of this flag,
> narrowed 2026-09-06:** it covers the Annex VII/Art. 43(2) conformity residual
> only, and does not cover the separate Annex III scoping defect — transport
> read for road traffic, and in-vehicle ADAS placed under §2 — which is
> resolved in the AI System Classification section above, in the same sentences
> as the claims it replaces, rather than flagged. See
> `inputs/20260905-arnaud/prep/domain-files/domain_files_packet.md` (row 5)
> for the full analysis and the primary citation.

**UNECE WP.29 R156 (SUMS)** imposes additional conformity requirements for
software update management in type-approved vehicles. The APLC's composite
versioning model and model update governance must satisfy R156 SUMS
requirements for software updates to vehicle functions. Specifically: any
update to an agent product within a vehicle safety function is a SUMS-governed
software update, requiring: documentation of the change and its impact on
vehicle safety; verification that the update does not introduce new risks; a
tested rollback capability; and post-update verification in the vehicle
environment. The APLC release governance and deployment governance at Stage 4
satisfy these requirements when designed to address them explicitly.

**R156 SUMS submission** must describe the manufacturer's software update
management system in the type approval documentation. For manufacturers
deploying agent products in vehicles, the APLC release process must be
documented as the SUMS implementation. The evidence bundle, tested rollback
procedure, and post-deployment verification are the SUMS release artifacts;
document them in the SUMS submission.

**ISO PAS 8800** (AI in road vehicles, under active development) will impose
AI-specific requirements on automotive AI systems. Organizations developing
automotive agent products should track ISO TC22/SC32 publications and plan for
ISO PAS 8800 compliance requirements to become type approval conditions. The
APLC's documentation structure is designed to accommodate emerging standards;
confirm alignment with ISO PAS 8800 requirements as the standard is finalized.

### Automated Decision-Making Governance

Autonomous driving decisions affecting road users cannot be delegated entirely
to agent products — the SAE Level classification and the corresponding human
oversight requirements determine the permissible degree of automation. EU AI
Act Article 14 mandates human oversight for all high-risk AI systems. For
automotive agent products, Article 14 human oversight requirements must be
mapped to the SAE Level framework at Stage 1:

- SAE Level 2 (partial automation): the human driver is the primary controller
  and must monitor the environment at all times. Agent products at Level 2 have
an advisory or alerting function; the driver retains all responsibility. Trust
architecture must ensure the driver cannot delegate responsibility to the agent
product.
- SAE Level 3 (conditional automation): the system handles all driving tasks in
  defined conditions, but the human must be able to resume control when
requested. Agent products at Level 3 must have a documented human takeover
request design and a specified takeover time window. Article 14 human oversight
is satisfied through the takeover capability.
- SAE Level 4 (high automation): the system handles all driving tasks without
  human intervention in defined operational design domain (ODD). Human
oversight may not be required within the ODD, but ODD boundaries must be
enforced and a fallback mechanism (minimum risk condition) must be specified.

The behavioral specification at Stage 2 must document the exact SAE Level
classification, the ODD definition (for Level 3 and 4), and the human oversight
mechanism that satisfies EU AI Act Article 14. This documentation is both an
Annex IV technical documentation requirement and a UNECE R157 (ALKS)
certification requirement.

GDPR Article 22 is not the primary constraint for most automotive agent
products — vehicle control decisions do not typically concern identified
individuals in the GDPR sense. However, fleet management agents that make
access decisions affecting individual fleet operators, insurance-linked
telematics agents that affect insurance pricing for identified policyholders,
and passenger-facing in-vehicle agents that personalize content or
recommendations may fall within GDPR Article 22 scope. Assess at Stage 1 for
each agent product type.

### Ongoing Monitoring Requirements

**ISO 26262 Part 7 field monitoring** requires that safety-critical deployed
systems are monitored against their safety goals throughout the operational
life of the vehicle. For agent products within vehicle safety functions, the
APLC output quality rate SLO must include safety-goal-derived acceptance
criteria: the SLO floor is not only a functional performance threshold but a
safety performance threshold derived from the ARP/ISO 26262 safety analysis.

**SOTIF (ISO 21448) field performance evaluation** requires systematic
collection of operational data to identify performance limitations and
triggering conditions discovered in the field. The APLC quality incident
classification must include a SOTIF incident category for behavioral
inadequacies — incidents where the agent product behaved inadequately without a
fault, in response to an unanticipated triggering condition. SOTIF field
findings must be routed back to the demand layer as validated evidence, not
treated as isolated quality incidents.

The behavioral drift monitoring at Stage 5 must be calibrated against the SOTIF
triggering condition analysis conducted at Stage 1. When operational data
reveals a pattern suggesting a new triggering condition — an input distribution
not anticipated at concept stage — that is a SOTIF finding requiring a SOTIF
response, not only a monitoring alert.

**UNECE WP.29 R155 (CSMS)** cybersecurity monitoring requirements mandate
ongoing monitoring for cybersecurity threats and vulnerabilities to deployed
vehicles. The APLC maintenance governance's security patch management satisfies
R155's vulnerability management obligations when the patch SLOs are calibrated
to R155's cybersecurity risk management requirements for the specific vehicle
context.

### Incident Notification

**UNECE WP.29 R155** requires notification of cybersecurity incidents to type
approval authorities. An agent product behavioral incident that is attributable
to a cybersecurity attack — prompt injection, model manipulation, sensor data
poisoning — is a R155 cybersecurity incident in addition to an APLC quality
incident. The incident triage at Stage 5 must include a cybersecurity
assessment: is this behavioral incident a cybersecurity incident that must be
reported under R155? The CSMS documentation must define the escalation path for
this determination.

Behavioral incidents in safety-critical vehicle agent products must be assessed
against **ISO 26262 Part 7 field incident** reporting obligations. A field
incident where the agent product contributed to an unsafe condition is
reportable through the applicable accident investigation and reporting
processes (national road accident reporting obligations vary by jurisdiction;
confirm the applicable framework for each deployment country).

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

For automotive agent products this encompasses behavioral incidents where the
agent product contributed to a vehicle accident or near-miss involving injury
or significant property damage. A fatal accident is the Article 73(4) case and
must be reported immediately and not later than 10 days after awareness — not
on any shorter or longer period read across from another framework. The
incident notification workflow must route safety incidents to a person with the
authority and the automotive safety domain knowledge to assess whether the
Article 73 threshold is met, and must do so early enough that the applicable
Article 73 period still has room in it. The R155 cybersecurity incident
reporting and the Article 73 serious incident reporting have different
addressees and different deadlines; both must be addressed in the notification
workflow, and the R155 timeline must not be used as a proxy for the Article 73
one.
