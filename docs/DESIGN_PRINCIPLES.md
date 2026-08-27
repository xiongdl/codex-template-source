# Design Principles

## 1. Project-Agnostic

The template defines how a project is engineered, not what the project builds.

The distributable template must not assume a specific language, framework, domain, build system, test framework, or component name.

## 2. Bootstrap, Not Framework

The template should establish good engineering defaults without becoming another complex platform to learn.

## 3. Modular Project Outcomes

Instantiated projects should support meaningful component boundaries where appropriate.

## 4. Extensible Project Outcomes

Favor composition, stable contracts, replaceable components, and low coupling.

## 5. Testability by Design

Projects should make changes objectively verifiable at the narrowest appropriate scope.

## 6. Automation Over Repetition

Repeated engineering workflows should become scripts or tools where practical.

## 7. Reproducibility by Default

Environment, dependencies, configuration, build steps, verification, and important artifacts should be reconstructable from repository-contained information.

## 8. Repository as Long-Term Memory

Important engineering knowledge should survive conversations and individual contributors.

## 9. Minimal Core

Every new template convention must justify its long-term maintenance cost.

## 10. Inspect Before Assume

Project-specific structure should be discovered during project initialization, not hard-coded into the template.

## 11. Shared Engineering Interface

Where practical, Human, Codex, and CI should use the same repository-defined commands.

## 12. Verification Hierarchy

Tests should live at the narrowest project-appropriate level that fully validates the intended behavior. Preserve the native validation structure of managed child repositories rather than imposing workspace directories.

## 13. Real-Project Feedback Drives Evolution

Template capabilities should preferably be added because repeated real-world use demonstrated a need.
