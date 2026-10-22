---
name: example-skill
description: "Run the bundled hello script and print a note filled in from the template. Use when the user asks for an example skill, asks how a skill folder is structured, or runs /example-skill."
---

# example-skill

This skill shows the folder layout this template uses. It does not change any files.

`<skill_dir>` is the directory containing this SKILL.md. In Claude Code that path is `${CLAUDE_SKILL_DIR}`.

## Steps

1. Run the script from this folder. It reads `templates/note.md`, fills in the placeholders, and prints the note. It does not write a file.

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/hello.py
```

If the user gave a name, pass it as one quoted argument:

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/hello.py "Ada"
```

2. Show the script output as-is. If `python3` is missing or the script exits non-zero, say what failed and show `templates/note.md` instead.

3. Tell the user that `templates/note.md` is the source template and was not modified.

4. Tell the user that `/create-skill` creates a new skill, and that this example folder can be deleted when they no longer want it.
