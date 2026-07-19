# Prompt Catalog for AI Agents

Replace text in `[]` with details from your project.

## 1. Understand a code path

```text
Trace how [feature] works. Identify the entry point, main functions,
data store, and related tests. Do not make changes yet.
```

## 2. Fix a small bug

```text
Fix [symptom] reproduced by [steps]. Limit changes to [scope].
Explain the cause and add a regression test.
```

## 3. Add tests

```text
Add tests for [target] without changing existing behavior.
Cover the normal case, boundaries, and a representative failure.
Test user-visible behavior rather than implementation details.
```

## 4. Refactor safely

```text
Improve the readability of [target]. Do not change observable behavior.
Confirm that the same tests pass before and after the change.
```

## 5. Review a diff

```text
Review this diff. Prioritize serious bugs, security, compatibility,
data loss, and missing tests. List concrete findings before a summary.
```

## 6. Create a plan only

```text
Plan how to achieve [goal]. Do not implement yet.
Include likely files, steps, tests, risks, and rollback.
Separate assumptions that require confirmation.
```

## 7. Update documentation

```text
Update user documentation for [code change].
Do not add behavior that cannot be verified from the code.
Look for explanations that are now outdated.
```

## 8. Evaluate a dependency

```text
Evaluate whether [library] is needed. Compare standard features and
existing dependencies, maintenance, size, and license. Do not add it yet.
```

## 9. Investigate an error

```text
Investigate this error: [error]. Report reproduction conditions, root
cause, the smallest fix, and verification. Label unsupported ideas as hypotheses.
```

## 10. Final check

```text
Before reporting completion, reread the diff. Check for out-of-scope
changes, debug code, secrets, and missing tests. Report commands and results.
```

Start with “understand” or “plan only,” let a person confirm the direction, then implement. Finish with the final-check prompt.
