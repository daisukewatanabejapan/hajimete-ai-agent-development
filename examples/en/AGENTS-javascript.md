# AGENTS.md

## About this project

This is a JavaScript project for [describe its purpose].

## Repository map

- `src/`: application code
- `test/` or `tests/`: tests
- `public/`: static files
- `package.json`: scripts and dependencies

Change this map to match your repository.

## Working rules

- Change only what the task requires.
- Preserve the project's existing ES Modules or CommonJS convention.
- Confirm whether changed code runs in a browser or Node.js.
- Add a regression test when fixing a bug where practical.
- Update `package-lock.json` only when dependencies change.
- Explain why a new package is needed.
- Never add API keys or passwords to the code.

## Checks

Keep only scripts that exist in `package.json`.

    npm ci
    npm test
    npm run lint
    npm run build

## Completion report

- What changed
- Commands run and their results
- Target runtime: browser or Node.js
- Checks that could not be run and why
