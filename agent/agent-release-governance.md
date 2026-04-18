# Agent Release Governance
## Stage 4: Release — Behavioral Release Governance Framework

*APLC document. Governs the transition from a built and evaluated agent product to a deployed agent product. Extends ASDLC `release-governance.md` for agent-specific requirements; does not replace it. Audience: release managers, product owners, compliance officers, CISOs.*

*Related documents: [aplc.md](../aplc.md), [agent-behavioral-specification.md](agent-behavioral-specification.md), [agent-behavioral-evaluation.md](agent-behavioral-evaluation.md), [agent-composite-versioning.md](agent-composite-versioning.md), [agent-regulatory-classification.md](agent-regulatory-classification.md), [agent-operations.md](agent-operations.md), [agent-maintenance.md](agent-maintenance.md), [agent-retirement.md](agent-retirement.md), ASDLC `release-governance.md`*

---

## What is Stage 4 — Release?

Stage 4 is where a built and evaluated agent transitions to a deployed product. It is not a deployment operation — it is a governance transition. The behavioral release gate is the structured assessment that the agent is ready for real users and that the governance infrastructure exists to detect when it stops being ready. The gate is not a go/no-go rubber stamp; it is the last point where problems are cheaper to fix than to encounter in production.

---

## Relationship to ASDLC Release Governance

The ASDLC `release-governance.md` establishes the foundational release gate: evidence bundle complete, independent validation passed, rollback procedure tested, accountable human sign-off, and compliance documentation complete. Every one of those conditions applies to an agent product release without modification. Stage 4 of the APLC does not relax, replace, or circumvent them.

What Stage 4 adds is the behavioral dimension: the agent-specific conditions that the ASDLC release gate does not address because they are not relevant to deterministic software. Deterministic software does not have a behavioral baseline that drifts. It does not have a foundation model that can be updated by a third party between releases. It does not require a four-layer probabilistic evaluation portfolio before release. The APLC Stage 4 gate adds the eleven conditions below on top of the ASDLC release gate conditions. Both sets must be satisfied. Neither substitutes for the other.

---

## Behavioral Release Gate (Detailed)

The S3→S4 gate is the checkpoint that authorises the transition from the Build & Evaluate stage to the Release stage. It requires eleven conditions. For each, the required evidence, the minimum standard, and the consequence of non-satisfaction are defined below.

---

### Gate Condition 1 — Engineering DoD Met

**What it requires:** All seven manifesto Definition of Done conditions have been satisfied and the engineering evidence bundle is complete. The seven conditions are: Shipped, Observable, Verified, Provable, Learned from, Governed, and Economical.

**Required evidence:** The engineering evidence bundle as defined in `manifesto-done.md`: evaluation reports with pass/fail results and metrics, trace IDs linking specification to execution to output, diffs showing exactly what changed, policy check outputs, and memory updates. The bundle must be complete and internally consistent. A missing trace ID or an evaluation report without a timestamp is an evidence gap, not a minor deficiency.

**Minimum standard:** All seven DoD conditions passed. No evaluation failures outstanding. Any past failures must have documented remediation confirmation in the bundle.

**If not met:** The gate does not open. The agent has not completed Stage 3 engineering. No amount of behavioral evaluation clearance compensates for an incomplete engineering DoD. The ASDLC makes this explicit: engineering evidence is the foundation; everything else is built on it.

---

### Gate Condition 2 — Behavioral Evaluation Portfolio Complete

**What it requires:** The four-layer behavioral evaluation portfolio from `agent-behavioral-evaluation.md` has been executed and reviewed. The evaluation clearance report has been signed by the named evaluation team lead.

**Required evidence:** The evaluation clearance report documenting:
- Layer 1 (Engineering): all P8 engineering evaluations pass; evidence bundle complete.
- Layer 2 (Behavioral coverage): results for each probabilistic assurance target in the behavioral specification; coverage percentages meeting minimum bars (80% core use cases, 50% edge cases, held-out set included).
- Layer 3 (Adversarial red-team): red-team report filed; all six attack categories covered; no Critical or High findings outstanding — either remediated before the report or, for High findings, mitigated with re-test confirmation.
- Layer 4 (Human preference): sampling methodology and sample size documented; rubric scores for each quality dimension; evaluator qualifications confirmed.
- Longitudinal stability: T0 stability measurement taken against the stability test set; baseline values documented.

**Minimum standard:** No Critical or High red-team findings outstanding. Every layer must have a documented status, not merely an assertion that work was done. The evaluation team lead's sign-off certifies the evidence is what it claims to be; the product owner's release approval accepts that the evidence is sufficient.

**If not met:** The gate does not open. A red-team clearance assertion without a filed report is not clearance. A Layer 2 status of "partially complete" that falls below the minimum coverage bars means the release decision is being made on insufficient evidence. The product owner may document a risk acceptance for specific Layer 2 shortfalls below the minimum coverage bars, but that risk acceptance must be named and explicit — not implicit in proceeding.

---

### Gate Condition 3 — Behavioral Baseline Document Established

**What it requires:** The quantitative behavioral profile of the agent at this release point, measured against the complete evaluation portfolio and filed as a standalone document before deployment proceeds.

The behavioral baseline is the reference for all future drift detection in Stage 5 (Operate). Every monitoring threshold, every stability deviation detection, every quality regression alert in Stage 5 is measured against the behavioral baseline established at Stage 4. An agent that is deployed without a behavioral baseline cannot be monitored for behavioral drift, because there is no reference state to drift from. This is not a documentation gap that can be filled after deployment — a behavioral baseline cannot be retroactively established. The measurement must be taken before the composite state changes.

**Required contents of the behavioral baseline document:**
- Scores for each Layer 2 probabilistic assurance target, with the target value and the measured value at this release
- Aggregate red-team clearance status (all Critical/High findings closed; Medium/Low findings listed with mitigation tracking)
- Human evaluation rubric scores for each quality dimension from the Layer 4 assessment
- T0 longitudinal stability measurement: the stability test set results at release time, as the reference for all future stability measurements
- The composite state hash (CSH) from the composite state manifest at this release — the baseline is bound to the composite state it was measured against

**Minimum standard:** The behavioral baseline document must be filed to the release artefact store before the Stage 4 deployment is authorised. It is referenced by manifest ID and by the CSH of the release-time composite state manifest.

**If not met:** The gate does not open. Stage 5 monitoring is architecturally dependent on the existence of a behavioral baseline. A deployment without one is operating without the ability to detect behavioral degradation. For regulated systems, a deployment without a behavioral baseline also means there is no documented performance record for regulatory examination.

---

### Gate Condition 4 — Composite State Manifest Filed

**What it requires:** A snapshot of all five composite state components at the point of release, filed to the audit trail before deployment proceeds. The manifest format, field requirements, and filing procedure are defined in `agent-composite-versioning.md`.

**Required evidence:** A completed composite state manifest with event type `initial_release` (for the first deployment) or `release` (for subsequent releases), including:
- Application code commit hash and container image digest
- System prompt version label and content hash
- Foundation model provider, model name, snapshot version (if available), and date confirmed
- Knowledge base snapshot ID, document count, and source manifest hash
- Memory state description and content hash (or `stateless` for stateless deployments)
- The computed CSH and the hash function used

The manifest must be reviewed by the release manager, signed by the named accountable human, and filed to the audit trail before the deployment record is created. Once filed, the manifest is immutable. Corrections require a new manifest with event type `correction` referencing the original manifest ID.

**Minimum standard:** A complete, signed, filed manifest. A manifest in draft state or awaiting signature is not filed. The CSH computed in the manifest is the behavioral identity of this release — it is the reference against which all operational CSH comparisons will be made in Stage 5.

**If not met:** The gate does not open. Deploying without a filed composite state manifest means the agent product enters production without a documented behavioral state. Incident investigation from that point forward has no verified starting point.

---

### Gate Condition 5 — EU AI Act Conformity Documentation

**What it requires:** For high-risk AI systems under EU AI Act Annex III: technical documentation per Annex IV complete and reviewed; the conformity assessment path completed; the EU Declaration of Conformity (EU DoC) signed and registered in the EU AI Office database.

The risk classification and conformity assessment path were determined at Stage 1 per `agent-regulatory-classification.md`. If that classification identified the system as high-risk, the gate condition is not optional. The EU DoC is a legal document — not a compliance summary — signed by the operator attesting that the system conforms to the applicable requirements of the EU AI Act.

**Required evidence:**
- Annex IV technical documentation complete and reviewed. The APLC documents produced across Stages 1–4 constitute the majority of Annex IV documentation — see the mapping table in `agent-annex-iv-mapping.md`. Any gaps identified in that mapping must be closed before the gate review.
- For systems requiring a notified body assessment (biometric identification systems and critical infrastructure AI safety components): the notified body conformity assessment certificate must be in hand before the Stage 4 gate review is scheduled. Notified body review has lead times that cannot be compressed at the last moment; the engagement must have been initiated at Stage 1.
- The EU DoC: signed by the named responsible person, referencing the conformity assessment procedure followed, the relevant standards applied, and — where applicable — the notified body certificate. The DoC is filed with the EU AI Office database before market placement.

**Post-Market Surveillance Plan (required for EU AI Act Annex III high-risk systems).** Before the Operational Readiness Gate can close, a Post-Market Surveillance Plan compliant with EU AI Act Article 61 must be filed as a gate artifact. The plan must contain:

1. *Surveillance objectives and scope* — which aspects of the agent's performance are under surveillance, the user population covered, and the regulatory risks being monitored.
2. *Data collection methodology* — which Stage 5 metrics constitute the surveillance data collection; collection frequency; statistical analysis methodology (minimum sample sizes, significance testing approach, trend analysis method).
3. *Evaluation criteria* — at what performance level does the surveillance system trigger a corrective action? Thresholds must be pre-committed in this plan; thresholds set after observing production data are not valid surveillance criteria.
4. *Reporting mechanism* — the format, content, recipients, and cadence of surveillance reports. For high-risk systems, reports must be provided to the EU AI Office on the schedule required under the Act.
5. *Actions and timelines* — what specific actions are triggered by which surveillance findings, within what regulatory timeframes.
6. *Notified body and market surveillance authority notification protocol* — when and how to notify the relevant authorities of serious incidents, significant changes, or performance degradations that affect conformity.

The Post-Market Surveillance Plan is a living document: it is updated when behavioral specifications change, when new performance thresholds are established after recalibration, or when regulatory guidance on Article 61 implementation is issued. Version history of the plan is maintained in the AGKB alongside behavioral specification version records.

**Minimum standard:** For high-risk systems: EU DoC signed and filed before any deployment to any EU market. For non-high-risk systems: documentation of the risk classification rationale, reviewed and current. Scope creep that moves a minimal-risk system into a high-risk category during development must have triggered a reclassification at Stage 2 or Stage 3. If the Stage 4 review reveals that the system's scope has expanded beyond the Stage 1 classification, the Stage 4 gate is paused until the conformity documentation reflects the current scope.

**If not met:** The gate does not open for EU market deployment. For high-risk AI systems, deploying without a filed EU DoC is a regulatory violation at the moment of deployment. The cost of non-compliance is not deferred to when a regulator discovers it.

---

### Gate Condition 6 — Named Accountable Human

**What it requires:** A named individual with product-level accountability for behavioral outcomes in production. This requirement originates in Principle 12 of the manifesto and is carried into the ASDLC release gate as Condition 4 (accountable human sign-off). The APLC extends that requirement to make explicit what "accountability" means for an agent product in production.

The accountable human is accountable for behavioral outcomes — not only for the act of deploying. The distinction matters. An accountable human who is accountable only for the deployment decision can disclaim responsibility for behavioral degradation detected at T+3 months ("the deployment was fine; the drift happened later"). The APLC's definition of accountability extends through Stage 5 monitoring, Stage 6 recalibration decisions, and the governance transitions that the accountable human authorises throughout the product's operational life.

**Required evidence:**
- A named individual (full name and role) recorded in the release artefact.
- A documented scope of accountability: what product-level behavioral outcomes is this person accountable for? This should reference the behavioral specification's hard boundaries and probabilistic assurance targets.
- The accountable human's dated sign-off on the complete evidence bundle, confirming they have reviewed it and accept production accountability.

**Minimum standard:** The accountable human must be a named individual, not a team, not a role occupied by a rotating cast. Accountability that cannot be traced to a person is not accountability. The named person must have the authority to halt a deployment, authorise a rollback, and escalate to legal or compliance — these are the powers that make the accountability real.

**If not met:** The gate does not open. A deployment without a named accountable human is an ungoverned deployment. The ASDLC makes this explicit and the APLC maintains it without exception.

---

### Gate Condition 7 — User-Facing Transparency

**What it requires:** Confirmation that users who interact with the deployed agent will be given the disclosures and information they are entitled to, and that the infrastructure to deliver those disclosures is live and verified before deployment.

The EU AI Act Article 50 imposes a mandatory disclosure requirement: users must be informed that they are interacting with an AI system, unless it is obvious from context. This is a pre-deployment requirement, not a post-deployment best practice. The disclosure infrastructure must be in place before users encounter the agent.

**Required evidence:**
- **AI disclosure:** documentation confirming that users are informed they are interacting with an AI agent, through what mechanism (in-product disclosure, onboarding screen, terms of service, persistent UI indicator), and that the mechanism is live and verified in the production environment.
- **Capability and limitation documentation:** user-accessible documentation covering what the agent can and cannot do, the scope of its knowledge, and the boundaries of its authority to take actions on the user's behalf. This documentation must be accurate as of the release version, not inherited from a prior version without review.
- **Escalation path:** the route by which a user who wants human review of the agent's output or decision can reach a human reviewer. The escalation path must be reachable — not advertised and nonfunctional. For regulated sectors, the escalation path must meet the service level required by the applicable regulation (GDPR Article 22 right to human review; sector-specific consumer protection requirements).

**Minimum standard:** All three elements live and verified in the production environment before deployment. "Verified" means tested: an actual user interaction with the disclosure mechanism has been confirmed to work; the escalation path has been end-to-end tested.

**If not met:** The gate does not open. For EU market deployments, missing AI disclosure is a direct Article 50 violation. For all deployments, missing escalation path infrastructure means the accountability chain breaks at the user boundary — the agent is deployed into an environment where users have no path to human recourse.

---

### Gate Condition 8 — Control State Record Present and Complete

**What it requires:** The control state record produced by the manifesto engineering loop must be present at the gate review as a distinct, standalone artefact. The control state record is the machine-readable record that states, for every required control, whether it passed, failed, was waived (with a current waiver), is stale, or requires-human-decision. It is not the same artefact as the evidence bundle (Gate Condition 1) or the evaluation clearance report (Gate Condition 2); it is verified independently of both.

**Required evidence:** A control state record filed before the gate review that:
- Lists every required control defined for this product.
- States the control status for each: `pass`, `waived` (with waiver reference), `deferred-to-gate` (for controls whose status is determined at the gate review itself), `fail`, `stale`, or `requires-human-decision`.
- For each `waived` control: references the waiver ID and confirms the waiver is current (not expired).
- Is timestamped and records the tool or process that produced it.

**Minimum standard:** At gate time, every control must be in status `pass`, `waived` (with a current, non-expired waiver), or `deferred-to-gate`. Controls in status `fail`, `stale`, or `requires-human-decision` at gate time make the gate fail. A control state record that is itself stale (produced more than 72 hours before the gate review for a system with active development, or at any time if a composite state component changed after the record was produced) must be regenerated before the gate review proceeds.

**If not met:** The gate does not open. A gate review conducted without a current control state record is a review conducted on an unknown control surface. The control state record is the gate's instrument panel; proceeding without it is operating blind.

---

### Gate Condition 9 — Waiver Governance

**What it requires:** All waivers referenced in the control state record (Gate Condition 8) or cited in satisfaction of any other gate condition must be valid at the time of the gate review and must satisfy the organizational independence requirement between the waiver grantor and the release approver.

**Required evidence:** For each waiver referenced at the gate:
- **Named grantor:** a named individual who granted the waiver. The waiver grantor must be different from the product owner who is approving evaluation clearance (Gate Condition 2) and from the accountable human signing off on the release (Gate Condition 6). An organization where the same person grants waivers and approves the release is not providing independent waiver governance.
- **Expiry date:** a specific date on or after which the waiver is no longer valid. Open-ended waivers without an expiry are not valid waivers.
- **Compensating control:** a documented control that is active during the waiver period and that partially or fully compensates for the control being waived.
- **Remediation plan:** a documented plan with target date for remediating the underlying condition so that the waiver is no longer needed.
- **Linked condition:** the specific gate condition or control state record entry that the waiver applies to.

**Minimum standard:** Every waiver must be current (expiry date is in the future at the time of the gate review). A gate pass that references an expired waiver is not a valid gate pass — the gate pass is retroactively invalidated from the moment the waiver expired if the underlying condition was not remediated. If a waiver expires during the canary period or during the full rollout, the organization must either renew the waiver before the expiry date or remediate the underlying condition before the expiry date.

**If not met:** The gate does not open. Expired waivers, waivers without named grantors, and waivers granted by the release approver are not valid. The gate reviewer must verify waiver validity as part of the gate review checklist, not as a post-review administrative step.

---

### Gate Condition 10 — Cost Envelope Review

**Cost Envelope gate condition:** The operational cost envelope filed at Stage 2 has been reviewed and signed by the Business Owner. The review confirms that the cost envelope was established based on Stage 3 evaluation data (actual cost-per-interaction measurements from the evaluation runs), not on pre-evaluation estimates. The signed cost envelope document is filed in the AGKB as a gate artifact. A deployment proceeding without a signed cost envelope has no economic governance and cannot be considered fully governed regardless of behavioral gate status.

---

### Gate Condition 11 — Epistemic Tier Labeling

**What it requires:** Every artefact submitted to the Behavioral Release Gate must carry an epistemic tier label identifying how the artefact was produced. The label is a machine-readable field in the artefact metadata or, for documents without structured metadata, a declared statement in the artefact header.

**Epistemic tier definitions:**
- `human-authored`: the artefact was produced directly by a human without agent assistance. Human-authored artefacts may use deterministic tools (spell-checkers, formatters, calculators) without losing this label, but any AI agent involvement in drafting, structuring, or generating content disqualifies the label.
- `tool-generated`: the artefact was produced by a deterministic tool (a script, a test harness, a linting tool, a hash function). The tool and its version must be identified.
- `agent-proposed-with-human-review`: the artefact was produced or substantially drafted by an AI agent, then reviewed and confirmed by a named human. The named reviewer's full name and the date of review must be recorded in the artefact metadata.
- `agent-generated`: the artefact was produced by an AI agent without human review.

**Minimum tier requirements by artefact type:**

| Artefact | Minimum required tier |
|---|---|
| Red-team report | `agent-proposed-with-human-review` (red-team lead is the named reviewer) |
| Evaluation clearance report | `agent-proposed-with-human-review` (evaluation team lead is the named reviewer) |
| Accountable human sign-off record | `human-authored` only |
| Compliance documentation (EU DoC, Annex IV) | `human-authored` or `tool-generated` only — `agent-generated` is not accepted |
| Behavioral baseline document | `tool-generated` or `agent-proposed-with-human-review` acceptable |
| Control state record | `tool-generated` acceptable; if `agent-proposed-with-human-review`, the reviewer must not be the release approver |
| Composite state manifest | `tool-generated` or `human-authored` acceptable |

**Minimum standard:** Every artefact submitted to the gate must carry a valid epistemic tier label. The gate reviewer must verify that each artefact's label meets the minimum tier requirement for that artefact type. An artefact with an insufficient tier label (e.g., `agent-generated` compliance documentation) is not accepted at the gate regardless of its content quality. An artefact with a missing label is treated as `agent-generated` for the purpose of the minimum tier check.

**If not met:** The specific artefact is rejected at the gate. The gate does not proceed until a compliant artefact is filed. Epistemic tier labeling cannot be remediated by assertion — a reviewer cannot assert that an unlabeled artefact was human-authored after the fact. The artefact must carry the label at filing time.

---

## Tier 4 Release Path — Policy Envelope Governance

### What changes at Tier 4

Tier 4 systems operate under a different release governance model than Tier 1–3 systems. At Tier 4, agents execute autonomously within a human-approved, machine-enforced policy envelope. The policy envelope defines the boundary within which the agent is authorized to act without human approval of individual actions. This changes the object of the Behavioral Release Gate without changing any of its conditions.

At Tier 3 and below, the Behavioral Release Gate is applied to a specific deployment: this version, this configuration, this behavioral profile, deployed to production. At Tier 4, the Behavioral Release Gate is applied to the **policy envelope specification**: its allowed change classes, blast radius ceiling, evidence schema, rollback conditions, kill-switch configuration, and the behavioral evaluation portfolio that validated the envelope's safety properties. The gate conditions are identical; what they assess is different.

### Envelope approval as release governance

Once a policy envelope passes the Behavioral Release Gate, agent-executed deployments that remain within the approved envelope do **not** require a separate gate pass. The envelope approval is the release governance for in-envelope actions. This is not a relaxation of governance — it is a restatement of where governance is applied. The gate was applied, at full rigor, to the envelope definition. Every in-envelope deployment inherits that governance.

The implication is that envelope definition is high-stakes in a way that individual deployments are not. An error in envelope definition that is not caught at the Behavioral Release Gate propagates to all in-envelope deployments without further gate review. The rigor applied to envelope gate review must reflect this: an envelope gate review is not a review of a single deployment; it is a review of the governance framework for all deployments the envelope will cover.

### Envelope change requires a new full gate pass

Any change that extends, modifies, or relaxes the policy envelope requires a full Behavioral Release Gate pass on the modified envelope before the change takes effect. Changes that trigger a new gate pass include, but are not limited to:

- A new change class added to the allowed change class list.
- The blast radius ceiling raised (higher scope, larger affected population, greater resource limits).
- A rollback condition loosened (the conditions under which the kill-switch fires or rollback triggers are relaxed).
- The evidence schema modified (what evidence is required for an in-envelope deployment is changed).
- The kill-switch configuration changed.
- The behavioral evaluation portfolio validating the envelope's safety properties replaced or reduced.

Changes to in-envelope deployment tooling, monitoring configuration, or operational procedures that do not modify any of the above envelope elements do not require a new gate pass. When in doubt, the release manager must treat the change as an envelope change until a determination is made that it is not.

### Tier 3 → Tier 4 transition is a governed event

The initial Tier 4 operation of any system is itself a governed transition. Before a system first operates at Tier 4 — before the agent first executes actions within the policy envelope without individual human approvals — the initial policy envelope definition must pass the Behavioral Release Gate. This gate pass is the formal record of the organization's acceptance that the envelope provides sufficient governance for the system's blast radius.

There is no organizational shortcut for this gate pass. A system that has operated at Tier 3 with a long and clean track record has a better evidentiary basis for envelope approval, but does not have a waiver from the gate. The track record is evidence; it is not a substitute for the gate. The gate pass for the initial envelope is distinct from and additional to the Tier 3 release gate pass that preceded Tier 4 operation.

### Kill-switch verification as explicit gate condition for Tier 4

For Tier 4 envelope approval, kill-switch verification is an explicit gate condition, not a documentation checklist item. The kill-switch must be tested as functional as part of the gate pass. Functional testing requires end-to-end verification of the full invocation path:

1. **Invocation:** the kill-switch is triggered by an authorized party using the defined invocation mechanism.
2. **Enforcement response:** the agent or the enforcement infrastructure responds by halting in-envelope execution within the defined response time.
3. **Confirmation signal:** the enforcement response generates a confirmation signal that is observable to the authorizing party and to the audit trail.
4. **Audit trail entry:** the invocation, enforcement response, and confirmation signal each generate an audit trail entry that is timestamped and attributed.

A kill-switch configuration that has not been tested in this end-to-end manner is not a compensating control and may not be cited as one in a waiver (Gate Condition 9). Documentation that describes how the kill-switch is designed to work is not a substitute for evidence that it does work. Kill-switch testing must be performed in a production-equivalent environment; sandbox-only testing is not sufficient for Tier 4 envelope approval.

---

## Composite State Manifest at Release

The formal procedure for creating and filing the composite state manifest at each release is as follows.

**Step 1 — Compile component versions.** Before the Stage 4 gate review, the release manager collects the current version identifier for all five composite state components per the format defined in `agent-composite-versioning.md`. Each component must be confirmed at the point of collection — not assumed from the last composite state manifest. The foundation model's date-confirmed field must reflect a confirmation made within 72 hours of the gate review.

**Step 2 — Compute the CSH.** The release manager or a designated technical role computes the Composite State Hash per the formula in `agent-composite-versioning.md`:
```
CSH = hash(code_commit || prompt_version || model_id || kb_snapshot_id || memory_state_hash)
```
The hash function used is recorded in the manifest. SHA-256 is the recommended default. If the organization uses a different hash function, it must be documented and applied consistently — a hash function change between releases renders historical CSH values incomparable.

**Step 3 — Complete the manifest.** The manifest is completed per the YAML format in `agent-composite-versioning.md`, with event type `initial_release` or `release`, the current timestamp in UTC, and the name and role of the person creating the manifest.

**Step 4 — Review and sign.** The manifest is reviewed by the release manager for completeness and accuracy. The named accountable human signs the manifest, attesting that the composite state it records is the state being authorized for production deployment. The signature and date are recorded in the manifest or in the manifest's audit trail record.

**Step 5 — File before deployment.** The signed manifest is filed to the release artefact store before the deployment is executed. Filing is irreversible — the manifest is immutable once filed. The manifest ID and CSH are recorded in the deployment record. If a discrepancy is discovered after filing, a correction manifest is filed with event type `correction` referencing the original manifest ID; the original manifest is not overwritten.

**Step 6 — Index.** The manifest is indexed by both manifest ID and CSH. Both indexes are required: manifest ID for sequential operational lookup; CSH for incident investigation, where the hash is typically recovered from operational logs before the manifest ID is known.

---

## Canary Behavioral Deployment

For agent products with significant user bases, a canary deployment pattern is required before full rollout. The canary period provides the earliest real-world behavioral signal against the new behavioral baseline before the entire user population is exposed.

**Canary configuration:**
- Deploy the new agent version to a controlled subset of the user population: 5–10% for most products; lower percentages (1–5%) for high-risk agent products operating in regulated domains.
- Route traffic deterministically rather than randomly where possible — deterministic routing allows users' complete interaction histories to be correctly associated with the version they experienced, which is necessary for both behavioral monitoring and regulatory audit.
- Define the canary period before deployment: minimum 48 hours for low-risk agent products; minimum 7 days for high-risk agent products classified under EU AI Act Annex III.

**Behavioral monitoring during the canary period:**
- Monitor against the new behavioral baseline (Gate Condition 3), not the prior release's baseline. The canary is testing whether the new release meets its own behavioral profile, not whether it matches its predecessor.
- Collect human evaluation samples from canary-population interactions during the canary period at the same sampling rate defined in the behavioral specification for Stage 5 production monitoring. Do not defer human evaluation sampling to the full rollout.
- Define a rollback trigger before the canary begins: if any monitored metric falls below the rollback threshold in the canary population, the rollout is halted and the rollback procedure is executed. The rollback trigger is a written condition, not a judgment call made in the moment.

**Canary rollback trigger examples:**
- Task success rate drops more than 5 percentage points below the behavioral baseline within the canary population.
- Any safety incident in the canary population.
- Human evaluation rubric scores on the Harm avoidance dimension return a "No" finding on any sampled interaction.
- CSH from operational monitoring diverges from the release-time CSH, indicating a component change occurred during the canary period.

**Canary approval to proceed to full rollout:** The product owner issues explicit written approval to proceed after reviewing the canary period monitoring results. Approval criteria:
- All monitored behavioral metrics within acceptable range after the full canary period.
- No safety incidents during the canary period.
- Human evaluation scores from the canary sample within the acceptable deviation range from the behavioral baseline.
- No rollback triggers activated.

Proceeding to full rollout without the product owner's explicit canary approval is a governance violation. Canary approval is not implied by the absence of rollback triggers — it is a separate affirmative decision.

---

## Behavioral Rollback

Behavioral degradation detected post-deployment requires a structured decision: rollback vs. targeted fix. The wrong decision in either direction has costs. Rolling back unnecessarily disrupts users and destroys operational continuity. Continuing to operate a degraded agent causes harm and accumulates liability.

### Rollback Criteria

**Safety incident (incident class: Safety or Adversarial).** Immediate rollback. A confirmed safety incident — the agent produced output in violation of its hard behavioral boundaries, caused or facilitated harm to a user or third party, or was exploited by adversarial input in production — requires rollback before root cause analysis is complete. The root cause analysis follows the rollback; it does not precede it. An agent that is known to be causing safety-class harm is not in a state where continued operation during investigation is acceptable.

**Behavioral incident (confirmed out-of-spec behavior at scale).** Rollback within 24 hours unless root cause is identified and contained. A behavioral incident means the agent is operating outside its behavioral specification in a confirmed, repeatable pattern — not a single anomalous interaction but a measured deviation from the behavioral baseline. If the root cause is identified within 24 hours and a targeted fix can be deployed that restores in-spec behavior, the rollback may be deferred in favor of the fix. "Identified and contained" means the mechanism of the deviation is understood and a fix is deployed, not merely that a hypothesis has been formed.

**Quality incident (degradation within behavioral specification).** Targeted fix preferred. A quality incident means the agent's output quality has declined — responses are less helpful, less accurate, less aligned with user expectations — but the behavioral specification hard boundaries are still being respected. Rollback is typically disproportionate for a quality incident; a targeted fix (system prompt adjustment, knowledge base update, recalibration) addresses the root cause without the disruption of a full rollback. Assess within 72 hours; if a targeted fix cannot be identified and scoped within 72 hours, escalate to behavioral incident treatment.

### Rollback Procedure per Component

**Code rollback.** Standard deployment tooling, reverting to the prior release tag. This is the rollback that software deployments have always performed. For agent products, a code rollback that does not revert the other composite state components may not restore the prior behavioral state. A code rollback is typically combined with a full composite state reversion to the prior release manifest.

**System prompt rollback.** Configuration system revert to the prior prompt version. Verify the restored prompt against the content hash from the prior composite state manifest — the content hash is the only reliable way to confirm that the configuration system returned the correct version, not a different version with the same label. Prompt rollbacks take effect immediately for new sessions; for stateful deployments where the prompt has already influenced session memory, assess whether a memory reset is also required.

**Foundation model rollback.** Provider version pinning if the provider exposes a snapshot version identifier and supports pinning to a specific snapshot. If the provider does not support pinning, deploy the tested fallback prompt that was validated against the current model version during Stage 3 adversarial testing. The fallback prompt is not a perfect substitute for rolling back the model — it is the best available mitigation when the model version cannot be controlled. Document the limitation explicitly: a foundation model rollback that relies on a fallback prompt rather than a version revert is a partial rollback. Its adequacy must be assessed against the specific behavioral regression.

**Knowledge base rollback.** Snapshot restoration from the snapshot ID recorded in the prior composite state manifest. Verify the restored state against the source manifest hash from the prior manifest. Knowledge base rollbacks may require index rebuilding; the rollback procedure must account for the time this takes. If the knowledge base serves multiple agent products, the rollback affects all of them — coordinate with all dependent teams before executing.

**Memory state rollback.** Full or partial memory reset per the memory governance procedures in `agent-maintenance.md`. A full memory reset returns the agent to its initial memory state (as recorded in the composite state manifest). A partial memory reset removes specific accumulated context identified as contributing to the behavioral regression. The scope of the memory reset must be determined by the root cause analysis; a full reset without root cause analysis is a destructive operation that eliminates evidence.

### Rollback Accountability

**Who authorises:** the product owner and the accountable human jointly. Neither can authorise a behavioral rollback without the other's concurrence. For safety incidents requiring immediate rollback, the accountable human is empowered to act unilaterally if the product owner is unreachable — but the product owner must be notified immediately and their concurrence recorded as soon as they are reachable.

**Time constraint:** trigger to authorisation decision within 4 hours for safety incidents; within 24 hours for behavioral incidents. The clock starts when the incident is classified, not when it is first detected. Classification requires confirmation — a single anomalous interaction is not sufficient to start the clock. A confirmed pattern from monitoring or from the stability test set starts the clock.

**Documentation:** every rollback, whether executed or decided against, is recorded as a version history event in the composite state audit trail per `agent-composite-versioning.md`. An event type of `rollback` records the pre-rollback CSH, the restored CSH, who authorized the decision, and the timestamp.

---

## EU AI Act Conformity Assessment

For high-risk AI systems under EU AI Act Annex III, the conformity assessment process is a governance obligation, not a documentation exercise. The process structure depends on which conformity assessment path applies to this system, as determined at Stage 1 per `agent-regulatory-classification.md`.

### Internal Control — Annex VI

The default path for most Annex III categories. The operator conducts an internal conformity assessment verifying that the AI system satisfies all applicable requirements of the EU AI Act. The technical documentation produced across the APLC stages is the evidentiary basis for the internal assessment.

The internal assessment must be conducted by a team with the competence to assess each of the applicable requirements — technical, governance, and human oversight requirements. An internal assessment conducted by the development team that built the system is structurally compromised in the same way that a red-team conducted by the builder is structurally compromised. For high-risk AI systems, involve personnel who are organisationally separate from the development team in the internal assessment.

The assessment must conclude with a determination: does the AI system conform to the applicable requirements? That determination is the basis for the EU DoC. Signing a DoC for a system that did not complete a genuine conformity assessment is a false declaration under EU law.

**EU AI database registration.** Following the conformity assessment and before market placement, the high-risk AI system must be registered in the EU AI Office database. The registration captures the system's identity, intended purpose, the operator's details, and the conformity assessment status. The registration must be updated when a material change is made to the system.

### Third-Party Assessment — Annex VII

Required for biometric identification systems and AI safety components in critical infrastructure. A notified body (an accredited conformity assessment body authorized by an EU member state) reviews the technical documentation and issues a conformity assessment certificate. The certificate is a prerequisite for the EU DoC; without it, the EU DoC cannot be issued.

Notified body engagement must be initiated at Stage 1 or Stage 2 at the latest. Notified bodies are subject to capacity constraints and review timelines that cannot be compressed by the operator. A Stage 4 gate that is waiting on a notified body certificate because the engagement was not initiated until Stage 3 will wait as long as the notified body's schedule requires. That delay is entirely avoidable and entirely attributable to late classification.

### Systems Below the High-Risk Threshold

For systems that are not high-risk under Annex III, the Stage 4 conformity gate requires documentation of the risk classification rationale, reviewed and current at the time of release. This documentation must be kept current as the system evolves.

**Scope creep and reclassification.** An AI system that began at Stage 1 with a minimal-risk classification can become a high-risk system if its scope expands during development. An agent product initially designed for informational responses that is expanded to include decision recommendations in a regulated domain may cross into Annex III scope. If a scope change during development could affect the risk classification, the release manager must trigger a reclassification review before the Stage 4 gate proceeds. Proceeding to release on a stale classification that no longer reflects the deployed system's actual capabilities is a governance failure.

---

*Stage 4 is not the end of governance — it is the beginning of governed production. The behavioral baseline established at Stage 4 is the foundation for all Stage 5 monitoring. The composite state manifest filed at Stage 4 is the reference for every incident investigation in Stage 5 and Stage 6. The named accountable human who accepts accountability at Stage 4 carries that accountability through the product's operational life. Release is not a handoff; it is a commitment.*

*Cross-references: ASDLC `release-governance.md` for the foundational release gate conditions this document extends; [agent-behavioral-evaluation.md](agent-behavioral-evaluation.md) for the evaluation portfolio that Gate Condition 2 requires; [agent-composite-versioning.md](agent-composite-versioning.md) for the composite state manifest format and filing procedure that Gate Condition 4 requires; [agent-regulatory-classification.md](agent-regulatory-classification.md) for the EU AI Act classification and conformity assessment path that Gate Condition 5 requires; [agent-annex-iv-mapping.md](agent-annex-iv-mapping.md) for the formal mapping of APLC documents to EU AI Act Annex IV documentation requirements referenced in Gate Condition 5; [agent-operations.md](agent-operations.md) for Stage 5 monitoring that depends on the behavioral baseline established at Gate Condition 3; [agent-maintenance.md](agent-maintenance.md) for memory governance referenced in the rollback procedure.*
