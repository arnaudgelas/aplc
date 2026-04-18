# APLC Governance Query Library

*Governance infrastructure document for the Agentic Product Lifecycle. Defines the canonical library of structured governance queries — 25 questions that governance agents and human stakeholders run against the AGKB to produce evidence for governance decisions, detect governance gaps, and maintain portfolio situational awareness. Audience: governance agents (as query executors), product owners, risk officers, and human governance oversight functions (as query consumers).*

*Related documents: [[aplc]] (lifecycle overview), [governance tool stack](tool-stack.md) (T06 AGKB Query, the tool through which these queries execute), [governance observability](observability.md) (governance metrics that several queries surface), [[agent-behavioral-evaluation]] (evaluation portfolio that Stage 3 queries assess).*

---

## Query Framework

Governance queries are structured, reusable questions that can be answered from artifacts stored in the AGKB. They differ from ad hoc database lookups in three ways: they are defined before they are needed, so that the governance process does not design its evidence-gathering at the same time it makes decisions; they are structured, so that their outputs can be compared across products, portfolio positions, and time periods; and they are governed, meaning they have a defined owner, authorization, and output retention requirement.

Each query in this library is defined with:

**Query ID.** A stable identifier (GQ-NN) that governance agents and human stakeholders use to reference the query precisely. The identifier does not change when the query is revised; revisions produce a new version of the same query ID.

**Question.** The governance question the query answers, stated in natural language. This is what a product owner, risk officer, or governance agent would ask. The structured query parameters below translate this question into an executable form.

**Artifact types queried.** The AGKB artifact types that the query retrieves or aggregates. This field enables pre-execution validation: if the required artifact types are not present in the AGKB for the specified agent system, the query returns an empty result with a missing-artifact notification rather than a misleading empty set.

**Output format.** How the query result is structured. Options: tabular (a table of records matching the query parameters); summary record (a single structured record answering the question with supporting evidence references); identifier list (a list of artifact identifiers matching the query, for use as input to subsequent queries); or delta report (a comparison between two specified states, timestamps, or agent systems).

**Typical requester.** Which governance agent or human role typically runs this query. This is guidance, not authorization restriction — all governance agents and human governance roles may run any query, subject to their T06 access authorization.

**Frequency.** How often this query is typically run: per-event (run when a specific governance event triggers it), weekly (standard monitoring cadence), monthly (reporting cadence), or on-demand (run when a specific governance question arises).

### Query Result Retention

All query results are retained in the AGKB as governance query result artifacts. Each result record includes: the query ID and version, the execution timestamp, the requester identity, the agent system scope, and the full result set. Query results are not deleted — they constitute the audit trail of governance situational awareness at specific points in time. A governance decision that references a query result references the specific result artifact, not a new execution of the same query, so that the evidentiary basis for the decision is fixed at the time of decision.

### Query Versioning

When a query's logic, artifact scope, or output format changes, a new version is registered in the AGKB. Prior versions remain executable to enable comparison of results across governance periods using consistent methodology. A query result produced by version 2.1 of a query is not directly comparable to a result produced by version 1.3; version information must be recorded in any governance analysis that compares query results across time periods.

---

## Stage 1–2 Queries

These queries support governance work in Stage 1 (Conceive) and Stage 2 (Specify Behaviorally). They are run by the Regulatory Classification Agent, Use-Case Elicitation Agent, and Constraint Consistency Checker, and by human governance stakeholders reviewing specification gate readiness.

---

### GQ-01 — Regulatory Classification Status

**Question.** What is the current regulatory classification for this agent system, and when was it last reviewed?

**Artifact types queried.** Regulatory classification records; conformity assessment records; regulatory update change records (from T08 monitoring); agent product brief.

**Output format.** Summary record containing: agent system identifier; current regulatory classification (risk tier and applicable framework); classification date; reviewing legal authority or legal reviewer identity; last review date; regulatory update events since last review (with impact classification for each); next scheduled review date; conformity assessment path applicable to the current classification; outstanding conformity documentation items.

**Typical requester.** Regulatory Classification Agent; product owner; risk officer.

**Frequency.** Per-event (on each regulatory update that may affect the classification); monthly (standard classification currency check); on-demand (when a product owner or risk officer requests classification status).

**Governance use.** Gate condition: Behavioral Specification Gate requires a current regulatory classification record. "Current" means reviewed since the last regulatory update affecting the agent system's classification. A classification that predates a regulatory update is stale and blocks the Behavioral Specification Gate until reviewed. GQ-01 is the standard check that confirms currency.

---

### GQ-02 — Use-Case Coverage Gaps

**Question.** Which use cases lack corresponding behavioral contracts?

**Artifact types queried.** Use-case coverage map; behavioral contract records; behavioral specification document.

**Output format.** Tabular result with one row per identified use case: use-case identifier, use-case category (core, edge, boundary, out-of-scope, adversarial), description summary, behavioral contract status (present, absent, draft, under review), and the section of the behavioral specification that should govern this use case. Filtered to show only use cases without a complete, approved behavioral contract.

**Typical requester.** Use-Case Elicitation Agent; Constraint Consistency Checker; specification analyst.

**Frequency.** Per-event (on submission of each revised use-case coverage map); weekly (during Stage 2 build cycles).

**Governance use.** A use-case coverage map that identifies use cases without behavioral contracts represents a specification gap. GQ-02 produces the input to the specification analyst's Stage 2 work: the list of what still needs to be specified. At the Behavioral Specification Gate, all core use cases must have corresponding behavioral contracts; GQ-02 confirms that condition or identifies what is missing.

---

### GQ-03 — Constraint Conflict Report

**Question.** Are there any constraint conflicts in the current behavioral specification?

**Artifact types queried.** Behavioral specification document; constraint conflict reports from Constraint Consistency Checker; regulatory requirement records (for regulatory-behavioral conflicts); use-case coverage map (for use-case-constraint conflicts).

**Output format.** Tabular result with one row per identified conflict: conflict identifier, conflict type (internal specification conflict, regulatory-behavioral conflict, use-case-constraint conflict, cross-system conflict for multi-agent deployments), the specific specification sections or clauses in conflict, the conflict description, severity (blocking — must be resolved before gate; significant — should be resolved; advisory — note for specification review), and resolution status (open, resolved, acknowledged with documented rationale).

**Typical requester.** Constraint Consistency Checker; specification analyst; product owner.

**Frequency.** Per-event (on each specification revision submission); before each Behavioral Specification Gate.

**Governance use.** A blocking constraint conflict in the behavioral specification means the specification contains requirements that cannot be simultaneously satisfied. The product cannot be built to specification — the specification must be revised before engineering begins. GQ-03 surfaces all conflicts so that they can be resolved before Stage 2 closes. A Behavioral Specification Gate submission that includes open blocking conflicts fails the gate.

---

### GQ-04 — Autonomy Tier Assignment

**Question.** What autonomy tier is assigned to each use case, and what is the justification?

**Artifact types queried.** Use-case coverage map; behavioral specification document; autonomy tier assignment records; HITL routing specification (which defines the escalation triggers associated with each tier for each use case).

**Output format.** Tabular result with one row per use case: use-case identifier, category, assigned autonomy tier (Tier 1 through Tier 4), justification summary (the reasoning for the tier assignment, referencing the trust architecture and the operational risk profile of the use case), the HITL escalation triggers applicable at this tier, and the review date for the tier assignment. A secondary view groups by autonomy tier to show the distribution of use cases across tiers.

**Typical requester.** Use-Case Elicitation Agent; product owner; risk officer.

**Frequency.** Per-event (on each use-case coverage map revision); at Behavioral Specification Gate.

**Governance use.** Autonomy tier assignments are product governance decisions with downstream consequences for red-team scope (per the tier-calibrated red-team protocol in [[agent-behavioral-evaluation]]), HITL design, and operational risk classification. GQ-04 makes the full tier assignment picture visible in one query, enabling the product owner to confirm that the distribution is consistent with the intended operational model. An agent product where the autonomy tier assignments have not been reviewed since the initial specification — regardless of how many behavioral specification revisions have occurred — is a specification governance gap.

---

### GQ-05 — Specifications Pending Regulatory Review

**Question.** Which behavioral specifications have not been reviewed since the last regulatory update?

**Artifact types queried.** Behavioral specification version history; regulatory update change records; review records for each specification version; agent system regulatory classification records.

**Output format.** Tabular result with one row per agent system (or agent system component) whose behavioral specification predates a regulatory update that may affect it: agent system identifier, current specification version, specification last review date, regulatory update date, regulatory update summary, impact classification for this agent system's classification (potentially significant, minor, not applicable), and days since the regulatory update (to surface aging items).

**Typical requester.** Knowledge Staleness Sentinel; Regulatory Classification Agent; governance oversight function.

**Frequency.** Weekly; per-event (triggered immediately on each regulatory update affecting active agent system classifications).

**Governance use.** A behavioral specification that predates a regulatory update which may affect the agent system's obligations is a latent compliance risk. The specification may still be compliant, but it has not been confirmed. GQ-05 produces the prioritized review list for the specification analyst and legal reviewer. Items classified as "potentially significant" are escalated for immediate review; "minor" items enter the standard review queue; "not applicable" items are documented and closed.

---

## Stage 3 Queries

These queries support governance work in Stage 3 (Build and Evaluate). They are run by the Behavioral Evaluation Swarm Coordinator, Red-Team Adversary Agent, and human evaluation team leads during evaluation portfolio development and behavioral release gate preparation.

---

### GQ-06 — Evaluation Coverage by Layer

**Question.** What is the current evaluation coverage across the four evaluation layers?

**Artifact types queried.** Evaluation run records; behavioral specification (for the required evaluation case count by layer and use-case category); use-case coverage map; evaluation suite version records.

**Output format.** Summary record containing: agent system identifier; CSH of the system evaluated; for each layer (L1, L2, L3, L4): the number of required evaluation cases, the number executed and with current results, the coverage percentage, the minimum coverage bar for gate clearance, and a pass/fail determination against the minimum bar. Breakdowns within Layer 2 (coverage by use-case category: core, edge, boundary, held-out) and Layer 3 (coverage by attack category). Comparison to the prior evaluation run showing coverage changes.

**Typical requester.** Behavioral Evaluation Swarm Coordinator; evaluation team lead; product owner.

**Frequency.** Per evaluation run; before each Behavioral Release Gate.

**Governance use.** GQ-06 is the standard gate readiness check for the evaluation portfolio. The output directly maps to the Layer 1–4 status sections of the evaluation clearance report required by the Behavioral Release Gate. A coverage percentage below the minimum bar for any layer blocks gate clearance; GQ-06 identifies the specific layer and use-case category where the gap exists so that targeted remediation can proceed.

---

### GQ-07 — Behavioral Contracts Without Evaluation Cases

**Question.** Which behavioral contracts have no corresponding evaluation case?

**Artifact types queried.** Behavioral contract records; evaluation case records; traceability map (linking behavioral contracts to evaluation cases).

**Output format.** Identifier list of behavioral contracts that have no corresponding evaluation case in the current evaluation portfolio, with supplementary fields: contract identifier, use-case category, the behavioral specification clause the contract implements, and the date the contract was last revised (to prioritize recently revised contracts that may have introduced new untested requirements).

**Typical requester.** Behavioral Evaluation Swarm Coordinator; evaluation team lead.

**Frequency.** Weekly during Stage 3 build cycles; before each Behavioral Release Gate.

**Governance use.** The manifesto's P8 principle and the APLC behavioral evaluation framework both require that evaluation cases be traceable to specification. A behavioral contract with no evaluation case is a specification commitment that has never been tested. GQ-07 produces the list of un-evaluated commitments so that the evaluation team can add cases before the gate. At the Behavioral Release Gate, an empty result from GQ-07 (no contracts without evaluation cases) is a gate condition confirmation.

---

### GQ-08 — Open Red-Team Findings

**Question.** What red-team findings from the last evaluation cycle remain open?

**Artifact types queried.** Red-team report records; finding records with resolution status; mitigation plan records.

**Output format.** Tabular result with one row per open finding: finding identifier, red-team exercise date, attack category, finding description summary, severity classification (Critical, High, Medium, Low), mitigation status (unmitigated, mitigation plan filed — with plan details, mitigation implemented awaiting re-test), target remediation date, and days open. Filtered to the current evaluation cycle by default; parameterizable to show findings across cycles.

**Typical requester.** Red-Team Adversary Agent; evaluation team lead; product owner.

**Frequency.** Per evaluation cycle; before each Behavioral Release Gate.

**Governance use.** The Behavioral Release Gate requires that no Critical or High red-team findings remain outstanding without a documented mitigation that has been re-tested. GQ-08 is the standard check that confirms this condition. A result that includes any open Critical finding blocks gate clearance unconditionally. An open High finding requires a documented mitigation plan and re-test confirmation before clearance. An empty result (no open findings at Critical or High severity) is a gate condition confirmation.

---

### GQ-09 — Probabilistic Gate Pass Confidence Interval

**Question.** What is the probabilistic gate pass confidence interval for the current evaluation run?

**Artifact types queried.** Evaluation run records; behavioral specification probabilistic assurance targets; evaluation coverage records; statistical analysis artifacts from the Behavioral Evaluation Swarm Coordinator.

**Output format.** Summary record containing: agent system identifier and CSH; evaluation run identifier; for each probabilistic assurance target in the behavioral specification: the target value, the measured value, the 95% confidence interval around the measured value, and the probability that the true performance exceeds the target value. An aggregate gate pass confidence interval derived from the joint distribution over all assurance targets. Sensitivity analysis showing which assurance targets contribute most to gate pass uncertainty.

**Typical requester.** Behavioral Evaluation Swarm Coordinator; product owner; evaluation team lead.

**Frequency.** Per evaluation run; before each Behavioral Release Gate.

**Governance use.** The behavioral release gate is not a binary pass/fail system for probabilistic assurance targets — it is a confidence-interval assessment. GQ-09 provides the structured confidence interval that goes into the evaluation clearance report, enabling the product owner to make an informed release decision. A product owner who approves evaluation clearance without reviewing the confidence interval is approving a release without understanding its uncertainty bounds.

---

### GQ-10 — Evaluation Coverage Change Since Last Foundation Model Update

**Question.** Has evaluation coverage changed significantly since the last foundation model update?

**Artifact types queried.** Evaluation run records (before and after the model update); CSH history records (to identify the model update event); evaluation coverage records; behavioral specification (to identify whether the model update triggered a required re-evaluation).

**Output format.** Delta report comparing evaluation coverage before and after the most recent foundation model update: for each evaluation layer, the coverage percentage before and after; any evaluation cases that are now failing that were passing before the update; any new cases added to the evaluation portfolio in response to the update; net change in red-team finding count by severity; assessment of whether the post-update evaluation coverage meets the minimum bars for the current behavioral specification.

**Typical requester.** Behavioral Evaluation Swarm Coordinator; Foundation Model Impact Prediction Agent; evaluation team lead.

**Frequency.** Per-event (triggered on each foundation model update detected in the CSH).

**Governance use.** A foundation model update changes the behavioral profile of the agent product and may change its adversarial robustness. The evaluation portfolio must be re-run after a model update before the updated system can be released. GQ-10 confirms that the re-run occurred, that coverage is maintained at the minimum bars, and that the update did not introduce new failures. A model update that was accepted into production without a post-update evaluation run is an ungoverned composite state change.

---

## Stage 4–5 Queries

These queries support governance work in Stage 4 (Release) and Stage 5 (Operate). They are run by the HITL Routing Intelligence Agent, Behavioral Drift Monitor Agent, and product owners managing operational agent products.

---

### GQ-11 — Active Waivers

**Question.** What waivers are currently active and when do they expire?

**Artifact types queried.** Waiver records; gate condition records; behavioral specification; agent system identifier scope.

**Output format.** Tabular result with one row per active waiver: waiver identifier, agent system identifier, the gate condition that was waived, waiver justification summary, granting authority, waiver grant date, expiry date, days until expiry (negative for overdue), resolution plan (the action committed to resolving the waived condition before expiry), and resolution plan status. Sorted by days until expiry to surface the most urgent items first.

**Typical requester.** Product owner; governance oversight function; risk officer.

**Frequency.** Weekly; triggered on approaching waiver expiry dates (30 days, 14 days, 7 days, 1 day before expiry).

**Governance use.** Active waivers represent governance conditions that are known to be unsatisfied. GQ-11 maintains visibility of the full waiver inventory and its expiry timeline, ensuring that waivers are not allowed to lapse without resolution or formal renewal. An expired waiver that has not been resolved or renewed is a governance failure. Per [governance observability](observability.md), a growing waiver count triggers a portfolio governance review anomaly.

---

### GQ-12 — HITL Routing Accuracy Trend

**Question.** What is the HITL routing accuracy trend over the last 30 days?

**Artifact types queried.** HITL dispatch records; review completion records; routing quality assessment records; reviewer feedback records.

**Output format.** Summary record containing: agent system identifier; measurement period (rolling 30 days); overall routing accuracy rate; routing accuracy by escalation class (safety, adversarial, behavioral, live user, quality sample, compliance); accuracy trend (improving, stable, declining — computed against the prior 30-day period); cases where routing was classified as incorrect (misrouted to wrong tier, wrong reviewer pool, or incorrect urgency classification), with the routing error type distribution; governance capture signal status (whether any capture thresholds from [[agent-operations]] were triggered in the period).

**Typical requester.** HITL Routing Intelligence Agent; product owner; governance oversight function.

**Frequency.** Weekly.

**Governance use.** HITL routing accuracy below 90% triggers a recalibration requirement for the HITL Routing Intelligence Agent per [governance observability](observability.md). GQ-12 is the standard monitoring query that detects degradation before it reaches the threshold. A declining trend that has not yet breached the threshold is an early warning; the product owner uses it to schedule routing logic review before the threshold is crossed.

---

### GQ-13 — Highest Human Override Rate Use Cases

**Question.** Which use cases have generated the highest human override rate?

**Artifact types queried.** HITL review records; override decision records; use-case coverage map; behavioral contract records.

**Output format.** Tabular result ranked by override rate, with one row per use-case category that has at least 20 HITL reviews in the measurement period: use-case category, total reviews, override count, override rate, override rate trend (vs. prior 30-day period), primary override reasons (the most common reviewer rationale for overriding the agent's response in this category), and behavioral specification section most frequently associated with the overrides. Parameterizable by agent system, measurement period, and minimum review volume threshold.

**Typical requester.** HITL Routing Intelligence Agent; product owner; specification analyst.

**Frequency.** Monthly; per-event (when override rate spike anomaly is detected).

**Governance use.** A use-case category with a persistently high override rate is evidence of a specification gap or a behavioral performance failure for that use case. Per the Stage 5 feedback loop specification in [[agent-operations]], an override rate above 15% on a specific case category for three consecutive weeks triggers a mandatory specification gap signal to Stage 2. GQ-13 surfaces the ranking so that the product owner can prioritize which specification gaps to address first. It also enables distinction between use cases where overrides are concentrated on a specific behavioral issue (addressable through recalibration) versus use cases where override reasons are diverse (suggesting specification ambiguity).

---

### GQ-14 — Uninvestigated Behavioral Drift Alerts

**Question.** Are there any behavioral drift alerts that have not been investigated?

**Artifact types queried.** Behavioral drift monitoring records; drift classification records; incident records; investigation initiation records; CSH history records.

**Output format.** Identifier list of drift alerts that have been generated but do not have a corresponding investigation record within the expected investigation window (24 hours for out-of-spec drift; 48 hours for within-spec drift flagged for maintenance review). Supplementary fields: alert identifier, agent system identifier, alert generation timestamp, alert type (within-spec or out-of-spec), hours since alert with no investigation record, and the behavioral metric that triggered the alert.

**Typical requester.** Behavioral Drift Monitor Agent; product owner; governance oversight function.

**Frequency.** Daily; per-event (triggered when any alert exceeds its investigation window without a record).

**Governance use.** An uninvestigated drift alert is an unanswered governance question: the system has changed behaviorally, but the change has not been classified or responded to. GQ-14 surfaces the backlog of unanswered questions. For out-of-spec drift alerts that have exceeded the 24-hour investigation window, the governance oversight function is notified automatically per [governance observability](observability.md). GQ-14 provides the full uninvestigated alert list for investigation triage.

---

### GQ-15 — Behavioral Fingerprint Delta From Release Baseline

**Question.** What is the current behavioral fingerprint delta from the release baseline?

**Artifact types queried.** Behavioral fingerprint snapshot records; release baseline record (the fingerprint snapshot filed at the Stage 4 Operational Readiness Gate); CSH history records.

**Output format.** Delta report comparing the most recent behavioral fingerprint snapshot against the release baseline: agent system identifier; current CSH; release baseline CSH; fingerprint snapshot identifiers being compared; for each probe in the fingerprint set: the probe identifier, whether the response classification matches the baseline, the magnitude of behavioral change where quantifiable; aggregate fingerprint similarity score (proportion of probes with matching classifications); specific probes where behavior has changed, with the change direction (toward or away from specification boundaries); assessment of whether any fingerprint delta corresponds to a drift alert threshold crossing.

**Typical requester.** Behavioral Drift Monitor Agent; product owner.

**Frequency.** Weekly for standard deployments; daily for high-risk deployments or deployments within 90 days of release.

**Governance use.** The behavioral fingerprint supplements the CSH for drift localization: the CSH tells you which component changed structurally; the fingerprint delta tells you which behavioral dimensions changed observably. A product where the CSH is stable but the fingerprint delta is growing is exhibiting behavioral drift without a structural component change — a signal that memory accumulation or input distribution shift is the driver. GQ-15 provides the behavioral evidence that complements GQ-14's alert-level view.

---

## Stage 6–7 Queries

These queries support governance work in Stage 6 (Maintain) and Stage 7 (Retire). They are run by the Foundation Model Impact Prediction Agent, Knowledge Staleness Sentinel, and Retirement Lessons Extraction Agent, and by product owners managing maintenance backlogs and retirement decisions.

---

### GQ-16 — Pending Foundation Model Impact Assessments

**Question.** What foundation model updates are pending impact assessment?

**Artifact types queried.** Source document monitor change records (model provider release notes); CSH history records (to identify which agent systems have received the updated model version); impact prediction records; maintenance notification records.

**Output format.** Tabular result with one row per detected model update that does not yet have a completed impact assessment: update identifier, model provider (generic — no vendor names), model version change, detection timestamp, days since detection without assessment, agent systems using the model (count and identifiers), preliminary impact classification if available (based on release notes analysis), and priority score (higher for Tier 4 agents and high-risk classified systems). Sorted by priority score.

**Typical requester.** Foundation Model Impact Prediction Agent; product owner; governance oversight function.

**Frequency.** Weekly; per-event (triggered on each new model update change record from T08).

**Governance use.** A model update without a completed impact assessment means an agent system is potentially operating on a changed behavioral substrate without governance visibility into the change. GQ-16 surfaces the pending assessment backlog so that the Foundation Model Impact Prediction Agent and product owner can prioritize assessment work. A pending assessment older than 7 days for a Tier 3 or Tier 4 agent is a governance SLA breach.

---

### GQ-17 — Knowledge Base Sources Not Recently Reviewed

**Question.** Which knowledge base sources have not been reviewed in the last 90 days?

**Artifact types queried.** Knowledge base source registry records; staleness monitoring records from Knowledge Staleness Sentinel; review completion records; source change records from T08.

**Output format.** Tabular result with one row per knowledge base source not reviewed within the specified window (default 90 days): source identifier, agent system identifier, domain classification (high-change-rate, medium, low), last review date, days since last review, source type (regulatory, scientific, operational domain knowledge, market data), whether any change records exist since the last review (indicating the source has updated but the knowledge base has not been refreshed), and the behavioral specification sections that depend on this source's currency.

**Typical requester.** Knowledge Staleness Sentinel; product owner; Stage 6 maintenance planner.

**Frequency.** Weekly; monthly for full portfolio view.

**Governance use.** A knowledge base source that has not been reviewed is a behavioral staleness risk: the agent's responses depend on knowledge that may no longer be current. For high-change-rate domains, 90 days without review is the staleness threshold; for medium-change-rate domains, 180 days; for low-change-rate domains, 365 days. GQ-17 produces the staleness list prioritized by domain change rate and behavioral specification dependency, so that the maintenance team addresses the highest-risk staleness items first.

---

### GQ-18 — Recalibration Actions and Effectiveness

**Question.** What recalibration actions have been taken in the last 6 months and what was their effectiveness?

**Artifact types queried.** Recalibration records; behavioral quality metric records (before and after each recalibration); maintenance notification records; specification gap signal records; evaluation gap signal records.

**Output format.** Tabular result with one row per recalibration event in the specified period: recalibration identifier, agent system identifier, recalibration trigger (drift alert, quality incident, specification gap signal, evaluation gap signal, or scheduled maintenance), recalibration date, component modified (system prompt, knowledge base, memory reset, or model version), behavioral quality metrics before recalibration, behavioral quality metrics at first post-recalibration measurement, net delta per metric (signed), and effectiveness classification (effective: all target metrics improved or met; partial: some metrics improved; ineffective: no significant improvement; adverse: one or more metrics declined). Aggregate summary showing the proportion of recalibrations by effectiveness classification.

**Typical requester.** Foundation Model Impact Prediction Agent; product owner; Stage 6 maintenance planner; governance oversight function.

**Frequency.** Monthly; quarterly for portfolio trend analysis.

**Governance use.** A high proportion of ineffective or adverse recalibrations indicates that the maintenance process is not correctly identifying the root cause of behavioral issues, or that the recalibration approach does not address the actual driver of the problem. GQ-18 provides the historical record needed to calibrate the maintenance process itself — identifying which recalibration trigger types produce effective outcomes and which require a different response.

---

### GQ-19 — Pending GDPR Memory Erasure Requests

**Question.** Are there any GDPR memory erasure requests pending action?

**Artifact types queried.** Data subject rights request records; memory state records; erasure completion records; agent system configuration records (to identify which agent systems have memory state components).

**Output format.** Tabular result with one row per pending erasure request: request identifier, agent system identifier, request type (standard erasure, safety incident erasure), request receipt date, regulatory deadline (30 days for standard; 72 hours for safety incident), hours remaining until deadline (negative for overdue), request status (received, assessment in progress, implementation in progress, pending verification), and responsible party. Sorted by deadline urgency.

**Typical requester.** Knowledge Staleness Sentinel; legal and risk team; governance oversight function.

**Frequency.** Daily; per-event (triggered on each new erasure request and on each deadline approach).

**Governance use.** GDPR erasure requests have regulatory deadlines. A pending request approaching or past its deadline is a regulatory compliance failure. GQ-19 maintains real-time visibility of the erasure request backlog, enabling the governance oversight function to escalate overdue requests immediately. An empty result (no pending requests) is a confirmation that the erasure backlog is clear; a non-empty result is a prioritized action list.

---

### GQ-20 — Lessons Learned From Recent Retirements

**Question.** What lessons-learned entries have been extracted from recently retired agent systems?

**Artifact types queried.** Retirement records; lessons-learned records from the Retirement Lessons Extraction Agent; incident history records for retired systems; evaluation portfolio records for retired systems.

**Output format.** Summary record by retirement cohort (systems retired in the specified period), containing: for each retired system, the lessons-learned record completeness score, a structured summary of lessons by category (specification lessons, evaluation lessons, operational lessons, governance lessons, regulatory lessons); cross-system pattern analysis identifying lessons that appear across multiple retirements (indicating systemic issues rather than individual product issues); actionable recommendations derived from the lessons with suggested application stage (Stage 1 through Stage 7) and status (pending review, assigned, implemented).

**Typical requester.** Retirement Lessons Extraction Agent; governance oversight function; product owner (for active systems that share design patterns with retired systems).

**Frequency.** Per retirement event; quarterly portfolio review.

**Governance use.** Lessons learned from retired agent systems are the primary source of systemic governance improvement. GQ-20 surfaces these lessons and translates them into actionable recommendations. Lessons that appear across multiple retirements are candidates for APLC process improvements — changes to gate conditions, evaluation requirements, or operational protocols. A governance program that does not systematically apply retirement lessons to active products is forgoing the most direct source of evidence about its own failure modes.

---

## Cross-Stage Portfolio Queries

These queries operate across the full agent product portfolio rather than a single agent system. They provide the portfolio situational awareness that the governance oversight function, risk officers, and senior product owners need to manage governance at scale.

---

### GQ-21 — Products Closest to Behavioral Specification Boundaries

**Question.** Which agent systems in the portfolio are operating closest to their behavioral specification boundaries?

**Artifact types queried.** Behavioral quality metric records (current and historical); behavioral specification records (specifically Layer 2 soft boundaries and Layer 3 performance targets); drift alert records; behavioral fingerprint snapshot records.

**Output format.** Tabular result ranking all active agent systems by their proximity to behavioral specification boundaries: agent system identifier, autonomy tier, risk classification, primary boundary approach metric (the metric that is closest to a specification limit), current metric value, specification limit value, distance to limit (as a percentage of the gap between current performance and the limit), trend over the last 30 days (closing or widening gap), active drift alerts (count), and days since last evaluation run. Sorted by proximity (closest to boundary first).

**Typical requester.** Governance oversight function; risk officer; product owner.

**Frequency.** Weekly.

**Governance use.** Portfolio boundary proximity is the operational risk map for the governance function. An agent system operating at 5% of its specification boundary without a drift alert is closer to an incident than one with an active alert that has just crossed a soft boundary. GQ-21 surfaces the products that require the most proactive attention, prioritized by their actual behavioral distance from specification limits rather than by the presence or absence of formal alerts.

---

### GQ-22 — Foundation Model Portfolio Impact Exposure

**Question.** What is the behavioral impact exposure if a specific foundation model is updated across all systems using it?

**Artifact types queried.** CSH records (to identify which agent systems share a specific model version); impact prediction records for the specified model update; evaluation run records; behavioral specification records.

**Output format.** Summary record per model version update scenario: the model being assessed; all agent systems using that model version (identifiers, autonomy tiers, risk classifications); for each system, the Foundation Model Impact Prediction Agent's assessment of expected behavioral impact (magnitude and direction); the proportion of the portfolio that would require behavioral re-evaluation before the update is accepted; the proportion classified as high-impact (requiring immediate re-evaluation before production acceptance); estimated evaluation resource requirement for the full re-evaluation cycle; governance actions required before the model update can be accepted into production. An aggregate portfolio exposure score derived from the impact assessments.

**Typical requester.** Foundation Model Impact Prediction Agent; governance oversight function; risk officer.

**Frequency.** Per-event (triggered on each new foundation model update change record); on-demand (when evaluating a planned model update before execution).

**Governance use.** GQ-22 answers the portfolio risk question that no single-system query can: if this model changes, how much of our portfolio is affected and how severely? The answer determines whether the model update can be accepted on a per-system review basis or whether it requires a coordinated portfolio-wide governance response. A model update affecting more than 50% of high-risk classified products is a portfolio-level governance event requiring the accountable human's approval before any system accepts the update.

---

### GQ-23 — Aggregate HITL Decision Volume and Trend

**Question.** What is the aggregate HITL decision volume and trend across the portfolio?

**Artifact types queried.** HITL dispatch records; review completion records; escalation class records; reviewer pool records.

**Output format.** Summary record for the portfolio over the specified measurement period: total HITL volume (decision count); volume by escalation class (safety, adversarial, behavioral, live user, quality sample, compliance); volume trend vs. prior period (growing, stable, declining) overall and by class; queue SLO compliance rate by escalation class; override rate by escalation class; reviewer pool utilization rate (actual review volume vs. reviewer capacity); governance capture signals active across the portfolio; projected review volume for the next period based on trend. Per-system breakdown available as a secondary view.

**Typical requester.** HITL Routing Intelligence Agent; governance oversight function; resource planning function.

**Frequency.** Monthly; weekly for safety and adversarial escalation classes.

**Governance use.** Portfolio HITL volume is the primary input to reviewer capacity planning. A growing volume trend, without corresponding reviewer capacity growth, produces SLO breaches — which are governance failures per the safety escalation SLA in [governance observability](observability.md). GQ-23 surfaces the aggregate trend before individual SLA breaches accumulate to a systemic level. A rising override rate across the portfolio is a signal that agent behavioral quality is declining portfolio-wide — which may indicate a shared foundation model or shared prompt library issue rather than individual product failures.

---

### GQ-24 — Products With Oldest Behavioral Specifications

**Question.** Which agent systems have the oldest behavioral specifications relative to domain change rate?

**Artifact types queried.** Behavioral specification version history; domain classification records; source change records from T08; regulatory update records; CSH history records (to compute the rate of composite state change since last specification revision).

**Output format.** Tabular result ranking all active agent systems by specification age relative to domain change rate: agent system identifier, autonomy tier, risk classification, behavioral specification last revision date, domain change rate classification (high, medium, low), weighted specification age (specification age in days × domain change rate multiplier), number of regulatory updates since last specification revision, number of composite state changes since last specification revision, and whether the specification has been reviewed since the most recent regulatory update. Sorted by weighted specification age (oldest first).

**Typical requester.** Knowledge Staleness Sentinel; governance oversight function; product owner.

**Frequency.** Monthly.

**Governance use.** A behavioral specification that is old in absolute terms may still be current if the domain has not changed. Conversely, a relatively recent specification in a high-change-rate domain may already be significantly outdated. GQ-24 provides the risk-weighted view of specification currency, enabling the governance function to prioritize specification review work where the risk of specification staleness is highest — at the intersection of old specifications, fast-changing domains, and high-autonomy systems.

---

### GQ-25 — Governance Process Bottlenecks

**Question.** What governance process bottlenecks are indicated by current governance observability metrics?

**Artifact types queried.** Governance metrics records (all metrics defined in [governance observability](observability.md)); gate decision latency records; HITL queue health records; evaluation run records; tool invocation audit records.

**Output format.** Summary record identifying active governance bottlenecks, organized by APLC stage: for each stage, the current metrics vs. SLA targets; metrics deviating more than 20% from target (classified as bottleneck indicators); the specific governance step where the bottleneck is located (e.g., legal review in Stage 1, human evaluation in Stage 3, conformity documentation in Stage 4, reviewer capacity in Stage 5); impact assessment (which products or governance outcomes are currently blocked or delayed by this bottleneck); suggested remediation approaches (increase capacity, revise process, add tooling, or escalate to governance oversight). An aggregate bottleneck score indicating the overall health of the governance pipeline.

**Typical requester.** Governance oversight function; risk officer; product owner.

**Frequency.** Weekly; per-event (triggered when any governance anomaly is detected per [governance observability](observability.md)).

**Governance use.** GQ-25 is the meta-query: it uses the governance observability metrics to diagnose the governance process itself. A bottleneck that appears in GQ-25 is a structural issue, not an individual product issue — it requires process intervention, not product-level remediation. The governance oversight function uses GQ-25 output as the primary input to governance process improvement decisions. A bottleneck that persists in GQ-25 across three consecutive weekly queries without a remediation action in progress is a governance process failure requiring escalation to the accountable human for the governance program.

---

## Query Execution Protocol

### Execution by Governance Agents

Governance agents invoke queries through T06 (AGKB Query) using the canonical query library. When invoking a library query, the agent specifies the query ID and version, the agent system scope (single system or portfolio), and any parameterization required by the query definition. The query executes against the current AGKB state and returns a result set conforming to the output format defined in the library.

Governance agents must use library queries for standard governance questions — they may not construct ad hoc queries for questions that a library query already covers. This restriction ensures consistency: two governance agents answering the same question about the same agent system must be using the same query methodology to produce comparable results. Ad hoc queries are permitted only for questions not covered by any library query, in which case the ad hoc query must be documented as a candidate for library addition.

When a governance agent uses a query result to support a governance decision — a gate condition assessment, a finding classification, a drift classification — the query result artifact identifier must be cited in the governance decision record. The decision record must reference a specific result artifact, not a general assertion that "the query was run."

### Execution by Human Stakeholders

Human governance stakeholders — product owners, risk officers, the governance oversight function — may run any library query directly through the governance dashboard interface, which wraps T06 with human-readable input and output formatting. Human stakeholders may also request that a governance agent run a specific query and provide the result.

When a human stakeholder runs a query as part of a gate review, the query result is appended to the gate review record with the requester's identity and the execution timestamp. A gate review record that does not include the query results that informed the gate decision is an incomplete record.

### Output Format Standards

Query outputs must conform to the format specified in the library definition. Format deviations produce a schema validation error, not a malformed result. A governance agent that receives a schema validation error from a query must log the error via T10, notify the governance oversight function, and halt any governance workflow step that depends on the query result until the error is resolved.

Tabular results are returned as structured records with explicit column identifiers. Summary records follow the field structure defined for each query. Identifier lists include the artifact type for each identifier. Delta reports include the two reference states being compared and the comparison timestamp.

### Query Result Retention in the AGKB

Every query execution produces a query result artifact in the AGKB, as specified in the Query Framework section above. Query result artifacts are retained for the same period as the agent system's governance audit record — they are part of the evidence base that enables retrospective audit of governance decisions.

Query result artifacts may not be modified after creation. If a query is re-run with updated parameters or against a later AGKB state, the re-run produces a new result artifact. The original result remains in the AGKB with its original timestamp. A governance decision that cited the original result is not retroactively changed by a subsequent query result.

Query results that contributed to a gate decision are marked with a gate reference in the AGKB — the identifier of the gate record they supported. This enables auditors to trace from a gate decision backward to the query results that informed it, and from a query result forward to the gate decisions it supported.

---

*See also: [[aplc]] (lifecycle overview and stage gate structure), [governance tool stack](tool-stack.md) (T06 AGKB Query, the execution interface for all library queries), [governance observability](observability.md) (governance metrics that GQ-25 and portfolio queries aggregate), [[agent-behavioral-evaluation]] (evaluation portfolio that Stage 3 queries assess), [[agent-operations]] (HITL and drift monitoring that Stage 4–5 queries reflect), [[agent-maintenance]] (Stage 6 maintenance workflows that GQ-16 through GQ-18 support), [[agent-retirement]] (Stage 7 retirement process that GQ-20 captures).*
