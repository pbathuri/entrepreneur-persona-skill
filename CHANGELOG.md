# Changelog

All notable changes to this repository are documented in this file.

## [2.0.0] - 2026-04-15

### Added

- **8th principle: "Why Now?" clarity** - timing thesis framework covering technology, regulation, behavior, market structure, and funding conditions. Integrated into all workflows, proposal template, script template, and competition rubric.
- **Validation gate** - pre-check mechanism before Workflows 2–4 ensures idea has been validated before producing deliverables. Includes gauntlet score threshold (avg ≥ 3.0) warning.
- **Industry adaptation layer** - new `references/industry-verticals.md` with per-vertical guidance for SaaS, Marketplace, Hardware/IoT, Biotech/Healthtech, CPG/D2C, Fintech, Edtech, and Climate/Energy. Auto-detection prompt for vertical classification.
- **Market landscape file** - new `references/market-landscape-2025.md` covering current VC funding environment, AI-specific red flags, regulatory checkpoints (EU AI Act, FDA SaMD, state privacy), business model red flags, and macro-to-micro economic integration.
- **Slide design checklist** - new `assets/deck-slide-checklist.md` with visual design rules, slide-specific guidance, and common mistakes.
- **Team alignment canvas** - new `assets/team-alignment-canvas.md` for co-founder teams: vision alignment, RACI matrix, equity/commitment, skill gaps, and conflict protocol.
- **Guided onboarding** - "Getting Started" section in SKILL.md with progressive pathway, example prompts, industry awareness prompt, and geography awareness.
- **Expanded delivery coaching** - 8 specific delivery bullets (plant feet, eye contact, pause after numbers, smile before starting, answer directly, stand behind team).
- **Iteration tracking** - scoring persistence instructions with score-range interpretation guide (< 2.0 through 4.0+).
- **Geography awareness** - guidance for non-US ventures covering regulatory adaptation, market sizing sources, and currency/distribution considerations.
- **Export guidance** - multi-format output instructions (slides, PDF, one-pager, investor memo) with tool recommendations.
- **13 new judge questions** - 8 for AI/technology/defensibility, 5 for macro environment/timing (bank now 75+).
- **"Why Now?" rubric row** - added to competition-rubrics.md detailed rubric table.

### Changed

- **Principle 6 expanded** - "Judge empathy" now includes explicit team weighting guidance (~50% VC, ~25% competition) and "accomplishments over titles" instruction.
- **Proposal template Section 7 (People)** - expanded from P1–P3 to P1–P5 with accomplishments table, founder-problem fit, partnership status tracking, and skill gap fill plan.
- **Pitch script template** - added "Why Now?" section (new section 5), expanded Team to (~20 sec) with accomplishments focus. Renumbered sections 5–11 to 6–12.
- **Deck slide structure** - expanded to 12 slides with "Why Now?" (slide 5) and expanded Team (~20s). Added visual design rules and checklist reference.
- **Presentation coaching rules** - expanded with billboard test, font size, image-over-bullets, color constraints, and checklist reference.
- **Version** bumped to 2.0.0 across plugin.json, manifest.json, marketplace.json.

## [1.0.0] - 2026-04-14

### Added

- **Claude Code plugin layout:** `.claude-plugin/plugin.json`, `marketplace.json`, and `manifest.json` for marketplace install and skill path discovery.  
- **`skills/` directory:** Skill moved to `skills/entrepreneur-persona/` (canonical path aligned with popular skill repos).  
- **Documentation:** `docs/INSTALLATION.md`, `docs/SKILL_FORMAT.md`, `docs/CONTRIBUTING.md`, and root `CLAUDE.md`.  
- **README:** Installation commands, comparison to other skill collections, FAQ, and discoverability-oriented structure.

### Changed

- **Breaking:** Previous path `entrepreneur-persona/` at repo root is now **`skills/entrepreneur-persona/`**. Update scripts, bookmarks, and relative paths accordingly.
