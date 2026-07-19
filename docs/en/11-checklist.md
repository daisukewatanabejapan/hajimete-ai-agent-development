# AI Agent Development Checklist

Not every item must apply. Record why an item is not relevant.

## Goal and scope

- [ ] The goal fits in one sentence
- [ ] AI responsibilities and non-responsibilities are separate
- [ ] Completion criteria are observable or testable
- [ ] The allowed change scope is clear

## Input and output

- [ ] Required input and missing-input behavior are defined
- [ ] External input length, format, and required fields are validated
- [ ] Output shape and allowed values are defined
- [ ] The agent does not guess without evidence

## Tools and permissions

- [ ] Every tool has minimum required permission
- [ ] Reading and writing are separate
- [ ] Sending, deletion, purchasing, and publishing require approval
- [ ] Retry limits and duplicate prevention are defined

## Security and privacy

- [ ] Secrets never enter prompts, code, or logs
- [ ] Personal data is limited to what is necessary
- [ ] Tool and web output is treated as data, not instructions
- [ ] Data leaving the system is reviewed

## Quality

- [ ] Normal, boundary, and failure cases are tested
- [ ] Previous failures are regression tests
- [ ] Real lint, test, and build commands are documented
- [ ] A person reviews the diff, not only the completion message

## Operations

- [ ] Runs, tools, results, approvals, and errors are recorded
- [ ] Failures stop safely or escalate to a person
- [ ] Cost, duration, and success rate can be observed
- [ ] Someone owns rule and test updates

## Before publishing

- [ ] README and usage examples exist
- [ ] Secrets and personal data were checked again
- [ ] Project and dependency licenses were reviewed
- [ ] A person completed final review
