# Contributing

Thanks for helping improve a **competition-focused** entrepreneurship skill. The goal is to stay **actionable and judge-realistic**, not generic startup advice.

## What to contribute

- **References:** New patterns, rubric cues, or citations in `skills/entrepreneur-persona/references/` (keep files focused; cross-link from `SKILL.md` if you add a major doc).  
- **Judge questions:** Additions to `judge-question-bank.md` should be phrased like real judges - specific, testable, and category-tagged.  
- **Templates:** Improvements to `assets/*` should stay aligned with Clapp-style sections and the workflows in `SKILL.md`.  
- **Validator:** Changes to `scripts/validate_proposal.py` should remain **stdlib-only** unless there is a strong reason otherwise.

## What to avoid

- **Scope creep:** This repo is intentionally **one deep skill** (pitch / proposal / Q&A depth), not a 20-skill catalog.  
- **Third-party PDFs or paywalled text** pasted verbatim - link or summarize in your own words.  
- **Nested `README.md` inside `skills/entrepreneur-persona/`** - use repo root or `docs/` instead.

## Audit and quality

For large instruction changes, consider running the procedure in [`AUDIT_BENCHMARK_PROMPT.md`](../AUDIT_BENCHMARK_PROMPT.md) and updating [`skills/entrepreneur-persona/AUDIT_REPORT.md`](../skills/entrepreneur-persona/AUDIT_REPORT.md).

## Pull requests

1. Describe **what founder or judge scenario** your change improves.  
2. Run `python3 skills/entrepreneur-persona/scripts/validate_proposal.py skills/entrepreneur-persona/assets/business-proposal-template.md` if you touch the validator or template headings.  
3. Keep diffs focused - no drive-by refactors in unrelated files.
