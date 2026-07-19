# OSS Showcase: Real-World `AGENTS.md` Examples

These open-source examples show what real projects put in `AGENTS.md`. File existence and content were verified on GitHub on July 20, 2026. Adapt ideas to your repository instead of copying rules blindly.

| Project | Main language | What you can learn |
| --- | --- | --- |
| [OpenAI Codex](https://github.com/openai/codex/blob/main/AGENTS.md) | Rust | Crate design, review rules, API compatibility, tests, and change-size guidance |
| [GitHub CLI](https://github.com/cli/cli/blob/trunk/AGENTS.md) | Go | Security disclosure, build and test commands, command structure, and architecture |
| [Datadog Stratus Red Team](https://github.com/DataDog/stratus-red-team/blob/main/AGENTS.md) | Go | Feature guidelines, local validation, and explicit prohibitions |
| [LiveKit Swift Client SDK](https://github.com/livekit/client-sdk-swift/blob/main/AGENTS.md) | Swift | Build and test commands, required local services, and SDK architecture |
| [Grafana Tempo Operator](https://github.com/grafana/tempo-operator/blob/main/AGENTS.md) | Go | Operator structure, code generation, local development, and deployment |
| [GraphFrames](https://github.com/graphframes/graphframes/blob/main/AGENTS.md) | Scala | Legacy-code policy, regression prevention, and multi-version testing |

## What to look for

1. Real commands instead of general advice
2. Architecture and change boundaries
3. Project-specific risks and prohibited actions
4. Test-environment and external-service prerequisites
5. Rules for public APIs and legacy areas

The linked files are maintained by their respective projects and may move or change. Inclusion does not imply that a project endorses this guide.
