# EU AI Act Annex IV — APLC Documentation Mapping

*Cross-lifecycle governance document. Required for all agent products classified as high-risk under EU AI Act Annex III. This document maps APLC governance artifacts to EU AI Act Annex IV technical documentation requirements, identifies coverage gaps, and specifies supplementary documentation required for full conformity.*

*Related documents: [agent-regulatory-classification.md](agent-regulatory-classification.md), [agent-release-governance.md](agent-release-governance.md), [aplc.md](../aplc.md)*

---

## Purpose

EU AI Act Annex IV defines nine technical documentation categories that providers and operators of high-risk AI systems must maintain. This mapping confirms which APLC documents satisfy each Annex IV requirement and identifies gaps that require supplementary documentation outside the APLC's standard output.

This mapping must be reviewed and updated: (a) at each major APLC Framework Version Record update; (b) when EU AI Office guidance on Annex IV interpretation is published; (c) when the agent product's regulatory classification changes.

---

## Annex IV Mapping Table

| Annex IV Category | Requirement Summary | Satisfying APLC Document(s) | Coverage | Gap / Supplementary Action Required |
|---|---|---|---|---|
| **1. General description** | Intended purpose, version information, basic elements, nature of software, interaction with hardware | `agent-conception.md` (Stage 1 product brief, persona design); `agent-composite-versioning.md` (component version identifiers, CSH manifest) | **Full** | None — the product brief and composite state manifest together satisfy the general description requirement. Ensure the manifest is filed at deployment as specified. |
| **2. Design and development process** | Design specifications, development methods, monitoring and testing procedures, validation procedures, intended users, contexts of use | `agent-behavioral-specification.md` (four-layer behavioral envelope, use-case coverage map); `agent-behavioral-evaluation.md` (four-layer evaluation portfolio); `aplc-stage3-inner-loop.md` (Stage 3 engineering process) | **Partial** | **Gap:** Annex IV 2 requires description of the development *process*, including version control, testing methodology, and quality management. The APLC documents specify requirements but do not produce a process description document. **Supplementary action:** Produce a "Development Process Description" document at Stage 3 that describes the specific tools, version control system, CI/CD pipeline, and testing infrastructure used. This document supplements but does not replace APLC Stage 3 artifacts. |
| **3. General capabilities and performance** | Monitoring, functioning, control; capabilities and limitations; accuracy, robustness, cybersecurity | `agent-behavioral-evaluation.md` (probabilistic assurance targets, tail risk limits, adversarial evaluation results); `agent-composite-versioning.md` (behavioral fingerprint); `agent-behavioral-specification.md` (Layer 3 performance targets, uncertainty protocol) | **Full** | None — the four-layer evaluation portfolio and behavioral specification together constitute a comprehensive capabilities and performance description. Ensure evaluation clearance report is filed at deployment. |
| **4. Performance metrics** | Appropriateness of performance metrics for the specific AI system | `agent-behavioral-specification.md` (Layer 3 probabilistic assurance target format, rationale for threshold selection); `agent-behavioral-evaluation.md` (probabilistic gate decision framework) | **Full** | None — the threshold specification process (pre-committed thresholds with documented rationale, Regulatory Owner approval for deviations from defaults) satisfies the "appropriateness" documentation requirement. |
| **5. Risk management** | Risk identification, analysis, evaluation; mitigation measures; residual risk | `agent-regulatory-classification.md` (risk classification and conformity path); `agent-behavioral-specification.md` (safety and alignment requirements, hard boundaries as risk controls); `agent-behavioral-evaluation.md` (red-team findings as risk identification outputs); `waiver-governance.md` (residual risk documentation via waiver records) | **Partial** | **Gap:** Annex IV 5 requires a documented risk management *system* per Article 9, not just risk identification outputs. The APLC produces risk evidence but not a risk management system document. **Supplementary action:** Produce an "AI Risk Management System Description" document at Stage 1 that describes the organization's continuous risk management process, referencing APLC stage gates as the operational implementation. Update this document when the regulatory classification changes or major new risks are identified. |
| **6. Changes throughout lifecycle** | Description of changes made to the system throughout the lifecycle | `agent-composite-versioning.md` (version history and audit trail); `agent-maintenance.md` (recalibration records, model update impact assessments); AGKB Category D (maintenance artifacts, CSH history) | **Full** | None — the CSH version history with required fields (previous CSH, new CSH, changed components, authorization, date, event type) directly satisfies this requirement. Ensure version history is maintained per the specification. |
| **7. Standards and specifications** | List of harmonised standards applied; technical specifications used | None — the APLC does not currently produce a standards compliance list | **Gap** | **Supplementary action (required):** Produce a "Standards Compliance Register" document at Stage 4 that lists: (a) EU AI Act harmonised standards applied (ISO/IEC 42001, ISO/IEC 23894, and any sector-specific standards as they become available); (b) Other technical standards referenced (ISO 27001 for security controls, GDPR technical safeguards standards, sector-specific standards such as IEC 62304 for medical software); (c) Where a harmonised standard has not been applied because none exists for the relevant category, a documented justification for the alternative compliance path taken. This register is updated at each Stage 4 release. |
| **8. EU Declaration of Conformity** | Signed EU Declaration of Conformity as required by Article 48 | Referenced in `agent-release-governance.md` (Operational Readiness Gate condition) | **Full** | None — the APLC specifies the EU DoC as a required gate artifact. The DoC itself is a legal document with prescribed content (Article 48(2)) that the deploying organization must produce; the APLC specifies when it must be produced and filed. |
| **9. Contact details** | Contact details of provider or authorized representative | `agent-release-governance.md` (named accountable human with documented scope); AGKB Category A (accountability role assignments) | **Partial** | **Gap:** Annex IV 9 requires the provider's legal contact details — registered business name, address, and representative contact — not just the named accountable human. **Supplementary action:** Add the provider's legal contact details to the composite state manifest as a required field for high-risk systems. Include: registered entity name, registered address, designated contact for market surveillance authority correspondence. |

---

## Summary: Required Supplementary Documents

For full Annex IV conformity, organizations must produce the following documents in addition to standard APLC outputs:

| Supplementary Document | Produced At | Maintained By | Trigger for Update |
|---|---|---|---|
| Development Process Description | Stage 3 (first production release) | Technical Owner | Each major Stage 3 cycle or toolchain change |
| AI Risk Management System Description | Stage 1 (and updated at classification changes) | Regulatory Owner | Regulatory classification change; major new risk category identified |
| Standards Compliance Register | Stage 4 (each release) | Regulatory Owner | New harmonised standards published; major product scope change |
| Provider Legal Contact Details (added to CSH manifest) | Stage 4 | Regulatory Owner | Legal entity change; contact change |

---

## How to Use This Document

**At Stage 1:** Review Annex IV categories 1, 5, and 9. Ensure the product brief contains sufficient information for the general description (category 1) and initiate the AI Risk Management System Description (category 5). Record the provider legal contact details for category 9.

**At Stage 3:** Produce the Development Process Description (category 2 gap). Ensure the evaluation portfolio produces evidence for categories 3 and 4.

**At Stage 4:** Complete the Standards Compliance Register (category 7). File the EU Declaration of Conformity (category 8). Verify all supplementary documents are present before the Operational Readiness Gate.

**Ongoing:** Maintain the version history (category 6) and update all documents when the trigger conditions in the table above are met.

---

*See also: `agent-regulatory-classification.md` for the classification process that determines whether Annex IV applies; `agent-release-governance.md` for the Operational Readiness Gate conditions that incorporate Annex IV compliance; `aplc-guide.md` for the integration with EU AI Act requirements across APLC stages.*
