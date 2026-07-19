"""Check that relative links in repository Markdown files point to existing files."""

import re
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parent.parent
LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def main() -> None:
    broken = []
    markdown_files = sorted(ROOT.rglob("*.md"))

    for markdown_file in markdown_files:
        content = markdown_file.read_text(encoding="utf-8")
        for target in LINK_PATTERN.findall(content):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path_text = unquote(target.split("#", 1)[0])
            if not path_text:
                continue
            resolved = (markdown_file.parent / path_text).resolve()
            if not resolved.exists():
                broken.append(f"{markdown_file.relative_to(ROOT)}: {target}")

    if broken:
        raise SystemExit("Broken local Markdown links:\n" + "\n".join(broken))

    print(f"All local Markdown links resolve ({len(markdown_files)} files).")


if __name__ == "__main__":
    main()
