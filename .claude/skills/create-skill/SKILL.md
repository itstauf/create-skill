---
name: create-skill
description: "Walk the user through adding a new Claude Code skill under .claude/skills. Use when the user asks to create a skill, add a skill, scaffold a skill, or runs /create-skill."
---

# create-skill

Create one new skill in the current project. The starter files are in `${CLAUDE_SKILL_DIR}/scaffold`.

## Rules

- Put the skill at `${CLAUDE_PROJECT_DIR}/.claude/skills/<name>/`.
- `<name>` uses only lowercase letters, numbers, and hyphens, and is 64 characters or fewer. It must match the `name` field in `SKILL.md`.
- Do not use a name that contains `claude` or `anthropic`.
- Do not use `create-skill` or `example-skill`.
- Do not overwrite an existing skill folder unless the user says to.
- Keep `scripts/` or `templates/` only when the new skill uses them.

## Steps

1. If the user has not already given them, ask for:
   - the skill name
   - a description of what the skill does and when to use it
   - the steps Claude should follow
   - whether it needs `scripts/`, `templates/`, both, or neither

2. Check the name against the rules above. If `${CLAUDE_PROJECT_DIR}/.claude/skills/<name>` already exists, stop and ask before changing it.

3. Copy `${CLAUDE_SKILL_DIR}/scaffold` so the new `SKILL.md` lands at `${CLAUDE_PROJECT_DIR}/.claude/skills/<name>/SKILL.md`. Do not leave a nested `scaffold/` folder inside the new skill.

4. Replace that `SKILL.md`. The first line must be `---`. Quote `description` when it contains a colon.

```markdown
---
name: <name>
description: Use when the user asks to ...
---

# <Title>

<steps>
```

5. If the skill does not need scripts, delete `scripts/` (including `.gitkeep`). If it does, replace `scripts/.gitkeep` with the real script and name that script in the steps. Do the same for `templates/` and `templates/.gitkeep`.

6. Show the new folder tree and the finished `SKILL.md`.

7. If you added a script, run it once. If it fails, say what failed.

8. Tell the user to run `/<name>` in Claude Code from this project, or to ask in a sentence that matches the description.
