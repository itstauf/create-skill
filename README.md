# create-skill

A public template for TygrLabs team members to create skills for [Claude Code](https://claude.com/claude-code).

This repo is the standard template everyone at TygrLabs uses when building a new skill.

## Structure

Each skill lives in its own folder under `.claude/skills/`. Folder names are lowercase with hyphens.

```
.claude/
└── skills/
    └── my-skill-name/
        ├── SKILL.md
        ├── scripts/      # optional
        └── templates/    # optional
```

## SKILL.md

Every skill folder contains a `SKILL.md` with:

- **name** — the skill's name (matches the folder name)
- **description** — when Claude should use the skill
- **instructions** — what Claude should do when the skill is used

```markdown
---
name: my-skill-name
description: Use when the user asks to ...
---

# My Skill Name

Step-by-step instructions for Claude go here.
```

## Scripts and templates

Any scripts or templates a skill needs go in the same folder as its `SKILL.md`.
