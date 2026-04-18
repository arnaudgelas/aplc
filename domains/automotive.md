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

Transport is a critical infrastructure sector under EU AI Act Annex III §2.
Agent products involved in vehicle safety functions — ADAS, autonomous driving,
active safety systems — are high-risk under Annex III §2 as safety components
in critical infrastructure management.

**ADAS advisory agents and autonomous driving monitoring agents** are
unambiguously Annex III §2 high-risk when deployed in operational vehicles. The
ASIL determination under ISO 26262 must be conducted at Stage 1 alongside the
EU AI Act classification. Both frameworks impose concurrent obligations: the EU
AI Act addresses the deployed agent product and its conformity requirements;
ISO 26262 addresses the software development process and the product's
functional safety assurance. A deployed ADAS agent product at ASIL C or D will
be Annex III §2 high-risk under the EU AI Act regardless of ASIL assignment.

**Vehicle diagnostics agents** deployed in production vehicles or in workshop
diagnostic systems must be assessed based on what decisions their outputs
enable. A diagnostics agent whose output determines whether a vehicle is
cleared for continued operation is contributing to a safety-critical decision
and is likely Annex III §2 in scope. A diagnostics agent whose output is a
workshop recommendation reviewed by a trained technician before any action is
taken may be limited-risk with GPAI operator obligations.

**Fleet management agents** and **warranty claim agents** do not typically
involve safety-critical vehicle functions and are not automatically Annex III
§2. They may fall under Annex III §5(b) if they make access decisions affecting
individuals (insurance-linked fleet scoring, warranty eligibility
determinations). Classify each agent product type at Stage 1 based on the
specific decision structure, not the general automotive context.

**ASIL determination at Stage 1** is the single most consequential
classification decision for automotive agent products, and it must be completed
before the behavioral specification work begins. The ASIL drives the autonomy
tier ceiling, the verification depth, the tool confidence level requirements,
and the conformity assessment path. A specification written without a confirmed
ASIL has no governing constraint, and discovering the correct ASIL assignment
after the evaluation portfolio has been built means rebuilding the evaluation
suite to the correct ASIL requirements.

### Conformity Requirements

For high-risk automotive agent products under EU AI Act Annex III §2, the
conformity assessment path is Annex VII (third-party assessment) — the same
Annex VII requirement that applies to aviation critical infrastructure safety
components. A notified body must review the Annex IV technical documentation
before the EU Declaration of Conformity can be issued. The Stage 4 release gate
must include notified body certification as a gate condition for agent products
within vehicle safety functions.

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

**EU AI Act Article 73** serious incident reporting applies to high-risk
automotive agent products. An Article 73 serious incident is one that has led
to, or may have led to, harm to health or safety. For automotive agent
products, this encompasses behavioral incidents where the agent product
contributed to a vehicle accident or near-miss involving injury or significant
property damage. The incident notification workflow must route safety incidents
to a person with the authority and the automotive safety domain knowledge to
assess whether the Article 73 threshold is met. The R155 cybersecurity incident
reporting and the Article 73 serious incident reporting have different
addressees and potentially different timelines; both must be addressed in the
notification workflow.
