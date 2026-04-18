# Agent Retirement
## Stage 7: Retire — Governed Retirement of an Agent Product

*APLC document. Governs the retirement of an agent product as a regulated lifecycle event. Audience: product owners, legal and compliance officers, data stewards, operations leads.*

*Related documents: [aplc.md](../aplc.md), [agent-composite-versioning.md](agent-composite-versioning.md), [agent-behavioral-evaluation.md](agent-behavioral-evaluation.md), [agent-operations.md](agent-operations.md), [agent-maintenance.md](agent-maintenance.md), [agent-regulatory-classification.md](agent-regulatory-classification.md), [agent-release-governance.md](agent-release-governance.md)*

---

## What is Stage 7 — Retire?

Retirement is the final governed stage of the Agentic Product Lifecycle. It is not shutting down a server — it is the managed dissolution of a product that has made consequential decisions, built user trust and dependency, and created regulatory obligations. An agent product that is silently decommissioned without a retirement process leaves users without migration paths, regulators without audit access, and the accountability chain dissolved. Retirement done right is as governed as release.

---

## Retirement Triggers and Decision

Retirement is a product decision, not an operational one. The conditions that justify retirement fall into four categories. The decision is owned by the product owner and the named accountable human jointly. It is not unilateral.

### Trigger 1 — Business Purpose No Longer Valid

The problem the agent was designed to solve no longer exists, or the organisation has exited the relevant business. An agent product whose purpose has been superseded by a business exit, a product portfolio change, or a fundamental shift in the problem space is no longer a maintained product — it is an operational liability. An agent whose behavioral specification is no longer being updated, whose knowledge base is no longer being maintained, and whose domain expertise is no longer being applied to its evaluation will degrade behaviorally over time without detection.

The retirement trigger is not "the product is no longer the primary focus." It is "the product's purpose is no longer valid and the organisation cannot commit to governing it." An agent product that is being governed — monitored, evaluated, maintained — can remain in service regardless of its commercial priority. An agent product that is no longer being governed must be retired.

### Trigger 2 — Behavioral Specification Unachievable

The agent cannot maintain compliance with its behavioral specification after multiple recalibration attempts. Continued operation means operating an agent product that is known to be out of specification.

This is the behavioral equivalent of a product recall. If Stage 6 recalibration cannot restore the agent to within-specification behavior — because the foundation model has changed in ways that make the behavioral specification unachievable with the current architecture, or because the agent's problem domain has evolved beyond the specification's reach — continued operation is not a risk management question. It is an ethical and regulatory one. An agent operating outside its behavioral specification is making consequential decisions according to a behavioral profile that has not been authorized and has not been evaluated.

The decision must be documented with the specific specification gaps that recalibration failed to close and the number of recalibration cycles attempted before the retirement decision was made.

### Trigger 3 — Regulatory Non-Compliance

The agent cannot meet applicable regulatory requirements in its current architecture. Continued operation of a non-compliant agent in a regulated domain is not a governance gap to be managed; it is a violation being perpetuated.

Regulatory non-compliance as a retirement trigger typically arises from one of three causes: the applicable regulatory framework changed in a way that the agent's architecture cannot accommodate (e.g., a new mandatory explainability requirement for AI systems making decisions of a type the agent makes, and the agent's architecture is not capable of producing the required explanations); the agent's scope expanded into a regulated domain that was not part of the original classification; or the risk classification at Stage 1 was incorrect and the agent has been operating without the required conformity documentation.

In all three cases, the remedy options are: remediate (rebuild the agent to meet the requirements), obtain a regulatory exemption or transition period (if available), or retire. If remediation is not technically or economically feasible and an exemption is not available, retirement is the only compliant option.

### Trigger 4 — Successor Ready

A successor agent product has been developed, evaluated, and is ready for full migration. Trigger 4 is the only planned retirement trigger. The other three are failure-mode triggers. Trigger 4 is the normal end of a product's lifecycle when a better product has replaced it.

Even for a planned retirement with a ready successor, the retirement process is mandatory. The existence of a successor does not eliminate the agent's user relationships, regulatory obligations, or decision records. Those must be governed through the retirement process regardless of how good the successor is.

### Retirement Decision Documentation

The retirement decision is a formal document. It records:
- The trigger or combination of triggers that justified the decision.
- The evidence supporting each trigger (specification non-compliance evidence, recalibration records, regulatory analysis, successor readiness confirmation).
- The identity of the product owner and accountable human who made the decision.
- For regulated agent products: legal and risk review confirmation. A regulated agent product cannot be retired without a review of the retirement's regulatory implications — ceasing operation of a high-risk AI system triggers post-market obligations, data retention requirements, and notification requirements that must be planned before the retirement begins, not discovered during it.
- The date of the decision and the planned retirement timeline.

The retirement decision document is filed to the product's audit trail. It is the opening artifact of the Stage 7 process.

---

## User Migration

Agent products build user dependency. A user who has been interacting with an agent for months or years may have incorporated it into their workflows, relied on it for record-keeping of past interactions, or have an expectation of continuity that is not acknowledged by the deploying organisation when the product is turned off without notice. User migration is not optional, and its adequacy is measured by user outcomes, not by the deploying organisation's convenience.

### Notification Requirements

**Notice period.** The minimum notice period is defined by risk tier:
- Low-dependency user relationships (the agent provides informational responses with no transaction history or personalised context): 30 calendar days minimum.
- High-dependency user relationships (the agent has accumulated interaction history, has been used for consequential transactions, or is embedded in the user's workflow in a way that creates a material transition burden): 90 calendar days minimum.

For regulated industries, sector-specific consumer notice requirements apply alongside these minimums. Financial services consumer protection rules, healthcare provider communication requirements, and insurance policyholder notice obligations may impose longer notice periods or specific communication content requirements. These must be identified in the regulatory classification document from Stage 1 (`agent-regulatory-classification.md`) and applied here. The APLC minimums are a floor, not a ceiling.

**Communication channels.** Notification must be delivered through every channel through which the user has interacted with the agent or received communications from the deploying organisation. Posting a notice on a webpage that users do not regularly visit is not notification. For each user communication channel in use (in-product notification, email, account dashboard, direct message), a notification must be issued through that channel.

**Content of notice.** Every retirement notice must include:
- What is being retired: the product name and a description sufficient for the user to know which product is ending.
- When: the specific date on which the product will cease to be available.
- What the user should do: a specific action the user must take before the retirement date — export their data, migrate to the successor, contact support, or acknowledge a transition.
- The successor option, if one exists: the name of the successor product, how to access it, and what the migration path is. If no successor exists, the notice must say so explicitly.
- How to access historical data and interaction records: a user's right to their own interaction history with the agent does not end when the agent is retired. The notice must specify how users can access or export their interaction data before and after the retirement date.

### Migration Support

**Documentation.** Complete, current documentation of the retired agent's capabilities, limitations, and interaction patterns, made available to users during the migration period. Documentation that is out of date at the time of retirement is not useful for migration.

**Data export tooling.** Self-service tooling that allows users to export their complete interaction history with the agent, their stored preferences or profiles, and any personalised context the agent accumulated. The tooling must be available for the full notice period and must remain available for a defined period after the retirement date. "After the retirement date" means after the agent stops serving new interactions — the data export capability does not retire on the same date as the agent.

**Human assistance.** For high-dependency users, self-service tooling is not sufficient. A defined human assistance channel must be available throughout the migration period. High-dependency users should be proactively identified and offered direct migration support rather than waiting for them to seek it.

**Decision record access for regulated domains.** For agent products that made consequential decisions in regulated domains — financial recommendations, healthcare suggestions, benefits determinations, insurance coverage assessments — users have a specific right that extends beyond generic data export: access to the records of the agent's decisions about them. A user who received a credit recommendation from the agent has a right, under applicable consumer protection and data protection law, to understand what decision was made and on what basis. Migration support in regulated domains must include a mechanism through which users can retrieve the agent's decision records for their own interactions.

This is not the same as the organisation's own record retention obligation (addressed below in Decision Record Retention). The user's right is to their own interaction and decision records; the organisation's obligation is to retain records for regulatory and accountability purposes. The two overlap but are not identical.

### Migration Verification

**Notification confirmation.** Before the retirement date, confirm that every user in scope has been notified through at least one channel. Notification confirmation is a compliance record: it documents what was sent, to whom, on what date, through what channel, and whether the notification was acknowledged.

**Migration progress tracking.** Throughout the notice period, track what percentage of the active user population has transitioned to the successor or alternative. Migration progress tracking serves two purposes: it identifies users who have not migrated and may need additional outreach; and it provides the evidence basis for the migration completion threshold decision.

**Migration completion threshold.** Define before the notice period begins: when is the agent's active user population small enough that decommissioning does not cause material user harm? The threshold must be expressed as a specific criterion — not "when we feel it's ready" but a measurable condition such as: the active user population (users who have interacted with the agent within the prior 30 days) has declined to fewer than [N] users; or [X]% of the user population has migrated to the successor or confirmed an alternative.

The migration completion threshold is a governance gate. Decommissioning before the threshold is met requires the same joint authorization as the retirement decision itself: product owner and accountable human together, with documented rationale.

---

## Decision Record Retention

Agent products make consequential decisions. Those decisions do not stop being consequential when the agent is retired. A user who received a financial recommendation from the agent two years ago and is now disputing it has the same right to investigate the basis of that decision after retirement as before it. A regulator examining whether the agent's decisions were fair and within its specification during its operational life has the same right to inspect the records after retirement. The organisation's obligation to maintain those records does not end with the agent's operation.

### What to Retain

The following categories of records must be retained after retirement:

**Composite state manifests for all production versions.** Every composite state manifest filed from the initial release through the final production release. These manifests constitute the chain of evidence for what the agent was — its complete behavioral state — at every point in its operational life. Without them, the agent's decisions cannot be attributed to a specific behavioral configuration. Incident investigations that arise after retirement depend on these manifests being retrievable.

**Behavioral evaluation portfolios for all releases.** The complete evaluation clearance report from each Stage 4 release, including the four-layer evaluation portfolio results, the red-team reports, and the behavioral baseline documents. These records document what the agent was evaluated to do, what adversarial vulnerabilities were identified and addressed, and what the behavioral profile was at each release. They are the primary evidence that the agent was built and operated responsibly.

**HITL review records for all escalated cases.** Every interaction that was escalated to a human reviewer through the Stage 5 HITL process, with the reviewer's decision and the rationale recorded. These records document that the human oversight mechanisms worked — that escalations were handled, that reviewers made considered decisions, and that the accountability chain functioned. They are also the user's right: a user whose case was escalated to human review is entitled to know what the reviewer decided and why.

**Safety incident records in full.** Every incident classified as a Safety incident during the agent's operational life, with the complete incident investigation report, the root cause assessment, and the remediation or rollback decision. Safety incident records cannot be summarized or redacted for retention purposes. The full record is required.

**Adversarial incident records in full.** Every incident classified as an Adversarial incident, with the same completeness requirements as safety incidents.

**Random interaction samples for statistical audit.** A statistical sample of the agent's interactions across its operational life, structured so that the sample is representative of the agent's full interaction distribution and sufficient to support statistical analysis of behavioral patterns. The sample does not need to be the complete interaction log — for large-scale deployments, complete interaction log retention is not practical. The sample must be defined, documented, and taken with a methodology that would satisfy audit scrutiny.

### How Long to Retain

The retention period is the longer of:

**Regulatory retention floor.** The applicable regulatory requirement for this agent product's domain and classification:
- EU AI Act post-market surveillance documentation for high-risk AI systems: technical documentation must be retained for 10 years after market placement. This period applies to all Annex IV technical documentation, including the composite state manifests and evaluation portfolios that constitute part of that documentation.
- SR 11-7 model documentation for banking models: 7 years for model documentation (model risk governance documents, validation reports, and change records).
- IEC 62304 post-market surveillance for medical device software: product lifetime plus the applicable post-market surveillance period defined in the manufacturer's post-market plan.
- GDPR-compliant retention schedules for personal data in interactions: governed separately — see GDPR conflict resolution below.
- Sector-specific consumer protection requirements for records of consequential decisions (financial advice, healthcare recommendations, insurance coverage determinations): consult applicable regulatory counsel for the specific jurisdiction and decision type.

**Statute of limitations floor.** The statute of limitations for claims related to the agent's decision domain. Retention periods that expire before the statute of limitations for potential claims leave the organisation without records to defend itself. The applicable statute of limitations must be assessed by legal counsel at the time of retirement planning, not at the time a claim arises.

Where the two floors differ, the longer governs. Where neither floor produces a determinate answer because the applicable regulation or statute of limitations is ambiguous, conservative retention — retaining longer — is the default. The cost of over-retention is storage. The cost of premature destruction is lost evidence and potential regulatory violation.

### GDPR Conflict Resolution

Personal data in interaction logs cannot be retained indefinitely under GDPR. Article 5(1)(e) requires that personal data be kept no longer than necessary for the purposes for which it was collected. The retention policy must resolve the apparent conflict between GDPR's storage limitation principle and the legitimate retention requirements documented above.

The resolution framework distinguishes three categories:

**Category A — Interaction data containing personal data.** The raw content of user interactions, including any personal data the user provided. This category is governed by GDPR. The retention period is the GDPR-compliant schedule established during the agent's operational life in `agent-operations.md`. After retirement, this schedule applies without modification. Personal data in interaction logs is deleted per the GDPR schedule, even if other records from the same time period are retained. GDPR does not permit extending personal data retention for organisational convenience.

**Category B — Decision records referencing interactions by anonymised identifier.** Records of the decisions the agent made, with user identity replaced by an anonymised ID that permits the decision record to be matched to an individual if they exercise their right of access but does not itself constitute personal data. Category B records may be retained longer than Category A records, because the anonymised decision record serves the legitimate regulatory purposes (audit, accountability, regulatory inspection) without retaining unnecessary personal data. The anonymisation must be robust — pseudonymisation that can be reversed with access to a lookup table held by the organisation is still personal data processing under GDPR.

**Category C — Composite state manifests, evaluation portfolios, HITL records, and incident records.** These records contain no personal data by design. Composite state manifests are technical configuration records. Evaluation portfolios are aggregated performance measurements. HITL records should be structured to capture the decision and rationale without personal data where possible — if they do contain personal data (e.g., a HITL review that quotes user interaction content), that content should be pseudonymised or redacted before archiving. Category C records are retained per the regulatory retention floor above.

**Archive structure.** The archive must be structured to maintain this three-category separation, so that GDPR deletion schedules can be applied to Category A records without affecting Category B or Category C records. A single undifferentiated archive from which selective deletion is technically difficult is an archive designed for convenience, not for compliance.

### Archive Requirements

All retained records must be stored in:

**Archival, access-controlled, immutable storage.** Archival means the records are not subject to routine modification as part of ongoing operations — they are closed records, not living documents. Access-controlled means only the accountable human and authorised personnel can retrieve them, and access is logged. Immutable means records cannot be modified or deleted except under the documented retention policy, with access-logged authorisation.

**Maintained accessibility after organisational change.** The archive must remain accessible to the accountable human and to authorised regulatory inspectors even if the deploying organisation changes structure, is acquired, changes its data infrastructure, or loses the personnel who managed the records during the agent's operational life. Archive infrastructure that depends on specific individuals or specific operational systems that will be decommissioned after retirement is not adequate. Archive accessibility is a property of the archive, not a consequence of operational continuity.

**Retrievable, not merely stored.** A record that is technically stored but practically unretrievable — in a deprecated format, on decommissioned infrastructure, indexed by a system that no longer operates — is not retained for compliance purposes. The archive must be tested for retrievability before the agent is decommissioned. Retrievability testing means actually retrieving sample records from the archive and confirming that their contents are legible and complete.

---

## Accountability Chain Preservation

After retirement, the accountability chain must remain resolvable. Accountability that exists only in the memories of former employees is not accountability — it dissolves with personnel turnover. The organisations that deployed an agent product made governance decisions throughout its lifecycle. Those decisions must remain traceable to the people who made them.

### The Accountability Archive

The accountability archive is a structured document that records the named individuals who held the accountable human role and made key governance decisions at each stage. It is filed as part of the decision record archive at retirement and retained for the same period.

**Required entries in the accountability archive:**

**Conception gate.** The person who approved the Agent Product Brief at Stage 1, accepting that the product was appropriately scoped, that the regulatory classification was accurate, and that the accountability chain was established.

**Behavioral specification gate.** The product owner who approved the behavioral specification at Stage 2, accepting that the behavioral specification was complete, that the probabilistic assurance targets were appropriate, and that the trust architecture was correctly designed.

**Behavioral release gate(s).** For each Stage 4 release: the named accountable human who signed the composite state manifest and accepted production accountability; the product owner who approved the evaluation clearance report; and, for regulated systems, the compliance officer who confirmed the compliance documentation was complete. Each release is a separate entry.

**Major governance decisions.** Each entry in the composite state version history that records an authorized component change (model updates, knowledge base updates, recalibrations, rollbacks) must have a named authoriser. The accountability archive is not a separate document from the version history — the version history itself serves as the accountability record for operational decisions. The accountability archive at retirement consolidates the authorisation records from the version history into a single, indexed document.

**Retirement decision.** The product owner and accountable human who jointly made the retirement decision, with the date and the trigger evidence.

### Continuity After Personnel Change

The accountability archive is tied to the product, not to the people in it. When the accountable human changes during the product's operational life — through departure, role change, or reassignment — the incoming accountable human receives the accountability archive and is responsible for its accuracy from the point of their appointment forward. The version history entry for the accountability transition is a `governance-event` entry recording the transition date and the names of both the outgoing and incoming accountable humans.

An organization that cannot produce the accountability archive for a retired agent product cannot demonstrate who was responsible for its governance at any specific point in its lifecycle. For regulated systems, this inability is itself a compliance finding.

---

## Regulatory Decommission Requirements

Retirement does not terminate all regulatory obligations. For regulated agent products, specific post-retirement compliance activities apply. These must be built into the retirement plan, not discovered after the agent is taken offline.

### EU AI Act — High-Risk AI Systems

Post-market surveillance obligations continue after the agent ceases active operation. The EU AI Act requires operators of high-risk AI systems to maintain a post-market surveillance system for the system's lifetime — and the technical documentation and surveillance records must remain accessible for 10 years after market placement ends, not 10 years after market placement begins.

**Post-retirement minimum compliance activities:**
- Maintain technical documentation accessibility: the Annex IV technical documentation must remain accessible to the EU market surveillance authority for the 10-year post-placement period.
- Respond to regulatory inquiries: the organisation must maintain the capacity to respond to regulatory inquiries about the retired system for the duration of the retention period. This requires retaining: a person with knowledge of the system's governance history, access to the accountability archive, and access to the retained records.
- Update the EU AI Office database: register the system's retirement, including the retirement date and the reason code. The database registration does not expire when the system is retired — it must be updated to reflect the system's retired status.
- Serious incident reporting obligations: if a serious incident related to the retired system comes to light after retirement (e.g., a delayed harm caused by a decision made during operation is identified after decommissioning), the serious incident reporting obligation under the EU AI Act still applies. The organisation must maintain a process for receiving, evaluating, and reporting serious incidents involving the retired system.

**Defined post-retirement surveillance period:** the period during which the minimum compliance activities above are maintained is 10 years after the date of last market placement. For systems with a long operational life, this may extend considerably beyond the retirement date. The organisation's retention plan must account for this period from the beginning — at Stage 1, not at Stage 7.

### Financial Services — SR 11-7

A formal model retirement report is required for banking models governed by SR 11-7. The report must be produced before or concurrent with the retirement decision and must include:

**Reason for retirement.** The trigger or combination of triggers, with supporting evidence. For Trigger 2 (behavioral specification unachievable), this includes the recalibration records documenting failed remediation attempts.

**Performance assessment over the model lifecycle.** A summary of the model's behavioral performance from initial deployment to retirement, against its behavioral specification and probabilistic assurance targets. This is drawn from the Stage 5 monitoring records and Stage 6 recalibration records. If the performance record shows sustained out-of-specification operation before retirement, that fact must be in the retirement report.

**Outstanding risk findings at retirement.** Any open findings from the evaluation portfolio, red-team reports, or incident records that were not fully resolved before retirement. Outstanding risk findings do not disappear when the agent is retired. If a known behavioral vulnerability was not remediated before retirement — because retirement was the chosen remedy — that finding must be documented and its status at retirement recorded.

**Successor model reference.** If retirement is triggered by a successor (Trigger 4), the successor model's identifier and the validation documentation for the succession. SR 11-7's model change governance requirements apply to the transition from a retired model to its successor.

### Medical Device Software — IEC 62304

Post-market surveillance under IEC 62304 continues throughout the product lifetime. For software-based medical devices, retirement does not end the post-market surveillance obligation — it initiates the post-retirement phase of surveillance. The manufacturer's post-market surveillance plan must define how surveillance obligations are discharged after the software is taken offline.

**Post-retirement surveillance under IEC 62304:**
- Maintain the software's lifecycle documentation: the complete IEC 62304 lifecycle documentation (software development plan, requirements, architecture, detailed design, implementation evidence, testing records) must remain accessible for the applicable post-market period.
- Vigilance reporting: if a serious incident or field safety corrective action related to the retired software is identified after retirement, the vigilance reporting obligations under applicable medical device regulation (MDR Article 87, FDA 21 CFR 803) still apply. The organisation must maintain the process infrastructure for receiving and reporting such events.
- End-of-life clinical implications: for medical device software where clinical use may continue even after organisational retirement (e.g., a device installed in a clinical setting that is no longer supported), the IEC 62304 post-market obligations apply until the last instance of clinical use is confirmed discontinued. Retirement is organisational; end-of-clinical-use is the operative event for IEC 62304 post-market purposes.

---

---

## Organizational Learning from Retirement

A retired agent product is the highest-signal input the organisation has for building better agent products. It has run in production, made real decisions, encountered adversarial inputs the Stage 3 red team did not anticipate, discovered specification gaps under real-world conditions, and accumulated a complete behavioral history. This knowledge does not carry forward automatically. Without a deliberate process for capturing and transmitting it, the organisation starts the next agent product from the same starting point — and repeats the same mistakes.

### The Retirement Learning Record

A *retirement learning record* is a required retirement artefact. It must be produced before the decommission is confirmed and filed to the product's audit trail alongside the retirement decision document. The retirement learning record is a structured document, not a free-form post-mortem. It must contain:

- **Primary retirement trigger with evidence.** The specific trigger or combination of triggers that caused retirement, with the evidence that was presented to the product owner and accountable human at the retirement decision. For Trigger 2 (behavioral specification unachievable), this includes the recalibration records and the specific specification elements that recalibration failed to restore. For Trigger 4 (planned succession), this includes the successor readiness confirmation.

- **Top 3 recurring behavioral failure patterns.** The three behavioral failure patterns — detected through Stage 5 monitoring, HITL overrides, or user escalations — that recurred most frequently throughout the product's operational life. "Recurring" means the pattern appeared in more than one incident or monitoring period and required more than one response cycle. The description must be concrete: not "quality issues in edge cases" but the specific use-case zone, the specific behavioral metric that reflected the failure, and the specific resolution that was applied each time it recurred.

- **Specification gaps discovered post-deployment.** Gaps in the Stage 2 behavioral specification that were identified during Stage 5 monitoring or Stage 6 recalibration — cases where real-world operation revealed that the specification was incomplete, ambiguous, or incorrect in ways that were not visible during Stage 2 or Stage 3. For each gap: what the specification said, what real-world operation revealed it should have said, and at what stage in the lifecycle the gap was first identified.

- **Evaluation portfolio shortfalls.** Categories of behavioral evaluation that the Stage 3 portfolio failed to cover, where that gap produced a production failure or required a late-stage recalibration. For each shortfall: what the evaluation missed, what production incident exposed the gap, and what evaluation approach would have caught it in Stage 3.

- **Governance waivers granted and their appropriateness in hindsight.** Every governance waiver granted during the product's lifecycle — emergency change procedure uses, recalibration gate bypasses, evaluation scope reductions, notification deferrals — with an assessment of whether each waiver was appropriate given what the organisation now knows about the product's behavior. Waivers that were appropriate remain on record as evidence of proportionate risk management. Waivers that in hindsight were not appropriate are the highest-priority learning for future products.

### Retention and Availability

The retirement learning record is not an internal post-mortem. It is an organizational knowledge asset. It must be retained in a location accessible to Stage 1 teams for future agent product conceptions in the same domain. Retirement learning records that are filed and forgotten are not knowledge assets — they are administrative completions.

For each domain in which the organisation has deployed agent products, the retirement learning records for all retired products in that domain must be available to the Stage 1 team when they begin the Agent Product Brief for a new product. The Stage 1 process should explicitly include a step: identify retired agent products in this domain and review their retirement learning records before finalising the product brief.

### Accountability for the Retirement Learning Record

The accountable human for the retiring product must review and sign the retirement learning record before the decommission is confirmed. The accountability that person holds for the product's lifecycle includes responsibility for ensuring that what the organisation should learn from the product is captured before the knowledge disperses. A decommission confirmation without a signed retirement learning record is an incomplete retirement.

The accountable human's review is not delegable to the engineering team. Engineering produces the input records; the accountable human confirms that the structured synthesis accurately reflects the product's lifecycle and does not omit significant failures or governance gaps.

### Portfolio-Level Pattern Review

For organisations with multiple deployed agent products, individual retirement learning records are necessary but not sufficient. Patterns that appear in a single retirement learning record may be specific to that product; patterns that appear across multiple retirement learning records are signals about the organisation's APLC practices, not about individual products.

A portfolio-level retirement pattern review should occur annually for organisations with three or more retirement learning records in their archive. The review asks: what failure patterns appear in more than one retirement learning record? What specification gap categories appear repeatedly? What evaluation shortfall categories appear repeatedly? What governance waiver patterns appear repeatedly?

The output of the portfolio-level review is a set of specific, actionable improvements to the APLC process: Stage 1 conception criteria to add, Stage 2 specification requirements to strengthen, Stage 3 evaluation categories to add as mandatory, Stage 4 gate conditions to revise, Stage 5 monitoring baselines to adjust. These improvements are governed changes to the APLC itself — they require the same evidence-backed change process as governed product changes, with the retirement pattern review as the evidence basis.

---

*Retirement is not a technical event. It is the final exercise of the accountability that the deploying organisation accepted when it placed an agent product in front of real users making real decisions. The records retained after retirement are the organisation's evidence that it governed the product well. The user migration executed before retirement is the organisation's fulfillment of the trust relationship it built. The accountability chain preserved after retirement is the organisation's commitment that the product's consequences — good and bad — remain attributable to the people who created them. An ungoverned retirement does not reduce the organisation's obligations; it simply makes them harder to fulfill when they come due.*

*Cross-references: [agent-composite-versioning.md](agent-composite-versioning.md) for composite state manifests and the version history that constitute the core of the decision record archive; [agent-behavioral-evaluation.md](agent-behavioral-evaluation.md) for the evaluation portfolios retained per this document's retention requirements; [agent-operations.md](agent-operations.md) for HITL records and incident records referenced in the retention policy; [agent-maintenance.md](agent-maintenance.md) for recalibration records that feed the SR 11-7 model retirement report and for the Stage 6 post-change review process referenced in the retirement learning record; [agent-regulatory-classification.md](agent-regulatory-classification.md) for the risk classification that determines which regulatory decommission requirements apply; [agent-behavioral-specification.md](agent-behavioral-specification.md) for the specification document whose gaps the retirement learning record captures for future Stage 1 teams.*

---

## Lessons Extraction Protocol

The Retirement Lessons Extraction Agent executes a structured knowledge extraction process at Stage 7 to capture institutional knowledge from the retiring agent system's full operational history. This knowledge is stored in AGKB for use by future agent systems.

**Extraction Scope:**
The lessons extraction covers the full operational history of the retiring agent system, from Conception Gate to retirement decision. Sources: all AGKB artifacts for this agent system, incident archive, HITL decision logs, evaluation history, recalibration history, behavioral fingerprint time series.

**Extraction Categories:**

1. **Specification Pattern Library Contributions:**
Extract reusable specification patterns: behavioral contracts that proved effective, constraint formulations that prevented incidents, use-case decompositions that enabled good evaluation coverage. Each pattern is tagged with: the domain context, the autonomy tier, the risk level, and the outcome evidence.

2. **Failure Mode Catalog Contributions:**
Extract failure modes encountered: behavioral incidents, red-team findings, HITL override patterns. For each failure mode: the failure mode description, the root cause (prompt ambiguity, knowledge gap, model limitation, context engineering failure), the remediation that worked, and the evaluation case that was added. Failure modes are tagged for discovery by future agent systems in the same domain.

3. **Evaluation Suite Harvest:**
The evaluation suite developed for this agent system contains cases that may have domain-general value. Cases are reviewed for reusability: domain-specific cases retained in the domain-specific evaluation library; general behavioral cases contributed to the cross-domain evaluation commons. The evaluation commons grows over the organisation's portfolio lifetime.

4. **Specification-to-Outcome Traceability:**
For each behavioral contract, document the outcome trace: was the contract verifiable in practice? Did the evaluation suite reliably detect violations? Did the specification language cause any evaluation ambiguity? This traceability data informs behavioral specification language improvement.

5. **Behavioral Footprint Record:**
The behavioral footprint is the comprehensive record of what this agent system was authorised to do: the full behavioral specification, the autonomy tiers assigned, the containment boundaries, and the gate decisions. The behavioral footprint is retained in AGKB as a permanent record, even after the agent system is retired.

**Extraction Quality Review:**
The extracted lessons are reviewed by the Behavioral Owner before contribution to AGKB. The review assesses: accuracy (is the lesson supported by the operational evidence?), generalizability (is the lesson applicable beyond this specific system?), safety (does the lesson reveal any sensitive security information that should be restricted?).

**Lessons Integration:**
Approved lessons are integrated into AGKB by the Retirement Lessons Extraction Agent. Integration triggers notification to active agent systems in the same domain, enabling them to incorporate relevant lessons into their next maintenance cycle.

---

## Retirement vs. Recalibrate Decision Framework

The decision to retire an agent system vs. continue maintenance (recalibrate) is a governance decision with significant operational and economic consequences. This framework provides the structured criteria for making that decision.

**Decision Trigger Conditions:**
The retirement vs. recalibrate decision is triggered by:
- Sustained behavioral specification compliance failure despite multiple recalibration attempts
- Foundation model withdrawal (model no longer available or supported)
- Regulatory framework change that invalidates the current behavioral specification
- Business case no longer justified (P11: economics of continued operation exceed value delivered)
- Architectural obsolescence (the agent system's architecture cannot accommodate required capabilities)

**Decision Criteria Matrix:**
Assess each criterion and score (High/Medium/Low):

| Criterion | Retire Indicator | Recalibrate Indicator |
| --- | --- | --- |
| Recalibration ROI | Cost to recalibrate > 50% of cost to rebuild | Cost to recalibrate < 20% of cost to rebuild |
| Specification currency | Specification requires fundamental rethinking | Specification requires targeted update |
| Model availability | Foundation model deprecated with no compatible successor | Compatible model available |
| Incident trajectory | Incident rate increasing despite recalibration | Incident rate stable or decreasing |
| Compliance posture | Cannot achieve compliance without architectural change | Compliance achievable through specification update |
| Operational value | Value delivered declining, P1 outcomes not met | P1 outcomes consistently met |

**Retirement Decision Authority:**
All four accountability roles must participate in the retirement decision:
- Business Owner: economic case for retirement vs. recalibration
- Behavioral Owner: behavioral quality assessment and specification currency
- Technical Owner: architectural assessment, recalibration feasibility
- Regulatory Owner: compliance posture, notification obligations

Retirement decision requires explicit approval from all four accountability roles. Disagreement between roles is escalated to organisational governance.
