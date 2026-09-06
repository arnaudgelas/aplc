#!/usr/bin/env python3
"""
check_overview_counts.py — verify APLC overview counts against their
authoritative detail specifications, by command rather than by memory.

Background: D-30 and D-31 (inputs/20260823-arnaud/remediation.md) found that
aplc.md and README.md state summary counts (CSH components, governance
tools, Behavioral Release Gate conditions) that drift from the detail
documents that define them, and that README.md's document inventory omits
files that exist on disk. Hand-patching each occurrence found by a person is
the mechanism that produced that drift — this script makes the check
mechanical and repeatable instead.

Authoritative counts are computed fresh on every run from the detail specs:
  - CSH components            -> agent/agent-composite-versioning.md
                                  (numbered "**N. " list items)
  - Governance tools           -> governance/tool-stack.md
                                  ("### T\\d\\d " headings)
  - Behavioral Release Gate    -> agent/agent-release-governance.md
    conditions                   ("### Gate Condition \\d+" headings)

This script does not silently regenerate prose (the overview documents are
hand-written narrative, not templated output), so this implements approach
(b) from the remediation plan (T4.3.1/T4.3.2, APLC portion): every overview
count must be an explicitly abbreviated summary that names its authority,
and this script is the mechanical check that the number stated still agrees
with that authority. Run it after editing any authoritative document or any
overview document, before committing.

It also checks that every *.md file directly under aplc/, aplc/agent/, and
aplc/governance/ is named somewhere in README.md's document inventory.

Usage:
    python3 aplc/tools/check_overview_counts.py

Exit 0 if every matched count agrees with its authority and every file is
listed; exit 1 (with each mismatch printed) otherwise.
"""
import re
import sys
import pathlib

TOOLS_DIR = pathlib.Path(__file__).resolve().parent
APLC = TOOLS_DIR.parent

WORDS = ["zero", "one", "two", "three", "four", "five", "six", "seven",
         "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
         "fifteen"]
WORD2NUM = {w: i for i, w in enumerate(WORDS)}
NUMBER_ALT = "|".join(WORDS[1:])


def count_matches(path: pathlib.Path, pattern: str) -> int:
    text = path.read_text(encoding="utf-8")
    return len(re.findall(pattern, text, re.MULTILINE))


def authoritative_counts():
    return {
        "csh_components": count_matches(
            APLC / "agent" / "agent-composite-versioning.md", r'^\*\*[0-9]+\. '
        ),
        "governance_tools": count_matches(
            APLC / "governance" / "tool-stack.md", r'^### T[0-9]{2} '
        ),
        "release_gate_conditions": count_matches(
            APLC / "agent" / "agent-release-governance.md",
            r'^### Gate Condition [0-9]+',
        ),
    }


PATTERNS = {
    "csh_components": re.compile(
        rf'\b({NUMBER_ALT})\b[\s-]+components?\b', re.IGNORECASE
    ),
    "governance_tools": re.compile(
        rf'\b({NUMBER_ALT})\b\s+(?:canonical\s+)?governance\s+tools?\b',
        re.IGNORECASE,
    ),
    "release_gate_conditions": re.compile(
        rf'\b({NUMBER_ALT})\b[\s-]*'
        r'(?:agent-specific|behavioral release gate|release-gate|release gate)'
        r'\s*conditions?\b',
        re.IGNORECASE,
    ),
}

# Files whose own numbered lists/headings ARE the authority: they enumerate
# every item by design and are not checked against themselves.
AUTHORITATIVE_FILES = {
    APLC / "agent" / "agent-composite-versioning.md",
    APLC / "governance" / "tool-stack.md",
    APLC / "agent" / "agent-release-governance.md",
}

# Known false positives: places where "<number> component(s)" appears but is
# not a claim about the total number of Composite State Hash components —
# e.g. "the one component ... you do not control" (a pointer into the six,
# not a total), or an unrelated "components" (Trust Architecture's three
# components: Principal Hierarchy, Permission Model, Conflict Resolution).
# Verified by reading each hit; documented here rather than silently
# swallowed by a looser regex, so a genuine future miscount in one of these
# same sentences is not masked by this allowlist growing unreviewed.
CSH_FALSE_POSITIVES = (
    "Three components are required",
    "is the one component of the composite state",
    "The foundation model is the one component",
)


def check_counts(auth) -> bool:
    ok = True
    for path in sorted(APLC.rglob("*.md")):
        if path in AUTHORITATIVE_FILES:
            continue
        text = path.read_text(encoding="utf-8")
        for key, pattern in PATTERNS.items():
            for m in pattern.finditer(text):
                word = m.group(1).lower()
                n = WORD2NUM[word]
                if key == "csh_components":
                    line_start = text.rfind("\n", 0, m.start()) + 1
                    line_end = text.find("\n", m.end())
                    line_end = len(text) if line_end == -1 else line_end
                    line_text = text[line_start:line_end]
                    if any(fp in line_text for fp in CSH_FALSE_POSITIVES):
                        continue
                if n != auth[key]:
                    line_no = text.count("\n", 0, m.start()) + 1
                    rel = path.relative_to(APLC.parent)
                    print(
                        f"FAIL  {rel}:{line_no}: '{m.group(0)}' states "
                        f"{word} ({n}) but the authority for {key} "
                        f"({_authority_label(key)}) is "
                        f"{WORDS[auth[key]]} ({auth[key]})"
                    )
                    ok = False
    if ok:
        print("OK    every matched overview count agrees with its authoritative spec")
    return ok


def _authority_label(key: str) -> str:
    return {
        "csh_components": "agent/agent-composite-versioning.md",
        "governance_tools": "governance/tool-stack.md",
        "release_gate_conditions": "agent/agent-release-governance.md",
    }[key]


def check_inventory() -> bool:
    """Every *.md directly under aplc/, aplc/agent/, aplc/governance/ must be
    named somewhere in README.md (the document inventory)."""
    readme = APLC / "README.md"
    readme_text = readme.read_text(encoding="utf-8")
    ok = True
    candidates = []
    for sub in ("", "agent", "governance"):
        d = APLC / sub if sub else APLC
        candidates.extend(sorted(d.glob("*.md")))
    for path in candidates:
        if path == readme:
            continue
        base = path.name
        if base not in readme_text:
            rel = path.relative_to(APLC.parent)
            print(f"FAIL  README.md document inventory omits {rel}")
            ok = False
    if ok:
        print("OK    README.md document inventory lists every top-level/agent/governance *.md file")
    return ok


def main() -> int:
    auth = authoritative_counts()
    print("Authoritative counts (computed by command from the detail specs):")
    for k, v in auth.items():
        print(f"  {k} = {v} ({WORDS[v]}) <- {_authority_label(k)}")
    print()

    counts_ok = check_counts(auth)
    print()
    inventory_ok = check_inventory()

    return 0 if (counts_ok and inventory_ok) else 1


if __name__ == "__main__":
    sys.exit(main())
