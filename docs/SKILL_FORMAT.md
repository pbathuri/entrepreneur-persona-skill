# Skill format (this repository)

The installable unit is **`skills/entrepreneur-persona/`**. It follows the usual Anthropic-style skill layout:

| Piece | Role |
|-------|------|
| `SKILL.md` | YAML frontmatter (`name`, `description`) + Markdown instructions |
| `references/` | Progressive disclosure — frameworks, rubrics, question bank, vignettes |
| `assets/` | Copy-paste templates (proposal, pitch script, refinement canvas) |
| `scripts/` | Optional tooling (`validate_proposal.py`, stdlib only) |

## Conventions

- **`name` in frontmatter** must be **kebab-case** and match the folder name `entrepreneur-persona`.  
- **No `README.md` inside the skill folder** — repo-level and `docs/` carry human-facing documentation so the skill tree stays portable.  
- **Description** (under 1024 characters): what the skill does, when to use it, and trigger phrases.  
- **Keep `SKILL.md` under ~5000 words**; put long reference material in `references/`.

## Official references

For platform-specific packaging and discovery paths, use the latest **Anthropic Claude / Claude Code** documentation for skills and plugins.

## Plugin metadata

This repo also ships [`.claude-plugin/`](../.claude-plugin/) (`plugin.json`, `marketplace.json`, `manifest.json`) so Claude Code can register the marketplace and install the plugin by name.
