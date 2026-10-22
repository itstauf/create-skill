# create-skill

**The TygrLabs template for creating a Claude Code skill.**

This repository is the starting point for a new [Claude Code](https://code.claude.com/docs/en/skills) skill. It contains a skill that walks you through creating another one, a small example you can run, and a scaffold of starter files.

Claude Code loads `create-skill` and `example-skill` from `.claude/skills/`. The scaffold is nested inside `create-skill`, so it is not a skill of its own.

## Quick start

From this repository:

```bash
git clone https://github.com/itstauf/create-skill
cd create-skill
```

See the example skill without starting Claude Code:

```bash
python3 .claude/skills/example-skill/scripts/hello.py
```

That prints a short note. It does not change `.claude/skills/example-skill/templates/note.md`. Pass a name if you want one:

```bash
python3 .claude/skills/example-skill/scripts/hello.py "Ada"
```

Then start Claude Code in this repository and run either command:

- `/example-skill` runs the same script and shows the note.
- `/create-skill` asks for a name, a description, the steps, and whether you need `scripts/` or `templates/`, then adds `.claude/skills/<name>/`. After it finishes, run `/<name>`.

To make a skill by hand instead:

```bash
cp -r .claude/skills/create-skill/scaffold .claude/skills/my-skill-name
```

Open `.claude/skills/my-skill-name/SKILL.md`. In this copy, `name` is already `my-skill-name`. Replace the description, the title, and the steps. If you use a different folder name, set `name` to that folder name. Start Claude Code in this repository and run `/my-skill-name`, or `/<folder-name>` if you chose another name.

## Use it in a repository you already have

`create-skill` is enough on its own, because the scaffold is inside that folder. From the root of the other repository:

```bash
git clone https://github.com/itstauf/create-skill /tmp/create-skill
mkdir -p .claude/skills
cp -r /tmp/create-skill/.claude/skills/create-skill .claude/skills/
```

Copy the example too only if you want it:

```bash
cp -r /tmp/create-skill/.claude/skills/example-skill .claude/skills/
```

Start Claude Code in that repository and run `/create-skill`.

For local Claude Code sessions in other projects on this machine, copy the same folders to `~/.claude/skills/` instead. Cowork and cloud sessions do not load skills from that home directory.

## Requirements

Claude Code. The example script uses Python 3 from the standard library. There is nothing to install with pip.

## Layout

Folder names under `.claude/skills/` are lowercase with hyphens.

```
.claude/skills/
├── create-skill/
│   ├── SKILL.md
│   └── scaffold/
│       ├── SKILL.md
│       ├── scripts/.gitkeep
│       └── templates/.gitkeep
└── example-skill/
    ├── SKILL.md
    ├── scripts/hello.py
    └── templates/note.md
```

`scaffold/` sits inside `create-skill` so it is not loaded as its own skill. `.gitkeep` is an empty file so Git keeps `scripts/` and `templates/` until a real file replaces it.

## SKILL.md

Every skill folder contains a `SKILL.md`. The first line is `---`. Frontmatter holds:

- `name`: the skill name. It matches the folder name.
- `description`: what the skill does and when Claude should use it.

```markdown
---
name: my-skill-name
description: Use when the user asks to ...
---

# My Skill Name

Step-by-step instructions for Claude go here.
```

That block is the scaffold file at `.claude/skills/create-skill/scaffold/SKILL.md`. Quote `description` if the text contains a colon.

## Scripts and templates

Any scripts or templates a skill needs go in that skill's folder, next to its `SKILL.md`. Leave `scripts/` and `templates/` out when the skill does not use them.

## Template repository

GitHub shows **Use this template** after an admin selects **Template repository** in the repository Settings. The clone steps above work either way.
