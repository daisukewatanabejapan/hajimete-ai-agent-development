# AGENTS.md

## About this project

This repository is a beginner-friendly guide to working with AI coding agents.

## Working rules

- Read the relevant files before making changes.
- Make the smallest change needed for the task.
- Do not modify unrelated files or text.
- Use short, clear language that beginners can understand.
- Explain specialist terms the first time you use them.
- Do not present unverified assumptions as facts.
- Never add API keys, passwords, or personal data.

## Verification

Run the sample tests and local Markdown link check from the repository root:

```bash
python3 -m unittest discover -s examples/five-minute-agent -v
python3 scripts/check_markdown_links.py
```

After a change, check that:

1. The automated tests and Markdown link check pass
2. Examples can be copied as written
3. The README and `AGENTS.md` do not contradict each other
4. Product-specific explanations link to official information

## Completion report

Briefly report:

- What changed
- How it was verified
- Anything that remains unverified or unresolved
