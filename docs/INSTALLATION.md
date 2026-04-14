# Installation

This repo is a **Claude Code plugin** with one deep skill under [`skills/entrepreneur-persona/`](../skills/entrepreneur-persona/). The skill follows the common layout used by popular skill collections (for example [slavingia/skills](https://github.com/slavingia/skills) and [mfwarren/entrepreneur-claude-skills](https://github.com/mfwarren/entrepreneur-claude-skills)).

## Claude Code (recommended)

From the Claude Code prompt:

```text
/plugin marketplace add pbathuri/entrepreneur-persona-skill
/plugin install entrepreneur-persona
```

If your Claude Code build expects a **local clone** first:

```bash
git clone https://github.com/pbathuri/entrepreneur-persona-skill.git
```

Then:

```text
/plugin marketplace add /absolute/path/to/entrepreneur-persona-skill
/plugin install entrepreneur-persona
```

Adjust the path to where you cloned the repository. Plugin metadata lives in [`.claude-plugin/`](../.claude-plugin/).

## Manual copy (any agent)

Copy the folder `skills/entrepreneur-persona/` into your environment’s skills directory (see current Anthropic / Claude Code docs for the exact path on your OS).

Preserve the internal structure:

- `SKILL.md` at the skill root  
- `references/`, `assets/`, `scripts/` alongside it  

## Cursor and other editors

- Add a **project rule** or **instruction** that loads [`skills/entrepreneur-persona/SKILL.md`](../skills/entrepreneur-persona/SKILL.md), or `@`-reference that file in chat.  
- Keep `references/` and `assets/` on disk so the model can open linked files.

## Validate a business proposal (optional)

From the **repository root**:

```bash
python3 skills/entrepreneur-persona/scripts/validate_proposal.py skills/entrepreneur-persona/assets/business-proposal-template.md
```

Replace the final path with your draft if it uses the same `## Section N:` headings as the template.

## Troubleshooting

- **Plugin name mismatch:** The install name is `entrepreneur-persona` (see [`.claude-plugin/plugin.json`](../.claude-plugin/plugin.json)).  
- **Skills not found:** Confirm `skills/entrepreneur-persona/SKILL.md` exists relative to the repo root.  
- **Validator errors:** Normalize headings to match [`business-proposal-template.md`](../skills/entrepreneur-persona/assets/business-proposal-template.md) or extend `SECTION_PATTERNS` in `validate_proposal.py`.
