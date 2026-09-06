# APLC Domain Guidance — Pharmaceuticals / Life Sciences

*Pharma and life sciences-specific regulatory guidance for agent products deployed in pharmaceutical and life sciences contexts.*

See the Pharma manifesto alignment for manifesto principle mappings.
See the [APLC Overview](../aplc.md) for the full agent product lifecycle framework.

---

## APLC Regulatory Guidance

*This section addresses product-level AI regulatory requirements that apply to
deployed agent products in pharmaceutical and life sciences contexts — distinct
from the ASDLC process-level requirements covered in the sections above. The
question answered here is: when you deploy an agent product in pharma, what
applies to the agent itself?*

See
[agent/agent-regulatory-classification.md](../agent/agent-regulatory-classification.md)
for the full EU AI Act classification workflow and Annex IV technical
documentation requirements. See
[agent/agent-conception.md](../agent/agent-conception.md) for trust architecture
design and the Stage 1 Conception Gate.

### AI System Classification

Pharmaceutical agent product types span a wide range of EU AI Act risk
classifications, and each product type must be assessed individually at Stage
1. Do not assume that a pharmaceutical context implies a single classification
tier across all agent products deployed in it.

**Pharmacovigilance agents** making safety signal decisions process health data
and potentially affect public safety by shaping regulatory submissions and risk
management decisions. Where the agent's output directly determines whether a
pharmacovigilance signal is escalated, suppressed, or filed with a regulatory
authority, the classification analysis must address whether this constitutes a
decision with significant implications for individuals' health and safety.
Depending on the scope of the decision and the degree of human oversight
designed into the trust architecture, pharmacovigilance agents are **not** reached by
Annex III §5(a), which is confined to AI systems used "by public authorities or
on behalf of public authorities to evaluate the eligibility of natural persons
for essential public assistance benefits and services, including healthcare
services, as well as to grant, reduce, revoke, or reclaim such benefits and
services" — a public-authority benefit-eligibility point, not a data-category
or biometric one (biometrics is Annex III point 1), and a pharmacovigilance
agent inside a marketing authorisation holder is not a public authority nor
acting on one's behalf. [Corrected 2026-09-06: this sentence previously glossed
§5(a) as biometric/health data and routed pharmacovigilance agents to it.] No
Annex III classification is asserted for these agents here; assess them at
Stage 1 against EU AI Act Article 6(1)/Annex I (Regulation (EU) 2017/745 on medical
devices and Regulation (EU) 2017/746 on in vitro diagnostic medical devices are
EU AI Act Annex I Section A entries), and against the pharmacovigilance obligations of
Regulation (EC) No 726/2004 and Directive 2001/83/EC, which apply
regardless. Article 6(1) is cumulative and EU AI Act Annex I membership of the instrument
is necessary but not sufficient: (a) the agent must be a safety component of,
or itself be, such a product, and (b) that product must be required to undergo
a third-party conformity assessment under that legislation. Where no Annex
reaches the agent, the Regulation names no "limited-risk" class: what remains
is the Article 50 transparency obligations where they are triggered, together
with any enhanced downstream duties this framework imposes of its own accord.
Those duties are not GPAI operator obligations — the Act imposes none on an "operator" (Article 3(8)) and Chapter V binds the
provider of the model; the deploying organisation's own duties follow from its
role, Article 16 as provider of the downstream system or Article 26 as its
deployer. The classification must be documented at
Stage 1 with the reasoning; do not assume out-of-scope without analysis.

**Regulatory submission agents** that generate dossier content, perform
consistency checks, and format submissions are typically out of EU AI Act Annex III scope
(and reached, if at all, only by the Article 50 transparency obligations —
"limited-risk" is this document's shorthand, not a class of the Regulation): they produce documentation for institutional review, not
decisions affecting individual access to services. The applicable duties are the
deploying organisation's own, by role: Article 50 transparency where the system
interacts directly with natural persons or generates synthetic content, Article
4 AI literacy at any risk class, and — only where the organisation is a body
governed by public law, a private entity providing public services, or a
deployer of an Annex III point 5(b) or (c) system — the Article 27 fundamental
rights impact assessment, which is a deployer duty on specified bodies and not a
GPAI obligation. However, if a regulatory
submission agent influences the content of a safety section in a way that
affects whether a drug's risk profile is accurately represented to a regulatory
authority, the implied public safety implications are substantial even if the
direct effect on individuals is indirect.

**Clinical trial monitoring agents** and **quality management agents** are
typically outside Annex III — reached, if at all, only by the Article 50
transparency obligations — absent specific features that bring them into
Annex III scope (such as direct patient data processing for individual clinical
decisions). The GPAI overlay in
[agent/agent-regulatory-classification.md](../agent/agent-regulatory-classification.md)
applies: document the GPAI model, confirm the provider's compliance
classification, and assess whether the foundation model is classified as posing
systemic risk.

**Drug interaction advisory agents** deployed in clinical or pharmacy settings
where their output informs dispensing decisions affecting individual patients
require careful Annex III analysis. An agent product whose output determines
whether a drug is dispensed to a patient or triggers a clinical warning is
**not** Annex III §5(a) high-risk: §5(a) is confined to public authorities, or
those acting on their behalf, evaluating eligibility for essential public
assistance benefits and services, and a dispensing or interaction-warning agent
in a clinical or pharmacy setting is not doing that. [Classification withdrawn
2026-09-06: this sentence previously read potentially Annex III §5(a)
high-risk, on the same misreading of §5(a) as a health-data point.] The route
to assess instead is Article 6(1)/Annex I, under which the agent is high-risk
where it is a safety component of, or is itself, a product covered by
Regulation (EU) 2017/745 (medical devices) or Regulation (EU) 2017/746 (IVDs)
— both EU AI Act Annex I Section A entries — and that product requires third-party
conformity assessment; clinical decision support software is frequently a
medical device in its own right under MDR Rule 11. Where it is not a device
under either Regulation, no Annex reaches it and no high-risk classification is
asserted here, which is a Stage 1 question for counsel rather than a clearance.
Classify these products based on the
actual decision structure — who acts on the output, and what are the
consequences — rather than the nominal description of the agent as "advisory."

### Conformity Requirements

**GxP validation** is the primary compliance framework for agent products used
in GxP-regulated environments, and it runs parallel to EU AI Act conformity
requirements. The APLC's behavioral baseline and evaluation portfolio provide
the validation evidence; they must be structured to satisfy GxP validation
documentation requirements.

The mapping to qualification stages is described in the ASDLC sections above.
For conformity assessment purposes, the key discipline is that the APLC's Stage
1 through Stage 4 artifacts collectively constitute the GxP validation package.
Specifically: the Agent Product Brief (Stage 1) is the User Requirement
Specification equivalent; the behavioral specification (Stage 2) is the
Functional Specification equivalent; the evaluation portfolio (Stage 3)
satisfies OQ requirements; and the composite state manifest (Stage 4) serves as
the configuration management record required by GAMP 5.

**For high-risk EU AI Act systems** in pharma, the Annex IV technical
documentation requirements must be addressed alongside the GxP validation
package. The two documentation structures are not identical: Annex IV requires
specific content about human oversight measures, accuracy and robustness
testing, and post-market monitoring plans that GxP documentation does not
always address in the same form. Produce a single integrated technical file
that addresses both regimes, not two separate documentation packages.

**For pharmacovigilance agent products**, the EudraVigilance technical
documentation requirements apply. The agent product's decision logic for signal
detection and causality assessment must be documented in sufficient detail to
support EMA inspection access (see Incident Notification below). The composite
state manifest, which records the exact configuration of the agent product at
any point in time, is the primary instrument for demonstrating to an EMA
inspector what version of the agent product was in use during any specified
period.

The conformity assessment path for most pharmaceutical high-risk agent products
is internal control (Annex VI), followed by registration of the provider and
the system under Article 49(1) in the EU database for high-risk AI systems
that the Commission maintains under Article 71 — a register the AI Office
does not hold. Article 49(1) excepts Annex III point 2 (critical
infrastructure) systems from that registration.
Third-party conformity assessment (Annex VII) is not required for most
Annex III categories applicable to pharma. Organizations that voluntarily elect
third-party review to support regulatory submissions in multiple jurisdictions
should document the rationale at Stage 1.

### Automated Decision-Making Governance

[citation withdrawn 2026-09-05: this paragraph previously stated the
governing GDPR restriction on solely automated decisions based on special
category data as an unqualified prohibition. The restriction is conditional,
not absolute — it carries consent and Member-State-law gateways that this
line omitted entirely, and the correct qualified form has not been signed
off. See `inputs/20260905-arnaud/prep/domain-files/domain_files_packet.md`.]
The automated-decision-making governance set out in this section — the
Stage 1 classification, human-review-path and permission-model requirements
described in the paragraphs below, and not any GDPR Article 22 or Article 9
restriction, which this file no longer states — applies to pharmaceutical agent
products that process individual patient health or genetic data and produce
decisions with significant individual effects. In the pharmaceutical context, this
primarily concerns clinical trial participant monitoring agents and patient
registry agents that process identifiable patient data.

Pharmacovigilance decisions that affect regulatory filings are not typically
GDPR Article 22 matters — the decision subject is the regulatory submission,
not an identified individual — but they have indirect patient safety
implications that are in some ways more severe than direct individual
decisions. While GDPR Article 22 does not technically require a human review
path for pharmacovigilance signal decisions, the regulatory implications of
incorrect signals are so significant that the escalation design should include
pharmacologist review for decisions that trigger regulatory reporting. This is
not a GDPR requirement; it is a product governance requirement derived from the
regulatory stakes of pharmacovigilance decisions.


For agent products processing individual patient data in clinical settings —
patient recruitment agents, protocol deviation flagging agents, safety
monitoring agents — the trust architecture must assign clinical oversight of
decisions affecting individual trial participants. The GCP obligation for
sponsor oversight of patient safety (ICH E6(R3)) operates as the governance
framework for these agent products regardless of GDPR Article 22 applicability.

The permission model at Stage 1 must specify what data access the agent product
has to patient-level data, what decisions the agent product can output
regarding that data, and what human review step is required before those
outputs affect clinical decisions. For GCP-regulated agent products, this
specification is the ICH E6(R3) quality management plan for the agent product's
role in the trial.

### Ongoing Monitoring Requirements

**EudraVigilance reporting obligations** apply to pharmacovigilance agent
products involved in individual case safety report (ICSR) processing and signal
detection. The agent product's contribution to EudraVigilance submissions must
be documented: when the agent's output contributes to a regulatory submission,
the accuracy of that output is subject to the same accuracy obligations as any
other pharmacovigilance process. Ongoing monitoring must demonstrate that the
agent product's signal detection and causality assessment accuracy remains
within the validated range against reference signal data.

For signal detection agents, the output quality rate SLO must include reference
signal accuracy metrics: the agent's sensitivity (proportion of true signals
correctly identified) and specificity (proportion of non-signals correctly
excluded) must be monitored against a reference standard. A decline in signal
detection accuracy that falls below the validated range is a pharmacovigilance
quality event requiring investigation and, potentially, regulatory
notification.

**GAMP 5 periodic review** applies throughout the operational life of validated
agent products. The periodic review must confirm: that the agent product's
configuration matches the validated baseline; that behavioral drift has not
occurred; that any changes since the last review were managed under change
control; and that the validation remains current given changes in the
regulatory or operating environment. The quarterly architectural health review
in ASDLC maintenance governance satisfies this obligation when it explicitly
addresses GxP validation currency.

**EU AI Act Article 72** post-market monitoring applies to any agent products
classified as high-risk. The monitoring plan must be a technical documentation
element before market placement. For pharmaceutical high-risk agent products,
the Article 72 monitoring plan should be integrated with the GxP ongoing
performance monitoring process rather than maintained as a separate compliance
document.

### Incident Notification

**EMA pharmacovigilance inspections** may require full access to the agent
product's decision trail for any pharmacovigilance activity the agent
contributed to. An EMA inspector examining a pharmacovigilance inspection
finding may request to see the specific decision the agent product made — the
signal assessment, the causality determination, or the ICSR processing — and
the evidence that the decision was correct. The composite state manifest and
the reasoning trace provide this evidence, but they must be designed from Stage
1 to support inspection access: the trace must be queryable by time period and
decision type, and the composite state manifest must record the exact agent
product configuration at the time of each decision.

The **decision record retention policy** for pharmacovigilance agent products
must be aligned with EMA inspection access requirements. EMA may request access
to pharmacovigilance records for any period within the product's approval
lifetime — potentially spanning decades. The decommission protocol for
pharmacovigilance agent products must include a plan for how the decision trail
will remain accessible to regulatory authorities after the agent product is
retired, in a format that inspectors can navigate.

For agent products in EU AI Act high-risk scope, **EU AI Act Article 73(1)**
binds the *provider* of a high-risk AI system, who must report any serious
incident to the market surveillance authorities of the Member States where the
incident occurred. It does not bind "operators" as a
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

In the pharmaceutical context, a serious incident is most likely to arise from
a pharmacovigilance agent product that fails to identify a safety signal,
resulting in delayed regulatory action on a genuine safety issue — an Article
3(49)(a) case where it leads to death or serious harm to a person's health, and
so subject to the 10-day period of Article 73(4) where a person has died and
the 15-day period of Article 73(2) otherwise. The incident classification
framework must include an assessment of whether a quality incident in a
pharmacovigilance agent product meets the Article 73 serious incident
threshold, and the escalation path must include the qualified pharmacovigilance
professional who can make that determination inside the applicable period.

For agent products in scope of **EU GMP or GDP requirements**, regulatory
notifications arising from agent product failures in manufacturing or
distribution decisions follow the applicable GMP/GDP notification framework,
not the EU AI Act framework alone. The incident notification workflow must map
to both obligations where both apply.
