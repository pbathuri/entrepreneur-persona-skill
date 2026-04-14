# Maintainer notes (Claude / agents)

This repository packages **one** high-depth skill for **pitch competitions**, **business proposals**, and **judge-style Q&A**.

## Layout

- **Plugin:** [`.claude-plugin/`](.claude-plugin/) — `entrepreneur-persona` plugin id.  
- **Skill root:** [`skills/entrepreneur-persona/`](skills/entrepreneur-persona/) — do not add `README.md` here.  
- **User docs:** [`docs/`](docs/), root [`README.md`](README.md).  
- **Audit:** [`skills/entrepreneur-persona/AUDIT_REPORT.md`](skills/entrepreneur-persona/AUDIT_REPORT.md).

## When editing the skill

- Prefer editing **`SKILL.md`** for workflow/persona changes; use **`references/`** for long tables and frameworks.  
- Keep **`description` in YAML** under 1024 characters and trigger-rich.  
- Run the proposal validator from repo root:  
  `python3 skills/entrepreneur-persona/scripts/validate_proposal.py skills/entrepreneur-persona/assets/business-proposal-template.md`

## When editing the repo

- Update **cross-links** if paths change (`AUDIT_BENCHMARK_PROMPT.md`, `CURSOR_COMPOSER_PROMPT.md`, etc.).  
- After structural changes, refresh **`CHANGELOG.md`**.
