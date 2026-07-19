# A Team Development Workflow

Treat AI as a development tool that requires direction and verification, not as an unsupervised team member.

## Basic flow

```text
Write Issue → AI proposes plan → human confirms → AI implements
→ CI → AI self-review → human review → merge
```

## 1. Issue

A person owns the goal, scope, completion criteria, and non-goals. Do not let AI silently decide ambiguous product requirements.

## 2. Plan

For multi-file or design work, ask for a short plan. Review API changes, data migration, permissions, and rollback.

## 3. Implementation

- One purpose per PR
- No unrelated refactoring
- Small, reviewable changes
- No secrets in prompts

## 4. AI self-review

```text
Review this diff. Prioritize correctness, security, compatibility,
and missing tests. Identify the affected file and explain each issue.
```

AI self-review does not replace human review.

## 5. Human review

People should focus on requirement correctness, design decisions, permissions, personal data, and operational impact.

## 6. Feed lessons back

- Repository-wide convention → `AGENTS.md`
- One-time condition → Issue or task prompt
- Mechanically testable rule → lint, tests, or CI
- Complex repeated process → reusable workflow

For the first two weeks, review every AI-generated diff. Track review findings, rework, and test failures, then expand from low-risk tasks.
