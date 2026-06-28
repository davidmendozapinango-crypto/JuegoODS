# Implementation Plan: Initial Project Features

**Branch**: `001-initial-project-features` | **Date**: 2026-06-28 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/001-initial-project-features/spec.md`

## Summary

Implement the Minimum Viable Product (MVP) of the SDG-themed Tombola desktop game. The work covers player registration and authentication (with recursive access-key validation), full player profile CRUD, themed N×N card generation for all 17 ODS, automated tombola gameplay with configurable draw speed, winner detection based on a project-defined figure pattern, binary persistence of players and games, report generation exported as plain text files, and a Spanish-language Pygame user interface integrated with SDG educational content.

The technical approach is a modular Python desktop application using Pygame for the graphical layer and binary files for data persistence. Each project challenge maps to a dedicated module to keep the UI decoupled from game rules and storage.

## Technical Context

**Language/Version**: Python 3.11+

**Primary Dependencies**: Pygame 2.5+ for the graphical interface; pytest for testing.

**Storage**: Binary files (`JUGADORES.bin`, `JUEGOS.bin`) for local data persistence.

**Testing**: pytest with unit, integration, and end-to-end test modules.

**Target Platform**: Desktop (Windows, Linux, macOS).

**Project Type**: desktop-app

**Performance Goals**:
- UI rendering at 60 frames per second during gameplay.
- Access-key validation feedback in under 1 second.
- Card generation for any allowed dimension in under 2 seconds.
- Profile updates persisted and reflected within 1 second.

**Constraints**:
- Card dimensions must be odd integers where 5 ≤ N ≤ 15.
- Access-key validation MUST be implemented recursively.
- All on-screen text MUST be in Spanish.
- Reports MUST be exported as UTF-8 plain text files with aligned columns.
- Binary file writes MUST be append-safe to avoid data loss.

**Scale/Scope**:
- Single-player local application.
- 17 selectable ODS themes, each with color, slogan, and figure pattern.
- Two cards per game (main and complement).
- Supports multiple consecutive rounds without re-authentication.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Compliance Status | Notes |
|---|---|---|
| I. Secure Data Handling | Pass | Access-key validation recursive; no plaintext secrets stored; append-safe binary writes planned. |
| II. Modular Maintainability | Pass | Modules: auth, core, persistence, reports, ui, ods. UI decoupled from rules and storage. |
| III. Quality Through Testing | Pass | pytest unit, integration, and end-to-end tests planned for each module. |
| IV. Data Integrity and Persistence | Pass | Fixed binary record schemas; explicit seek/tell management; read validation and graceful corruption handling. |
| V. Spanish-Language User Experience | Pass | Centralized Spanish message catalog; all Pygame text in Spanish. |

No constitution violations identified. No complexity tracking required.

## Project Structure

### Documentation (this feature)

```text
specs/001-initial-project-features/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)

```text
src/
├── __init__.py
├── main.py              # Application entry point
├── config.py            # Constants, paths, ODS catalog, validation rules
├── common/
│   ├── __init__.py
│   └── errors.py        # Shared exceptions
├── auth/
│   ├── __init__.py
│   ├── player.py        # Player dataclass
│   ├── registration.py  # Player registration
│   ├── login.py         # Authentication
│   ├── profile.py       # View/update/delete profile
│   └── validator.py     # Recursive access-key validation
├── core/
│   ├── __init__.py
│   ├── card.py          # Card generation and figure patterns
│   ├── game.py          # Tombola draw, marking, winner detection
│   └── points.py        # Score and sum calculations
├── persistence/
│   ├── __init__.py
│   ├── players.py       # JUGADORES.bin read/write
│   └── games.py         # JUEGOS.bin read/write
├── reports/
│   ├── __init__.py
│   ├── summary.py       # Player summary report
│   ├── ranking.py       # TOP 5
│   ├── gantt.py         # Frequency Gantt chart
│   ├── logs.py          # Game logs
│   └── export.py        # Plain-text report export
├── ui/
│   ├── __init__.py
│   ├── app.py           # Pygame main loop and screen manager
│   ├── screens.py       # Screen definitions and transitions
│   ├── renderer.py      # Card/number rendering
│   ├── assets.py        # Image/font loading
│   └── messages.py      # Spanish message catalog
└── ods/
    ├── __init__.py
    ├── data.py          # ODS names, colors, slogans, figure patterns
    └── messages.py      # Rotating educational messages
```

### Tests

```text
tests/
├── __init__.py
├── test_auth.py
├── test_card.py
├── test_game.py
├── test_persistence.py
└── test_reports.py
```

### Assets and Data

```text
assets/
├── images/ods/          # ODS icons/images
├── fonts/
└── sounds/

data/
├── JUGADORES.bin
└── JUEGOS.bin
```

**Structure Decision**: Single-project desktop app layout with modules aligned to the five project challenges. Tests mirror the source modules. Assets and runtime binary files are kept outside `src/`.
