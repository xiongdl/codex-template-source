# Project Automation

Recommended project-level interface:

Inspection and validation commands are `status` and `verify`. `status` is non-destructive and reports current capability honestly; `verify` checks only the supported baseline.

Executable lifecycle commands are `setup`, `build`, `test`, and `clean`. Enable them incrementally when the project's actual toolchains and environments are known. A command may initially report `NOT_IMPLEMENTED` or `UNAVAILABLE`.

The instantiated project defines what these operations mean.

Human, Codex, and CI should prefer the same entry points where practical.
