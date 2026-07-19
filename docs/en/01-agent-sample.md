# A Small AI Agent Development Example

In this example, an agent classifies an incoming support message and prepares a reply draft.

The first version does not send anything. AI performs the classification and drafting, and a person reviews the result.

## AI response or AI agent?

A chat response may be enough for a single question. An agent receives a goal, checks available information, uses permitted tools, and verifies the result.

```text
Receive a goal
    ↓
Observe the situation
    ↓
Choose the next action
    ↓
Use a tool
    ↓
Verify the result
    ↓
Finish or ask a person for help
```

This repeated process is the agent loop.

## Goal

Classify a message into one of three categories and create a reply draft:

- `question`: a usage question
- `bug`: a defect report
- `other`: anything else

## Define input and output first

Example input:

```text
Nothing happens when I select Save.
I am using Safari.
```

Example output:

```json
{
  "category": "bug",
  "summary": "The Save action does not respond in Safari",
  "reply_draft": "Thank you for the report. Could you share the time it occurred and your Safari version?",
  "needs_human_review": true
}
```

A fixed output shape makes downstream processing and testing easier.

## Agent logic

Language-neutral pseudocode:

```text
function handleInquiry(inquiry):
    if inquiry is empty:
        return error("The inquiry is empty")

    category = classify(inquiry)
    summary = summarize(inquiry)
    replyDraft = createReply(inquiry, category)

    result = {
        category: category,
        summary: summary,
        reply_draft: replyDraft,
        needs_human_review: true
    }

    if result does not match the required format:
        return error("The output format is invalid")

    return result
```

The agent is not given unlimited freedom:

- Reject empty input
- Limit categories to three values
- Fix the output format
- Do not allow automatic sending
- Validate the result

## Adding tools

Start without external tools. Add one only when it is needed.

| Tool | Purpose | Main caution |
| --- | --- | --- |
| FAQ search | Find previous answers | Avoid outdated answers |
| Customer lookup | Check account details | Restrict data access |
| Ticket creation | Hand work to a person | Prevent duplicates |
| Email sending | Send a reply | Require human approval |

Give every tool the minimum required permission. Separate read tools from write tools.

## First tests

Test at least:

1. A clear question
2. A clear defect report
3. An ambiguous message
4. Empty and unusually long input

Keep failed examples as test cases. When implementing this sample, first display or save results without sending them. Add tools only after the simple version behaves safely.
