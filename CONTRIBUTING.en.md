# Contributing Guide

[日本語](./CONTRIBUTING.md) | [English](./CONTRIBUTING.en.md)

Corrections, clearer explanations, and beginner-friendly examples are welcome.

## Open an issue

Briefly describe:

- The page or sample involved
- What is unclear or incorrect
- The explanation or behavior you expected

Do not include API keys, passwords, or personal information.

## Open a pull request

1. Keep the change focused on one purpose.
2. Use short language that beginners can understand.
3. When changing Japanese content, check the corresponding English version too.
4. Run these commands from the repository root:

```bash
python3 -m unittest discover -s examples/five-minute-agent -v
python3 scripts/check_markdown_links.py
```

In the pull request, explain what changed, why it changed, and how you verified it.

## Small changes are welcome

Typo fixes and small clarity improvements are useful. For a large change, open an issue first to discuss its goal.
