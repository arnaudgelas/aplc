# Initiative Authorization Gate — APLC Cross-Cutting

*Normative specification for the gate that authorises an agent to exercise* initiative *— surfacing action opportunities not assigned by a human — within a defined domain and a defined set of action classes. This gate operates parallel to the Stage 4 Release Gate and is layered on top of it, not in place of it. Audience: system stewards, IGM revision authorities, product owners, accountable humans, internal audit (3rd line), and external regulators reviewing the agent's authorisation chain.*

**Status:** Normative APLC artefact (Wave 1, item W1.11; coherence-review BLOCKER B12).

**Cross-references:** `aplc.md` (Initiative Authorization Gate description), `aplc-guide.md` (initiative metrics and audit), `governance/governance-integration-note.md` (Tier 4 / relocation / substrate composition rule), `governance/composition-rule.md` (composition rule), `governance/authority-accountability-matrix.md` (authority matrix), `integration/loop-readiness-for-agent-opportunities.md` (AEM loop-readiness re-entry for agent-surfaced opportunities), `intelligence-governance-manifesto/manifesto-principles.md` Principle 14 (claims as attack surfaces), `agentic-enterprise-manifesto/manifesto.md` Principle 6 (initiative through substrate depth).

---

## 1. What this gate authorises and what it does not

**Authorises.** An agent product to exercise *initiative* for a specifically enumerated set of `(domain, action class)` pairs: to surface action opportunities — structured agent recommendations meeting the criteria in Section 4 — not assigned by a human, drawing on the IGM-governed substrate to perceive institutionally relevant patterns within the listed action classes.

**Does not authorise.** Autonomous *execution* of initiative-surfaced action opportunities. An agent with initiative authorisation surfaces opportunities; the human accountability layer (per AEnt-M Principle 8 consequence-class roles) decides whether and how to act. Initiative authorisation grants *recommendation authority*, not *action authority*. Action authority remains governed by:

- The AEM Tier (1–4) the agent operates within for the relevant action class.
- The AEnt-M relocation stage (Full synchronous → Parallel → Monitored → Operational) for that action class.
- The AEnt-M consequence-class accountability assignment (Workflow Owner / Decision Reviewer / Accountable Authority / Dual Authority).

The composition rule in `governance/composition-rule.md` continues to apply to every action — initiative authorisation does not relax it.

**Scope.** Initiative authority is granted **per-domain × per-action-class**, not globally. An agent may be authorised to surface settlement-reconciliation opportunities (one action class within the financial-services domain) and not authorised to surface regulatory-filing opportunities (another action class within the same domain). The gate record enumerates the authorised pairs explicitly; pairs not listed are not authorised by implication.

---

## 2. Pass conditions (all three required)

### Condition 1 — Substrate-depth condition

The IGM-governed domain graph supporting the listed action classes is measurably deep on four dimensions:

| Dimension | Threshold | Measurement |
|---|---|---|
| **Coverage** | > 80% | Fraction of the action class's institutional knowledge addressed by claims in the substrate, measured against a domain-expert-validated reference scope. |
| **Connectivity** | Rising over the prior measurement window | Per the connectivity proxy defined in `agentic-enterprise-manifesto/companion-guide.md:13–28`. A flat or declining connectivity trend disqualifies the substrate even if coverage is above threshold. |
| **Freshness** | > 90% | Fraction of claims within their decay class's revalidation cadence (per AEnt-M Principle 10 decay classes / IGM Principle 5). Stale claims past their revalidation cadence count against freshness regardless of their epistemic tier. |
| **Contradictions** | Typed and tracked | Every active contradiction in the action class's claim family is typed (logical / temporal supersession / jurisdictional divergence / scope mismatch — per IGM Principle 4) and tracked in the substrate's contradiction register. Untyped contradictions disqualify the condition regardless of the other three dimensions. |

**Confirmed by:** the IGM revision authority for the domain. The revision authority's sign-off attests that the four measurements were taken on the substrate state recorded in the gate record's CSH (per `aplc/agent/agent-composite-versioning.md` and the knowledge-base CSH integration in `aplc.md`).

### Condition 2 — Constraint-legibility condition

The institutional constraints governing the listed action classes are machine-reasonable, not document-buried (per AEnt-M Principle 6, Initiative Condition 2; companion-guide.md:31–41).

| Sub-condition | Threshold | Measurement |
|---|---|---|
| **Machine-readable constraint coverage** | > 80% of action classes | The fraction of action classes in scope whose institutional constraints (regulatory boundaries, internal policy limits, jurisdictional scope, blast-radius ceilings) exist in a machine-readable form the agent can reason over directly — not as prose the agent must interpret heuristically. |
| **Agent self-classification accuracy** | > 90% | The agent's accuracy in classifying candidate actions against the constraint architecture, validated against a held-out reference set scored by qualified human reviewers. The reference set must be independent of any training or fine-tuning data the agent was exposed to, and must include adversarial cases (constraints that look applicable but are not, and constraints that look inapplicable but apply). |

The held-out reference set must be refreshed at least every 12 months, or whenever the constraint architecture changes materially. A reference set frozen since first validation is a reference set the agent has effectively memorised; it does not measure ongoing classification capability.

### Condition 3 — Governance-relocation condition

At least one action class within the proposed initiative scope has demonstrated **control equivalence** per AEnt-M Principle 7: evidence that decision quality under substrate-resident governance is stable or improved relative to the synchronous pre-action-check baseline. The control-equivalence evidence is the four signals defined in `agentic-enterprise-manifesto/companion-guide.md:83–91` — decision-quality comparison, error detection rate, response time to degradation, audit reconstructability.

**Degradation monitoring active and tested.** Degradation monitoring on the relocated action class is operational, instrumented to detect:

- Decision-quality deterioration relative to the synchronous baseline.
- Substrate-state degradation (epistemic-tier demotion, contradiction emergence, freshness decay) for the claim families the action class consumes.
- Control-evaluation failure (relocation-evidence signals falling out of acceptable range).

**Tested:** a deliberate degradation injection has been performed within the prior 90 days and the monitoring detected and responded within the SLO defined for the consequence class. A test that the team has never run is not evidence of operational monitoring; it is an aspirational claim. The injection-test record is part of the gate evidence.

---

## 3. Decision rule

**All three conditions met → initiative authorised** for the agent in the listed `(domain, action class)` pairs. The gate record enumerates the pairs.

**Any one condition not met → initiative not authorised.** No partial authorisation. No "authorised for surfacing but not for routing to a human" — that is not a coherent intermediate state; the failure mode is an agent that surfaces low-quality opportunities into human review queues, consuming attention without providing value, which is precisely what the gate exists to prevent. The agent operates as a Stage-4-released assigned-task executor for the action classes in question until the failing condition is restored.

**Waivers.** The Initiative Authorization Gate does **not** accept waivers. The conditions are the operational evidence that initiative is safe to grant for the listed pairs; a waiver is a record that the evidence does not exist. Granting initiative without the evidence converts the gate from a substantive check to a formality. If a condition cannot be satisfied, the gate fails — the team works to satisfy the condition or scopes the authorisation more narrowly to pairs where the condition does hold.

---

## 4. Time-bounding and review cadence

**Quarterly review.** Initiative authorisation is reviewed every 90 days from the date of last authorisation. The review re-evaluates all three conditions against current evidence. Prior authorisation does not roll forward by default. A review that finds any condition has slipped below threshold updates the authorisation accordingly — typically by removing affected pairs from the authorised list and reverting the agent to assigned-task execution for those pairs.

The review is conducted by the system steward and the IGM revision authority for the domain, the same two signatories as the original authorisation. The review record is filed in the AGKB alongside the original authorisation record.

**No "renewal-by-extension."** A review that does not produce updated evidence is not a review — the evidence in the original authorisation may be up to 90 days old by the review date and must be refreshed. A review record that cites the original measurements without re-measurement is not a valid review and the authorisation lapses.

---

## 5. Auto-revoke triggers

Initiative authorisation auto-revokes for the affected action class when any of the following occurs between quarterly reviews. Auto-revocation does not require a meeting — the monitoring system raises the revocation event, the gate record is updated, the agent reverts to assigned-task execution for the affected pair, and the system steward and IGM revision authority are notified within the SLO for the consequence class of the affected action class.

| Trigger | Source | Effect |
|---|---|---|
| Coverage falls below 80% for the action class's claim family | IGM substrate-state monitoring | Revoke initiative for that pair |
| Connectivity declines over a sustained window | IGM substrate-state monitoring | Revoke initiative for the affected pairs |
| Freshness falls below 90% | IGM substrate-state monitoring (decay-cadence overflow) | Revoke initiative for the affected pairs until freshness is restored |
| Contradictions accumulate untyped | IGM contradiction register | Revoke initiative for the affected pairs |
| Machine-readable constraint coverage falls below 80% | Constraint-architecture audit | Revoke initiative across the constraint group |
| Agent self-classification accuracy falls below 90% | Periodic re-validation against held-out reference set | Revoke initiative across the affected action classes |
| Control-equivalence evidence falls behind synchronous baseline | AEnt-M relocation-evidence monitoring | Revoke initiative for the affected pair |
| Degradation-monitoring injection test fails | Quarterly injection-test cycle | Revoke initiative across all pairs the monitoring covers, until the monitoring is restored and re-tested |
| IGM Principle 14 incident: confirmed contradiction-injection or claim-poisoning attack on the substrate | Substrate-security owner | Revoke initiative for all pairs depending on the affected claim family until substrate integrity is restored and re-validated |

The agent is not silently downgraded. A revocation event is logged, the affected human accountability roles are notified, and the agent's behaviour is observably different (it stops surfacing opportunities for the affected pairs). A team that does not notice the revocation has not been monitoring the agent.

---

## 6. Accountable signatories

**System steward.** Signs the gate. Accountable for the agent's operational governance — that the constraint-architecture audit was conducted, that degradation monitoring is operational, that the agent's self-classification accuracy was validated against a real held-out set rather than a re-used training set, that the injection test was run.

**IGM revision authority for the domain.** Co-signs. Accountable for the substrate-state attestation — that the coverage / connectivity / freshness / contradiction measurements are accurate, that the named substrate authorities for each claim family in scope are current, that no Principle 14 incident is open against the affected claim families.

**Both signatures required.** Neither alone is sufficient. A system steward who signs without the IGM revision authority is asserting substrate state they are not accountable for; an IGM revision authority who signs without the system steward is asserting agent-side conditions (constraint legibility, classification accuracy, monitoring) they are not accountable for. The two-signature requirement is the structural protection against a single point that could grant authority on insufficient evidence.

**Conflict of interest.** Neither signatory may be the same person as the product owner who benefits from the authorisation, the engineering team lead who built the agent, or the operations lead who will be relieved of synchronous-check workload by the relocation that initiative authorisation enables. The same conflict-of-interest principle that applies to waiver grantors (`aplc/waiver-governance.md` Section 2) applies here, with stricter enforcement: the gate cannot be passed under conflict.

---

## 7. Evidence required at the gate

The gate record contains all of the following artefacts. A gate record missing any artefact is not a passing gate record.

**Metrics dashboard (substrate state).** A dashboard or equivalent structured report showing, per `(domain, action class)` pair in scope:
- Coverage measurement against the domain-expert reference scope, with measurement date.
- Connectivity time series over the prior measurement window.
- Freshness measurement, with the count of claims past revalidation cadence.
- Contradiction register entries with type assignments.

**Steward attestation (constraint legibility and monitoring).** A signed attestation from the system steward stating:
- Which action classes have machine-readable constraint definitions, with pointers to the constraint repository.
- The agent's self-classification accuracy measurement, the held-out reference set used, the date of measurement, and the qualified human reviewer who scored the reference set.
- Confirmation that degradation monitoring is operational, with pointers to the monitoring instrumentation.
- The date and outcome of the most recent degradation-injection test.

**IGM authority sign-off (substrate state).** A signed attestation from the IGM revision authority for the domain stating:
- The coverage / connectivity / freshness / contradiction measurements as recorded.
- The named Semantic, Assertion, Inference, and Revision authorities for each claim family in scope.
- Absence of open Principle 14 incidents against the affected claim families, or — if any are open — their scope and why they do not affect this authorisation.

**Class register entry.** The class register (per `governance/governance-integration-note.md` Section 3) is updated to reflect each authorised pair, the AEnt-M relocation stage for the action class, and the consequence class.

**CSH at gate time.** The composite-state hash at the moment of authorisation, including the IGM-governance metadata per the knowledge-base CSH specification in `aplc.md` Section 1. This anchors the authorisation to a specific substrate state; substrate-state changes that move the CSH retrigger the auto-revoke logic.

**Loop-readiness pointer.** Reference to the AEM loop-readiness gate that any opportunity surfaced under this authorisation must pass before re-entering the engineering loop (see `integration/loop-readiness-for-agent-opportunities.md`). Initiative authorises *surfacing*; loop-readiness governs *acting on what is surfaced*.

---

## 8. What initiative authorisation does and does not change downstream

**Does change.** The agent may surface action opportunities — structured recommendations meeting the criteria in `aplc-guide.md` Section "Initiative metrics and audit" — that were not assigned by a human. These enter the human accountability layer per the consequence class of the recommended action. Surfaced opportunities are recorded regardless of whether a human accepts them, per the audit requirements.

**Does not change.** The composition rule — every action's permissibility = MIN(AEM tier, IGM epistemic gate, AEnt-M consequence class) — remains the binding constraint. The accountable human for each consequence class remains the decision-maker. The Stage 4 envelope (if any) and its prerequisites remain in force; envelope withdrawal cascades to initiative authorisation as well, since initiative-surfaced opportunities are still subject to the envelope's allowed change classes and blast-radius ceiling.

**Initiative without execution authority.** An agent with initiative authorisation but no Tier 4 envelope or a low AEnt-M relocation stage on the affected action classes will surface opportunities that route to synchronous human approval before any action proceeds. This is the intended pattern for early-stage initiative: the agent's perception capability is exercised; the human's decision authority is preserved. As the action class advances through AEnt-M relocation stages and the AEM envelope authorises higher-tier autonomy, the human approval becomes asynchronous, then sample-based — but the initiative-authorisation gate is what justifies the agent surfacing the opportunity in the first place.

---

## 9. Failure modes and counter-controls

These failure modes describe how an Initiative Authorization Gate can fail in operation. Each is paired with the counter-control that the gate's design is intended to provide.

**Failure: Substrate-depth metric gaming.** A team adjusts the reference scope used to compute coverage, lowering the denominator until coverage clears 80% by definition. *Counter-control:* the reference scope is owned by the IGM revision authority and a domain expert independent of the team seeking initiative authorisation. Reference-scope changes between quarterly reviews require a documented rationale and are flagged in the substrate-security audit for review.

**Failure: Self-classification accuracy theatre.** The held-out reference set is constructed to favour the agent — easy cases, cases similar to training data, cases without adversarial framing. The agent achieves >90% accuracy on a set that does not test classification capability. *Counter-control:* the held-out reference set construction is reviewed by a domain expert independent of the team that built the agent; adversarial cases are required; reference-set refresh on a 12-month cadence prevents memorisation. (See `aplc-guide.md` audit requirements for additional sampling discipline.)

**Failure: Injection test that always passes.** The degradation injection test is implemented in a way that always succeeds — the injected degradation is detectable but does not stress the monitoring infrastructure under realistic conditions. *Counter-control:* the injection test must include conditions calibrated to the failure modes the monitoring is intended to catch; the test specification is reviewed by the IGM revision authority and substrate-security owner; the test is re-specified at each quarterly review to prevent regression to a fixed and defeated test.

**Failure: Initiative-bypass attack (W2.23 red-team category).** An adversary or insider attempts to grant initiative authority without all three conditions met — e.g., by gaming substrate-depth metrics, by submitting a reference-scope change that artificially boosts coverage, or by bypassing the two-signature requirement. *Counter-control:* the integrity audit defined in `aplc/agent/agent-behavioral-evaluation.md` "Initiative-bypass attack" red-team category. The audit reviews the gate evidence, looks for metric tampering, verifies that signatures came from authorised parties without conflict of interest, and verifies that auto-revoke triggers are wired to live measurement rather than a static value.

**Failure: Contradiction-injection attack against the substrate (W2.23 red-team category).** An adversary introduces contradictory claims into the substrate to manipulate the agent's reasoning. If the contradictions are not caught by IGM Curate or the contradiction register, the agent's surfaced opportunities are corrupted at the substrate layer, and initiative authorisation is being exercised on a poisoned substrate. *Counter-control:* IGM Principle 14 (claims as attack surfaces); the substrate-security owner's quarterly red-team of the graph; the auto-revoke trigger when a Principle 14 incident is open against an affected claim family.

---

## 10. DRAFT items needing author judgment

- **DRAFT — author review needed:** the four substrate-depth thresholds (coverage > 80%, freshness > 90%, agent self-classification accuracy > 90%, machine-readable constraint coverage > 80%) are illustrative starting values, calibrated to be operationally tractable. Domain owners must confirm them against their own historical baselines before first authorisation. Reasonable variation is expected; the gate's structural integrity does not depend on these specific figures.
- **DRAFT — author review needed:** the 90-day quarterly review cadence and the 12-month held-out reference-set refresh cadence are calibrated against the assumption that substrates change slowly relative to model and prompt versions. Faster-moving regulatory domains may require shorter cadences. The IGM revision authority for the domain decides.
- **DRAFT — author review needed:** the degradation-injection test design is left at the level of "calibrated to the failure modes the monitoring is intended to catch." A worked example for a settlement-operations agent's substrate-degradation monitoring is needed; deferred to the next editorial pass. Until then, the IGM revision authority and substrate-security owner approve injection-test designs case by case.
- **DRAFT — author review needed:** the conflict-of-interest test for the two signatories is specified informally. A formal test (a named-roles-may-not-overlap matrix) should be added and cross-referenced from `governance/authority-accountability-matrix.md` once that matrix is published.
