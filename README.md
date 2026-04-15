<p align="center">
  <img src="https://img.shields.io/badge/version-2.0.0-blue" alt="Version 2.0.0">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License">
  <img src="https://img.shields.io/badge/judge_questions-75%2B-orange" alt="75+ Judge Questions">
  <img src="https://img.shields.io/badge/industries-8_verticals-purple" alt="8 Industry Verticals">
  <img src="https://img.shields.io/badge/python-stdlib_only-lightgrey" alt="No Dependencies">
</p>

# Entrepreneur Persona — Your AI Pitch Coach for Business School Competitions

> **Load one skill. Get a mentor who's coached 200+ startups through idea competitions, pitch nights, and accelerator applications — and won't let you skip validation.**

Whether you're prepping for the **Kelley IdeaFestival**, **MIT $100K**, **Harvard NVC**, **Rice Business Plan Competition**, **Booth New Venture Challenge**, or your **New Venture Creation** final — this skill turns Claude into a **competition-grade startup mentor** that challenges your assumptions, scores your answers like a real judge, and produces **submission-ready deliverables**.

---

## What makes this different

| Most AI tools do this | This skill does this instead |
|---|---|
| "Great idea! Here's a business plan." | **"Who hurts, how badly, how often? You haven't validated yet."** |
| Generic 10-slide template | **12-slide deck aligned to Sequoia/YC/Kawasaki** with timing cues |
| "Your market is huge!" | **"Your SOM math assumes 5% adoption — show me the channel that gets you there."** |
| No financial rigor | **Units x (Price - COGS) = Gross Profit** — every number shows its assumption |
| Same advice for every idea | **Industry-specific guidance** for SaaS, marketplace, hardware, biotech, CPG, fintech, edtech, climate |
| Ignores timing | **"Why Now?"** — the question that separates funded startups from class projects |

---

## Quick start (2 commands)

```text
/plugin marketplace add pbathuri/entrepreneur-persona-skill
/plugin install entrepreneur-persona
```

Then try:

```text
"I have a startup idea about [your idea]. Help me validate it."
```

**Local clone** (works with Claude Code, Cursor, or any editor):

```bash
git clone https://github.com/pbathuri/entrepreneur-persona-skill.git
```

```text
/plugin marketplace add /absolute/path/to/entrepreneur-persona-skill
/plugin install entrepreneur-persona
```

Full setup for Cursor, VS Code, and troubleshooting: **[docs/INSTALLATION.md](docs/INSTALLATION.md)**.

---

## The workflow: idea to pitch-ready in 5 stages

```
  VALIDATE          PROPOSE           DECK            SCRIPT          PRESSURE-TEST
 ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
 │ Problem   │───>│ 7-Section│───>│ 12-Slide │───>│ 5-Minute │───>│ Judge    │
 │ Discovery │    │ Business │    │ Pitch    │    │ Spoken   │    │ Gauntlet │
 │ & Mom Test│    │ Proposal │    │ Deck     │    │ Script   │    │ (10 Qs)  │
 └──────────┘    └──────────┘    └──────────┘    └──────────┘    └──────────┘
      │                │               │               │               │
  Validation      "Why Now?"      Billboard       Delivery        Score 1-5
  Gate ────────> enforced in ──> test + visual ─> coaching ──────> per answer
  (must pass)    every section    checklist       (8 bullets)     + fix plan
```

**The validation gate** prevents you from building a polished deck for an idea you haven't tested. Most AI tools skip this. We don't.

---

## What's inside

| Component | What it does | For your... |
|-----------|-------------|-------------|
| **8 Mentor Principles** | Problem-first thinking, validation hierarchy, conservative financials, "Why Now?", team-as-top-tier, judge empathy | Mindset |
| **75+ Judge Questions** | Across 9 categories: validation, finance, competition, distribution, operations, team, travel/events, AI/tech, macro timing | Q&A prep |
| **12-Slide Deck Structure** | Hook → Problem → Solution → Market → Why Now? → Competition → Traction → Model → GTM → Funds → Team → Ask | Pitch deck |
| **7-Section Proposal Template** | Clapp-style: Summary, Industry, Marketing, Operations, Financial, Timeline, People (P1-P5 expanded) | Written plan |
| **5-Minute Script Template** | Timing-marked with pauses, emphasis, transitions — aim for 4:30 with buffer | Spoken pitch |
| **Industry Verticals Guide** | SaaS, marketplace, hardware, biotech, CPG, fintech, edtech, climate — each with key metrics + validation Qs | Tailored advice |
| **Market Landscape 2025** | VC red flags, AI moat analysis, regulatory checkpoints (EU AI Act, FDA SaMD), macro-to-micro economics | Current context |
| **Deck Slide Checklist** | Visual rules: 30pt+ font, billboard test, one message/slide, images > bullets | Slide design |
| **Team Alignment Canvas** | RACI matrix, equity/vesting, vision alignment, conflict protocol — for co-founder teams | Team clarity |
| **Idea Refinement Canvas** | 6-block single-page canvas: problem, customer, alternatives, UVP, metrics, next actions | Quick validation |
| **Proposal Validator** | Python script — checks all 7 sections, word counts, financial keywords, gross-profit formula | Quality check |

---

## Built for business school

### Competitions this skill prepares you for

| Competition | School | What the skill covers |
|------------|--------|----------------------|
| **IdeaFestival** / **Shoemaker Challenge** | Kelley (Indiana) | 7-page proposal, pitch script, judge Q&A |
| **$100K Entrepreneurship Competition** | MIT Sloan | Technical moat, traction-heavy deck, 90-second pitch |
| **New Venture Competition** | Harvard Business School | Problem-solution fit, social enterprise framing |
| **Business Plan Competition** | Rice Jones | Investment-grade financials, cap table, exits |
| **New Venture Challenge** | Chicago Booth | Lean validation, customer discovery, unit economics |
| **BASES $150K Challenge** | Stanford | Market timing, product demo, growth metrics |
| **Wharton Business Plan Competition** | UPenn Wharton | Full business plan with operations depth |
| **Dare to Dream** / **1000 Pitches** | Michigan Ross | Rapid pitch format, competitive positioning |
| **Darden Venture Summit** | UVA | Investor-style Q&A, use of funds |
| **Hult Prize** | Cross-university | Impact as market inefficiency, not charity |
| **Texas Venture Labs (TVLIC)** | UT Austin McCombs | Due diligence, financial modeling |
| **Startup Challenge** | Duke Fuqua | Early-stage validation, team narrative |

### Courses where students use this

- **New Venture Creation** — business proposal writing with financial projections
- **Entrepreneurship Lab / E-Lab** — lean validation and customer discovery
- **Startup Garage** — prototype-to-pitch workflow
- **Lean Launchpad** — hypothesis testing and pivot decisions
- **Business Plan Development** — 7-section Clapp-style plans
- **Technology Entrepreneurship** — SaaS/hardware-specific guidance

---

## Example prompts to try right now

**Starting from zero:**
> *"I noticed a problem with [X] and want to explore if it's a business."*

**Writing a proposal:**
> *"I need a 7-page business proposal for my university idea competition."*

**Building a deck:**
> *"Build a 5-minute pitch deck for my SaaS product."*

**Practicing delivery:**
> *"Write a 4:30 spoken pitch script with timing cues and transitions."*

**Getting destroyed (in a good way):**
> *"Score my pitch answers like a tough judge — hardest 10 questions."*

**Testing your assumptions:**
> *"We have no competitors and will take 30% market share in year one."*
> *(Expect pushback. That's the point.)*

**Industry-specific:**
> *"I'm building a marketplace in Europe — adapt for my market."*

**Timing thesis:**
> *"Why is now the right time for my AI startup?"*

---

## How this compares

| | Generic ChatGPT | [slavingia/skills](https://github.com/slavingia/skills) | [mfwarren/entrepreneur-skills](https://github.com/mfwarren/entrepreneur-claude-skills) | **This skill** |
|--|--|--|--|--|
| **Validation gate** | No | No | No | **Yes — blocks unvalidated ideas** |
| **Judge question bank** | No | No | Partial | **75+ across 9 categories** |
| **Industry adaptation** | No | No | No | **8 verticals with specific metrics** |
| **Financial formula enforcement** | No | No | No | **Units x (Price - COGS) enforced** |
| **"Why Now?" framework** | No | No | No | **5-dimension timing analysis** |
| **Proposal validator** | No | No | No | **Python script, stdlib only** |
| **Competition rubric alignment** | No | No | No | **11-category scoring rubric** |
| **Delivery coaching** | No | No | No | **8 specific stage presence bullets** |

---

## Validate a proposal

From the repo root:

```bash
python3 skills/entrepreneur-persona/scripts/validate_proposal.py skills/entrepreneur-persona/assets/business-proposal-template.md
```

Checks: 7 section headings present, word counts per section, 16 financial keywords, gross-profit formula detection. **No dependencies** — Python 3 stdlib only.

---

## Repository layout

```
.claude-plugin/              # Plugin registration (marketplace install)
skills/entrepreneur-persona/
  SKILL.md                   # 8 principles, 5 workflows, validation gates
  references/                # 8 files: patterns, frameworks, rubrics, 75+ Qs, financials, vignettes, verticals, market landscape
  assets/                    # 5 templates: proposal, script, canvas, slide checklist, team canvas
  scripts/                   # validate_proposal.py (stdlib Python)
docs/                        # Installation, format spec, contributing guide
```

---

## FAQ

**Do I need to pay for anything?**
No. MIT License, no API keys, no dependencies. Works with Claude Code (free tier included).

**Is this only for MBA students?**
No. Undergrads, hackathon teams, and early-stage founders all use the same frameworks. The rigor level adjusts to what you bring.

**Does this replace my professor or mentor?**
No. It **augments** preparation — structure, question practice, evidence discipline. Your mentor provides judgment and connections this tool can't.

**Can I use this with Cursor or other editors?**
Yes. Add the `SKILL.md` as a project rule or `@`-reference. Keep the `references/` and `assets/` folders accessible. See [docs/INSTALLATION.md](docs/INSTALLATION.md).

**Can our entrepreneurship center adopt this?**
Yes. Fork it, customize the judge questions for your competition rubric, and point students at your fork. [MIT License](LICENSE).

**Where's the full audit and benchmark?**
See [`AUDIT_REPORT.md`](skills/entrepreneur-persona/AUDIT_REPORT.md) and [`BENCHMARK_REPORT.md`](BENCHMARK_REPORT.md). The skill was benchmarked against winning pitch patterns from YC, TechCrunch Disrupt, MIT $100K, Harvard NVC, and Shark Tank.

---

## For professors and program directors

This skill is designed to be **assigned as a tool** in entrepreneurship courses:

1. **Fork this repo** for your program
2. **Customize** `references/judge-question-bank.md` with your competition's rubric
3. **Students install** with 2 commands and immediately get structured mentorship
4. **Proposal validator** gives automated feedback on section completeness and financial rigor
5. **Works offline** — no API keys, no accounts, no data leaves the student's machine

The skill enforces the same frameworks you teach: **Lean Canvas**, **Mom Test**, **Business Model Canvas**, **JTBD**, **Customer Development**, **Crossing the Chasm** — applied to each student's specific idea, not lectured generically.

---

## Contributing

See **[docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)**. We especially welcome:
- Judge questions from real competitions
- Industry-specific validation frameworks
- Templates for competition formats we haven't covered

Changelog: **[CHANGELOG.md](CHANGELOG.md)**.

---

## License

[MIT](LICENSE) — free to use, fork, and customize for your program.

---

<p align="center">
  <code>claude</code> · <code>claude-code</code> · <code>claude-plugin</code> · <code>anthropic</code> · <code>entrepreneurship</code> · <code>pitch-deck</code> · <code>startup</code> · <code>business-plan</code> · <code>idea-competition</code> · <code>pitch-competition</code> · <code>business-school</code> · <code>mba</code> · <code>student-founder</code> · <code>validation</code> · <code>kelley</code> · <code>new-venture</code>
</p>
