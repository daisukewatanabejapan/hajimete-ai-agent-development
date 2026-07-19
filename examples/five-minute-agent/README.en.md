# Five-Minute Agent

[日本語](./README.md) | [English](./README.en.md)

This tiny sample classifies a support request, drafts a reply, and stops for human review.

## 1. Requirements

- Python 3.9 or later
- A terminal

No API key, external package, or network connection is required.

## 2. Run it

From the repository root:

```bash
cd examples/five-minute-agent
python3 agent.py
```

Try your own input:

```bash
python3 agent.py --text "Nothing happens when I click Save"
python3 agent.py --text "How do I change my password?"
```

## 3. Test it

```bash
python3 -m unittest -v
```

## Example output

```json
{
  "category": "bug",
  "summary": "Nothing happens when I click Save",
  "reply_draft": "Thank you for the report. Please share your environment and reproduction steps.",
  "needs_human_review": true,
  "trace": [
    "input_validated",
    "request_classified",
    "reply_drafted",
    "output_validated"
  ]
}
```

## What it teaches

```text
Input → validation → classification → draft → validation → human review
```

- Reject empty and oversized input
- Limit output to three categories
- Record processing steps in `trace`
- Never send the reply automatically
- Test both success and failure cases

## Is this generative AI?

This first sample uses deterministic local rules for classification and drafting. It does not call a generative model.

That is intentional: everyone can learn and test the safety controls around a model before dealing with API setup. In a production version, you can replace `classify()` and `draft_reply()` with model calls while keeping input validation, output validation, human approval, and tests.

## Try next

1. Add a new request to `test_agent.py`
2. Change one classification keyword
3. Confirm that a test fails
4. Fix the behavior and rerun the tests

Connect a model only after you understand the local version. Never put an API key in code or Git.
