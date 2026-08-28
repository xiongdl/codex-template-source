# Project Automation

Recommended project-level interface:

Inspection and validation commands are `status` and `verify`. `status` is non-destructive and reports current capability honestly; `verify` checks only the supported baseline.

Executable lifecycle commands are `setup`, `build`, `test`, and `clean`. Enable them incrementally when the project's actual toolchains and environments are known. A command may initially report `NOT_IMPLEMENTED` or `UNAVAILABLE`.

The instantiated project defines what these operations mean.

Human, Codex, and CI should prefer the same entry points where practical.

Keep this entry point as a thin workspace orchestrator. Child-repository-native build, test, and generation implementations remain in the child repository; workspace composition and cross-repository checks belong here when needed.

Do not add a command merely because a deterministic procedure could be automated. Codex may surface the opportunity, but a repository change requires explicit Engineering Task scope.
