# APLC Domain Guidance — Aviation

*Aviation-specific regulatory guidance for agent products deployed in the aviation sector.*

See the Aviation manifesto alignment for manifesto principle mappings.
See the [APLC Overview](../aplc.md) for the full agent product lifecycle framework.

---

## APLC Regulatory Guidance

*This section addresses product-level AI regulatory requirements that apply to
deployed agent products in the aviation sector — distinct from the ASDLC
process-level requirements covered in the sections above. The question answered
here is: when you deploy an agent product in aviation, what applies to the
agent itself?*

See
[agent/agent-regulatory-classification.md](../agent/agent-regulatory-classification.md)
for the full EU AI Act classification workflow and Annex IV technical
documentation requirements. See
[agent/agent-conception.md](../agent/agent-conception.md) for trust architecture
design and the Stage 1 Conception Gate.

### AI System Classification

Aviation is a critical infrastructure sector under EU AI Act Annex III §2: AI
systems intended to be used as safety components in the management and
operation of critical infrastructure, including road traffic, rail, water, gas,
heating, electricity — and by extension, aviation as critical transport
infrastructure. Agent products involved in safety-critical aviation decisions
are high-risk under EU AI Act Annex III §2.

**Flight planning agents** involved in actual flight operation planning — not
simulation or training tools — that produce outputs affecting real flight
operations must be assessed against Annex III §2. Where the agent's output is
an input to an operational safety decision (route planning, fuel calculation,
weather risk assessment for operational dispatch), the safety-component test is
likely met.

**Maintenance diagnostic agents** producing recommendations affecting continued
airworthiness determinations are candidates for Annex III §2 high-risk
classification. A maintenance agent whose output determines whether an aircraft
is airworthy for further flight is a safety component in the management of
aviation critical infrastructure.

**Air traffic management advisory agents** deployed in live ATC operations are
unambiguously Annex III §2 high-risk. The DO-278A assurance level framework
governs the software development process for these systems; the EU AI Act
imposes parallel product-level obligations.

**Certification documentation agents** and **safety analysis agents** used in
the development or certification of airborne systems are not themselves
deployed in operational aviation; they are tools used in the development
process. They are typically outside Annex III scope as agent products. However,
the ASDLC process-level requirements throughout this document address how these
tools are governed in the development lifecycle.

**DO-178C DAL classification must be determined at Stage 1 alongside EU AI Act
classification.** The two frameworks address different questions — the EU AI
Act addresses the deployed agent product, while DO-178C addresses the software
being produced by the development process — but for agent products deployed in
operational aviation, both apply concurrently. A flight planning agent deployed
in operations is governed by EU AI Act as a deployed AI product and may also be
governed by DO-178C if it contains airborne software components. Determine both
classifications at Stage 1 before Stage 2 specification work begins.

### Conformity Requirements

For high-risk aviation agent products under EU AI Act Annex III §2, the
**conformity assessment path is Annex VII (third-party assessment)** for AI
systems used as safety components in critical infrastructure. Unlike most other
Annex III categories, §2 critical infrastructure safety components require a
notified body review rather than internal self-certification. This is a
significant planning requirement: notified body engagement has lead times that
cannot be compressed, and the notified body must review the Annex IV technical
documentation before the EU Declaration of Conformity can be issued. The Stage
4 release gate must include notified body certification as a gate condition for
agent products classified under Annex III §2.

The Annex IV technical documentation requirements are satisfied by the APLC
artifact chain as described in
[agent/agent-regulatory-classification.md](../agent/agent-regulatory-classification.md).
For aviation agent products, the behavioral specification must explicitly
address: the failure modes the agent product is designed to handle, the
uncertainty protocol for aviation-specific edge cases, and the escalation
design that ensures the pilot or operator retains final authority. EU AI Act
Article 14 (human oversight) mandates human oversight for all high-risk
systems; for aviation, this is redundant with the existing regulatory
requirement that the pilot in command retains final authority — but the trust
architecture must document how the agent product's design enforces this, not
merely assert it.

**EASA Part-21 and FAA Part 21** change approval requirements apply to agent
products incorporated into certified aircraft systems. The EU AI Act
Declaration of Conformity does not substitute for Part 21 change approval; both
are required. The release gate compliance documentation condition must confirm
both filings are in order before an aviation agent product is deployed in an
operational context.

For **ground-based systems under DO-278A**, the EU AI Act classification still
applies to the deployed agent product independent of the DO-278A assurance
level of the software it supports. A DO-278A AL-3 ground-based ATM system is a
critical infrastructure safety component and is high-risk under Annex III §2
regardless of the DO-278A assurance level.

### Automated Decision-Making Governance

Flight safety decisions must have a human in the loop by regulation. EU AI Act
Article 14 mandates human oversight for high-risk AI systems, requiring that
high-risk systems are designed to be effectively overseen by natural persons
during the period of their use. For aviation agent products, this is not an
additional design constraint imposed by the EU AI Act — it is the existing
regulatory framework expressing its requirements in AI Act terminology.

The trust architecture's principal hierarchy for aviation agent products must
reflect the regulatory requirement that the pilot in command (for airborne
systems) or the air traffic controller (for ATC systems) retains final
authority. The agent product can provide analysis, recommendations, and alerts;
it cannot make binding safety decisions without explicit human confirmation.
This is the Tier 1 (observe only) constraint applied at the product
architecture level, not only at the development governance level.

The behavioral specification at Stage 2 must document the pilot or controller's
override capability explicitly: under what conditions can the human override
the agent's recommendation, how is the override executed, and what does the
agent product do after the override. An agent product that does not support
unconditional human override does not satisfy Article 14 or the existing
aviation regulatory framework for pilot authority.

GDPR Article 22 is not the primary constraint for aviation agent products; most
aviation decisions do not concern identified individuals' legal or similarly
significant effects in the GDPR sense. However, passenger-facing agent products
in commercial aviation — seat assignment agents, disruption management agents,
fare pricing agents — may fall within GDPR Article 22 scope where their
decisions significantly affect individual passengers. Assess GDPR Article 22
applicability at Stage 1 for any passenger-facing agent product.

### Ongoing Monitoring Requirements

**EASA PART-21 continued airworthiness monitoring** applies to certified
aviation systems throughout their operational life. For agent products
incorporated into certified systems, the APLC's behavioral monitoring and drift
detection must be structured to produce data that satisfies EASA continued
airworthiness requirements — specifically, that anomalous behavior is detected,
classified, and reported through the appropriate airworthiness reporting
channel.

The output quality rate SLO for safety-critical aviation agent products must be
calibrated against the system's safety objectives (as established by the ARP
4754A/4761A safety assessment), not only against functional performance
metrics. A behavioral drift event that exceeds the output quality SLO threshold
is a potential continued airworthiness issue if the affected function
contributes to safety objectives.

**EU AI Act Article 72** post-market monitoring applies to high-risk systems
and requires a monitoring plan as part of the technical documentation. For
aviation agent products, the Article 72 monitoring plan must be integrated with
the EASA continued airworthiness monitoring process to avoid parallel but
disconnected monitoring obligations.

For **DO-278A ground-based CNS/ATM systems**, continued operational performance
monitoring requirements are established by EASA and national aviation
authorities. The APLC stewardship model and the output quality rate SLO provide
the engineering infrastructure; the monitoring data must feed into the
applicable regulatory reporting channels.

### Incident Notification

**ICAO Annex 13** requires occurrence reporting for aviation safety
occurrences, including incidents where safety was compromised or may have been
compromised. A behavioral incident in a safety-critical aviation agent product
that caused or may have caused an unsafe condition is an ICAO Annex 13
occurrence. The incident classification framework at Stage 5 must include a
safety occurrence assessment: does this quality incident constitute an aviation
safety occurrence that must be reported?

**EASA Part-21 serious failure reporting** applies to certified aircraft
systems. A malfunction or failure of a system that has led to, or may have led
to, an unsafe condition must be reported to EASA. For agent products
incorporated into certified aircraft systems, a behavioral incident meeting the
Part-21 serious failure criteria must be reported. The APLC escalation path
must include a named person with airworthiness authority who can make the
Part-21 determination for safety incidents.

**EU AI Act Article 73** serious incident reporting applies to high-risk agent
products. For aviation, an Article 73 serious incident overlaps significantly
with the ICAO and EASA reporting obligations: an agent product incident that
has led to, or may have led to, harm to health or safety is reportable under
all three frameworks. The incident notification workflow must address all three
reporting channels — ICAO occurrence reporting, EASA Part-21 serious failure
reporting, and EU AI Act Article 73 market surveillance authority notification
— and must ensure that the reporting timelines and addressees for each are
clearly assigned in the incident management process at Stage 5.
