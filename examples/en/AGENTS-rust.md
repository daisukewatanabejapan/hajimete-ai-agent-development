# AGENTS.md

## About this project

This is a Rust project for [describe its purpose].

## Repository map

- `src/`: application or library code
- `tests/`: integration tests
- `examples/`: usage examples
- `Cargo.toml`: package and dependency definitions

Change this map to match your repository.

## Working rules

- Change only what the task requires.
- When adding `unsafe`, explain why it is needed and state its safety invariants.
- Explain the user impact of public API changes.
- Add a regression test when fixing a bug where practical.
- Follow the repository's existing policy for `Cargo.lock`.
- Never add API keys or passwords to the code.

## Checks

    cargo fmt --check
    cargo clippy --all-targets --all-features -- -D warnings
    cargo test --all-features

## Completion report

- What changed
- Commands run and their results
- Any impact on `unsafe` code or public APIs
- Checks that could not be run and why
