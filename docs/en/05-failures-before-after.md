# Common Failures and Improvements (Before / After)

These simplified examples represent failures that often occur in AI-assisted development.

## 1. The scope expanded

### Before

```text
Clean up the login area.
```

The agent changed authentication and dependencies when only a message needed editing.

### After

```text
Improve the guidance shown after a failed login.
Change only LoginForm and its tests.
Do not change the authentication API, dependencies, or design.
```

## 2. The answer invented facts

### Before

```text
Answer using the FAQ.
```

### After

```text
Use only information explicitly stated in the FAQ.
If the answer is missing, return “needs confirmation” and do not guess.
Include the titles of the FAQ entries used.
```

## 3. Tests were assumed to have run

### Before

```text
Test it when you are done.
```

### After

```text
Run npm test and npm run lint.
If a command cannot run, do not claim success; report the command and reason.
```

## 4. A draft was sent automatically

### Before

One tool allowed both drafting and sending email.

### After

Separate drafting from sending and require human approval before delivery.

## 5. The same action ran repeatedly

### Before

The system retried until it succeeded.

### After

Set a retry limit, delay, and escalation condition. Add an idempotency key to write operations.

## 6. `AGENTS.md` was too abstract

### Before

```markdown
- Write high-quality code.
- Follow best practices.
```

### After

```markdown
- Run `go test ./...` after a change.
- Explain the impact before changing a public API.
- Add a regression test for bug fixes.
```

Prefer executable commands and decision criteria over abstract ideals.

## Retrospective template

```text
Expected:
What happened:
Cause:
Constraint or test to add:
```

Keep failed input and turn it into a test case.
