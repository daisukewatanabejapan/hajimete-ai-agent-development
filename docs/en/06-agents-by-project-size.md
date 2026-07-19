# `AGENTS.md` Templates by Project Size

A longer `AGENTS.md` is not automatically better. Keep only the decisions your project needs.

## Solo project

For one developer, one application, and short development cycles.

- [Open the template](../../examples/en/scales/AGENTS-solo.md)
- Focus on the purpose, test command, and protected areas
- Require confirmation for destructive or external actions

## Small team

For 2–10 people using review and CI.

- [Open the template](../../examples/en/scales/AGENTS-team.md)
- Include ownership, PR, review, CI, and dependency rules
- Identify design decisions that require a person

## Large project or monorepo

For multiple teams, services, or build systems.

- [Open the template](../../examples/en/scales/AGENTS-monorepo.md)
- Keep only global rules at the root
- Put a focused `AGENTS.md` inside each major subtree
- Document checks for the changed area instead of always running everything

| Question | If yes |
| --- | --- |
| Are you the only developer? | Solo template |
| Do you use PR review and CI? | Team template |
| Are there multiple owners or build systems? | Monorepo template |

Begin with the smallest template. Add a rule only when the team repeatedly needs the same explanation.
