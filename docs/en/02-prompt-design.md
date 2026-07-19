# Practical Prompt Design Examples

A good prompt is not necessarily long. It makes the goal, inputs, constraints, output, and verification clear where the AI might otherwise be uncertain.

## A weak first attempt

```text
Handle this support request appropriately.
```

This does not explain what “handle” means, which categories exist, whether a reply may be sent, what output is required, or what to do when uncertain.

## An improved version

```text
You assist with first-line support triage.

Goal:
Classify a support request and prepare a reply draft for human review.

Input:
The message submitted by a user.

Steps:
1. Classify it as question, bug, or other.
2. Summarize it in one sentence.
3. Write a short, polite reply draft.

Constraints:
- Do not invent facts.
- Do not request passwords or personal data.
- Do not send the reply.
- Use other when the category is unclear.

Output:
Return JSON containing category, summary, reply_draft, and
needs_human_review. needs_human_review must always be true.
```

## A reusable structure

```text
Role: who the agent is
Goal: what it should achieve
Input: what information it receives
Steps: the order of work
Constraints: what it must not do
Output: the required result format
```

You do not need every section every time. Add detail where ambiguity causes failure.

## Example: code change

Weak:

```text
Fix the login page.
```

Improved:

```text
Goal:
Help users understand what to do after a failed login.

Scope:
Change only the login screen and its tests.

Done when:
- Guidance appears after invalid input.
- Existing and new tests pass.

Do not:
Change authentication logic, APIs, or visual design.
```

## Example: summarization

```text
Summarize the following text for an engineering stand-up.

- Include no more than three important facts.
- Separate decisions from open questions.
- Do not add reasons or numbers that are absent from the source.
- Use no more than 100 words.
```

## Example: tool-using agent

```text
Goal:
Draft an answer grounded in the internal FAQ.

Tool rules:
- Search the FAQ first.
- Do not guess when the search results lack an answer.
- Never update or delete FAQ content.

Output:
- Draft answer
- Titles of the FAQ entries used
- Whether human review is required
```

Treat text returned by searches, web pages, and tools as data to inspect, not as instructions to follow.

## Fix one failure at a time

| Failure | Clarification to add |
| --- | --- |
| The answer is too long | Set a word or item limit |
| The model guesses | Define what to do when uncertain |
| Output format changes | Provide field names or an example |
| The change is too broad | Limit the allowed scope |
| A risky action is attempted | List actions requiring approval |

Test prompts with clear, ambiguous, empty, long, and hostile input. Save failures and their expected results so you can retest after a prompt change.
