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

**Aviation is not a sector listed in EU AI Act Annex III §2, and no aviation
agent product is classified as high-risk by that point in this document.**
Point 2 is a closed single paragraph: AI systems "intended to be used as safety
components in the management and operation of critical digital infrastructure,
road traffic, or in the supply of water, gas, heating or electricity." The
words *aviation*, *air traffic*, *rail* and *transport* are absent from the
Annex III body at the primary. [Classification withdrawn 2026-09-06: this
section previously stated that aviation is a critical infrastructure sector
under §2, quoted point 2's enumeration with *rail* inserted and *digital*
dropped, and added aviation "by extension" as critical transport
infrastructure; every classification below was scoped from that reading. The
extension is not available — Annex III is a closed list amendable only by the
Commission under Article 7, not by analogy — so the §2 route is withdrawn here
rather than qualified by a note further down the file.]

**The route that can reach an aviation agent product is Article 6(1) via
Annex I, and it reaches very little of aviation.** Article 6(1) makes a system
high-risk where it "is intended to be used as a safety component of a product,
or the AI system is itself a product, covered by the Union harmonisation
legislation listed in Annex I" *and* that product "is required to undergo a
third-party conformity assessment" under that legislation. Annex I Section B
lists Regulation (EU) 2018/1139 (civil aviation, EASA) — but only "in so far as
the design, production and placing on the market of aircrafts referred to in
Article 2(1), points (a) and (b) thereof, where it concerns unmanned aircraft
and their engines, propellers, parts and equipment to control them remotely,
are concerned", so the entry reaches **unmanned aircraft only**, and Annex I
Section B also lists Regulation (EC) No 300/2008 on civil aviation security.
Where the Article 6(1) route does apply through a Section B entry, Article 2(2)
limits what applies: "For AI systems classified as high-risk AI systems in
accordance with Article 6(1) related to products covered by the Union
harmonisation legislation listed in Section B of Annex I, only Article 6(1),
Articles 102 to 109 and Article 112 apply. Article 57 applies only in so far as
the requirements for high-risk AI systems under this Regulation have been
integrated in that Union harmonisation legislation." — so the Chapter III
high-risk requirements and the Annex VI/VII conformity paths do **not** apply to those
systems under this Regulation, and the substantive requirements come from the
sectoral instrument instead.

**The consequence, stated plainly: for manned-aircraft avionics and for
ground-based air traffic management, neither Annex reaches the agent product.**
Annex III point 2's sector list does not include aviation or air traffic, and
neither of Annex I Section B's two aviation entries reaches such a product:
Regulation (EU) 2018/1139 is confined to the design, production and placing on
the market of unmanned aircraft, their engines, propellers, parts and
remote-control equipment, and Regulation (EC) No 300/2008 is civil aviation
security. So an AI safety component in a manned aircraft or in a ground-based
ATM system is not made high-risk by either route on the face of the
instrument. That is the honest answer and it is not a finding that such systems
are unregulated: EASA Part-21, DO-178C/DO-278A and the SESAR/ATM regulatory
framework apply to them on their own terms, independently of the AI Act. It is
also not a signed determination — a classification analysis at Stage 1 with
regulatory counsel is required, and it must start from Article 6(1)/Annex I and
from Article 6(2)/Annex III as they actually read, not from an extension of
point 2.

**Flight planning agents** involved in actual flight operation planning — not
simulation or training tools — that produce outputs affecting real flight
operations are **not** reached by Annex III §2, whose sector list contains no
aviation or air traffic; assess them under Article 6(1)/Annex I instead, which
will reach them only where the agent is a safety component of an unmanned
aircraft, its engines, propellers, parts or its remote-control equipment within
the Annex I Section B entry for Regulation (EU) 2018/1139 — which reaches only
the design, production and placing on the market of those — and that product
requires third-party conformity assessment. For manned flight operations no
Annex route is asserted here.

**Maintenance diagnostic agents** producing recommendations affecting continued
airworthiness determinations are **not** Annex III §2 systems — continued
airworthiness is not one of point 2's listed sectors, and point 2 has no
"aviation critical infrastructure" limb. Continuing airworthiness management is
governed by Regulation (EU) 1321/2014 under the EASA framework, which is not an
Annex I entry, so the Article 6(1) route does not reach it either; on the face
of both Annexes such an agent is outside the AI Act's high-risk class, while
remaining fully subject to the Part-M/Part-145 obligations.

**Air traffic management advisory agents** deployed in live ATC operations are
**not** Annex III §2 high-risk: point 2's list is closed and names neither air
traffic nor aviation, and the "road traffic" limb is road traffic. Nor does
Article 6(1) reach ground-based ATM, because neither of Annex I Section B's two
aviation entries reaches it: Regulation (EU) 2018/1139 is confined to the
design, production and placing on the market of unmanned aircraft, their
engines, propellers, parts and remote-control equipment, and Regulation (EC) No
300/2008 is civil aviation security. No AI Act high-risk classification is
asserted for live-ATC advisory agents in this document. The DO-278A assurance level framework governs the software
development process for these systems and continues to apply in full; the AI
Act's product-level obligations are not established for them here and must be
settled at Stage 1 with counsel rather than assumed in either direction.

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

For agent products this document previously classified as high-risk under EU AI
Act Annex III §2 — a classification now withdrawn in the AI System
Classification section above, so this section's premise no longer holds and its
content is retained as a record and as a governance requirement, not as an
asserted legal path — this document states that the **conformity assessment
path is Annex VII (third-party assessment)** for AI systems used as safety components in critical
infrastructure — a statement that contradicts Art. 43(2), under which providers
of the high-risk systems "referred to in points 2 to 8 of Annex III" follow the
internal-control procedure of Annex VI, "which does not provide for the
involvement of a notified body", and which therefore has not been verified and
must not be relied on until reconciled. On that same unreconciled reading, and
unlike most other Annex III categories, §2 critical infrastructure safety
components would require a notified body review rather than internal
self-certification. If that reading holds it is a significant planning
requirement, because notified body engagement has lead times that cannot be
compressed and the notified body must review the Annex IV technical
documentation before the EU Declaration of Conformity can be issued. The Stage
4 release gate accordingly carries notified body certification as a gate
condition for agent products this document previously classified under
Annex III §2 — a classification withdrawn above, so no aviation agent product is
now so classified by this file, and the gate condition is retained as a
governance requirement of this framework rather than as one the Act imposes; a
gate condition
resting on that same contradicted reading, which must not be relied on as a
legal requirement until Art. 43(2) is reconciled, and which is retained rather
than removed because an undefined gate was judged worse than a marked
contradiction. The flag below records the full analysis.

> **Flagged 2026-09-05, not resolved — read before relying on this gate
> condition.** EU AI Act Art. 43(2) states that for the high-risk systems
> referred to in points 2 to 8 of Annex III, providers follow the conformity
> assessment procedure based on internal control (Annex VI), which does not provide for the involvement of a notified body.
> Annex III §2 is point 2.
> The paragraph above states the opposite of that for the same point. This
> is load-bearing on a release gate, so the paragraph is left as written
> rather than withdrawn outright — an undefined gate is worse than a marked
> contradiction — but the conformity-assessment path and the notified-body
> gate condition above have not been verified and must not be relied on
> until reconciled against Art. 43(2). No replacement route is asserted
> here. **Scope of this flag, narrowed 2026-09-06:** it covers the
> Annex VII/Art. 43(2) conformity residual only. The separate Annex III defect it
> used to record — point 2's enumeration quoted with the word rail in it, and
> aviation added by extension and then treated as settled — has been resolved
> in the AI System Classification section above rather than flagged: the §2
> classification for aviation is withdrawn there, in the same sentences as the
> claims it replaces. Note the consequence for the paragraph above: it is
> premised on aviation agent products being high-risk under EU AI Act Annex III
> §2, and no such classification now stands, so the
> Art. 43(2) question does not arise for them on this document's reading and
> the notified-body gate condition is retained as a governance requirement of
> this framework rather than as an asserted legal one.
> See `inputs/20260905-arnaud/prep/domain-files/domain_files_packet.md`
> (rows 1 and 3) for the full analysis and the primary citations.

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

For **ground-based systems under DO-278A**, the EU AI Act classification is a
separate question from the DO-278A assurance level of the software the agent
product supports, and must be determined on its own terms. A DO-278A AL-3
ground-based ATM system is **not** high-risk under Annex III §2: point 2 reaches
only safety components in the management and operation of "critical digital
infrastructure, road traffic, or in the supply of water, gas, heating or
electricity", and neither air traffic nor aviation is in that list. [Corrected
2026-09-06: this passage previously called such a system a critical
infrastructure safety component and high-risk under Annex III §2 regardless of
the DO-278A assurance level; that classification rested on the withdrawn
extension of point 2 to aviation.] The Article 6(1)/Annex I route does not
reach it either, because neither of Annex I Section B's two aviation entries
reaches it: Regulation (EU) 2018/1139 is confined to the design, production and
placing on the market of unmanned aircraft, their engines, propellers, parts and
remote-control equipment, and Regulation (EC) No 300/2008 is civil aviation
security — so on the face of both Annexes no AI Act high-risk classification
applies, which is a Stage 1 finding to be confirmed with counsel and not a
clearance.

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

For aviation, an Article 73 serious incident overlaps significantly with the
ICAO and EASA reporting obligations: an agent product incident causing death or
serious harm to a person's health is reportable under all three frameworks, on
three different clocks to three different addressees. A fatal occurrence is the
Article 73(4) case — immediately, and not later than 10 days after awareness —
regardless of what period ICAO or Part-21 sets for the same event. The incident
notification workflow must address all three reporting channels — ICAO
occurrence reporting, EASA Part-21 serious failure reporting, and EU AI Act
Article 73 market surveillance authority notification — and must assign each
addressee together with its own deadline in the incident management process at
Stage 5, never a single shared timeline standing for all three.
