# Waiver Governance — APLC Cross-Cutting

*Waivers as governance debt: gate conditions, accountability, mandatory expiry, and portfolio oversight for agent products.*

See [Agent Conception](agent/agent-conception.md) for Conception Gate conditions that may be waived.
See [Agent Behavioral Specification](agent/agent-behavioral-specification.md) for Behavioral Specification Gate conditions that may be waived.
See [Agent Behavioral Evaluation](agent/agent-behavioral-evaluation.md) for Behavioral Release Gate conditions that may be waived.
See [Agent Release Governance](agent/agent-release-governance.md) for Operational Readiness Gate conditions that may be waived.
See ASDLC waiver governance for the corresponding ASDLC framework and the relationship between the two.

---

## Section 1: What a Waiver Is and What It Is Not

A waiver is a formal record that a specific gate condition cannot be satisfied at this time. It is not a removal of the condition, an acknowledgement that the condition was unreasonable, or a sign-off that the risk is acceptable in perpetuity. It is governance debt: the organization has decided that carrying the residual risk is acceptable for a defined period, under a defined compensating control, with a defined plan to remediate the underlying condition. Like financial debt, governance debt has a carrying cost — the cost of operating with an unmet condition must be named explicitly, not assumed away by the act of filing the waiver.

**A waiver is a formal record containing:** a named gate condition (by name and gate, not a vague description), a rationale for why the condition cannot be satisfied now, a specific risk description stating what could go wrong as a result of proceeding without the condition met, a named compensating control that is operational at the time of issuance, a named human who accepts accountability for the residual risk, an expiry date, a remediation plan with a named owner and target dates, and a linked pointer to the gate condition document and section.

**A waiver is not an exemption.** The condition remains required. The waiver is temporary governance debt, not a permanent resolution. When the waiver expires, the condition is due.

**A waiver is not a decision by engineering.** Waivers require product owner authorization. The decision to carry governance debt on an agent product is a product decision, not an engineering call.

**A waiver is not a fast path.** The compensating control must provide equivalent risk mitigation during the waiver period. A waiver with no credible compensating control is not a waiver — it is an unacknowledged gate failure.

The APLC does not have optional gate conditions. Every condition in every gate is required. If a condition is not met, one of two outcomes follows: a waiver (if there is a credible compensating control and a credible remediation plan) or a gate failure (the product returns to the prior stage). There is no third outcome where the condition is informally set aside and the gate is passed anyway. Informal non-compliance is not a governance mode — it is a governance failure that leaves no audit trail and no accountability.

---

## Section 2: Waiver Requirements

Every waiver must include all of the following. A waiver missing any element is not a valid waiver and must be rejected at the gate.

**Condition waived.** The specific gate condition being waived, identified by gate name and condition name as they appear in the gate specification document. A waiver is scoped to exactly one condition. Vague descriptions ("evaluation coverage wasn't quite complete") are not acceptable — the condition must be precisely identified so the waiver can be linked to its governing specification and the governance graph can reflect the specific waived state. If multiple conditions require waivers, each requires its own waiver record.

**Rationale.** Why the condition cannot be satisfied at this time: resource constraint (a required reviewer is unavailable), timeline constraint (a compliance deadline precedes the evaluation completion date), or technical constraint (an evaluation methodology requires tooling not yet available). "We decided this wasn't necessary" is not a rationale — it is a statement that the condition should be removed from the gate, which is a gate specification decision, not a waiver decision.

**Risk description.** A statement of the specific risk introduced by not satisfying the gate condition. Not a general description of the condition. A specific statement of what could go wrong as a result of proceeding without the condition being met. "Red-team coverage gap" is not a risk description. "The system's handling of indirect prompt injection through third-party tool outputs has not been adversarially tested; an attacker who can influence those outputs may be able to redirect agent actions in ways not detected by the current evaluation suite" is a risk description.

**Compensating control.** A specific control that is active during the waiver period to reduce the risk introduced by the unmet condition. The compensating control must be operational at the time the waiver is issued — not planned. "Human review of all tool call outputs before agent action execution, until red-team coverage is complete" is a compensating control. "We will add monitoring next sprint" is not. If no credible compensating control can be identified, the waiver cannot be granted. Proceed to gate failure instead.

**Grantor.** The named human who grants the waiver. The grantor must not be the same person as the release approver for the deployment, or the evaluation team lead who benefits from the waiver. Granting a waiver on a condition that benefits the granter's own approval chain is a conflict of interest. For safety and alignment condition waivers, product owner and legal/risk sign-off is required from distinct named individuals.

**Expiry date.** A specific calendar date by which the condition must be satisfied or the waiver renewed. There are no permanent waivers. Maximum durations vary by condition type — see Section 3. A waiver without an expiry date is not a valid waiver.

**Remediation plan.** A specific plan for satisfying the underlying gate condition before the waiver expires. The plan must name an owner, a target completion date that precedes the expiry date, and the specific action required to satisfy the condition. "Complete domain expert review of the use-case coverage map by [date] and file the signed review record to the gate artefact" is a remediation plan. "Improve coverage over time" is not.

**Linked condition.** The gate condition document and section to which the waiver applies. The waiver record must link directly to the governing specification so that the governance graph can represent the waiver accurately and the gate reviewer can verify the scope.

---

## Section 3: Maximum Waiver Durations by Condition Type

The maximum duration for a waiver is set by the condition type. These are ceilings, not targets — the remediation plan should aim for the shortest viable period, not the maximum permitted period.

| Condition Type | Maximum Duration |
| --- | --- |
| Red-team coverage gap (non-Critical finding) | 30 days |
| Behavioral evaluation coverage shortfall | 45 days |
| Domain expert reviewer unavailable | 14 days |
| Compliance documentation incomplete | 30 days |
| Behavioral baseline gap | 14 days |
| Escalation design not fully resourced | 30 days |

**Critical red-team findings: no waiver permitted.** A Critical finding must be remediated and re-tested before the gate can pass. There is no compensating control that provides equivalent mitigation for an unresolved Critical adversarial finding against a deployed agent product. If the finding cannot be remediated, the product does not pass the Behavioral Release Gate.

**Safety and alignment conditions: maximum 7 days.** Waivers on conditions that directly govern the agent's safety behavior, alignment constraints, or hard boundary enforcement are granted for a maximum of 7 days. Both product owner and legal/risk sign-off are required. A safety and alignment condition waiver at 7 days that has not been remediated does not renew — it expires and the gate condition reverts.

---

## Section 4: Waiver Lifecycle States

A waiver moves through defined states from issuance to closure. The governance graph represents the underlying gate condition's state throughout.

**Issued.** The waiver has been formally created by the grantor and accepted at the gate. The gate condition state is set to waived. The compensating control is active and confirmed. The remediation plan is in progress.

**Active.** The waiver is within its validity period. The gate condition state remains waived. Governance monitoring tracks the remediation plan's progress and the compensating control's continued operational status. The waiver's expiry date is visible in the product's governance graph node alongside all other active waivers.

**Expiring.** The waiver is within 7 days of its expiry date without remediation confirmed. The grantor and product owner are notified. Three outcomes are possible: remediation completes before expiry (the condition is satisfied, the waiver closes as expired-remediated, the gate condition state updates to pass), the waiver is renewed (see renewal constraints below), or the expiry date passes without either.

**Expired-remediated.** The underlying condition was satisfied before the expiry date. The waiver closes. The gate condition state updates to reflect the satisfied condition. The waiver record is retained in the governance archive for audit purposes.

**Expired-lapsed.** The expiry date passed without the condition being satisfied and without a valid renewal. The waiver is no longer valid. The gate condition reverts to its pre-waiver state — typically a gate failure state. Any agent product currently deployed in production under this waiver must have its governance status reviewed immediately. An expired-lapsed waiver on a deployed agent product is a governance incident: the product is operating with an unmet gate condition that is no longer covered by any compensating control record or remediation accountability. The product owner and accountable human must be notified immediately and a remediation decision made within 24 hours.

**Renewed.** The waiver has been extended with an updated rationale, an updated expiry date, and a re-confirmed compensating control. A renewal requires the same authorization as original issuance — it is not an administrative extension. A maximum of one renewal is permitted per waiver. A second renewal request requires escalation to the accountable human and a documented review of why remediation has not been completed and whether the condition's specification or the organization's capability to meet it requires revision. A second renewal is not automatically granted — it is an accountability conversation, not a form submission.

---

## Section 5: Emergency Waivers

Emergency waivers address situations where a production safety fix or critical behavioral correction must be deployed faster than the full gate process permits. They are not a mechanism for accelerating planned releases. The emergency criterion is narrow: an active production risk that cannot wait for normal gate processing.

**Maximum duration: 14 days.** An emergency waiver that reaches 14 days without either full gate remediation or conversion to a standard waiver expires on the same terms as a standard expired-lapsed waiver.

**Authorization requirements.** Emergency waivers require accountable human authorization — not product owner authorization alone. The accountable human is the named individual with documented scope of accountability for the agent product. Product owner sign-off is necessary but not sufficient. Legal/risk must be notified in real time, not after the fact.

**Compensating control requirement.** A real-time compensating control must be active at the moment the emergency waiver is issued. There is no grace period for compensating control activation in an emergency waiver — if the control is not operational, the waiver cannot be issued.

**Remediation plan requirement.** A remediation plan targeting the 14-day window must accompany the emergency waiver at issuance. The plan must identify the specific steps, the owner, and the target dates within the 14-day period.

**No emergency waiver stacking.** A second emergency waiver for the same condition before the first expires is not permitted. An organization that finds itself needing to stack emergency waivers on the same condition has a systemic problem — either with the condition's achievability under its current architecture, or with its remediation capability. That problem requires a governance response: a formal review by the accountable human and a structural remediation plan. Another emergency waiver is not the response.

---

## Section 6: Waiver Portfolio Governance

Individual waivers are point decisions. Portfolio-level waiver tracking makes the aggregate governance debt visible.

**Governance graph visibility.** All active waivers for an agent product are visible in its governance graph node. The governance graph represents the product's current gate condition state including which conditions are waived, which waivers are in the expiring state, and which waivers are approaching their maximum permitted duration. A product's aggregate waiver state is not buried in individual waiver records — it is a visible governance signal.

**Elevated governance debt threshold.** A product with more than 3 active waivers simultaneously is in an elevated governance debt state. This state requires a product owner review: what is the aggregate risk profile of the active waivers taken together, are the compensating controls collectively providing adequate mitigation, and is the remediation plan portfolio on track? Elevated governance debt state is not a block on operations — it is a mandatory accountability review. If the review concludes that the aggregate debt is not manageable, the product owner must either accelerate remediation or make an explicit decision to scale back deployment scope until debt is reduced.

**Repeated waiver pattern.** If the same condition is waived more than twice across the product's lifecycle, this is a governance pattern signal. Two outcomes are plausible: the condition's specification is miscalibrated for this product type and requires review, or the organization's capability to satisfy the condition is structurally insufficient and requires investment. In either case, a third waiver on the same condition should not be issued without first conducting a condition review — not just a waiver review. The question is not "should we grant another waiver" but "why has this condition been unachievable twice, and what structural change addresses that?"

**Quarterly waiver portfolio review.** The accountable human conducts a quarterly review of the product's active waiver portfolio. The review addresses four questions: are all active waiver remediation plans on track against their target dates? Are any waivers approaching expiry without confirmed remediation progress? Does the total waiver debt remain appropriate given the product's current operational risk profile and user base? Are any waiver patterns emerging that indicate structural capability gaps rather than point exceptions?

The quarterly review is not a formality. An accountable human who signs off on a quarterly review without examining the remediation plan status of each active waiver has not conducted a review — they have signed a document. The review record must reflect the specific waivers examined, their current remediation status, and any actions taken as a result.

---

## Section 7: Relationship to the ASDLC Waiver Governance

The ASDLC and APLC are separate governance frameworks with separate gate condition sets and separate accountability chains. Their waiver processes are parallel, not unified.

**APLC waivers on shared conditions.** Some APLC gate conditions overlap with or extend ASDLC gate conditions. The clearest example is the engineering DoD condition: the APLC's Behavioral Release Gate condition requiring engineering DoD met per manifesto P8 corresponds directly to the ASDLC's Release Gate evidence bundle condition. An APLC waiver on this condition must be reflected in the corresponding ASDLC waiver record, because both frameworks govern the same underlying requirement. Operating with an APLC waiver on a shared condition while the ASDLC record is silent is an inconsistency in the governance record that will surface as an audit finding.

**An ASDLC waiver does not automatically waive the corresponding APLC condition.** The frameworks have different scope, different accountability chains, and different gate grantor roles. An ASDLC waiver is granted within the ASDLC accountability structure; it carries no authority over APLC gate conditions. An organization that treats an ASDLC waiver as implicitly covering the corresponding APLC condition has collapsed two separate governance frameworks into one — reducing the accountability that both frameworks are designed to produce. Each framework's conditions must be explicitly waived within that framework.

**Cross-framework visibility.** For organizations running both APLC and ASDLC concurrently, the waiver portfolio review should include a cross-framework reconciliation check: are there any conditions where one framework carries an active waiver and the corresponding condition in the other framework is marked as passing without acknowledgement of the shared risk? If so, the governance records are inconsistent and must be reconciled before the next gate review in either framework.
