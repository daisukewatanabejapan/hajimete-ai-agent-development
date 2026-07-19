# FAQ: Common Beginner Questions

## How is an agent different from chat AI?

Chat AI mainly returns an answer. An agent works toward a goal by inspecting information, using permitted tools, and verifying results.

## Do I need `config.toml` at the beginning?

No. Start with `AGENTS.md` and a small task. Configure Codex later when you need to change its behavior.

## Where should `AGENTS.md` live?

Usually at the repository root. In a monorepo, add focused files inside subtrees that need different rules.

## What should it contain?

Start with the project purpose, repository map, working test commands, protected areas, and completion-report format.

## Is a longer file better?

No. Prefer concrete decisions and executable commands over abstract ideals.

## Why does AI change unrelated files?

State the allowed scope and non-goals in the task. Add “keep the diff minimal” and “avoid unrelated formatting” to `AGENTS.md`.

## What if the project has no tests?

Do not pretend tests exist. Document available build, lint, or manual checks, then add tests around important behavior.

## May I give the agent an API key?

Never put one directly in a prompt or repository. Use environment variables or secret management and keep it out of logs.

## Can I merge AI changes directly?

At first, always have a person review the diff and test results. Permissions, personal data, database changes, and public APIs need human judgment.

## Should I make the prompt longer after a failure?

Identify one cause first. Clarify scope, output format, uncertain behavior, or verification. Keep the failed input as a test case.

## How much should I automate?

Begin with low-impact, reversible work. Keep human approval for sending, deletion, purchasing, and publishing.
