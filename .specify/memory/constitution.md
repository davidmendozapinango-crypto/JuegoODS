<!--
SYNC IMPACT REPORT
Version change: 0.0.0 → 1.0.0
Modified principles: all placeholders replaced with concrete principles
Added sections: Core Principles (I-V), Technology & Constraints, Development Workflow, Governance
Removed sections: none
Templates requiring updates:
  - .specify/templates/plan-template.md: Constitution Check gate should reference principles I-V
  - .specify/templates/spec-template.md: ✅ aligns with quality/test requirements
  - .specify/templates/tasks-template.md: ✅ already includes testing/security/documentation tasks
  - .specify/templates/commands/*.md: no files present, nothing to update
Follow-up TODOs:
  - RATIFICATION_DATE is marked TODO pending team approval.
-->

# JuegoODS Constitution

## Core Principles

### I. Secure Data Handling
All user input MUST be validated before processing. The recursive access-key validator MUST be implemented exactly as specified in the project requirements. Sensitive values such as raw passwords MUST NOT be stored in binary files or logs; only validated, non-sensitive player profile data may persist in `JUGADORES.bin`. Binary file writes MUST use append-safe operations to prevent accidental data loss or corruption.

**Rationale**: The project explicitly requires recursive validation and binary persistence; secure handling prevents data corruption and protects player information.

### II. Modular Maintainability
Code MUST be organized into single-responsibility modules (e.g., `auth`, `core`, `persistence`, `reports`, `ui`, `ods`). Logic MUST NOT be duplicated across modules; reusable helpers for validation, rendering, and persistence MUST be centralized. The Pygame graphical layer MUST remain decoupled from game rules and data persistence.

**Rationale**: The five project challenges map naturally to independent modules. Clear separation simplifies testing, debugging, and future enhancements such as replacing the UI or storage layer.

### III. Quality Through Testing
Every non-trivial function MUST have at least one unit test. Tests MUST be executed before any commit, and all failing tests MUST be fixed before merging changes. Integration tests MUST cover binary file read/write cycles and the full game flow from login to winner detection.

**Rationale**: Reliable tombola mechanics, recursive validation, and report generation depend on verifiable behavior; tests catch regressions in randomization, persistence, and scoring.

### IV. Data Integrity and Persistence
`JUGADORES.bin` and `JUEGOS.bin` MUST use fixed, documented record structures. File operations MUST explicitly manage `seek()` and `tell()` to avoid overwriting existing records. Data MUST be validated both on write and on read; corrupted records MUST be reported gracefully without crashing the application.

**Rationale**: Binary persistence is a mandatory requirement. Fixed schemas and careful pointer management ensure that player history and game logs remain recoverable across sessions.

### V. Spanish-Language User Experience
All text rendered in the Pygame interface MUST be in Spanish, including menus, labels, error messages, slogans, and winner announcements. Educational content MUST be clear, culturally appropriate, and aligned with the active Sustainable Development Goal theme. A centralized message catalog SHOULD be used to enforce terminology consistency.

**Rationale**: The project documentation explicitly requires the graphical interface to be in Spanish, and the educational purpose depends on clear, goal-relevant messaging.

## Technology & Constraints

- **Programming Language**: Python 3.x.
- **Graphics Library**: Pygame for the graphical user interface.
- **Persistence**: Binary files (`JUGADORES.bin`, `JUEGOS.bin`) for data storage.
- **Card Dimensions**: N×N where N is odd and 5 ≤ N ≤ 15.
- **Number Range**: 1 to N×N, unique within each card and each tombola draw.
- **Validation**: Access-key validation MUST be implemented recursively.
- **Language**: All on-screen text MUST be in Spanish.
- **Version Control**: Git with meaningful, atomic commits.

## Development Workflow

1. **Plan First**: Every feature or fix MUST start with a clear specification or task breakdown aligned with the five project challenges.
2. **Implement in Modules**: Changes MUST stay within the module that owns the responsibility; cross-module changes require updated interfaces and tests.
3. **Test Continuously**: Write or update tests before or alongside implementation. No commit may leave the test suite failing.
4. **Review for Quality**: Before considering a task complete, verify that the code is readable, adequately commented only when necessary, and free of debug prints or hardcoded secrets.
5. **Update Documentation**: Changes to data formats, workflows, or UI text MUST be reflected in the corresponding document under `docs/`.
6. **Validate the UI**: Run the Pygame application to confirm Spanish text renders correctly and the active SDG theme is visible.

## Governance

- **Authority**: This constitution supersedes ad-hoc conventions. All design and implementation decisions MUST align with its principles.
- **Amendments**: Any change to this constitution MUST be documented in the Sync Impact Report, include a version bump rationale, and receive explicit team approval.
- **Versioning**: Follow semantic versioning. MAJOR for incompatible governance changes or removed principles; MINOR for new principles or materially expanded guidance; PATCH for wording clarifications, typos, or non-semantic refinements.
- **Compliance Review**: Every implementation phase MUST include a constitution check verifying security, modularity, testing, data integrity, and Spanish-language UI compliance.

**Version**: 1.0.0 | **Ratified**: TODO(RATIFICATION_DATE): pending team approval | **Last Amended**: 2026-06-28
