# AGENTS.md

## Repository

This monorepo contains multiple services and shared libraries.

## Global rules

- Identify the target and its dependents before changing code.
- Do not change another team's area without approval.
- Do not edit generated files manually.
- Check consumers when changing a shared library.

## Areas

- `apps/web/`: web team; read its nested `AGENTS.md`
- `services/api/`: API team; read its nested `AGENTS.md`
- `packages/`: shared code; preserve backward compatibility

## Verification

- Test the changed area first
- Test affected consumers after a shared change
- Report whether repository-wide checks are still needed

## Completion report

- Changed areas and owners
- Affected services
- Checks run and checks still pending
