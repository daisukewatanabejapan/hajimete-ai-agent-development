# Your First AI Agent Development Guide

[日本語](./README.md) | [English](./README.en.md)

> **Learn safe, practical AI agent development with Codex and AGENTS.md—in 10 minutes.**

This small, practical guide is not about handing everything over to AI. It is about learning how to build software with AI safely and confidently.

You do not need advanced configuration or specialist knowledge. Start with one `AGENTS.md` file, learn how to describe a task, and check what the AI changed.

## Run something in five minutes

No API key or external package is required. Run a tiny agent that classifies a support request and creates a safe reply draft.

It is a deterministic local example for learning a safe control loop; it does not call a generative AI model.

```bash
cd examples/five-minute-agent
python3 agent.py
python3 -m unittest -v
```

See [Five-Minute Agent](./examples/five-minute-agent/README.en.md) for the walkthrough.

![AI agent development demo](./assets/agent-development-demo.gif)

## Who this guide is for

- You are using an AI coding agent for the first time
- An AI changed more code than you expected
- You do not know what to write in `AGENTS.md`
- You want to use AI safely in a personal project or small team

## Get started in 10 minutes

### 1. Copy `AGENTS.md`

Copy [`AGENTS.en.md`](./AGENTS.en.md) to the root of your repository and rename it to `AGENTS.md`.

### 2. Change only three things

Adapt these sections to your project:

1. About this project
2. Test commands
3. Things the agent must not change

If your project has no tests yet, say so. Do not invent a command that does not work.

### 3. Ask for one small task

For your first task, choose something you can easily review, such as fixing a typo or adding one test.

```text
Goal:
Fix the typo in the README.

Scope:
Change README.md only.

Done when:
The typo is fixed and the meaning of the surrounding text is unchanged.

Do not:
Change the structure or design.
```

### 4. Review the result

Do not rely only on the agent saying that it finished. Check:

- Were only the expected files changed?
- Are there unrelated changes?
- Did the tests pass?
- Were any passwords or tokens added?

## Remember four fields

| Field | What to write |
| --- | --- |
| Goal | What you want to achieve |
| Scope | What the agent may change |
| Done when | How you will know it is complete |
| Do not | What must remain unchanged |

You can copy [`examples/en/REQUEST_TEMPLATE.md`](./examples/en/REQUEST_TEMPLATE.md) when writing a task.

## Learn a little more

After your first task, continue with these three short chapters:

1. [A small AI agent development example](./docs/en/01-agent-sample.md)
2. [Practical prompt design examples](./docs/en/02-prompt-design.md)
3. [How to think about system design](./docs/en/03-system-design.md)

They explain fundamentals that do not depend on a specific model or framework. No API key is required.

### Practical guides

4. [AI agent design patterns](./docs/en/04-design-patterns.md)
5. [Common failures and improvements (Before / After)](./docs/en/05-failures-before-after.md)
6. [`AGENTS.md` templates by project size](./docs/en/06-agents-by-project-size.md)
7. [A team development workflow](./docs/en/07-team-workflow.md)
8. [A catalog of prompts for AI agents](./docs/en/08-prompt-catalog.md)

### See the whole picture

9. [AI agent architecture at a glance](./docs/en/09-architecture.md)
10. [FAQ: common beginner questions](./docs/en/10-faq.md)
11. [AI agent development checklist](./docs/en/11-checklist.md)
12. [OSS Showcase: real-world `AGENTS.md` examples](./docs/en/12-showcase.md)

## What is `AGENTS.md`?

`AGENTS.md` tells an AI agent how work should be done in a repository. It can describe the project, commands, test procedures, and important restrictions.

Put durable project rules in this file instead of repeating them in every task. Keep one-time instructions in the task itself.

Choose an example to get started:

- [`AGENTS-minimal.md`](./examples/en/AGENTS-minimal.md): minimum version
- [`AGENTS-java.md`](./examples/en/AGENTS-java.md): Java project
- [`AGENTS-go.md`](./examples/en/AGENTS-go.md): Go project
- [`AGENTS-rust.md`](./examples/en/AGENTS-rust.md): Rust project
- [`AGENTS-javascript.md`](./examples/en/AGENTS-javascript.md): JavaScript project
- [`AGENTS-python.md`](./examples/en/AGENTS-python.md): Python project
- [`AGENTS-node.md`](./examples/en/AGENTS-node.md): existing Node.js example

See OpenAI's official [`AGENTS.md` guide](https://developers.openai.com/codex/guides/agents-md) for product details.

## Plan larger changes

Create a short plan before work that changes several files or requires design decisions. [`PLANS.en.md`](./PLANS.en.md) is a simple template.

`PLANS.md` is not a required Codex configuration file. It is a convention used by this guide to organize larger work.

## Five safety rules

1. Start with a small task
2. State the scope and completion criteria
3. Review destructive or hard-to-reverse actions yourself
4. Do not provide API keys, passwords, or personal data
5. Have a person review the diff and test results

## Do I need `config.toml`?

Not at first.

`AGENTS.md` describes how work should be done in a project. `.codex/config.toml` configures Codex itself. Learn it later when you need to adjust models, approvals, sandboxing, or MCP.

When you do, check OpenAI's official [`config.toml` reference](https://developers.openai.com/codex/config-reference) instead of copying an old example.

## Common mistakes

### Asking the agent to “make it better”

The scope and definition of success are unclear. Be specific:

```text
Rewrite the login error so a first-time user knows what to do next.
Change only the login screen and its tests. Do not change authentication behavior.
```

### Omitting test instructions

The agent may not guess the right checks. Put real, working commands in `AGENTS.md`.

### Asking for everything at once

Research, implementation, refactoring, and documentation are easier to review when divided into small completion units.

## Scope of this guide

This guide begins with AI-assisted software development using tools such as Codex, then introduces the fundamentals of designing a small AI agent. It does not teach you how to train an AI model.

## Contributing

Corrections, clearer explanations, and beginner-friendly examples are welcome. See [`CONTRIBUTING.en.md`](./CONTRIBUTING.en.md) for the steps.

## License

Released under the [MIT License](./LICENSE). You may copy and adapt these templates for your own projects.
