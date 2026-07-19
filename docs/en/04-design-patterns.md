# AI Agent Design Patterns

A design pattern is a reusable answer to a common problem. Combine only the patterns your project needs.

## 1. Draft → Human Review

AI prepares a draft; a person makes the final decision.

```text
Input → AI draft → automatic validation → human approval → action
```

Use it first for email, public content, and code changes where mistakes matter.

## 2. Read Before Write

Inspect the current state with read-only tools. Put updates behind a separate tool and approval step.

```text
Search or read → proposed change → approval → update
```

This is useful for databases, issues, and cloud configuration.

## 3. Router

Classify input and send it to a focused process.

```text
Request → classification → question / bug / other
```

Keep the destinations limited and define where uncertain input goes.

## 4. Plan → Execute → Verify

Separate planning, small execution steps, and verification.

```text
Goal → plan → small change → test → next change
```

Use it for migrations and multi-file work. Update the plan when new facts appear.

## 5. Bounded Retry

Define the retry count and stopping condition.

```text
Attempt → failure → inspect cause → retry at most twice → escalate
```

This prevents loops, runaway cost, and duplicate updates. Write operations also need an idempotency mechanism.

## 6. Evidence First

Return supporting evidence with every answer or decision.

```text
Search → select evidence → answer + sources → human review
```

Use it for internal knowledge, policy, and technical research. Do not guess when evidence is missing.

## Choosing a pattern

| Situation | Start with |
| --- | --- |
| Sending or publishing externally | Draft → Human Review |
| Updating data | Read Before Write |
| Different request types | Router |
| Complex work | Plan → Execute → Verify |
| Unreliable external service | Bounded Retry |
| Accuracy and accountability matter | Evidence First |

A good first combination is Draft → Human Review plus Plan → Execute → Verify.
