# AGENTS.md

## About this project

This is a Go project for [describe its purpose].

## Repository map

- `cmd/`: executable applications
- `internal/`: internal packages
- `pkg/`: packages intended for external use
- `go.mod`: module and dependency definitions

Remove entries that do not exist in your repository.

## Working rules

- Change only what the task requires.
- Explain before significantly changing a package's responsibility.
- Do not ignore errors; return them in a form the caller can handle.
- Consider a table-driven regression test when fixing a bug.
- Update `go.mod` and `go.sum` only when dependencies change.
- Never add API keys or passwords to the code.

## Checks

    gofmt -l .
    go vet ./...
    go test ./...

If `gofmt -l .` prints a filename, format the Go files you changed.

## Completion report

- What changed
- Commands run and their results
- Checks that could not be run and why
