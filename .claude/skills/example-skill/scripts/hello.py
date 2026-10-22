#!/usr/bin/env python3
"""Print a note filled in from templates/note.md. Does not write any files."""

import sys
from datetime import date
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
TEMPLATE = SKILL_DIR / "templates" / "note.md"


def main():
    if not TEMPLATE.is_file():
        sys.stderr.write(f"Missing template: {TEMPLATE}\n")
        return 1

    name = sys.argv[1] if len(sys.argv) > 1 else "there"
    text = TEMPLATE.read_text(encoding="utf-8")
    filled = text.replace("{{when}}", date.today().isoformat()).replace("{{name}}", name)
    sys.stdout.write(filled)
    if not filled.endswith("\n"):
        sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
