# Errata

Dated corrections to previously published content in this repository. Each entry
records what was wrong, what was done about it, and when.

## 2026-09-06

- **`agent-regulatory-classification.md:154` gave the technical-documentation
  language duty to "operators" and stated it as a standing requirement; it binds
  the *provider* and it is request-triggered.** The paragraph read: *"The
  technical documentation must be in a language accepted by the relevant market
  surveillance authority of the member state. For operators placing AI systems
  in multiple EU member states, confirm language requirements at Stage 1 rather
  than at Stage 4."* **Article 21(1) of Regulation (EU) 2024/1689 obliges
  "Providers of high-risk AI systems" to supply, "upon a reasoned request by a
  competent authority", the information and documentation demonstrating
  conformity with the Section 2 requirements "in a language which can be easily
  understood by the authority in one of the official languages of the
  institutions of the Union as indicated by the Member State concerned".** Two
  faults, in the same sentence and closing by two different acts: the holder is
  the provider and not the six-role *operator* class of Article 3(8), and there
  is no standing duty to hold the documentation in every market's language in
  advance — the obligation arises on a reasoned request. A deployer acquires it
  only through Article 25(1). The Stage 1 advice is kept because Article 21(1)
  allows no lead time once the request arrives, and it is now addressed to the
  provider. Read at primary 06.09.2026 against
  `inputs/20260902-arnaud/sources/OJ_L_202401689_AIAct.html.gz`, SHA-256
  `a0f437e8966746b88b15d35bc9e7a9dbe930e2938a941548524a565121c7929b` — the
  artefact `D-09`, `D-10`, `D-61` and `D-66` were read against, reused and not
  re-fetched.
- **This site is `D-68`'s class and was missed by every enumeration the entry
  records, including its own correction.** It is **live at `aplc` `HEAD`
  (`821e242`) and was live in the working tree until this edit** — the only site
  in this repository of which that was still true. It escapes `D-68`'s regex
  because the duty verb next to *operators* is `confirm`, which is not in the
  entry's verb list, and it escaped the verb-free widening too. **The register's
  `aplc` limb therefore reads 18 sites in 8 files at `HEAD`, not 17 in 8 and not
  the heading's 16 in 7** — the second consecutive day on which this entry's
  count moved by one, which is the entry's own argument for reading it as a
  floor.
- **`D-73`: this file's tracking state has changed and the register is stale on
  it.** `errata.md` is no longer untracked — `git -C aplc ls-files --stage
  errata.md` returns a blob and `git -C aplc status --short errata.md` returns
  `A ` (06.09.2026, 20:17 CEST): it is **staged and not committed**. So it is now
  walked by `git ls-files`, unlike when the entry below was written, but it is
  still absent from `HEAD` and `git -C aplc diff` (unstaged) still does not show
  this entry. **`aplc` last committed 02.05.2026 at `821e242`**, so nothing in
  this file, and none of the corrections it records, reaches a reader holding
  `HEAD` of this repository. That is not a closed state and this line exists so
  the next reader does not read it as one.
- **Gates, run 06.09.2026 20:19 CEST from the corpus root.**
  `tools/register-crossref.sh` **exit 0, four consecutive runs, byte-identical**
  (md5 `14bf051ba840a746a583484a7d9313fe`), defects **73**, tasks **55**.
  `tools/link-check.sh` **broken 4 / total 1051 across 5 repos** — the total was
  **1046** before this pass and the movement was named in advance: **+5**, being
  the one `../errata.md` link added by the edit above and four added by the
  companion `D-62` edit in `agentic-engineering-manifesto/domains/pharma.md`.
  **Broken did not move, and was not expected to.**
- **This repository contains no `.html` file, so no rebuild follows from this
  edit.**

- **Five cross-references named a path but no repository, and two named a path
  that had been flattened; the repository is now named and the two flattened
  paths point at the files that exist.** `initiative-authorization-gate.md:7`
  listed `governance/governance-integration-note.md`,
  `governance/composition-rule.md`,
  `governance/authority-accountability-matrix.md` and
  `integration/loop-readiness-for-agent-opportunities.md` as bare paths in a
  sentence that already named two other repositories explicitly, and `:21`
  repeated the composition-rule path; `aplc.md:143` and `:181` repeated
  `governance/governance-integration-note.md`. None of those four files exists
  under `aplc/`; all four exist under `agentic-engineering-manifesto/`
  (`governance-integration-note.md` 259 lines, `composition-rule.md` 228,
  `authority-accountability-matrix.md` 326,
  `loop-readiness-for-agent-opportunities.md` 281 — each opened, not judged by
  size, on 06.09.2026). Each was prefixed with the repository name, which is the
  same treatment already carried by `asdlc/asdlc.md:250`. **Naming the
  repository does not make the path resolve for a reader holding only the
  `aplc` tree** — it tells that reader which tree to go and get, which is the
  most a cross-repository reference in a separately-cloned repository can do.
  · **Two references were not missing documents but flattened names, and were
  repaired rather than annotated:** `aplc.md:243` wrote
  `asdlc/governance-agents.md` and `agent/agent-operations.md:609` wrote
  `asdlc/operations-governance.md`; the files exist at
  `asdlc/governance/agents.md` (827 lines) and `asdlc/operations/governance.md`
  (1278 lines). A hyphen stands where a directory separator belongs in both, so
  these are one mechanism, not two coincidences.
  · **Deliberately not changed:** `aplc-guide.md:296` and `errata.md` write
  `regulatory/foundation-model-third-party-register.md` as a bare path, but each
  names *AEM* in the same sentence, so the prose already identifies the tree and
  a prefix would add nothing. `agent/agent-retirement.md:256` — "Trigger 4
  (planned succession)" — is the name of a retirement trigger and not a
  reference to a document; it is left standing on purpose and a later sweep
  optimising for a lower count must not "fix" it.
  · **No line was added or removed in any file touched:**
  `initiative-authorization-gate.md` 179 lines, `aplc.md` 413,
  `agent/agent-operations.md` 609, before and after.
  · **This file is untracked in git and this repository last committed
  `821e242` in May 2026, so `git diff` shows nothing for these edits and nobody
  reading `HEAD` receives them** — that is `D-73`, and this entry is not a
  close of `D-32` at `HEAD`.
- **`D-29` needed no edit here: the definitions table the register asks for is
  already in the tree, and its six line citations were re-checked against the
  files rather than trusted.** `governance/observability.md` carries a
  *Time-Bound Governance Figures — Definitions* section naming, for each figure,
  what starts the clock and what stops it; `governance/tool-stack.md:217` and
  `agent/agent-operations.md:127` each carry an inline clause distinguishing
  their own figure from the others and linking to that section. Every cited line
  was opened on 06.09.2026 and every one is exact — `observability.md:244`
  Tier 3 Commit 1 hour, `:245` Tier 4 Operate 30 minutes, `:253` immediate
  escalation 30 minutes, `:255` urgent out-of-hours 1 hour,
  `tool-stack.md:217` T13 queue SLO 1 hour, `agent/agent-operations.md:127`
  out-of-spec notification 1 hour. **The register's `[DRIFT of labelling]`
  verdict survives re-derivation: the five figures are four different measured
  quantities and reconciling them to one number would destroy four true
  measurements.** As above, none of this reaches `HEAD` (`D-73`).

- **Twelve annex citations in `domains/` named no instrument on their own line
  and were being read as the sector instrument's annexes. The instrument is now
  named on the line; no citation was changed, renumbered or removed.** Every one
  of the twelve is an EU AI Act annex. Because the surrounding prose names
  MiFID II, Solvency II or the medical-devices Regulation, an attribution pass
  that resolves an annex number to the nearest instrument named on the line --
  or, failing that, to the last one named within twenty lines -- filed them
  under that instrument instead. Those three instruments genuinely have annexes
  at the numbers concerned, so no mechanical bound can refuse the reading and
  none was asserted; only the prose can settle it. Sites, each read at the site
  before it was touched: `domains/financial-services.md:113`, `:124`, `:127`,
  `:129`; `domains/insurance.md:119`, `:142`, `:145`, `:148`;
  `domains/pharma.md:52`, `:54`, `:68`, `:107`. In each, the instrument name was
  inserted ahead of the annex number and nothing else was altered; every file
  has the same number of lines it had before.
  · **One of the twelve was hidden by a line break rather than by a missing
  name.** `domains/insurance.md:118-119` already named the instrument, but the
  wrap split it -- the instrument name ended one line and its annex number began
  the next -- so a line-scoped reader saw an annex number with Solvency II as
  the nearest name above it. The paragraph was re-wrapped so the name and the
  number sit on one line. It is a pure re-wrap: word for word identical, byte-
  identical under the checker's own normalisation, and still seven lines long.
  · **`domains/financial-services.md:128-129` was re-wrapped rather than
  inserted into.** That sentence carries a pinned fixture snippet in
  `tools/citation-known-disagreements.tsv`, and an insertion inside the pinned
  words would have broken the pin and turned a live fixture into a false
  regression. The instrument name was placed ahead of the pinned words instead,
  which leaves them intact and re-anchors by one line.
  · **Named rather than fixed, because they are the same class and were not in
  this pass's scope:** `domains/pharma.md:50` carries an EU AI Act annex read as
  the medical-devices Regulation's, and `domains/financial-services.md:129-130`
  splits a second annex citation across a line break, which hides it from a
  line-scoped reader altogether instead of mis-filing it. Both are recorded here
  so the next pass does not have to re-find them.
  · This file is untracked in git, so `git grep` does not see it; it was
  enumerated with `command grep` over `git ls-files` plus
  `git ls-files --others --exclude-standard`, 30 `.md` files scanned.

- **D-57: quotation and restatement faults in the Annex I / Article 6(1)
  re-attributions written in the entries below. The conclusions hold; the
  support was incomplete.** Re-derived at the hashed primary
  (`inputs/20260902-arnaud/sources/OJ_L_202401689_AIAct.html.gz`, sha256 prefix
  `a0f437e89667`, recomputed here).
  **(1) Article 2(2) was quoted as if it were one sentence.** The quotation
  closed after "only Article 6(1), Articles 102 to 109 and Article 112 apply".
  At the primary the provision is **two sentences**; it continues: "Article 57
  applies only in so far as the requirements for high-risk AI systems under this
  Regulation have been integrated in that Union harmonisation legislation."
  The downstream inference — Chapter III and the Annex VI/VII paths do not
  attach — is unaffected and correct; the defect is that a truncation was
  presented as complete. The second sentence is restored inside the quotation at
  `domains/aviation.md` and `domains/automotive.md`, and the fragment in this
  file is marked as sentence 1 of 2 with the remainder given. **3 sites.**
  **(2) The Annex I Section B item 20 entry was restated more narrowly than it
  reads.** Three conclusion-bearing sentences said "unmanned aircraft and their
  remote control equipment", dropping "their engines, propellers, parts". The
  entry reads "unmanned aircraft and their engines, propellers, parts and
  equipment to control them remotely", and is further confined to "the design,
  production and placing on the market of" those. An agent that is a safety
  component of an unmanned aircraft's engine or of a part is inside the entry
  and outside the old shorthand. The verbatim quote at `domains/aviation.md` was
  and is correct; the restatements are corrected to match it. **4 sites**
  (`domains/aviation.md` x3 plus the "consequence" paragraph, and this file).
  **(3) "The Annex I Section B aviation entry", singular — Section B has two.**
  Item 13 is Regulation (EC) No 300/2008 (civil aviation security) and item 20
  is Regulation (EU) 2018/1139; `domains/aviation.md` names 300/2008 correctly
  and then reasoned from a single entry. The conclusion is unchanged and right,
  but the reasoning did not dispose of 300/2008. Every such sentence now
  disposes of **both**: 2018/1139 is confined to the design, production and
  placing on the market of unmanned aircraft, their engines, propellers, parts
  and remote-control equipment, and 300/2008 is civil aviation security —
  neither reaches manned-aircraft avionics or ground-based ATM. **3 sites.**
  **The aviation conclusion was not reopened.** Item 20 is 2018/1139 and the
  qualifier quoted at `domains/aviation.md` is verbatim; "air traffic" occurs
  **0 times in the entire Regulation** (positive control: "2018/1139" -> 8;
  "ATM" word-bounded -> 0, while a naive case-insensitive substring search
  returns 11 hits inside other words). Only the support was changed.
  **(4) Article 6(1) was invoked as a route without limb (b).** The
  re-attribution sentences named the correct Annex I Section A/B memberships but
  omitted the operative filter: Article 6(1) is cumulative, and (b) requires
  that the product "is required to undergo a third-party conformity assessment".
  Annex I membership of the instrument is necessary and **not sufficient**. Both
  limbs are now stated at `domains/pharma.md` and at the two re-attribution
  entries in this file. **3 sites.** No conclusion was weakened to make it
  easier to support; the corpus still does not assert that any particular
  product *meets* (a) and (b), which remains a Stage 1 merits question.
  **(5) A clause duplicated by an earlier edit today.**
  `domains/automotive.md` read "is contributing to a safety-critical decision
  and is contributing to a safety-critical decision". The second occurrence is
  deleted. A flattened whole-repository scan for the same shape (a 2-8 word
  clause repeated across "and"/"or"/comma, whitespace-insensitive so it catches
  the line-wrapped case that a single-line `grep` missed) found **one** further
  candidate, `agent/agent-release-governance.md` "in the manifest or in the
  manifest's audit trail record", which is not a duplication and is left alone.
  **(6) "limited-risk" is not a term of Regulation (EU) 2024/1689.** The Act's
  classes are prohibited practices, high-risk, the Article 50 transparency
  obligations, and the rest; "limited risk AI system" MISSes the primary
  (control: "transparency obligations for providers" HITs). Five sites used it
  as though it were a class of the instrument. Four are rewritten to say what
  the Act says — outside the high-risk class, with the Article 50 transparency
  obligations where triggered — at `domains/automotive.md`, `domains/pharma.md`
  (x2) and `domains/insurance.md`; the fifth, at `domains/pharma.md`, keeps the
  word and marks it in the same sentence as this document's own shorthand.
  **5 sites.**
  **Enumerated with `command grep` run from inside `aplc/` with quoted globs**
  (an unquoted `--include=*.md` produced a false zero earlier today), because
  **this file is untracked and `git grep` does not reach it**:
before editing, `Art(icle|\.) ?2\(2\)` -> 4 · `2018/1139` -> 4 ·
  `300/2008` -> 2 · `Art(icle|\.) ?6\(1\)` -> 26 · `limited.risk` -> 5 ·
  duplicated-clause shape -> 2 candidates, 1 real; after editing the same six
  probes return 5 · 12 · 11 · 32 · 9 · 1, the rises being the corrections
  themselves. The trap reproduced live: an **unquoted** `--include=*.md` errors
  out under `zsh` and yields **0**, where the quoted glob yields 11 — and
  `git grep '300/2008'` reaches 1 file while `command grep` finds 7 matches in
  this untracked file alone. Beyond the lines named in the finding: the second
  Annex I restatement in this file, two further `limited-risk` sites in
  `domains/pharma.md` and one in `domains/insurance.md` — **4 sites**.
  Nine quotations were byte-compared against the primary through the checker's
  own `normalizeForMatch` (which trims and maps every dash to a space, so short
  tokens cannot be anchored by surrounding whitespace): **9 HIT, 0 MISS**, with
  five same-digit-width or whole-token negative controls all MISSing
  ("Article 58 applies only in so far as…", "propellors", "second-party
  conformity assessment", "Regulation (EC) No 300/2018", "limited risk AI
  system") and three positive controls HITting. `2019/214` is a proper prefix of
  `2019/2144` and returns a hit on its own — tokens were compared whole.
  **Nothing in this entry is signed, and the word "verified" is not used as a
  verdict.**

- **D-57 — NEW DEFECT CLASS: a phantom classification category. The document
  that is this repository's authority on EU AI Act classification listed a ninth
  Annex III category. Annex III has eight points.**
  `agent/agent-regulatory-classification.md` carried, under the instruction "For
  each Annex III category, assess: in scope / out of scope / borderline", a
  numbered entry "9. Democratic processes", described as "a distinct
  sub-category from Category 8", placing political messaging, voter outreach and
  political advertising optimisation agents in scope. Re-derived at the hashed
  primary (`inputs/20260902-arnaud/sources/OJ_L_202401689_AIAct.html.gz`, sha256
  prefix `a0f437e89667`, recomputed here): Annex III runs `ANNEX III` ->
  `ANNEX IV` with **eight numbered points and no more** — point 5 ends at (d),
  point 6 ends at (e), point 8 ends at (b), and point 2 has no sub-points at
  all. The phantom entry's content is **Annex III 8(b)**, already stated one
  entry above it, **minus 8(b)'s express exclusion**: "This does not include AI
  systems to the output of which natural persons are not directly exposed, such
  as tools used to organise, optimise or structure political campaigns from an
  administrative or logistical point of view." So the defect was doubly
  consequential — it invented a division of the instrument, and the invented
  division was strictly broader than the real one, sweeping campaign-logistics
  agents into a high-risk class the sub-point excludes by name.
  **Why this class is distinct from D-57's structural-vocabulary entry above.**
  A wrong *article* number sends a reader to a real provision that says
  something else, and the mismatch is visible on arrival. A wrong *division*
  (Title VIII) sends a reader to a division that does not exist. A **phantom
  category inside an otherwise correct enumeration** is worse than either: the
  eight entries around it are right, so the list reads as authoritative, and a
  reader assessing "each Annex III category" in the order given will assess a
  category the instrument does not contain and record an in-scope determination
  against it. It is unfalsifiable at the point of use for the same reason the
  Title VIII citation was, but it is disguised by correct neighbours.
  **How it survived the pass that found everything else.** The line carried no
  "Annex III" string — it sat under a heading that did — so the
  string enumeration (`grep -rn 'Annex III'`, which reaches only lines carrying
  the literal string) could not see it. No line total is recorded for that
  command: this file discusses Annex III at length and would supply a large
  share of any repository figure, so the figure would describe the errata rather
  than the corpus it was meant to measure. It was found by **block
  enumeration**: reading the whole category list from its introducing sentence
  to its closing paragraph and checking every
  entry against the eight points. Five of the previous pass's 39 findings were
  likewise invisible to string search. **Method note for future passes: a list of
  the divisions of an instrument must be enumerated by block and counted against
  the instrument, never matched by the instrument's name.**
  **Fix, not deletion.** The category is removed and its subject matter is
  restated under point 8, where the instrument puts it, with 8(b)'s exclusion in
  the same sentence as the classification (F2): an agent whose output voters see
  directly is within 8(b); a campaign agent used only to organise, optimise or
  structure a campaign administratively or logistically, to whose output natural
  persons are not directly exposed, is excluded by 8(b) itself. Negative control
  under the checker's own `normalizeForMatch`: a probe for "9. Democratic
  processes" MISSes the primary; the 8(b) exclusion quoted above HITs. A second
  site of the same shape — `agent/agent-conception.md:194`, which floated "AI
  systems that influence elections" as a free-standing category alongside the
  eight — was corrected in the same way.

- **D-57: `domains/aviation.md` — a whole domain file scoped from Annex III
  point 2, which does not reach aviation. Six sites. Re-attributed to Article
  6(1)/Annex I, and where neither Annex reaches the case, that is now what the
  file says.**
  The AI System Classification section opened "Aviation is a critical
  infrastructure sector under EU AI Act Annex III §2", quoted point 2's
  enumeration with the word *rail* inserted and the word *digital* dropped, and
  added aviation "by extension … as critical transport infrastructure"; the
  classification was then treated as settled at five further sites, twice with
  the word *unambiguously* or *regardless*. At the primary, Annex III point 2
  reads "intended to be used as safety components in the management and
  operation of critical digital infrastructure, road traffic, or in the supply
  of water, gas, heating or electricity" (HIT), and the words *aviation*, *air
  traffic*, *rail*, *transport* and *maritime* are each **0 occurrences in the
  Annex III body**. The extension is not available: Annex III is amendable only
  by the Commission under Article 7, not by analogy from a domain file.
  **What actually covers aviation was determined rather than assumed, and the
  answer is mostly "neither Annex".** Article 6(1) makes a system high-risk
  where it is a safety component of, or is itself, a product covered by the
  Union harmonisation legislation listed in **Annex I** and that product
  requires third-party conformity assessment. Annex I Section B lists Regulation
  (EU) 2018/1139 (civil aviation / EASA) — but only "in so far as the design,
  production and placing on the market of aircrafts referred to in Article 2(1),
  points (a) and (b) thereof, where it concerns unmanned aircraft and their
  engines, propellers, parts and equipment to control them remotely, are
  concerned" (HIT; a manned-aircraft twin MISSes) — and Regulation (EC) No
  300/2008 on civil aviation security. So of Section B's two aviation entries,
  2018/1139 reaches **unmanned aircraft, their engines, propellers, parts and
  remote-control equipment only**, and 300/2008 is aviation security — neither
  reaches manned-aircraft avionics or ground ATM. For **manned-aircraft avionics and for ground-based air
  traffic management, neither Annex reaches the agent product**, and the file now
  says exactly that, in the sentence that used to assert §2 high-risk, together
  with the point that this is not a finding that such systems are unregulated —
  EASA Part-21, DO-178C/DO-278A and the ATM framework apply on their own terms.
  Where the Article 6(1) route does apply through a Section B entry, Article 2(2)
  limits it: "only Article 6(1), Articles 102 to 109 and Article 112 apply"
  (HIT — this is sentence 1 of 2; Article 2(2) continues "Article 57 applies
  only in so far as the requirements for high-risk AI systems under this
  Regulation have been integrated in that Union harmonisation legislation", so
  the fragment above is not the whole provision), so this Regulation's Chapter
  III requirements and its Annex VI/VII conformity paths do not attach to those
  systems.
  **The existing in-file flag was not treated as covering this.** `errata.md`
  and the flag at `aviation.md` record a deliberate disclosed residual on the
  **Annex VII / Article 43(2)** conformity question — an undefined release gate
  judged worse than a marked contradiction. **That judgment stands and is not
  reversed here.** But it is a different question from Annex III scoping, and
  the flag also happened to mention the *rail*/extension defect while sitting 76
  lines below the classification it qualified. Under F2 a qualification 76 lines
  from its claim does not qualify it: the claim travels stripped. The Annex III
  defect is therefore **resolved in the classification sentences themselves**,
  and the flag's scope is explicitly narrowed in the flag to the Article 43(2)
  residual only. One consequence is recorded in-sentence at both files: the
  conformity section is premised on a §2 classification that no longer stands, so
  it is retained as a record and as a governance requirement of this framework,
  not as an asserted legal path.

- **D-57: `domains/automotive.md` — "Transport is a critical infrastructure
  sector under EU AI Act Annex III §2." The point says *road traffic*. Five
  sites.** *Transport* additionally sweeps in rail, air and maritime, none of
  which is in point 2, and the difference decides classification. Two limits are
  now stated in the same sentence as every §2 claim in the file: the system must
  be a **safety component**, and it must be in the **management and operation of
  road traffic** — the traffic system — which is where traffic-signal control,
  traffic management centres and roadside infrastructure agents sit. **An AI
  system inside a single vehicle is not managing or operating road traffic**, so
  the paragraphs that called ADAS advisory and autonomous-driving monitoring
  agents "unambiguously Annex III §2 high-risk … regardless of ASIL assignment",
  and a vehicle diagnostics agent "likely Annex III §2 in scope", are corrected
  and **re-attributed rather than deleted**: in-vehicle agent products go through
  **Article 6(1)/Annex I**, whose Section B lists Regulation (EU) 2018/858
  (approval and market surveillance of motor vehicles) and Regulation (EU)
  2019/2144 (general safety type-approval requirements) — the type-approval
  regime these functions already sit inside — and, under Article 6(1)(b), only
  where that product is required to undergo a third-party conformity assessment;
  Annex I membership of the instrument is necessary and not sufficient. Article
  2(2) again limits what this Regulation adds. ASIL assignment does not determine the AI Act route
  in either direction. As at `aviation.md`, the pre-existing Article 43(2) flag
  is narrowed in place to the conformity residual and does not cover this.

- **D-57: scope limits missing from six of the eight Annex III category entries
  in `agent/agent-regulatory-classification.md`, and two entries wrong on their
  face. All corrected in-sentence (F2).** Point **1** was missing 1(c) emotion
  recognition entirely, 1(a)'s exclusion of biometric verification "the sole
  purpose of which is to confirm that a specific natural person is the person he
  or she claims to be", and the chapeau's "in so far as their use is permitted
  under relevant Union or national law" — a verification-only agent read as in
  scope. Point **2** had *rail* inserted into the enumeration and *digital*
  and "and operation" dropped (byte control: "road traffic, rail, or in the
  supply of water" MISSes; the instrument's wording HITs). Point **3** was
  missing the confinement of all four sub-points to "educational and vocational
  training institutions at all levels". Point **5** was missing 5(b)'s "with the
  exception of AI systems used for the purpose of detecting financial fraud",
  presented its own heading as an operative criterion, and listed an insurance
  "claims triage agent" as in scope when 5(d)'s triage limb is **emergency
  healthcare patient triage**. Point **6** gave "individual risk assessment" and
  "prediction of criminal offenses" without 6(a)'s *victim* subject or 6(d)'s
  "not solely on the basis of the profiling of natural persons as referred to in
  Article 3(4) of Directive (EU) 2016/680" — and profiling-only offence
  prediction is not point 6 but the Article 5(1)(d) prohibition. Point **7**
  listed "detecting undeclared items", which is in no sub-point of point 7
  (*undeclared* is 0 occurrences in Annex III); 7(d) is "detecting, recognising
  or identifying natural persons", "with the exception of the verification of
  travel documents", and the file now says a customs agent looking for
  undeclared items is not reached by point 7 rather than inventing a limb for
  it. Point **8** was missing 8(b)'s exclusion (see the phantom-category entry
  above). Points 3 and 4 corresponded; every entry was checked, not sampled.

- **D-57: two internal contradictions inside this repository, resolved rather
  than papered over — `agent/agent-regulatory-classification.md` had not
  received the withdrawals its own `domains/` files already carried.**
  (i) The **claims agent** paragraph placed claims settlement "in scope for EU
  AI Act Annex III Category 5 (access to essential private services)".
  `domains/insurance.md` withdrew exactly that claim: 5(a) is public-authority
  benefit eligibility, 5(b) creditworthiness and credit scoring, 5(c) life and
  health insurance pricing, 5(d) emergency calls and dispatch and emergency
  healthcare triage — claims settlement is none of them, and "Access to and
  enjoyment of essential private services and essential public services and
  benefits" is the **heading** of point 5, not a test. The classification is
  withdrawn here too; **no replacement is asserted**, because whether a claims
  agent is high-risk on some other basis has not been settled — it is a live
  Stage 1 question for counsel, not an out-of-scope clearance. The GDPR Article
  22 exposure the paragraph also asserted is unaffected and is retained.
  (ii) The **underwriting agent** paragraph called any underwriting agent "an
  Annex III system under the EU AI Act" and then discussed personal lines under
  that classification. 5(c) reaches "risk assessment and pricing in relation to
  natural persons in the case of life and health insurance" and no other line,
  so non-life personal lines (motor, home, travel) is outside 5(c), and 5(b)
  does not help. The limit is now in the same sentence as the classification;
  the national-law indirect-discrimination point is retained and marked as
  applying whether or not the agent is Annex III high-risk.

- **D-57: `domains/pharma.md` glossed Annex III §5(a) as "(biometric/health
  data)" at two sites. 5(a) is a public-authority benefit-eligibility point.**
  At the primary, 5(a) covers AI systems used "by public authorities or on
  behalf of public authorities to evaluate the eligibility of natural persons
  for essential public assistance benefits and services, including healthcare
  services, as well as to grant, reduce, revoke, or reclaim such benefits and
  services" (HIT). It is not a data-category point and not a biometric point —
  biometrics is Annex III point **1** — and a pharmacovigilance agent inside a
  marketing authorisation holder, or a dispensing/interaction-warning agent in a
  pharmacy, is not a public authority nor acting on one's behalf. Both
  classifications are withdrawn and **re-attributed rather than deleted**: the
  route to assess is Article 6(1)/**Annex I**, under which Regulation (EU)
  2017/745 (medical devices) and Regulation (EU) 2017/746 (IVDs) are Annex I
  Section A entries and clinical decision support software is frequently a
  device in its own right — and, under Article 6(1)(b), only where that device
  is required to undergo a third-party conformity assessment, Annex I
  membership of the instrument being necessary and not sufficient; where the agent is not a device under either
  Regulation, **no Annex reaches it and the file says so** rather than asserting
  a class. The sectoral pharmacovigilance obligations are noted as applying
  regardless.

- **D-57: the Article 6(3) contradiction, handed back unadjudicated by the
  correspondence pass, is settled here at the primary.**
  `agent/agent-regulatory-classification.md` stated that "if the use case is in
  scope, the high-risk requirements apply regardless of how carefully the system
  is built", and, of employment systems, that the classification holds
  "regardless of … the degree to which humans are involved in the final
  decision". **Article 6(3) contradicts the unqualified form of both.** It reads:
  "By derogation from paragraph 2, an AI system referred to in Annex III shall
  not be considered to be high-risk where it does not pose a significant risk of
  harm to the health, safety or fundamental rights of natural persons, including
  by not materially influencing the outcome of decision making", applying where
  the system performs "a narrow procedural task", improves "the result of a
  previously completed human activity", detects decision-making patterns and "is
  not meant to replace or influence the previously completed human assessment,
  without proper human review", or performs "a preparatory task" — with the
  carve-back that a listed system "shall always be considered to be high-risk
  where the AI system performs profiling of natural persons".
  **The resolution, and it is a narrowing rather than a reversal.** The original
  sentences are right about one thing and wrong about another, and the
  distinction is what the file now states: design choices **cannot** move a use
  case between Annex III points or out of a point it falls in, but a design that
  keeps the system inside one of the four Article 6(3) conditions, and that does
  not profile natural persons, **does** take it out of the high-risk class. The
  route is not free — Article 6(4) requires the provider to document the
  assessment before placing the system on the market and to register itself and
  the system under Article 49(2), and Article 80 lets a market surveillance
  authority re-evaluate the classification. For the employment site specifically,
  the file now records that candidate ranking and screening agents will normally
  profile natural persons and so remain high-risk under the carve-back, while an
  agent confined to a narrow procedural or preparatory task that does not profile
  may not be, and that the determination is made against the four named
  conditions in the classification record rather than by asserting that design is
  irrelevant.

- **D-57: a residual of this repository's own Annex IV point 9 correction, at
  `agent/agent-annex-iv-mapping.md`.** The D-57 entry below records that Annex IV
  point 9 is the Article 72 post-market performance evaluation system and not a
  contact-details point, and that the mapping **table** was corrected. The
  narrative "How to Use This Document" section still told the reader to "Record
  the provider legal contact details for category 9" at Stage 1. Contact details
  are an Annex IV point **1(a)** requirement ("its intended purpose, the name of
  the provider and the version of the system"); the sentence is re-attributed
  there, and Annex IV point 9 is moved to the Ongoing paragraph with its actual
  Article 72 / 72(3) content. **Method note:** a correction applied to a table
  and not to the prose that instructs the reader how to use the table leaves the
  defect operative on exactly the reader who follows the instructions.

- **Method note (this pass).** Two enumerations were run from **inside** this
  repository, because a root-level `git grep` is blind to a nested repository and
  a `git grep` of any kind is blind to this untracked `errata.md`. (1) String:
  `command grep -rn 'Annex III' --include='*.md' .` -> **109 lines**, 125
  occurrences, 16 files — reproducing the correspondence pass's 109 exactly.
  (2) **Block**: every numbered enumeration of the divisions of Annex III was
  read from its introducing sentence to its close and each entry checked against
  the instrument — **two such blocks** (`agent-regulatory-classification.md`
  categories 1-9, `agent-conception.md`'s inline list), **nine entries checked in
  the numbered block, one phantom, six wrong or scope-dropped, two
  corresponding**. Neither the phantom nor five of the previous pass's findings
  were reachable by string search. **40 byte-comparisons** were run through the
  checker's own `normalizeForMatch` (`tools/citation-consistency.mjs:351-359`)
  against the hashed primary, each positive control paired with a prefix-safe
  negative twin swapped within digit width or without prefixing (`digital` ->
  omitted, `rail` for the enumeration, `financial fraud` -> `insurance fraud`,
  `unmanned` -> `manned`, `point 8` -> `9. Democratic processes`); **0
  unexpected results**. `normalizeForMatch` trims its argument, so a bare short
  token would return spurious substring hits (a bare " ai " returned 1,634 in the
  preceding pass); every probe here is a full clause or a whole-token anchored
  string. **Nothing in this pass is signed.** Every adjudication is a model
  research pass prepared at the primary and marked; a model cannot sign, and the
  domain readings most likely to be wrong are named in the files themselves as
  Stage 1 questions for counsel rather than settled.

- **D-57 — NEW DEFECT CLASS: a structural-vocabulary error. Two sites cited
  "Title VIII of the EU AI Act". Regulation (EU) 2024/1689 has no Titles at all.**
  Enumerated at the hashed primary
  (`inputs/20260902-arnaud/sources/OJ_L_202401689_AIAct.html.gz`, sha256 prefix
  `a0f437e89667`, recomputed here), the Act is divided into **thirteen Chapters,
  I to XIII, subdivided into Sections** — I General provisions; II Prohibited AI
  practices; III High-risk AI systems; IV Transparency obligations for providers
  and deployers of certain AI systems; V General-purpose AI models; VI Measures
  in support of innovation; VII Governance; VIII EU database for high-risk AI
  systems; IX Post-market monitoring, information sharing and market
  surveillance; X Codes of conduct and guidelines; XI Delegation of power and
  committee procedure; XII Penalties; XIII Final provisions. *Title* is the
  structural vocabulary of the older directives and of the Treaties, not of this
  Regulation: the only three occurrences of "Title" plus a numeral anywhere in
  the instrument are cross-references to **Title V TEU** and **Title V of Part
  Three TFEU**, in recitals. A byte-comparison for `TITLE VIII` against the
  primary MISSes; `CHAPTER VIII EU DATABASE FOR HIGH-RISK AI SYSTEMS` HITs.
  **Why this class matters and why it is recorded separately.** A wrong article
  number sends a reader to a real provision that says something else, and the
  reader can see the mismatch. A wrong *division* sends the reader to a division
  that does not exist. Opening the Act and finding no Title VIII, the reader
  cannot tell whether the claim is wrong or whether they have misunderstood the
  instrument's organisation — the citation is unfalsifiable at the point of use,
  and the natural recovery (assume the numeral is right and look for Chapter
  VIII) lands on the **EU database for high-risk AI systems**, which has nothing
  to do with general-purpose AI models. The defect therefore fails safe in
  neither direction.
  **What GPAI actually is.** **Chapter V, Articles 51 to 56**, in four Sections:
  Section 1 classification rules (Articles 51–52); Section 2 "Obligations for
  providers of general-purpose AI models" (Articles 53–54); Section 3
  "Obligations of providers of general-purpose AI models with systemic risk"
  (Article 55); Section 4 codes of practice (Article 56). **Every duty in Chapter
  V binds the provider of the model.** Corrected at
  `agent/agent-regulatory-classification.md:86` and `:90`, which now state the
  Chapter, its Section structure, its article range, and the duty-holder, and say
  in-sentence that the Regulation has no Titles.
  **Enumeration and scope.** `command grep -rn 'Title [IVX]' --include='*.md' .`
  run from inside `aplc/` returned **4 lines before this pass**. **Two were the
  defect** — `agent/agent-regulatory-classification.md:86` and `:90`, both making
  a load-bearing claim about where GPAI is regulated. **Two were correct and were
  deliberately left alone**: the earlier D-57 hand-forward entry in this file,
  which quotes the wrong string in order to record that it is wrong. A wrong
  string quoted inside its own retraction is correct behaviour, not a defect, and
  a blanket replacement over all four sites would have destroyed the record of
  the error. **No citation site in this repository used *Title* correctly for
  another instrument** — stated of citation sites, not of every line, because
  this file elsewhere reports the Act's own recitals cross-referring to Title V
  TEU and Title V of Part Three TFEU, which is the word used correctly for other
  instruments and is not a defect. Each site was checked individually rather
  than assumed,
  because *Title* is the right structural word for the Treaties and for several
  directives, and the same enumeration run against the Act itself found exactly
  that usage in its recitals. After this pass the same command returns **6
  lines**, all of them records rather than claims: the corrected sentence at
  `agent/agent-regulatory-classification.md:86`, which names the string "Title
  VIII" in order to reject it, and five lines in this file.

- **D-57: Annex IV technical documentation was attributed to "providers and
  operators". Article 11(1) is passive; the duty binds the provider.** At the
  hashed primary, Article 11(1) reads "The technical documentation of a high-risk
  AI system shall be drawn up before that system is placed on the market or put
  into service and shall be kept up-to date" — passive, naming no holder in that
  sentence. The holder is settled by the Article's place and its context, and the
  Act states it explicitly in one place: **Article 22(3)(a)** empowers an
  authorised representative to "verify that the EU declaration of conformity
  referred to in Article 47 and the technical documentation referred to in
  Article 11 have been drawn up and that an appropriate conformity assessment
  procedure has been carried out by **the provider**". Corroborating: Article 11
  sits in **Chapter III, Section 2**, and **Article 16(a)** obliges providers of
  high-risk AI systems to "ensure that their high-risk AI systems are compliant
  with the requirements set out in Section 2"; **Article 18(1)** obliges "The
  provider" to keep the Article 11 documentation at the disposal of the national
  competent authorities for ten years. **Operator is the wrong class** — Article
  3(8) defines it as "a provider, product manufacturer, deployer, authorised
  representative, importer or distributor", five of whose six members do not draw
  up Annex IV documentation; an authorised representative in particular keeps a
  copy and verifies, under Article 22(3)(a) and (b). **The one route in** is
  **Article 25(1)**: a distributor, importer, deployer or other third party that
  renames, substantially modifies, or changes the intended purpose of a system
  "shall be considered to be a provider of a high-risk AI system for the purposes
  of this Regulation" and becomes subject to Article 16. Corrected at
  `agent/agent-annex-iv-mapping.md:11`, which now states the passive
  construction, the three provisions that resolve it, and the Article 25(1)
  route. **This is the fourth site of the same defect**, after the three the
  Article 73 pass corrected — it is a pattern in this repository, not an
  isolated slip.

- **D-57: Annex IV row 8 cited Article 48 for the EU declaration of
  conformity. Article 48 is CE marking; the declaration of conformity is
  Article 47 — and the same file states it correctly 17 lines above.** At the
  hashed primary (`inputs/20260902-arnaud/sources/OJ_L_202401689_AIAct.html.gz`,
  sha256 prefix `a0f437e89667`), read at the structural subdivisions
  `id="art_47"` and `id="art_48"`, **Article 47 is "EU declaration of
  conformity"** with five paragraphs — 47(1) "The provider shall draw up a
  written machine readable, physical or electronically signed EU declaration of
  conformity for each high-risk AI system, and keep it at the disposal of the
  national competent authorities for 10 years"; 47(2) "The EU declaration of
  conformity shall contain the information set out in Annex V"; 47(3) single
  declaration where other Union harmonisation legislation also requires one;
  47(4) the provider assumes responsibility and keeps it up to date; 47(5)
  delegated acts amending Annex V. **Article 48 is "CE marking"**, also five
  paragraphs, none of which is about the declaration: 48(1) the general
  principles of Article 30 of Regulation (EC) No 765/2008, 48(2) digital CE
  marking for systems provided digitally, 48(3) affixing visibly, legibly and
  indelibly, 48(4) the notified body identification number, 48(5) CE marking
  under other Union law.
  **This is a citation that names a real article and describes a different
  one**, so no structural check can catch it — Article 48 genuinely has a
  paragraph (2), and the sub-clause test therefore passes on `Article 48(2)`
  while the claim attached to it belongs to 47(2). Only a reader comparing the
  claim to the provision finds it.
  **Corroborated by the Act's own cross-reference, byte-compared at the
  primary:** Article 22(3)(a) empowers an authorised representative to "verify
  that the EU declaration of conformity referred to in **Article 47** and the
  technical documentation referred to in Article 11 have been drawn up" —
  **HIT**; the same sentence with "Article 45" and with "Article 48"
  substituted (same digit width) both **MISS**.
  **Corrected in place, re-attributed rather than deleted:** at
  `agent/agent-annex-iv-mapping.md` row 8, "Article 48" became "Article 47" and
  "Article 48(2)" became "Article 47(2)", with the Annex V content requirement
  named. **A second error in the same cell is corrected in the same edit:** the
  cell said the DoC is the document "the deploying organization must produce",
  which contradicts Article 47(1) ("The provider shall draw up") and
  contradicts this same file's own opening paragraph, where the provider/
  operator distinction is established at length; the cell now binds the
  **provider** and says "not the deployer" in the same sentence.
  **Left alone because they are already correct:** the same file's line 11 and
  this errata file's D-57 entry above both quote Article 22(3)(a) naming
  **Article 47**, and neither was touched. **The two duties are not conflated
  anywhere else in this repository:** outside this errata file the only two
  CE-marking mentions are
  (`agent/agent-regulatory-classification.md`, in an MDR context, and
  `agent/agent-conception.md`, listing Stage 4 release activities) carry no
  article number and neither merges the marking with the declaration.
  **Enumerated, not assumed:** searching the whole repository from inside it for
  `Article 47`/`Article 48` in any form, plus "declaration of conformity" and
  "CE mark", returns 25 sites in 8 files, of which 5 are numeric Article 47/48
  citations. Of those 5, **one was wrong** (row 8, both its numbers), **three
  were already correct and were left alone** (line 11 here, this errata file,
  and the Article 47 cross-reference), and **one is a different instrument** —
  `agent/agent-regulatory-classification.md` cites **Solvency II** Article 48,
  which at the Solvency II primary (`sii.html.gz`, sha256 prefix
  `1e6a28843ac3`) is "Actuarial function", whose 48(1)(b) and 48(1)(i) do cover
  the models underlying technical provisions and capital requirements; that
  citation is a Solvency II matter and was **not** modified by this pass.
  Prefix-safe controls: `Article 4` matches 4 sites, disjoint from the 5
  Article 47/48 sites, so no prefix bleed; the digit-width swap `Article 45`
  matches 0.
  **One hazard this correction creates, recorded rather than left to be
  discovered:** the citation-consistency extractor files this row's articles
  under **GDPR**, because the line names no instrument and GDPR is the nearest
  name to its left — the run reports "GDPR Art. 47 - 2 site(s), not checked"
  where before it reported "GDPR Art. 48 - 1 site(s)". **GDPR does have an
  Article 47** ("Binding corporate rules"), so if GDPR Art. 47 were ever
  enumerated `complete:true` in the structure table, this now-correct AI Act
  citation would fire as FABRICATED against the wrong instrument. This is the
  same live false-accusation risk already recorded for GDPR Art. 72, and it is
  a defect of the attribution step, not of the corrected prose.
  **Measured, not inferred:** the checker was run with this row reverted and
  again with it corrected, at one tree state — sub-clause `checked` 409 -> 410
  and `no structure data` 25 -> 26 (one `48(2)` citation replaced by `47(2)`
  and `47(1)`), while **`OK` 383, sub-clause `fabricated` 1, and section 6
  "truly new" 0 did not move in either direction**. The reverted file was
  restored and confirmed byte-identical.

- **D-57: Annex IV point 9 was described as "Contact details of provider or
  authorized representative". It is the post-market performance evaluation
  system.** Found while settling the entry above, at the same primary. Annex IV
  has exactly nine numbered points and **none of them is a contact-details
  point**. Point 9 is "A detailed description of the system in place to evaluate
  the AI system performance in the post-market phase in accordance with Article
  72, including the post-market monitoring plan referred to in Article 72(3)".
  The mapping table therefore both asserted a requirement Annex IV does not
  contain and omitted one it does — and the omitted one is a substantive
  documentation obligation the APLC has material for. Negative control: a probe
  for a tenth Annex IV point MISSes; a probe for "contact details of the provider
  or the authorised representative" MISSes anywhere in the Act. **No duty was
  deleted.** The contact-details requirement is real and is **re-attributed
  in-sentence** to its actual sources — Annex IV point **1(a)**, "its intended
  purpose, the name of the provider and the version of the system", plus
  **Article 16(b)** and the EU declaration of conformity — and moved into row 1
  of the mapping table with its supplementary action intact. Row 9 now carries
  the Article 72 post-market evaluation requirement, its coverage assessment, and
  a note recording what the row previously said.

- **D-57: "Operator obligations under Articles 28–29" for GPAI. Articles 28 and
  29 are about notifying authorities and notified bodies, and the Act imposes no
  GPAI obligation on an "operator" at all.** At the primary, **Article 28 is
  "Notifying authorities"** and **Article 29 is "Application of a conformity
  assessment body for notification"** — both in Chapter III, Section 4, addressed
  to Member States and to conformity assessment bodies. Neither mentions
  general-purpose AI. The four duties the site listed under them — technical and
  organisational measures, monitoring for misuse, fundamental rights impact
  assessment, logging — are a mixture of real duties from elsewhere and
  unsourced material, and are **re-attributed rather than deleted**, at
  `agent/agent-conception.md:204`: Article 16 for the provider of a downstream
  high-risk system, Article 26 (and 26(5)) for its deployer, **Article 27** for
  the fundamental rights impact assessment — which is a deployer duty confined to
  bodies governed by public law, private entities providing public services, and
  deployers of Annex III point 5(b) or (c) systems, **not** a GPAI obligation and
  not one that attaches to every high-risk deployment — Article 50 transparency,
  Article 4 AI literacy, and Article 25(1) for role conversion. The same fiction
  of a "GPAI operator obligation" tier is corrected at
  `domains/automotive.md:47`, `domains/pharma.md:41` and `:47`,
  `domains/financial-services.md:85`, `aplc-guide.md:244`, `:478`, `:486`, and
  `agent/agent-regulatory-classification.md:58`, `:92`, `:94`, `:107` (which had
  the *operator*, not the provider, conducting the Article 43 internal
  conformity assessment). Byte-compared negative controls
  `Article 28 Obligations of operators of general-purpose AI models`,
  `obligations of operators of general-purpose AI` and
  `obligations of deployers of general-purpose AI models` all MISS the primary;
  `Article 28 Notifying authorities` and
  `SECTION 2 Obligations for providers of general-purpose AI models` HIT.
  One claim at `agent/agent-regulatory-classification.md:92` could not be
  sourced at all — that a downstream organisation acquires extra transparency or
  documentation duties because the model it uses is classified systemic-risk —
  and is **marked unsourced in-sentence (F2)** rather than removed, since Article
  55 binds only the provider of the model.

- **Method note.** Every quotation above was byte-compared against the hashed
  primary through the checker's own `normalizeForMatch`, and **78 probes** were
  run in total with **0 unexpected results**, each positive control paired with a
  prefix-safe negative twin. Numerals were swapped only within digit width
  (`11`->`17`, `10`->`15`, `47`->`48`, `72`->`74`, `5 (b)`->`7 (b)`,
  `two weeks`->`four weeks`); roman numerals were chosen so that neither string
  prefixes the other (`V`->`IX`, never `V`->`VI`; `VIII`->`IX`; `XIII`->`XIV`;
  `III`->`XII`; `Annex IV`->`Annex VI`, `Annex XI`->`Annex XII`); word swaps were
  chosen the same way (`providers`->`deployers`, `provider`->`operator`,
  `drawn up`->`maintained`, `practice`->`conduct`, `service`->`use`,
  `training`->`testing`, `systems`->`models`, `distributor`->`contractor`). One
  probe, a caret rendering of the Article 51(2) compute threshold, MISSed because
  the Act sets it as a superscript; the sentence in
  `agent/agent-regulatory-classification.md:92` was rewritten to close the
  quotation before the numeral rather than to assert a quotation that does not
  match.


- **D-57: Article 73 was described as binding "providers and operators" and was
  stated with no reporting deadline at all. Both faults are corrected in-sentence
  at every site; the deployer's duty is Article 26(5), not Article 73.** Read end
  to end at the hashed primary
  (`inputs/20260902-arnaud/sources/OJ_L_202401689_AIAct.html.gz`, sha256 prefix
  `a0f437e89667`), **Article 73 has eleven paragraphs**, and **Article 73(6)
  carries no lettered sub-items**. **Article 73(1) binds the *provider*** of a
  high-risk AI system placed on the Union market, who must report any serious
  incident to the market surveillance authorities of the Member States where the
  incident occurred. "Operator" is a different and far broader class: Article 3(8)
  defines it as "a provider, product manufacturer, deployer, authorised
  representative, importer or distributor". The word *operator* does not occur
  anywhere in Article 73. A **deployer**'s own duty is **Article 26(5)** — monitor
  the system on the basis of the instructions for use, inform providers under
  Article 72, and, on identifying a serious incident, "immediately inform first
  the provider, and then the importer or distributor and the relevant market
  surveillance authorities of that incident"; Article 73 applies *mutatis
  mutandis* only where the deployer cannot reach the provider, and the duty does
  not cover sensitive operational data of law-enforcement deployers. **The three
  clocks, none of which this repository previously stated:** the general report is
  due immediately after the provider has established a causal link or the
  reasonable likelihood of one, and in any event **not later than 15 days** after
  the provider or, where applicable, the deployer becomes aware of the incident
  (**Art. 73(2)**); **not later than 10 days** where a person has died
  (**Art. 73(4)**); and **not later than two days** for a widespread infringement
  or a serious incident within Article 3(49)(b), a serious and irreversible
  disruption of the management or operation of critical infrastructure
  (**Art. 73(3)**). A **fundamental-rights infringement is Article 3(49)(c)**,
  which is not in the Article 73(3) carve-out and therefore carries **no shorter
  clock than the general 15-day period**. All three periods run from *awareness of
  the incident*, not from completion of an internal assessment. Sites were
  enumerated by `command grep -rn 'Art\. 73\|Article 73' --include='*.md' .` run
  from inside this repository, before any of the corrections below, and it
  reached more sites than the handover, which had named seven. Separate
  enumerations were run for `Art. 26(5)`, for `serious incident`, and for the
  literal clock strings `15 days` / `10 days` / `2 days`; together they found
  four further duty-or-clock sites that do not cite Article 73 by name. **Two of
  those enumerations came back empty at that moment**, which is why the
  paragraph above had to *state* the deployer's duty and the three periods
  rather than re-attribute them: no site here cited Article 26(5), and no site
  here gave any of the three periods in an EU AI Act context.
  **No figure is recorded for any of these enumerations, deliberately.** This
  entry cites Article 26(5), names all three periods and uses the words *serious
  incident*, so re-running any of those commands today measures this note as
  well as the repository, and the number moves again each time an entry is added
  to this file with no content file changing. The sites are named below instead;
  a named site is a claim about one line, which nothing written elsewhere can
  move. Corrected in-sentence, with the deadline placed in the same sentence as
  the duty it governs and never in a footnote or a nearby table:
  `domains/financial-services.md` (the sole "providers and operators" wording),
  `domains/insurance.md`,
  `domains/automotive.md`, `domains/aviation.md`, `domains/pharma.md`,
  `agent/agent-operations.md` §6 of the safety-incident response,
  `governance/knowledge-base.md` AGKB compromise step (d),
  `agent/agent-retirement.md` post-retirement serious-incident bullet, and
  `governance/observability.md` "Regulatory Response Commitments". The serious
  incident threshold was also restated at the sites that gave it: the repository
  had "one that has led to, or may have led to, harm to health, safety, or
  fundamental rights", which is not the Act's formulation and omits two limbs.
  **Article 3(49)** defines a serious incident as an incident or malfunctioning
  "that directly or indirectly leads to any of the following": (a) the death of a
  person, or serious harm to a person's health; (b) a serious and irreversible
  disruption of the management or operation of critical infrastructure; (c) the
  infringement of obligations under Union law intended to protect fundamental
  rights; (d) serious harm to property or the environment. **Nothing was deleted
  and no content requirement was invented:** Article 73 prescribes no report
  content in any of its eleven paragraphs, and the sites now say so, pointing at
  the Commission guidance mandated by Article 73(7) (due 2 August 2025) as the
  forthcoming source. **54 byte-comparisons** were run through the checker's own
  `normalizeForMatch` against the hashed primary, **0 unexpected**; every positive
  control has a prefix-safe negative twin, with numerals swapped only within the
  same digit width (`15`→`17`, `10`→`12`, never `15`→`1`) and words chosen so that
  neither string is a prefix of the other (`investigations`→`inspections`,
  `irreversible`→`irreparable`, `protect`→`safeguard`, `two`→`five`,
  `reach`→`contact`, `monitor`→`supervise`, `develop`→`publish`,
  `distributor`→`contractor`). The two clock inversions found in the
  `agentic-engineering-manifesto` pass were run here as negative controls and both
  MISS the primary: death on a two-day clock, and a 10-day fundamental-rights
  clock. **Nothing in this entry is signed.** Each reading is
  `[PREPARED AT PRIMARY, UNSIGNED]`.

- **D-57: a "Regulatory Response Commitments" row contradicted the row above it
  about when the EU AI Act clock starts.** In `governance/observability.md`, one
  row set a policy-set 24-hour assessment window "chosen to sit inside the
  regulatory reporting deadline", while the row immediately below it defined that
  regulatory deadline as running "from assessment completion". A deadline that
  starts when the assessment ends cannot be a deadline the assessment sits inside;
  the two rows could not both be true. The Act settles it: Article 73(2), (3) and
  (4) each run from the date the provider or, where applicable, the deployer
  *becomes aware* of the serious incident. The notification row now states the
  duty-holder, the addressee and all three periods, and says explicitly that they
  run from awareness rather than from completion of the assessment above.

- **D-57: Article 72 post-market monitoring was attributed to "operators".** In
  `agent/agent-retirement.md`, post-retirement obligations were introduced with
  "The EU AI Act requires operators of high-risk AI systems to maintain a
  post-market surveillance system". Article 72 is headed "Post-market monitoring
  by providers and post-market monitoring plan for high-risk AI systems" and
  Article 72(1) reads "Providers shall establish and document a post-market
  monitoring system"; both were byte-compared, each against a negative control
  swapping the duty-holder, which missed. Corrected to *providers*, and to
  *monitoring* rather than *surveillance* — Article 74 is where market
  *surveillance* sits, and it is a duty on authorities, not on the organisation.

- **D-57 — handed forward, not adjudicated here.** Two further "operators"
  attributions were found by the same enumeration and are outside the Article 73
  incident-duty chain this pass covered, so they are recorded rather than changed:
  `agent/agent-annex-iv-mapping.md:11` says Annex IV technical documentation must
  be maintained by "providers and operators", where Article 11(1) is drafted in
  the passive and allocates the duty elsewhere; and
  `agent/agent-regulatory-classification.md:86` says "Title VIII of the EU AI Act
  governs providers and operators of general-purpose AI models", where the
  instrument has no Title VIII — general-purpose AI models are Chapter V. Neither
  was settled at the primary in this pass.
- **Remaining annex attributions closed in this repository.** The
  2026-09-06 entry above closed the annex citations named in the routing brief;
  a re-derivation of the same class from the checker's own refusal list -- run
  over the full list rather than over a four-instrument filter of it -- found
  **three further citations at two sites here**, both of them invisible to the
  earlier enumeration. `agent/agent-regulatory-classification.md:239` filed two
  EU AI Act annex citations under the GDPR, which has no annexes, because the
  GDPR is named earlier in the same very long line;
  `agent/agent-regulatory-classification.md:276` filed one under DORA, which has
  none either, by carry-forward from the line above. Both fixed by **pure
  insertion of the instrument name**; `domains/pharma.md:50` fixed the same way.
  No citation was deleted, re-worded or renumbered, and every edited file has
  exactly the line count it had before.
  · **Named rather than fixed:** `domains/financial-services.md:129-130` splits
  an annex citation across a line break, which hides it from the extractor
  altogether rather than mis-filing it. The line carries the pinned side-A text
  of a live ground-truth fixture, and re-wrapping it would break that pin, so it
  is recorded here instead. Fifteen further annex citations elsewhere in this
  repository are split the same way and are likewise hidden rather than
  mis-attributed; they are a separate defect from the one this entry closes.
  · This file is untracked in git, so `git grep` does not see it; the
  enumerations above ran over `git ls-files` **plus**
  `git ls-files --others --exclude-standard`, which does.
- **Annex citations hidden by a line break, closed.** Sixteen annex-and-numeral
  citations across this corpus are split across a line break — the word on one
  line, its numeral on the next. The 2026-09-06 entry above records the class
  and leaves it unfixed. Unlike a mis-filed citation, these produce **no
  citation record at all**, so no check in this corpus has ever seen them and
  none was ever verified; that is a different defect from mis-attribution, not
  a smaller one. **Thirteen are in this repository**: `domains/automotive.md`
  at 83-84, `domains/aviation.md` at 42-43, 151-152 and 172-173,
  `domains/financial-services.md` at 69-70 and 129-130, `domains/insurance.md`
  at 31-32, `domains/pharma.md` at 86-87 and 156-157, and four in this file at
  821-822, 928-929, 943-944 and 977-978. Each was closed by moving **one word**
  across the break. Nothing was added, removed, re-worded or renumbered; every
  file has the line count it had before; and the text is byte-identical under
  the checker's own normalisation once blockquote and list markers are stripped
  — asserted in the writing script, which refuses to write otherwise.
  · **The pinned-fixture site was re-measured rather than inherited.**
  `domains/financial-services.md:129-130` carries the pinned side-A text of a
  live ground-truth fixture, and the entry above records it as unfixable for
  that reason. The fixture is matched by a **normalised three-line sliding
  window**, not by a fixed line, so moving one word to the next line leaves the
  pinned words contiguous inside that window; measured before and after, the
  fixture re-anchors to **the same line** it did before and the row's state is
  unchanged. No fixture or adjudication table was edited.
  · **What was gained.** The nine `domains/` sites now yield nine citation
  records, every one attributed to the instrument its own sentence names. The
  four sites in this file gain nothing and are re-wrapped for the record's own
  consistency only: this file is **untracked in git**, so the extractor never
  opens it — which is also why the enumerations ran over `git ls-files`
  **plus** `git ls-files --others --exclude-standard`, and why `git grep` is
  not evidence here.
  · **No site was left.** Every one of the sixteen was opened and read before
  anything moved; each is a citation of the instrument the surrounding sentence
  names, so none of the four "leave it alone because it is right" cases the
  previous pass found recurs in this class. A re-scan of the same 210 files
  returns **zero** remaining, against 662 same-line occurrences unchanged
  before and after.
- **A corpus claim in this file was measuring this file: bare absence-and-count
  claims about this repository, corrected without substituting a new number.**
  The class is a claim about *this corpus* that its own file falsifies — a note
  recording that something is absent, or that it appears at so many lines,
  published into a file that is itself inside the search space, so that the
  sentence moves the number it reports. It is distinct from a claim about the
  text of an external instrument: a note here quoting a phrase cannot change how
  often that phrase appears in the instrument, and every claim of that second
  kind in this file was left exactly as it stood. Four sites here were of the
  corpus-scoped kind and all four are corrected. The sharpest is the Article 73
  enumeration paragraph above, which recorded an empty result for the deployer's
  own provision inside a paragraph that cites that provision twice *before*
  reaching the claim — so the figure was already wrong at the moment it was
  written, which is a different and worse fault than one that drifted afterwards.
  The other two had drifted: the Annex III string-enumeration aside, whose line
  total this file now supplies a large share of, and the CE-marking sentence,
  which said there were only two mentions in the repository while this file had
  come to carry several more. The fourth was true in one sense and false in
  another, and both are now recorded in place: the sentence saying that no site
  here used the word *Title* correctly for another instrument holds of citation
  sites, which is what the entry is about, but not of every line, because this
  file itself reports the Act's recitals cross-referring to two Treaty Titles —
  and it reported them at a line above the claim, so the literal reading was
  false before the claim was written. It is now scoped to citation sites.
  · **The substance was corrected too, not only the number, at the first site.**
  Its point was that a duty had to be *stated* rather than re-attributed, and
  that point rested on a zero. It now rests on the named sites instead, which is
  the stronger half of the original argument and the half that survives
  re-measurement.
  · **The form of the correction is the same at every site, and it is not a
  smaller number.** A figure written "excluding this note" goes stale at the next
  entry with no word changing, which is the same trap one order out. Each
  sentence now makes a claim about named lines — what is at them, and what is
  attributed there — which nothing written elsewhere can move. Where a figure was
  dropped the sentence says why, so a reader does not read the absence as an
  oversight rather than as a choice.
  · **Controls.** A fresh two-word negative control was chosen only after
  confirming it was absent from every Markdown and HTML file in the corpus, and
  was then run with the identical command and file set as a positive control that
  hit a large share of them. Its result is deliberately not written here as a
  figure, and the string itself is not reproduced: recording a control in a
  published file is what burns it, and earlier controls in this corpus are
  already unusable for exactly that reason, some of them recorded in this file.
  That is the same effect this entry describes, one level up. **The cost of this
  form is real and is stated rather than hidden: a reader cannot re-run a control
  they cannot see.** The positive control carries the weight instead — it is
  supposed to be present, so publishing it cannot burn it, and a run in which it
  fails to hit is a broken search rather than a demonstrated absence.
  · This file is untracked under `D-57`, so `git -C aplc diff` does not show
  this entry. It was written anyway, and this line says so.


## 2026-09-05

- **D-65 / D-61: Annex III §5(b) was cited for insurance pricing, insurance
  claims, fraud detection, AML and fleet/warranty decisions. It reaches none
  of them, and every site is corrected in its own sentence.** Read at the
  hashed primary (`inputs/20260902-arnaud/sources/OJ_L_202401689_AIAct.html.gz`,
  sha256 `a0f437e8…c7929b`), Annex III point 5(b) is "AI systems intended to
  be used to evaluate the creditworthiness of natural persons or establish
  their credit score, **with the exception of AI systems used for the purpose
  of detecting financial fraud**". Insurance risk assessment and pricing is a
  different point, §5(c), whose text is limited to "risk assessment and
  pricing in relation to natural persons in the case of life and health
  insurance". "Access to and enjoyment of essential private services and
  essential public services and benefits" is the **heading** of point 5, not
  operative text in either sub-point, and several sites had been treating it
  as a criterion. `§5(b)` was enumerated across this repository by
  `grep -rn '§5(b)' aplc/` — 14 occurrences, 12 of them in body files
  (`domains/insurance.md` 5, `domains/financial-services.md` 6,
  `domains/automotive.md` 1) and 2 in this errata file; the sweep that handed
  the defect over had named 2 classified sites and 2 unclassified. Corrected:
  `domains/insurance.md` underwriting advisory (§5(b) → §5(c), and non-life
  personal lines marked as reached by neither point), claims processing
  (classification under §5(b) withdrawn — §5(a) is public authorities, §5(b)
  is creditworthiness, §5(c) is life-and-health pricing, and claims settlement
  is none of the three), fraud detection (the §5(b) analysis is an inversion
  of that point's own exception and is withdrawn), pricing optimization (the
  negative classification was pinned to the wrong point; it now names §5(c)
  and §5(b) and says on the face of the instrument neither covers non-life
  commercial or fleet pricing); `domains/financial-services.md` credit
  decisioning, customer advisory, fraud detection and trading/AML on the same
  four grounds; `domains/automotive.md` fleet management and warranty claim
  agents. **Where neither point covers a case, that is what the file now says.**
  No replacement high-risk classification is asserted anywhere a withdrawal
  was made, because none has been signed off, and no claim was deleted
  silently. Byte-comparisons and one-word-swap negative controls:
  `python3 inputs/20260905-arnaud/prep/d65-fix/bytecheck.py` — 20 probes, 20
  controls, 0 needing review; every MISS's control hits.

- **F2: the Art. 43(2) conformity-path contradiction in `domains/aviation.md`
  and `domains/automotive.md` is now marked inside the asserting sentences,
  not only in the blockquote below them.** The judgment recorded in the
  2026-09-05 entry below stands unchanged — an undefined gate was judged worse
  than a marked contradiction, so nothing is cut and no replacement route is
  asserted. What changed is only where the caveat sits: a blockquote is
  stripped the moment the paragraph is extracted, and the paragraph then reads
  as a flat requirement. Each asserting sentence in both files now carries, in
  the same sentence, that this document's Annex VII reading contradicts
  Art. 43(2) — under which providers of the high-risk systems "referred to in
  points 2 to 8 of Annex III" follow the internal-control procedure of
  Annex VI, "which does not provide for the involvement of a notified body" — that
  it has not been verified and must not be relied on until reconciled, and
  that the notified-body gate condition is retained rather than removed for
  the reason the flag gives. Both blockquote flags are kept in place.

- **`domains/pharma.md`: the dangling anaphor left by the GDPR Article 22
  withdrawal has been given a referent, without restoring the withdrawn
  claim.** The withdrawal deleted the sentence that stated the GDPR
  restriction, leaving the next sentence opening "This governance applies
  to…" with no antecedent. That sentence now names its own referent — the
  Stage 1 classification, human-review-path and permission-model requirements
  set out in the paragraphs below — and states expressly that it is not any
  GDPR Article 22 or Article 9 restriction, which this file no longer states.
  The withdrawn prohibition is not restored and no qualified form of it is
  asserted; that remains unsigned.

- **Every calibration default in this repository now carries its register in
  the same sentence as the number.** Three registers are used: *measured*
  (with the measurement named), *policy-set* (a chosen default, said so), and
  *illustrative* (a worked hypothetical). Where neither a measurement nor an
  authorial choice could be established, the figure is marked *origin not
  established* rather than assigned a register on a guess — the FTE estimates
  in `aplc-guide.md` are marked that way, since no staffing study stands
  behind them. **No figure was changed and none was deleted.** The 20%
  initiative-acceptance re-gate threshold, the Tier-0 eligibility bright
  lines, the four substrate-depth and constraint-legibility thresholds and
  their cadences, the evidence-tier corroboration counts and age cut-offs,
  the governance-capacity ratio bands, the waiver duration ceilings, the
  four-layer evaluation coverage bars, the probabilistic assurance defaults,
  and every SLA, SLO and anomaly-detection table are now marked in place.
  Regulatory figures — the EU AI Act retention periods, the DORA reporting
  windows, GDPR's response period — are left as they are, because their
  origin is the instrument and is already named. The caveat is deliberately
  in-sentence rather than in a footnote: a footnoted qualifier is stripped
  the first time a figure is lifted into a slide, and a sentence is harder to
  strip than a footnote (`D-42`, `D-43`).
- **The three-month gate rubber-stamping window is marked as unsupported in a
  stronger sense than the rest, in its own sentence.** It sits in
  `governance/observability.md`, not in `agent/agent-human-oversight.md`. No
  safety-critical field has a validated, non-disruptive method for
  distinguishing functional oversight from rubber-stamping in live operations
  (`D-15`), so the window is an author default standing in for a
  discrimination the field has not solved. The HITL governance capture
  detection thresholds in `agent/agent-operations.md` carry the same
  qualification.
- **Three internal divergences are named where they occur rather than
  reconciled.** The knowledge-staleness threshold for high-change-rate
  domains (30 days in `governance/observability.md` and
  `agent/agent-maintenance.md`, 90 days in `governance/queries.md`), and the
  HITL override-rate specification-review trigger (10% over 30 days in
  `agent/agent-behavioral-specification.md`, 15% over three weeks in
  `agent/agent-operations.md`). None is measured, so none can be preferred on
  evidence; the divergence is recorded in the text rather than resolved by
  picking one.

- **Oversight-transition criteria demoted from evidence to precondition, and
  an engagement test added.** `agent/agent-human-oversight.md`'s Oversight
  Pattern Transition Protocol certified a move to less restrictive oversight
  on 90 days without specification violations plus an override rate below
  threshold. Both are instances of a refuted inference: a clean record and a
  low override rate are exactly what a fully disengaged reviewer produces, and
  the override rate is a composite of the agent's error rate and the
  reviewer's disengagement that declines identically under both. Criteria 1
  and 2 are now labelled preconditions that license testing, the 90 days is
  marked an uncalibrated author default, and a fifth criterion adds the
  **proposed and unvalidated** Engagement Falsification Protocol (double-blind
  synthetic fault injection, blinded to reviewers and their supervisors, every
  injected item intercepted and discarded, outcomes registered as supported
  within scope / contradicted / inconclusive). Its limits are in the text: it
  does not reach in-envelope HOLL execution, excludes irreversible and
  person-affecting actions, and cannot be powered on a low-volume queue.
  Where it cannot be run, the gate record must state that the transition rests
  on envelope design, post-hoc audit and an author default against an open
  problem in human factors. **This document authorises no live fault
  injection.**
- **No numeric pass criterion is asserted for the protocol.** The research
  synthesis behind it carries one only as an embedded figure image with no
  text equivalent; the criterion is stated structurally instead and no numeral
  is quoted.
- **HITL capture detection demoted, and the added-reviewer response
  corrected.** `agent/agent-operations.md`'s capture thresholds are now stated
  to be adequate to fire the condition and inadequate to clear it. The
  response previously escalated to "add at least one external reviewer" for a
  persistent capture pattern; that directly contradicted the agentic
  engineering manifesto's `adoption-metrics.md` ("Do not add more reviewers.
  Reduce autonomy scope ... The problem is volume, not capacity") for the same
  trigger, and the evidence settles against this repository: two-person crews
  have been reported making omission and commission errors at rates
  statistically indistinguishable from solo operators with highly reliable
  decision aids. The response now reduces scope first and does not add
  reviewers to the same queue at the same volume. **Independent review is not
  withdrawn**: blind post-hoc adjudication by reviewers outside the live loop,
  working from different evidence with their own authority, is a different
  intervention and is retained as the final step, strengthened to require
  blinding to the original decision and to the agent's confidence signalling.
- **Solvency II Article 127 escalation citation withdrawn.**
  `domains/insurance.md` named a Solvency II provision as imposing an
  immediate supervisory-notification duty on the undertaking, tied to a
  defined notifiable-event term and a named determination made under it.
  Article 127 is *Implementing measures* — it is addressed to the European
  Commission and imposes no duty on any undertaking. The citation was cut.
  Which provision actually creates an undertaking's notification duty on
  this point has not been signed off, and no replacement citation is
  asserted.
- **Annex III §5(b) over-scoping withdrawn.** The same file classified
  personal-lines insurance pricing agents generally as EU AI Act Annex III
  high-risk under the §5(b) access-to-essential-services point. The
  Annex III point that reaches insurance risk assessment and pricing carries a
  life-and-health-only limitation that the withdrawn sentence dropped.
  Whether and how that limitation bears on non-life personal-lines pricing
  (motor, home, travel) has not been signed off, so no replacement
  classification is asserted.
- **Bare GDPR Article 22 citation withdrawn.** `domains/pharma.md` cited
  GDPR Article 22 for a restriction on solely automated decisions based on
  special category data, stated as an unqualified prohibition. The
  restriction is conditional, not absolute — it carries consent and
  Member-State-law gateways that the withdrawn line omitted entirely. The
  citation was cut; the correct qualified form has not been signed off and
  is not asserted here.
- **Art. 43(2) / Annex VII conformity-path contradiction flagged, not
  fixed.** `domains/aviation.md` and `domains/automotive.md` each state that
  the conformity assessment path for their Annex III §2 category is
  Annex VII (third-party assessment, notified body review). EU AI Act Art. 43(2)
  states that for the high-risk systems referred to in points 2 to 8 of
  Annex III — which includes point 2 — providers follow the conformity
  assessment procedure based on internal control (Annex VI), with no
  notified-body involvement. The two statements contradict each other for
  the same point. Both files carry a dated flag recording this; the
  conformity-assessment path and the notified-body gate condition in both
  files are **not verified and must not be relied on** until reconciled.
  This is load-bearing on a release gate, so nothing was cut or rewritten
  and no replacement route is asserted — an undefined gate was judged worse
  than a marked contradiction. `aviation.md`'s flag also covers a related,
  separate defect in the same file's AI System Classification section,
  which quotes Annex III point 2's enumeration with a word not in the
  instrument's list and extends it by reasoning not in the instrument; that
  is flagged by reference, not re-quoted, and also not fixed.
- **Malformed OJ reference corrected in the exemplar.**
  `governance/knowledge-base.md` gave, as the `e.g.` exemplar of a correct
  regulatory-source registry entry, `"European Parliament and Council,
  Regulation (EU) 2024/1689 (EU AI Act), OJ L 2024/1689"`. Three faults
  against the primary: the comma after `L` was dropped, which is the
  pre-2023 issue-number style rather than the post-2023 form; the
  publication date was omitted; and the title read "European Parliament and
  Council" where the Regulation reads "of the European Parliament and of
  the Council". Corrected to `"Regulation (EU) 2024/1689 of the European
  Parliament and of the Council (EU AI Act), OJ L, 2024/1689, 12.7.2024"`.
  Both the corrected title form and the corrected OJ form occur verbatim in
  the hashed primary; neither of the two superseded forms occurs in it at
  all. The exemplar is load-bearing because a reader copies it. One
  occurrence in this repo; `grep -rn "OJ L" aplc asdlc` returns this line
  and no other. D-62 family: right instrument, wrong reference form.
- **D-62 / RD-2: `agent/agent-regulatory-classification.md` asserted the
  Article 43 conformity route backwards, and this file is the authority the
  rest of the repository classifies from.** Its "Mandatory third-party
  assessment (Annex VII) triggers" list named *Critical infrastructure
  (Annex III, Point 2)* as a trigger. Read at the hashed primary
  (`inputs/20260902-arnaud/sources/OJ_L_202401689_AIAct.html.gz`, sha256
  prefix `a0f437e89667`), Article 43(2) says the opposite: "for high-risk AI
  systems referred to in points 2 to 8 of Annex III, providers shall follow
  the conformity assessment procedure based on internal control as referred to
  in Annex VI, which does not provide for the involvement of a notified body."
  Annex III §2 is point 2 and sits inside points 2–8. `domains/automotive.md`,
  `domains/aviation.md` and `domains/pharma.md` all had it right; the
  classification file had it backwards, and it is upstream of the Stage 4
  release gate. Corrected in the asserting sentences, which now quote
  Article 43(2) and record that the previous statement was the inverse.
- **Same paragraph, second fault, which no other site contradicted: Annex III
  point 1 was said to have "no self-assessment path".** Article 43(1) at the
  same primary: for point 1 systems where the provider has applied harmonised
  standards under Article 40 or common specifications under Article 41, "the
  provider shall opt for one of the following conformity assessment procedures
  based on: (a) the internal control referred to in Annex VI; or (b) the
  assessment of the quality management system and the assessment of the
  technical documentation, with the involvement of a notified body, referred
  to in Annex VII." The choice exists. Annex VII becomes obligatory for point 1
  only under the second subparagraph of Article 43(1) — standards absent, not
  applied, only partly applied, or published with a restriction. Corrected,
  and Article 43(3) (Annex I Section A products) added, having been absent.
  Because no corpus site disagreed, the citation-consistency check was
  structurally blind to this; it was found by reading the paragraph.
- **F2: the fourth "mandatory third-party trigger" — organisational conflict
  of interest — is unsourced and now says so in its own sentence.** No
  provision of the AI Act converts an Annex VI route into an Annex VII one
  because the assessing team lacks independence. The competence and
  independence requirement is retained as a governance requirement of this
  framework, marked as such, rather than deleted or left attributed to the Act.
- **The same inverted rule was carried by three further sites and all three
  are corrected**: `agent/agent-release-governance.md` (the Stage 4 evidence
  bullet and the "Third-Party Assessment — Annex VII" section, both of which
  named critical-infrastructure AI safety components as requiring a notified
  body) and `agent/agent-conception.md` (Step 4, which additionally treated
  law-enforcement deployment as an Annex VII trigger; Article 43(1) provides
  only that for a point 1 system put into service by law enforcement,
  immigration or asylum authorities or by Union institutions, the market
  surveillance authority acts as the notified body). No gate condition was
  removed: the notified-body certificate remains a Stage 4 gate condition
  wherever the Annex VII route actually applies. Conformity-route sites were
  enumerated by
  `grep -rniE '(annex (vi|vii)([^i]|$)|notified body|third-party (conformity )?assessment|self-assessment|internal control)' --include='*.md' aplc/`
  — 55 lines across 10 files before these corrections, of which 9 stated the
  route wrongly: `agent/agent-regulatory-classification.md` :109, :121, :122,
  :124 and :126(a); `agent/agent-release-governance.md` :106 and :375; and
  `agent/agent-conception.md` :212 and :214. All 9 are corrected. The same
  command run after the corrections returns 70 lines across the same 10
  files — the count rose because the corrections quote Article 43; it is a
  measure of prose, not of defects, and must not be compared with the 55 as
  though it were.
- **The 2026-09-05 disclosed residual in `domains/aviation.md` and
  `domains/automotive.md` is preserved unchanged.** Neither file was touched.
  The judgment recorded above — that an undefined release gate was worse than
  a marked contradiction — stands. The distinction drawn here is that those
  two files *disclose* a contradiction in dated flags, whereas
  `agent-regulatory-classification.md` *asserted the inverse as the operative
  rule*; the corrected files now point at the flags rather than repeating the
  claim.
- **D-62: `domains/insurance.md` attributed model validation to Solvency II
  Article 120 and invented an annual cadence.** Read at the hashed primary
  (sha256 prefix `1e6a28843ac3`), Article 120 is *Use test* — whether the
  internal model "is widely used in and plays an important role in their
  system of governance". Validation is **Article 124**, *Validation
  standards*, which requires that undertakings "shall have a regular cycle of
  model validation which includes monitoring the performance of the internal
  model, reviewing the ongoing appropriateness of its specification, and
  testing its results against experience". The Directive fixes no period.
  Both faults are corrected in the asserting sentences: the article is
  re-attributed to 124, and the annual cadence is marked unsourced (`F2`)
  rather than deleted, since a firm may hold itself to it as internal policy.
  The same fabricated cadence appeared unattributed at `domains/insurance.md`
  Ongoing Monitoring and at `domains/financial-services.md` Solvency II; both
  are marked in-sentence on the same basis. `asdlc/domains/insurance.md`
  carries the identical Article 120 error and is outside this repository —
  recorded here so the two stay consistent, not corrected here. The pair
  agreed with each other and was therefore invisible to a disagreement check.
- **D-62: `agent/agent-conception.md` softened AI Act Article 50(1) into an
  on-request duty.** The file read "EU AI Act Article 50 requires that AI
  systems interacting with humans disclose their AI nature on request", and
  then offered "Only when asked, or proactively?" as an open design choice.
  Article 50(1) at the primary is a by-design duty: "Providers shall ensure
  that AI systems intended to interact directly with natural persons are
  designed and developed in such a way that the natural persons concerned are
  informed that they are interacting with an AI system, unless this is obvious
  from the point of view of a natural person who is reasonably well informed,
  observant and circumspect, taking into account the circumstances and the
  context of use." The phrase "on request" does not occur in Article 50. The
  sentence now quotes 50(1) in full, records that obviousness is the only
  relief, notes the criminal-offence carve-out in the same paragraph, and the
  design question is reframed so that it no longer presents a settled point as
  open. A duty stated more weakly than the instrument states it is worse than
  one omitted, because the text reads as compliant.
- **Controls for all of the above.** Every quotation was byte-compared against
  the hashed primaries through the checker's own `normalizeForMatch`
  (`node tools/citation-consistency.mjs` normalisation, reused via
  `inputs/20260905-arnaud/prep/q9-pairs/probe.mjs`): 16 probes — 11
  quotations, each HIT with its one-word-swap negative control MISSing, and 5
  load-bearing absence claims ("on request" in Article 50; Annex VII for
  points 2–8; "no self-assessment path"; annual validation; Article 120 as the
  validation provision), each a MISS with its negative control also MISSing
  and each paired with a positive control HITting in the same article to prove
  the search reached the text. AI Act `a0f437e89667`, Solvency II
  `1e6a28843ac3`.
- **D-62: GDPR Article 12(3)'s response period was stated in the wrong unit at
  `agent/agent-maintenance.md`, and unsourced in the same unit at
  `governance/observability.md`.** Read at the hashed primary (sha256 prefix
  `9952f3f336d4`), Article 12(3) requires the controller to provide information
  on action taken "without undue delay and in any event within one month of
  receipt of the request", and "that period may be extended by two further
  months where necessary, taking into account the complexity and number of the
  requests". `agent-maintenance.md` gave "30 calendar days" with a "60-day
  extension"; neither figure occurs in the Regulation. **A month is not 30
  days**, and a maintenance document is precisely where a reader converts a
  stated number into a schedule, so the correction restores the Regulation's
  own unit rather than converting it, and says in the same sentence that the
  day-counts are unsourced (`F2`). GDPR response-period sites were enumerated
  by
  `grep -rniE '(30|60|thirty|sixty)[ -]?(calendar |business |working )?day|one month|two further months|Art(icle)?\.? ?12\(3\)' --include='*.md' aplc/`
  — 45 lines across 15 files (run after these corrections; the two corrected
  sites are among them), of which exactly 2 stated a GDPR response period:
  `agent/agent-maintenance.md:358` (the site handed over) and
  `governance/observability.md:283`, a Regulatory Response Commitments table
  row reading "Complete erasure within 30 calendar days" under a header
  declaring rows "sourced from the named instrument except where marked
  policy-set" and carrying no such mark — the same wrong unit, presented as
  sourced. Both corrected. Every other match is a policy-set APLC interval
  with no regulatory attribution. Byte-compared with controls: three Article
  12(3) clauses HIT with one-word-swap negative controls MISSing; "30 calendar
  days", "60-day extension" and "thirty days" each MISS in the Regulation,
  their negative controls also MISSing, with the three HITs above serving as
  the positive controls proving the search reaches Article 12.
- **`domains/insurance.md` Article 124 correction pinned to the primary's own
  identifiers, and no prose/table split found.** Following the parallel
  correction in `asdlc`, both insurance sites now carry the three strings a
  primary-based correction converges on regardless of prose — Article 124,
  *Validation standards*, and "a regular cycle of model validation" — plus the
  clause the Directive actually enumerates, "which includes monitoring the
  performance of the internal model, reviewing the ongoing appropriateness of
  its specification, and testing its results against experience". Article 120
  is named as *Use test* where it is cited. `asdlc/domains/insurance.md`
  carries the same defect in a Layer 4 table row as well as in prose;
  `aplc/domains/insurance.md` has no table row citing Solvency II validation —
  `grep -n '^|' aplc/domains/insurance.md | grep -i 'solvency\|validat'`
  returns nothing — so the prose/table pairing does not exist here. Measured
  across the full 1,117-character span of Article 124 at the primary,
  "annual", "year", "yearly", "frequency", "independen", "board" and
  "backtest" each occur zero times and "regular cycle" once; the board-report
  requirement this file states is accordingly marked as a requirement of this
  framework rather than of Article 124.
- **Handed back to the tool owner, not corrected here: the checker's article
  structure data omits AI Act Article 43(3), (4) and (5).**
  `tools/regulatory-article-structure.json` records paragraphs `1`, `2` and
  `6` for `EU_AI_ACT` Article 43, so `node tools/citation-consistency.mjs`
  now reports the newly added, correct citations of Article 43(3) and
  Article 43(4) as `FABRICATED — Art. 43 has no paragraph (3)/(4)`. Both
  paragraphs are present verbatim in the hashed primary: 43(3) opens "For
  high-risk AI systems covered by the Union harmonisation legislation listed
  in Section A of Annex I, the provider shall follow the relevant conformity
  assessment procedure as required under those legal acts", and 43(4) opens
  "High-risk AI systems that have already been subject to a conformity
  assessment procedure shall undergo a new conformity assessment procedure in
  the event of a substantial modification"; each was byte-compared with a
  one-word-swap negative control that missed. The three flags are a gap in
  the tool's reference data, not defects in this repository, and the citations
  are left as the instrument reads. `tools/` is outside this repository's
  write scope and was not modified.

- **D-57: stale 2021-proposal law presented as the adopted Regulation —
  Article 5(1)(c) and Article 61.** Two provisions in this repository were
  carried over from the Commission's 2021 proposal, not the adopted
  Regulation (EU) 2024/1689.
  (i) `agent/agent-regulatory-classification.md` restricted the Article 5(1)(c)
  social-scoring prohibition to "AI systems used by public authorities or on
  their behalf" and concluded that "a private enterprise agent product that
  performs behavioral scoring for internal purposes is not automatically
  covered". Article 5(1)(c) as adopted names no actor: it prohibits "the
  placing on the market, the putting into service or the use of AI systems for
  the evaluation or classification of natural persons or groups of persons over
  a certain period of time based on their social behaviour or known, inferred
  or predicted personal or personality characteristics, with the social score
  leading to" either of the two limbs at (c)(i) and (c)(ii). The
  public-authority qualifier was in the 2021 proposal and was removed. The
  conclusion drawn for private enterprises was therefore not a narrowing of a
  real limb but the inversion of a duty that binds them. Corrected, with both
  limbs quoted at primary; the same gloss at `agent/agent-conception.md` Step 1
  ("social scoring by public authorities") was corrected with it. Control on
  the normalised primary: "for the evaluation or classification of natural
  persons" → 1; " by public authorities " → 3, none in Article 5; nonsense
  needle → 0.
  (ii) `agent/agent-release-governance.md` required the post-market
  surveillance plan to be "compliant with EU AI Act Article 61" at two sites.
  Article 61 of the adopted Act is "Informed consent to participate in testing
  in real world conditions outside AI regulatory sandboxes"; post-market
  monitoring is Article 72, cited correctly elsewhere in this repository. This
  was post-market monitoring in the 2021 proposal only. **This defect is worse
  than an uncited assertion: the citation is well-formed, so every
  locator-keyed check in this estate passes it.** Corrected to Article 72, and
  the artifact renamed to the Act's own term, "post-market monitoring plan"
  (Article 72(3)).
  A sweep of every `Article N` / `Art. N` token in this repository against the
  113 article titles of the adopted Act found **no further AI Act stale-draft
  survivals** beyond these two. `Article 48` at
  `agent/agent-regulatory-classification.md` is Solvency II, not the AI Act,
  and is left as written; its article number has not been checked at a primary
  and is flagged here, not corrected.

- **D-57: "the EU AI Office database" — a body that does not hold it, a duty
  that does not apply universally, and a document that is not filed in it.
  Ten sites.** `agent/agent-regulatory-classification.md` (2),
  `agent/agent-release-governance.md` (3), `agent/agent-retirement.md`,
  `aplc-guide.md`, `domains/financial-services.md`, `domains/insurance.md`,
  `domains/pharma.md`. Three faults:
  (i) **Owner.** "eu ai office database" occurs **0** times in the normalised
  primary, against " ai office " at **97** and " eu database " at **34**;
  nonsense needle **0**. Article 71 titles the register "EU database for
  high-risk AI systems listed in Annex III"; Article 71(1) provides that "the
  Commission shall, in collaboration with the Member States, set up and
  maintain" it, and Article 71(6) makes the Commission its controller. The AI
  Office does not hold it.
  (ii) **Scope.** A flat "must be registered" is wrong for critical
  infrastructure. Article 49(1) applies "with the exception of high-risk AI
  systems referred to in point 2 of Annex III". Each of the ten sites now
  carries that exception in the sentence making the claim.
  (iii) **Destination of the EU declaration of conformity.** Three sites
  (`agent/agent-release-governance.md` ×2, `agent/agent-regulatory-classification.md`)
  said the EU DoC is "registered in" or "filed with" that database. Article
  47(1) requires the provider to "draw up a written machine readable, physical
  or electronically signed EU declaration of conformity for each high-risk AI
  system, and keep it at the disposal of the national competent authorities for
  10 years after the high-risk AI system has been placed on the market or put
  into service". Kept, not filed. Article 49 registers the provider and the
  system, never the declaration.
  Enumeration was wrap-safe, run with `command grep` from inside `aplc/` —
  `command grep -rlEz --include='*.md' '(EU[[:space:]]+)?AI[[:space:]]+Office[[:space:]]+database' .`
  → 7 files, 10 occurrences as the sweep found them, 05.09.2026.

  **Corrected 06.09.2026 (`D-72`), and the correction is the point rather than
  the wording.** This bullet previously spelled its nonsense negative-control
  needle and asserted in the same breath that a search of this tree for it came
  back empty; it then asserted that the enumerating command came back empty
  after the edits. **This file falsifies both.** Spelling the needle placed it
  inside the tree the search covers, and the correction prose above quotes the
  enumerated phrase itself — so what breaks the post-edit zero is **this entry's
  own `D-57` heading**, named here rather than counted, because a count would go
  stale at the next rebuild of the built twin without a word of this sentence
  moving. ***Withdrawing a number is not enough while the quotation survives to
  be counted again.*** The needle is accordingly described and not respelled,
  and it is retired for every later pass. **The weight moves to the positive
  control, which this entry cannot burn because that string is supposed to be
  present: the 7-file, 10-occurrence result above.** The cost is stated rather
  than talked down — a reader cannot re-run a control they cannot see, so the
  negative half is now this note's word and not something reproducible on the
  page. Re-derived with `command grep -rlEz --include='*.md'` run from inside
  `aplc/`, branch `main` at `821e242`, 06.09.2026.

- **D-57: `agent/agent-release-governance.md` asserted a post-market report and
  a schedule the Act does not create.** The file required that "reports must be
  provided to the EU AI Office on the schedule required under the Act". Article
  72 obliges the provider to "establish and document a post-market monitoring
  system" and makes the plan "part of the technical documentation referred to
  in Annex IV". **It creates no report to any body and no schedule.** The text
  now says so, and re-attributes: Annex IV documentation is kept at the
  disposal of the national competent authorities for 10 years (Article 18(1))
  and produced on a competent authority's reasoned request (Article 21(1));
  serious incidents go to "the market surveillance authorities of the Member
  States where that incident occurred" (Article 73(1)) on the Article 73
  clocks; reporting to the AI Office is a general-purpose AI model duty under
  Article 55(1)(c) and does not reach the provider of a high-risk AI system in
  that capacity. The duty is bounded and re-attributed, not deleted.

- **D-57: `agent/agent-regulatory-classification.md` — an unanchored
  post-market claim whose nearest locator was the wrong article.** The
  Stage 5 paragraph asserted that post-market surveillance obligations "are
  specified by regulation", with the nearest citation 14 lines below and
  pointing at Article 5 (prohibited practices). Rewritten with Article 72(1)
  and 72(3) quoted in the sentence making the claim, Article 73(1) named for
  the separate serious-incident duty, and the monitoring frequency and periodic
  conformity review it asserted marked as this framework's own — Article 72
  sets neither.

- **D-57: DORA Article 19 was given three deadlines it does not contain.**
  `domains/insurance.md` (three sites) and `domains/financial-services.md` (one
  site, not in the sweep that opened this entry) attributed an initial
  notification "within 4 hours of classification", an intermediate report
  "within 72 hours" and a final report "within 1 month" to DORA Article 19.
  **DORA sets no clock.** Article 19(4) requires the three submissions "within
  the time limits to be laid down in accordance with Article 20, first
  paragraph, point (a), point (ii)" — the ESAs' regulatory technical standards,
  which Article 20 first paragraph (a)(ii) directs them to develop to
  "determine the time limits for the initial notification and for each report
  referred to in Article 19(4)". Controls on the normalised DORA primary,
  whole-token anchored: "4 hours" **0**, "24 hours" **0**, "72 hours" **0**,
  "hours" **1**, "one month" **1**, and the Article 19(4) deferral clause
  **1**; nonsense needle **0**. All four sites now state that the Regulation
  fixes no deadline and direct the reader to the RTS adopted under Article 20,
  first paragraph, point (a)(ii), recording which version was relied on. The
  same three figures carrying a framework label rather than a provision are
  outside this repository.

- **D-57: 21 CFR Part 820 cited as the provision that makes something a
  medical device.** `agent/agent-regulatory-classification.md` and
  `agent/agent-conception.md` each said a product "is a medical device under 21
  CFR Part 820". Part 820 is the FDA quality system regulation — what a
  manufacturer must do once it has a device — not a device-definition
  provision. Device status is the FD&C Act §201(h) definition, with
  classification at 21 CFR Part 860. Both sites restated, and aligned with the
  Agentic Engineering Manifesto's own wording at
  `agentic-engineering-manifesto/domains/medical-devices.md`, which already has
  it right: "21 CFR Part 820 (QMSR, effective February 2026, replacing the
  prior QSR)". No primary for Part 820 or the FD&C Act is on disk; this
  correction is corpus-internal consistency plus the removal of a category
  error, and is not signed at a primary.

- **Method note for the six entries above.** Every quotation introduced by them
  was byte-compared against the hashed primaries after normalising with the
  checker's own `normalizeForMatch` (lower-case, dash→space, curly→straight
  quotes, whitespace collapse, **trim**) — needles normalised first and padded
  after, since the checker trims its argument and a padded needle silently
  degrades to zero at a comma or full stop. 11 quotations, 11 matches, with a
  nonsense negative control missing. Article-number controls were whole-token
  anchored so that `Article 4` (14) does not absorb `Article 47` (19) or
  `Article 49` (19). AI Act primary:
  `inputs/20260902-arnaud/sources/OJ_L_202401689_AIAct.html.gz`, sha256 prefix
  `a0f437e89667`, matched against the decompressed text at
  `inputs/20260905-arnaud/prep/annex1-correspondence/aiact.txt`. DORA primary:
  `inputs/20260905-arnaud/prep/asdlc-standards/sources/dora_fulltext.txt`,
  sha256 prefix `25328c7e39c4`.

- **Checker flag created by the Article 71 correction, disclosed not
  adjudicated.** Before the correction above, this repository cited AI Act
  Article 71 nowhere; the only Article 71 citation in the estate was
  `agentic-engineering-manifesto/integration/igm-aplc-integration-test.md:197`.
  Citing the correct owner of the EU database therefore gives the key
  `EU_AI_ACT|Art.71` a second file and `node tools/citation-consistency.mjs`
  section 2 now flags one pair for it (jaccard 0.02). Isolated by masking:
  rewriting `Article 71` to a nonsense token throughout this repository, in a
  scratch copy, takes the flagged-pair count from 71 to 70 and back. **The two
  sides agree** — the AEM line reads "No Article 49 registration. The EU
  database under Art. 71 covers Annex III high-risk systems. Nothing is filed."
  The flag is the keyword-overlap heuristic comparing a 17-word snippet against
  a long one, not a disagreement; the alternative to producing it is to leave
  the register attributed to a body that does not hold it. No adjudication row
  was added — `tools/` is outside this repository's write scope. Section 4
  reports sub-clause fabrications 1 and section 6 reports 0 truly new
  fabricated quotations, both unchanged by these corrections; two consecutive
  runs agreed on every figure.

- **D-57: the EU declaration of conformity is still "filed" — ten sites that
  survived the entry above, because that entry swept a string and these sites
  use a verb.** The `"the EU AI Office database"` entry in this file enumerated
  the string `AI Office database` and corrected the ten sites carrying it. **The
  filing verb was never enumerated on its own**, so every site asserting that the
  EU DoC is "filed" *without naming a database* passed the sweep untouched — in
  the very repository whose errata says the declaration is filed nowhere.
  Re-derived at the hashed primary
  (`inputs/20260905-arnaud/prep/annex1-correspondence/aiact.txt`, sha256 prefix
  `ba20f0b165e1`, 582,441 normalised chars): `shall be filed` **0**, `filed with`
  **0**, `eu ai office database` **0**, nonsense needle **0**, against
  ` ai office ` **97**, `declaration of conformity` **28** and
  `at the disposal of the national competent authorities` **3**. Article 47(1):
  the provider "shall draw up a written machine readable, physical or
  electronically signed EU declaration of conformity for each high-risk AI
  system, and keep it at the disposal of the national competent authorities for
  10 years after the high-risk AI system has been placed on the market or put
  into service"; "a copy of the EU declaration of conformity shall be submitted
  to the relevant national competent authorities upon request". Article 71(1):
  "the Commission shall, in collaboration with the Member States, set up and
  maintain an EU database". Article 49(1) registers "themselves and their
  system", never the declaration.
  **Ten sites, corrected in the sentence making the assertion:** `aplc-guide.md`
  (:248, :391, :393), `agent/agent-release-governance.md` (:120, :122),
  `agent/agent-regulatory-classification.md` (:22, :132, :272),
  `agent/agent-annex-iv-mapping.md` (:28, :52). **Five of these were outside the
  sweep that opened this entry and outside the enumeration that reported five:
  they were found only by reading around each flagged site rather than the line**
  — `:122` and `:272` restate the flagged claim one and two sentences later,
  `:22`, `:132` and `:28` state it in a different grammatical person.
  **Two clusters contradicted their own file, and the distance is the defect.**
  `aplc-guide.md:244` already read "Article 47(1) — drawn up and kept at the
  disposal of the national competent authorities for 10 years, not filed
  anywhere" — **147 lines** from :391, far outside the `F2` range, so :391 read
  as the rule on its own. `agent-release-governance.md:100` and `:107` say the
  DoC "is not filed in any database" / "is not filed with any database" — **20
  and 13 lines** from :120. `agent-regulatory-classification.md:261` says "It is
  **not** filed in any database" — **11 lines** from :272. In every case the
  correct statement is now inside the claiming sentence, not upstream of it.
  Enumeration was wrap-safe and quoted:
  `command grep -rlEz --include='*.md' 'signed[[:space:]]+and[[:space:]]+filed' .`
  → 2 files before, **0** after; `'filed[[:space:]]+with[[:space:]]+the[[:space:]]+EU'`
  → **0** after; `'File[[:space:]]+the[[:space:]]+EU'` → **0** after;
  `'zorkmid[[:space:]]+wibblefrotz'` → **0** throughout. A normalised whole-file
  scan (dash→space, lower-case, whitespace collapsed) over every `.md` in this
  repository, matching `\b(file|filed|filing)\b` within a declaration-of-conformity
  context, returns only the corrected forms and one unrelated own-process use
  (`agent-annex-iv-mapping.md:21`, the composite state manifest "filed at
  deployment", an internal gate artifact, left as written).

- **D-57: DORA Article 19's three clocks, at the site inside this repository
  that the entry below missed — and a correction to that entry's own scope
  statement.** `aplc-guide.md:298` attributed to "DORA Article 19" an initial
  notification "within 4 hours of classification as major", an intermediate
  report "within 72 hours" and a final report "within one month". **DORA sets no
  clock.** Re-derived at the hashed primary
  (`inputs/20260905-arnaud/prep/asdlc-standards/sources/dora_fulltext.txt`,
  sha256 prefix `25328c7e39c4`, 303,607 normalised chars): `4 hours` **0**,
  `four hours` **0**, `72 hours` **0**, nonsense needle **0**, against
  `major ict related incident` **44**, `initial notification` **9** and the
  Article 19(4) deferral clause
  `article 20, first paragraph, point (a), point (ii)` **1**. Article 19(4)
  requires the three submissions "within the time limits to be laid down in
  accordance with Article 20, first paragraph, point (a), point (ii)" — the
  ESAs' regulatory technical standards. The site now says the Regulation fixes
  no deadline and directs the reader to the RTS, with its version recorded.
  **Correction to the entry below.** That entry closed the same defect at four
  sites and stated that "the same three figures carrying a framework label
  rather than a provision are outside this repository." **That is wrong.**
  `aplc-guide.md` is inside this repository and its heading labels **the
  provision** — "DORA Article 19" — not a framework. The scope sentence is
  withdrawn: the correct statement is that the sweep which opened that entry
  enumerated `domains/` only.

- **D-57: a seven-year retention floor attributed to SR 11-7, which sets no
  retention period.** `agent/agent-retirement.md:144`, under a heading reading
  "**Regulatory retention floor.** The applicable regulatory requirement",
  asserted "SR 11-7 model documentation for banking models: 7 years for model
  documentation". Re-derived at both guidance texts on disk:
  `inputs/20260905-arnaud/prep/D-20-primary/sources/sr1107a1.txt` (sha256 prefix
  `d8ef34391721`, 66,784 normalised chars) — `7 years` **0**, `seven years`
  **0**, `retention period` **0**, `record retention` **0**, `retain` **1**, and
  that one occurrence is "select and **retain vendor models**", not records;
  nonsense **0** against `model risk` **86**.
  `inputs/20260902-arnaud/sources/SR2602a1.txt` (sha256 prefix `9da63f8700ba`,
  21,119 chars) — `7 years` **0**, `retention` **0**, `retain` **0**, against
  `model risk` **49**. **Neither guidance document sets any retention period.**
  The figure is retained and its attribution withdrawn, in the same sentence,
  converging on the wording already carried at `governance/observability.md:205`
  and across `asdlc/`: "a policy-set seven years … with no instrument setting
  that period", plus a direction to name the actual source — the institution's
  records schedule or the applicable examination record requirements.

- **D-57: GDPR Article 22(4)'s gateway stated as bare "Member State law", at
  three sites in this repository. The earlier fix was scoped to `domains/pharma.md`
  and the scoping was the defect.** `agent/agent-regulatory-classification.md:170`,
  `domains/financial-services.md:156` and `domains/insurance.md:166` each said
  Article 22(4) prohibits solely automated decisions based on special category
  data "except where the individual has given explicit consent or where Member
  State law provides for it". Re-derived at the hashed GDPR primary
  (`inputs/20260905-arnaud/prep/domain-files/sources/gdpr.html.gz`, sha256 prefix
  `fd3f4cffd904`, 350,797 normalised chars; nonsense **0**). Article 22(4):
  "**decisions referred to in paragraph 2** shall not be based on special
  categories of personal data referred to in Article 9(1), unless **point (a) or
  (g) of Article 9(2)** applies **and suitable measures to safeguard the data
  subject's rights and freedoms and legitimate interests are in place**" — each
  clause matching the primary once. Three faults in the old form: it bit on all
  solely automated decisions rather than the Article 22(2) subset; the second
  gateway is Article 9(2)(g) — "necessary for reasons of substantial public
  interest, on the basis of **Union or Member State law** which shall be
  proportionate to the aim pursued, respect the essence of the right to data
  protection and provide for suitable and specific measures to safeguard the
  fundamental rights and the interests of the data subject" — not any Member
  State law that "provides for it"; and the safeguards condition, which applies
  on top of either gateway, was dropped entirely. `domains/pharma.md:163`
  already recorded this defect and withdrew its own citation, but that
  correction was scoped to the pharma file by a list of sites rather than by an
  enumeration, and the three sites above kept the flat form. All three now carry
  the qualified statement. (A fourth site,
  `agentic-engineering-manifesto/domains/insurance.md:222`, is outside this
  repository's write scope and is recorded here, not corrected here.)

- **D-57: FCA expectations attributed to instruments that set none — the one
  `UNCHECKABLE` in the sweep, now retrieved and closed.**
  `agent/agent-regulatory-classification.md:210` was headed "FCA PS22/3 / FCA AI
  and Machine Learning in Financial Services" and asserted that "the FCA expects"
  firms to explain AI-driven decisions to customers, monitor for model drift,
  maintain governance records and route material AI changes through model risk
  management. The two AI publications the FCA and the Bank of England have
  jointly issued were **retrieved, both HTTP 200 at first attempt with
  `--compressed`**: DP5/22,
  `https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence`
  (retrieved 2026-09-06, sha256 prefix `81c81cef03435b85`, 119,388 normalised
  chars), and FS2/23,
  `https://www.bankofengland.co.uk/prudential-regulation/publication/2023/october/artificial-intelligence-and-machine-learning`
  (retrieved 2026-09-06, sha256 prefix `6d97acba3a2c28a9`, 57,093 chars). The
  direct PDF paths under `fca.org.uk` return **HTTP 404** and the FCA
  publications search returns **HTTP 403**; both figures are recorded rather than
  swallowed, and the documents were obtained from the joint publisher instead.
  DP5/22 states its own purpose as "to share and obtain feedback on: the
  potential benefits, risks, and harms related to the use of AI in financial
  services; how the current regulatory framework could apply to AI; whether
  additional clarification may be helpful" (**1** match, nonsense **0**) — a
  discussion paper, not a statement of expectations. FS2/23 "provides a summary
  of the responses to DP5/22" (**1**), anonymised. `the fca expects` occurs
  **0** times in either. "PS22/3" is neither document. The four duties are
  retained as this framework's own and the attribution to the FCA is withdrawn
  in the sentence that made it, with the reader directed to the Handbook
  provisions that do bind the firm.

- **Method note for the five entries above.** Every quotation was byte-compared
  against the hashed primaries after normalising with the checker's own
  `normalizeForMatch` (lower-case, dash→space, curly→straight quotes, whitespace
  collapse, **trim**), needles normalised first and padded after. **16
  quotations, 16 matches**, with the nonsense needle `zzqx wibblefrotz` at **0**
  in every one of the six sources. Prefix-safe, whole-token article controls on
  the AI Act primary: ` article 4 ` **83** does not absorb ` article 47 ` **19**;
  ` article 2 ` **50** does not absorb ` article 22 ` **6**; `article 49(1)`
  **4**. Every glob was quoted — an unquoted `--include=*.md` errors under `zsh`
  while the pipeline still prints `0`, which is indistinguishable from a real
  zero. **Content was retained in every case; only attribution was withdrawn or
  corrected. No control, no adjudication row and no `struck-strings` entry was
  deleted.** These entries are recorded here even though `errata.md` is
  untracked, so `git -C aplc diff` does not show them.

- **Checker movement created by the five entries above, isolated by masking —
  disclosed, not adjudicated.** `node tools/citation-consistency.mjs` was run
  before and after, twice each, byte-identical within each pair. Reversing
  exactly the edits above in a scratch copy of the working tree and re-running:
  disagreeing pairs **73 → 72**, sub-clause citations with no structure data
  **46 → 35**, sub-clause fabrications **1 → 1** (unchanged), refused
  **18 → 18** (unchanged). Masking `Article 47`, `Article 49` and `Article 71`
  to a nonsense token throughout this repository, in a scratch copy, moves pairs
  **74 → 71** and no-structure-data **52 → 27**, confirming that **every unit of
  movement this pass causes is confined to the `EU_AI_ACT|Art.47/49/71` keys** —
  the correct owner and the correct provision, for which
  `tools/regulatory-article-structure.json` carries no sub-clause structure.
  Those citations are therefore *declared as unchecked*, not passed and not
  failed. No adjudication row was added: `tools/` is outside this repository's
  write scope.
  **Six new fabricated-quotation flags were created and then removed at source.**
  Quoting the absent needles (`4 hours`, `72 hours`) and the FCA/BoE material
  inside the corrected sentences made the checker read them as quotations
  attributed to the nearest instrument label — DORA and, for the FCA paragraph,
  `EU_AI_ACT`, since no FCA primary is registered. **The corpus sentences were
  restated without double-quoted spans and the verbatim quotations kept here
  instead**, where they do not flag. `aplc/` now contributes **0** truly-new
  fabricated findings. The 11 truly-new findings in the final run are all in
  `agentic-engineering-manifesto/`, outside this repository's write scope and
  being worked concurrently.

### D-57 · `aplc-guide.md:296` — DORA Art. 26 TLPT scope: the surviving cross-repo twin (`G7`)

- **Struck.** *"DORA Article 26 requires **advanced financial entities** to conduct
  Threat-Led Penetration Testing (TLPT) at least every three years."*
- **Why.** DORA uses no "advanced" class of financial entity. At the hashed DORA
  primary (`inputs/20260905-arnaud/prep/asdlc-standards/sources/dora_fulltext.txt`,
  sha256 prefix `25328c7e39c4`, 303,607 normalised chars measured through the
  checker's own `normalizeForMatch`, normalising first and padding after):
  `advanced financial entities` **0** · `significant financial entities` **0**.
  Positive controls on the same harness: `threat led penetration testing` **3** ·
  `TIBER-EU` **3** · `at least every 3 years` **1** · the word form
  `at least every three years` **0** (a digit-and-word split, both checked).
  Negative control `zorkmid frotzwibble` **0**, so the zeros are demonstrated
  absences and not a dead search.
- **What Art. 26(1) actually binds.** Read in full at the primary:
  *"Financial entities, other than entities referred to in Article 16(1), first
  subparagraph, and other than microenterprises, which are identified in
  accordance with paragraph 8, third subparagraph, of this Article, shall carry
  out at least every 3 years advanced testing by means of TLPT."* The competent
  authority may, on the entity's risk profile and operational circumstances,
  request that the frequency be reduced or increased. **"Advanced" qualifies the
  *testing*, not a class of entity** — which is how the defect was manufactured.
  The third subparagraph of Art. 26(8) is the one beginning *"Competent
  authorities shall identify financial entities that are required to perform
  TLPT taking into account the criteria set out in Article 4(2)"*. Note that the
  primary writes **"paragraph 8, third subparagraph, of this Article"**, not
  "Article 26(8), third subparagraph" — `Article 26(8)` returns **0** at the
  primary; the short form is the corpus's own restatement and is not quoted here
  as the Regulation's words.
- **This was the twin of a defect already corrected, one repository over.** The
  same night, AEM `regulatory/foundation-model-third-party-register.md` §3.5 was
  corrected out of the identical defect, where the wrong class was worded
  *"significant financial entities"*. That correction landed in AEM only. The
  aplc carrier survived it because it worded the same wrong class differently —
  **`advanced` rather than `significant`** — so no string-scoped sweep of the
  corrected phrase could ever have reached it.
- **Recorded as `G7` evidence.** `G7` is *a corrective pass scoped by a list,
  where the list is the defect*. `tools/struck-strings.tsv` is that list, and it
  carries **no row for either wording** — the AEM correction added none. This is
  the seventh generator demonstrating itself within hours of being opened, which
  is the point of recording it: a second, independent instance is what
  distinguishes a generator from a one-off. The file's own header already
  records the same shape at larger scale ("THE LARGEST CITATION WITHDRAWAL THIS
  PROGRAMME HAS RUN HAD NO ROW HERE AT ALL"). `tools/` is outside this pass's
  write scope, so no row was added; a row for **both** wordings belongs in the
  same edit as any future strike.
- **Anchor caveat for whoever adds that row, measured after the final edit.**
  Masked-copy measurement (correction notes replaced by a placeholder in a scratch
  copy): in `aplc-guide.md` **both phrases are 0 in live prose** — `advanced
  financial entities` **0**, `significant financial entities` **0**. The corrected
  paragraph names the two rejected class words as *advanced* and *significant*
  in italics and keeps the counts here, rather than carrying the full phrases;
  that is a deliberate second pass, because the first version of this correction
  kept them as backticked needles and **created three truly-new fabricated-quotation
  flags** by doing so (see the movement note below). Unmasked, the phrases survive
  at exactly two kinds of site: **this file** (`advanced` 3, `significant` 4) and
  **the correction note at `aplc-guide.md:296`** (1 each) — text *about* the
  strike, not the strike. **A struck row anchored on either bare phrase would fire
  on the correction that retires the defect and on this entry.** Anchor on the
  full struck assertion, not the phrase — the same trap the `struck-strings.tsv`
  header records at its ":130" and "Annex 11 s 11" notes. No control was deleted;
  the control moved to where it does not flag.
- **Verified how.** Re-derived from the primary rather than inherited from the
  adjudication that handed it back. Enumerated both wrap-safe
  (`command grep -rlEz --include='*.md' 'advanced[[:space:]]+financial[[:space:]]+entities' .`,
  quoted glob — an unquoted `--include=*.md` errors under zsh while still
  printing a count) and by a normalised whole-file scan with dashes mapped to
  spaces; both return the single carrier. Positive control `DORA` **426** across
  the three repos confirms the scanner was live — a first run of it returned 0
  files and would have scored every needle as a false absence.
- **This file is untracked under `D-57`, so `git -C aplc diff` does not show
  this entry. It was written anyway and this line says so.**

### D-57 / D-61 · `agent/agent-conception.md:286` — an EU AI Act Annex IV citation filed under GDPR, and the annex shape enumerated

- **Struck.** *"Accountable for: regulatory classification, conformity
  assessment, documentation (Annex IV), GDPR compliance, sector-specific
  regulatory obligations."* The line named no instrument, so the attribution
  mechanism supplied the nearest one — **GDPR**, from the words "GDPR
  compliance" four words later on the same line.
- **Corrected to** *"documentation (**EU AI Act** Annex IV)"*. **Content
  retained, no citation deleted, nothing else on the line touched:** the edit is
  a pure ten-byte insertion, and the line is **byte-identical to its predecessor
  once the inserted `eu ai act ` is removed**, compared through the checker's own
  `normalizeForMatch` (normalised first, padded after).
- **Why, re-derived at the primaries rather than inherited.** **GDPR has no
  annexes**: **0** `id="anx_` in the hashed primary
  (`inputs/20260905-arnaud/prep/domain-files/sources/gdpr.html.gz`) against a
  positive control of **198** `id="art_` in the same file. The **EU AI Act** has
  **13** `id="anx_` against **226** `id="art_`
  (`inputs/20260902-arnaud/sources/OJ_L_202401689_AIAct.html.gz`, sha256 prefix
  `a0f437e89667`), and `anx_IV`'s own heading was READ: "**ANNEX IV Technical
  documentation referred to in Article 11(1)**" — which is precisely what the
  Regulatory Owner is accountable for on this line.
- **`refused` was not `fixed`, and this is the fix.** The no-annex bound had made
  this site **visible again** — §1 named it as a provable mis-attribution with
  file and line rather than resolving it silently to GDPR — but a bound refuses;
  it never supplies a replacement. Naming the instrument closes it: the site now
  produces a live `EU_AI_ACT | annex | Annex IV` triple and has left the refusal
  list (no-annex refusals **6 → 5**).
- **Second site in this repository, same shape, different article.**
  `agent/agent-release-governance.md:156` read "missing AI disclosure is a direct
  **Article 50** violation" and was carried onto GDPR by "GDPR Article 22" four
  lines above. **GDPR Art. 50 is *International cooperation for the protection of
  personal data*; EU AI Act Art. 50 is *Transparency obligations for providers
  and deployers of certain AI systems***, read at both hashed primaries. The
  instrument is now named on the line.
- **Both shapes enumerated across this repository and
  `agentic-engineering-manifesto`.** `command grep` run from **inside each repo**
  with **quoted globs** and `--exclude-dir=node_modules`, cross-referenced
  against the checker's own `--dump-triples`. The `command grep` file set
  (**30** here, **113** in AEM) was proved equal to `git ls-files` +
  `git ls-files --others --exclude-standard`, **so this untracked `errata.md` is
  inside the scan** — `git grep` alone would have missed it.
  - **Bare `Annex N` on an instrument-less line: 326** across the two repos.
    Beyond `:286`, **22** are carried onto an instrument that is not the AI Act
    — CSDR **8**, MDR **6**, MIFID_II **4**, SOLVENCY_II **4** — and read at the
    site every one is an EU AI Act annex. In this repository:
    `domains/insurance.md:119`, `:142`, `:145`, `:148` (→ SOLVENCY_II),
    `domains/financial-services.md:124`, `:127`, `:129` (→ MIFID_II), and
    `domains/pharma.md:52`, `:54`, `:68`, `:107` (→ MDR). **Reported, not
    fixed:** no bound reaches them, because `hasAnnexes` is **UNKNOWN** for
    CSDR, MIFID_II and SOLVENCY_II and absent means unknown rather than "assume
    none"; and re-attributing eleven sites here at once would change the
    membership and the representative pairs of the `EU_AI_ACT|Annex III / IV /
    VI / VII` §2 groups — the same census trade T4.36 priced and declined. Each
    needs adjudication at its own site.
  - **Bare `Art. N` on an instrument-less line: 548** across the two repos, of
    which **40** resolve to GDPR and **six are wrong** — the two fixed by this
    pass in this repo and AEM's `_swarm-changelog.md:284`, `:285`,
    `eu-ai-act-addendum.md:322`, `iso-42001-crosswalk.md:179` and
    `nist-ai-rmf-crosswalk.md:28`. The remaining GDPR attributions are correct
    (Art. 22, Art. 9(2), Art. 12(3)), read at the site. **Clusters, not
    singletons:** the sixteen-citation `agent-annex-iv-mapping.md:28` shape
    repeats here as adjacent-bullet drag.
  - The **wrap-safe** scan (`command grep -rlEz --include='*.md' 'Annex[[:space:]]+([IVXLC]+|[0-9]+)'`,
    quoted glob) and a normalised whole-file scan with dashes mapped to spaces
    added no file the line-scoped scan missed — but the wrap shape is **live in
    this repository** at `domains/insurance.md:118-119`, where "EU AI" ends one
    line and "Act Annex IV" begins the next, so the line-level recogniser sees
    no instrument and Solvency II on `:117` takes the annex.
- **Fresh negative control, proved against a positive.** `plimberwauxen
  thrangloscoot` — **0** whole and **0** for each half, line-scoped and
  wrap-safe, in both repositories and on the edited lines; positive controls on
  the identical commands returned `Annex` **317** hits over **30** files scanned
  here and **203** over **113** in AEM, and `EU AI Act` **1** on each edited line
  after the edit. **None of `zorkmid`, `frotzwibble`, `zzq` or `wibblefrotz` was
  used** — an errata entry that records a control retires it.
- **Prefix-safe controls, whole tokens, because a digit is not a word.** On
  `:286`, `Annex I(?![VXLC0-9])` → **0** while `Annex IV(?![0-9IVXLC])` → **1**,
  `Annex III(?![0-9IVXLC])` → **0** and `Annex IVX` → **0**: `Annex I` does not
  match `Annex IV` under the control used.
- **Movement, isolated and named.** Across both repositories: triples
  **1882 → 1883**, GDPR **234 → 228**, EU_AI_ACT **1146 → 1153**, unattributed
  **460 → 459**, no-annex refusals **6 → 5**. The `--dump-triples` diff against
  the baseline is **exactly** the six GDPR→EU_AI_ACT moves plus this annex
  citation. **Everything else is unchanged line for line:** §2 pairs **73**,
  groups **96**, truly new **0**, sub-clause OK **564** / fabricated **1** / no
  structure data **27**, §3c rows **158**, `--known-only` exit **0**,
  `register-crossref` **exit 0**, `link-check` **broken 4 / total 1043**,
  `tools/check_overview_counts.py` **exit 0** (every matched overview count
  agrees with its authoritative spec; README inventory complete). Full run twice,
  **byte-identical**.
- **No rebuild is needed for this repository: it contains no `.html` file at
  all.** The twelfth AEM rebuild is named in that repository's errata.
- **This file is untracked under `D-57`, so `git -C aplc diff` does not show this
  entry. It was written anyway and this line says so.** Being untracked, it is
  also **not walked by the checker's `git ls-files`**, so nothing written here
  can move a census count — which is why the article and annex numbers are
  spelled out in this entry and deliberately are not in the companion entry in
  `agentic-engineering-manifesto/errata.md`, which *is* tracked and *is*
  scanned. `command grep` reaches this file regardless, and the enumeration
  above was run that way for exactly that reason.

---

[← Back to README](README.md)
