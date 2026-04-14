# Entrepreneur Persona — Claude Code skill for pitch competitions and business plans

**A Claude Code plugin and Anthropic-style skill** that turns your AI into a **competition-seasoned startup mentor** — focused on **idea validation**, **startup pitch decks**, **5-minute presentation scripts**, **business proposals** (including Clapp-style 7-section plans), and **judge-style Q&A**. Use it when you are preparing for an **idea competition**, **university pitch night**, **demo day**, or your **first investor-style conversation**.

Repository: [github.com/pbathuri/entrepreneur-persona-skill](https://github.com/pbathuri/entrepreneur-persona-skill)

**See also:** [entrepreneur-persona-llm](https://github.com/pbathuri/entrepreneur-persona-llm) — model-agnostic copy of this playbook for any LLM.

---

## Installation (Claude Code)

```text
/plugin marketplace add pbathuri/entrepreneur-persona-skill
/plugin install entrepreneur-persona
```

**Local clone** (then point marketplace at the path):

```bash
git clone https://github.com/pbathuri/entrepreneur-persona-skill.git
```

```text
/plugin marketplace add /absolute/path/to/entrepreneur-persona-skill
/plugin install entrepreneur-persona
```

Full paths, Cursor setup, and troubleshooting: **[docs/INSTALLATION.md](docs/INSTALLATION.md)**.

---

## What you get

| Layer | Purpose |
|-------|---------|
| **[`skills/entrepreneur-persona/SKILL.md`](skills/entrepreneur-persona/SKILL.md)** | Seven mentor principles, five workflows (ideate → propose → deck → script → stress-test), quality bar for claims and numbers |
| **`references/`** | Pitch patterns, validation frameworks (Lean, Mom Test, JTBD, Chasm), **competition rubrics**, **60+ judge questions**, financial modeling guide, **benchmark vignettes** (YC, Disrupt, Shark Tank–style structures) |
| **`assets/`** | Fill-in **business proposal template**, **pitch script template**, **idea refinement canvas** |
| **`scripts/validate_proposal.py`** | Optional **stdlib Python** checker for section headings, length heuristics, and financial signals |

**No API keys.** Validator uses Python 3 only.

---

## Repository layout

```text
.claude-plugin/          # plugin.json, marketplace.json, manifest.json
skills/
  entrepreneur-persona/ # SKILL.md, references/, assets/, scripts/, AUDIT_REPORT.md
docs/                     # INSTALLATION, SKILL_FORMAT, CONTRIBUTING
README.md
CHANGELOG.md
CLAUDE.md                 # Maintainer notes for agents
```

Skill format details: **[docs/SKILL_FORMAT.md](docs/SKILL_FORMAT.md)**.

---

## Who it is for

- **Student founders** and **hackathon** teams writing a **business plan** or **pitch deck** under time pressure  
- **Early-stage entrepreneurs** who want **honest feedback** (not generic encouragement)  
- Anyone practicing **startup pitch** delivery and **investor Q&A**

---

## How this compares to other Claude entrepreneurship skills

| | [slavingia/skills](https://github.com/slavingia/skills) (*Minimalist Entrepreneur*) | [mfwarren/entrepreneur-claude-skills](https://github.com/mfwarren/entrepreneur-claude-skills) | **This repo** |
|--|--|--|--|
| **Shape** | Many lean skills, book-aligned journey | Large catalog (marketing, sales, ops, finance, etc.) | **One deep skill** |
| **Sweet spot** | Community → validate → ship → grow | Day-to-day founder operations | **Pitch competition + proposal + judge Q&A** |
| **Extras** | Slash-style commands per skill | `npx` installers, broad docs | **Judge question bank**, **rubric lens**, **proposal validator**, **audit report** |

All three are **complementary**. This project doubles down on **what judges ask**, **evidence hierarchy**, and **submission-ready structure**.

---

## Example prompts

- *“Help me validate my startup idea before I build an MVP.”*  
- *“I need a 7-page business proposal for my university idea competition.”*  
- *“Outline a 5-minute pitch deck for a hardware prototype.”*  
- *“Write a 4:30 spoken pitch script with timing cues.”*  
- *“Stress-test my pitch like a judge — hardest questions, score my answers.”*  
- *“We have no competitors and will take 30% market share in year one.”* (Expect pushback and reframing.)

---

## Validate a proposal (optional)

From the **repo root**:

```bash
python3 skills/entrepreneur-persona/scripts/validate_proposal.py skills/entrepreneur-persona/assets/business-proposal-template.md
```

---

## FAQ

**What is a Claude Code skill?**  
A packaged set of instructions and reference files Claude Code can load when your task matches the skill’s description and triggers. This repo follows common patterns from popular skill collections and adds **plugin metadata** under `.claude-plugin/`.

**Is this only for students?**  
No. The voice is tuned for **idea competitions** and **accelerator-style** rigor; any early-stage founder preparing a **pitch** or **written plan** can use it.

**Does this replace a human mentor or judge?**  
No. It **augments** preparation — structure, question practice, and evidence discipline — not final judgment.

**How is this different from a single long ChatGPT prompt?**  
The skill uses **progressive disclosure** (`references/`, `assets/`), a **question bank**, **templates**, and an optional **validator**, so the model can ground answers in consistent, competition-aligned material.

**Where is the full audit?**  
See **[`skills/entrepreneur-persona/AUDIT_REPORT.md`](skills/entrepreneur-persona/AUDIT_REPORT.md)**. Re-run the benchmark procedure with **[`AUDIT_BENCHMARK_PROMPT.md`](AUDIT_BENCHMARK_PROMPT.md)** if you change workflows heavily.

**Why is there no `README` inside the skill folder?**  
By convention (and to match Anthropic-style portability), documentation lives at **repo root** and in **`docs/`** — not inside `skills/entrepreneur-persona/`.

**Can I fork this for my university lab?**  
Yes — **[MIT License](LICENSE)**. Keep attribution and avoid redistributing third-party PDFs you do not own.

---

## Reference PDFs (local only)

If you keep competition or vendor PDFs on your machine for context, **do not commit them** — `*.pdf` is listed in `.gitignore`. Use official sources and your own materials locally.

---

## Contributing

See **[docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)**. Changelog: **[CHANGELOG.md](CHANGELOG.md)**.

---

## License

[MIT](LICENSE).

---

## Suggested GitHub topics

`claude` · `claude-code` · `claude-plugin` · `anthropic` · `ai-agents` · `skills` · `entrepreneurship` · `pitch-deck` · `startup` · `business-plan` · `idea-competition` · `pitch-competition` · `student-founder` · `validation` · `cursor-ai`
