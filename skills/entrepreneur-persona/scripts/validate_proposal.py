#!/usr/bin/env python3
"""
Validate a markdown business proposal against Clapp-style section headings.

Length heuristic: optional --max-words flags sections longer than a rough "one page"
(~250 words by default for dense proposals). Tune per competition PDF guidelines.

Section detection expects `## Section N: ...` headings matching `assets/business-proposal-template.md`. For alternate heading styles, normalize the
draft to that template or extend SECTION_PATTERNS in code.

Uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


# Headings expected from assets/business-proposal-template.md (titles may include parentheticals).
SECTION_PATTERNS: list[tuple[int, re.Pattern[str]]] = [
    (1, re.compile(r"^##\s+Section\s+1:\s*Summary\b", re.IGNORECASE | re.MULTILINE)),
    (2, re.compile(r"^##\s+Section\s+2:\s*Industry/Market\b", re.IGNORECASE | re.MULTILINE)),
    (3, re.compile(r"^##\s+Section\s+3:\s*Marketing\b", re.IGNORECASE | re.MULTILINE)),
    (4, re.compile(r"^##\s+Section\s+4:\s*Operations\b", re.IGNORECASE | re.MULTILINE)),
    (5, re.compile(r"^##\s+Section\s+5:\s*Financial\b", re.IGNORECASE | re.MULTILINE)),
    (6, re.compile(r"^##\s+Section\s+6:\s*Timeline\b", re.IGNORECASE | re.MULTILINE)),
    (7, re.compile(r"^##\s+Section\s+7:\s*People\b", re.IGNORECASE | re.MULTILINE)),
]

FINANCIAL_KEYWORDS = [
    "f1",
    "f2",
    "f3",
    "f4",
    "f5",
    "price",
    "cogs",
    "gross profit",
    "year1",
    "year 2",
    "y1",
    "y2",
    "assumption",
    "revenue",
    "projection",
    "unit",
    "$",
]


def _word_count(chunk: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", chunk))


def _find_section_body(text: str, pattern: re.Pattern[str]) -> str | None:
    m = pattern.search(text)
    if not m:
        return None
    start = m.end()
    rest = text[start:]
    next_h2 = re.search(r"^##\s+(?!#)", rest, re.MULTILINE)
    end = next_h2.start() if next_h2 else len(rest)
    return rest[:end].strip()


def analyze_proposal(text: str, max_words: int) -> dict:
    present: dict[int, bool] = {}
    bodies: dict[int, str] = {}
    for num, pat in SECTION_PATTERNS:
        body = _find_section_body(text, pat)
        bodies[num] = body or ""
        present[num] = body is not None and len(body.strip()) > 0

    section_words = {n: _word_count(bodies[n]) for n in bodies}

    fin_text = bodies.get(5, "").lower()
    fin_hits = [kw for kw in FINANCIAL_KEYWORDS if kw.lower() in fin_text]
    gross_signals = bool(
        re.search(r"gross\s+profit", fin_text)
        or re.search(r"\bunits?\s*[*×x]\s*\(", fin_text, re.IGNORECASE)
        or re.search(r"\(\s*price\s*[-–]\s*cogs", fin_text, re.IGNORECASE)
    )

    long_sections = [n for n, wc in section_words.items(
    ) if present.get(n) and wc > max_words]

    return {
        "present": present,
        "section_words": section_words,
        "financial_keywords_found": fin_hits,
        "gross_profit_mentioned": gross_signals,
        "long_sections": long_sections,
        "total_words": _word_count(text),
    }


def print_report(result: dict, max_words: int) -> None:
    print("Business proposal validation checklist")
    print("=====================================")
    for n in range(1, 8):
        ok = result["present"].get(n, False)
        wc = result["section_words"].get(n, 0)
        status = "OK" if ok else "MISSING or empty"
        print(f"  Section {n}: {status}  ({wc} words)")
    print(f"\nTotal words (file): {result['total_words']}")

    if result["long_sections"]:
        print(f"\n! Length warnings (>{max_words} words / section):")
        for n in result["long_sections"]:
            print(f"    - Section {n}: {result['section_words'][n]} words")
    else:
        print("\nLength: no section exceeds the word threshold.")

    print("\nFinancial section (Section 5) signals:")
    if not result["present"].get(5):
        print("  ! Section 5 missing — cannot evaluate F1–F5.")
    else:
        kws = result["financial_keywords_found"]
        print(
            f"  Keyword hits ({len(kws)}): {', '.join(sorted(set(kws))) or '(none)'}")
        if result["gross_profit_mentioned"]:
            print("  OK: Gross-profit style language or formula pattern detected.")
        else:
            print(
                "  ! Warning: No clear gross profit / Units*(Price-COGS) style signal — "
                "add F4 math explicitly per competition guide."
            )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check Clapp-style proposal sections, word counts, and financial cues."
    )
    parser.add_argument("markdown_file", type=Path,
                        help="Path to proposal .md")
    parser.add_argument(
        "--max-words",
        type=int,
        default=250,
        help="Warn if any section body exceeds this many words (default: 250).",
    )
    args = parser.parse_args()
    path: Path = args.markdown_file
    if not path.is_file():
        print(f"Error: file not found: {path}", file=sys.stderr)
        return 1
    text = path.read_text(encoding="utf-8", errors="replace")
    result = analyze_proposal(text, args.max_words)
    print_report(result, args.max_words)

    missing = [n for n in range(1, 8) if not result["present"].get(n)]
    if missing:
        print(f"\n! Missing or empty sections: {missing}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
