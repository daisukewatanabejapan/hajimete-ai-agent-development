# AI Agent Architecture at a Glance

An AI agent is not just a model. It combines instructions, input, tools, validation, human approval, and operational records.

```mermaid
flowchart TB
    U["User / Issue"] --> T["Goal, scope, done criteria"]
    A["AGENTS.md<br/>Durable repository rules"] --> C
    T --> C["Build context"]
    K["Code, docs, search results"] --> C
    C --> P["Plan"]
    P --> M["AI model chooses the next action"]
    M --> R{"Tool needed?"}
    R -->|No| O["Answer or proposed change"]
    R -->|Yes| G["Least-privilege tool"]
    G --> V["Validate result with code"]
    V --> M
    O --> Q["Tests, lint, diff review"]
    Q --> H{"Human approval required?"}
    H -->|Yes| X["Human review"]
    H -->|No| D["Done"]
    X -->|Approve| D
    X -->|Revise| P
    C -.-> L["Logs, evals, monitoring"]
    G -.-> L
    Q -.-> L
```

| Element | Responsibility |
| --- | --- |
| Task prompt | One-time goal, scope, and completion criteria |
| `AGENTS.md` | Durable repository conventions and commands |
| Context | Code, documents, and results used for decisions |
| AI model | Chooses an answer or next action |
| Tools | Search, test, and modify files |
| Validation | Check formats, tests, lint, and diffs |
| Human approval | Protect sending, publishing, deletion, and other boundaries |
| Logs and evals | Investigate failures and improve the system |

For a first version, stop at `task → AI draft → tests → human review`. Add external sending and automatic updates only after you have tests and operational evidence.
