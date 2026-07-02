# Tasks: Initial Project Features

**Input**: Design documents from `/specs/001-initial-project-features/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: Included. Every non-trivial function MUST have unit tests per the project constitution.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies on incomplete tasks)
- **[Story]**: Maps to user stories from spec.md: [US1], [US2], [US3], [US4], [US5]
- Include exact file paths in descriptions

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project directory structure per implementation plan (`src/`, `tests/`, `assets/`, `data/`, `docs/`)
- [x] T002 Create `requirements.txt` with `pygame>=2.5` and `pytest`
- [x] T003 [P] Create `pyproject.toml` with src package configuration
- [x] T004 [P] Create `.gitignore` ignoring `data/*.bin`, `__pycache__/`, `.venv/`
- [x] T005 Create application entry point `src/main.py` that initializes Pygame, loads assets, and starts the screen manager

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T006 [P] Create `src/config.py` with paths, constants, and state catalog
- [x] T007 [P] Create shared exceptions in `src/common/errors.py` (`DuplicateCedulaError`, `PlayerNotFoundError`, `ValidationError`, `CorruptedDataError`)
- [x] T008 [P] Implement explicit `seek()`/`tell()` positioning helpers in `src/persistence/players.py` to prevent record overwrite
- [x] T009 [P] Implement explicit `seek()`/`tell()` positioning helpers in `src/persistence/games.py` for append-only writes
- [x] T010 [P] Create `Player` dataclass in `src/auth/player.py`
- [x] T011 [P] Create `Card` dataclass in `src/core/card.py`
- [x] T012 [P] Create `Game` dataclass in `src/core/game.py`
- [x] T013 Create ODS theme catalog in `src/ods/data.py` with all 17 themes, colors, slogans, and figure masks
- [x] T014 Create Spanish message catalog in `src/ui/messages.py`
- [x] T015 [P] Implement asset loader for ODS images and fonts in `src/ui/assets.py` with fallback handling for missing files

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Register and Log In (Priority: P1) 🎯 MVP

**Goal**: A new user registers with valid personal data and a secure access key, then logs in successfully to access the game.

**Independent Test**: Register a player, verify `data/JUGADORES.bin` stores the record, then log in with the same credentials and reach the main menu.

### Tests for User Story 1

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T016 [P] [US1] Write unit tests for recursive access-key validator in `tests/test_auth.py`
- [x] T017 [P] [US1] Write integration tests for player registration and login persistence in `tests/test_persistence.py`

### Implementation for User Story 1

- [x] T018 [US1] Implement recursive access-key validator in `src/auth/validator.py`
- [x] T019 [US1] Implement player registration logic in `src/auth/registration.py`
- [x] T020 [US1] Implement player login logic in `src/auth/login.py`
- [x] T021 [US1] Implement `JUGADORES.bin` read/write in `src/persistence/players.py`
- [x] T022 [US1] Implement welcome, register, and login screens in `src/ui/screens.py` using the Spanish message catalog
- [x] T023 [US1] Wire registration/login flow in `src/ui/app.py`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Manage Player Profile (Priority: P2)

**Goal**: An authenticated player views, updates, or deletes their own profile and access key.

**Independent Test**: Log in, update the player's name or access key, verify the changes persist in `data/JUGADORES.bin`, then delete the profile and confirm it can no longer log in.

### Tests for User Story 2

- [x] T024 [P] [US2] Write unit tests for profile update and delete in `tests/test_auth.py`
- [x] T025 [P] [US2] Write integration tests for profile persistence changes in `tests/test_persistence.py`

### Implementation for User Story 2

- [x] T026 [US2] Implement profile view/update/delete logic in `src/auth/profile.py`
- [x] T027 [US2] Update `src/persistence/players.py` to support modify and delete operations with full file rewrite
- [x] T028 [US2] Implement profile screen in `src/ui/screens.py` using the Spanish message catalog

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Create Themed Cards (Priority: P2)

**Goal**: An authenticated player chooses a card size and ODS theme, then views the generated main and complement cards before playing.

**Independent Test**: Log in, select dimension 5 and any ODS theme, and verify two valid 5×5 cards are displayed with unique numbers and the selected theme.

### Tests for User Story 3

- [x] T029 [P] [US3] Write unit tests for card generation and uniqueness in `tests/test_card.py`
- [x] T030 [P] [US3] Write unit tests for figure mask scaling in `tests/test_card.py`

### Implementation for User Story 3

- [x] T031 [US3] Implement card generation and figure mask application in `src/core/card.py`
- [x] T032 [US3] Add dimension and theme validation in `src/core/card.py`
- [x] T033 [US3] Implement card creation screen in `src/ui/screens.py` using the Spanish message catalog and enforcing authenticated-session validation before allowing dimension/theme selection
- [x] T034 [US3] Implement card renderer in `src/ui/renderer.py`

**Checkpoint**: At this point, User Stories 1, 2, and 3 should all work independently

---

## Phase 6: User Story 4 - Play a Tombola Round (Priority: P2)

**Goal**: An authenticated player with valid cards starts a game, watches the automatic number draw, and sees a winner announcement when a card completes the ODS figure.

**Independent Test**: Start a game with two cards and force or observe a completed figure; verify the game stops, labels "GANADOR", shows the cell sum, and saves the game record.

### Tests for User Story 4

- [x] T035 [P] [US4] Write unit tests for tombola draw uniqueness in `tests/test_game.py`
- [x] T036 [P] [US4] Write unit tests for winner detection in `tests/test_game.py`
- [x] T037 [P] [US4] Write integration tests for game persistence in `tests/test_persistence.py`
- [x] T038 [US4] Write end-to-end integration test for full game flow from login to winner detection in `tests/test_game.py`

### Implementation for User Story 4

- [x] T039 [US4] Implement tombola draw and number marking in `src/core/game.py`
- [x] T040 [US4] Implement winner detection using figure masks in `src/core/game.py`
- [x] T041 [US4] Implement score/sum calculation in `src/core/points.py`
- [x] T042 [US4] Implement append-only `JUEGOS.bin` write in `src/persistence/games.py`
- [x] T043 [US4] Implement game screen with configurable draw speed in `src/ui/screens.py` using the Spanish message catalog
- [x] T044 [US4] Implement results screen in `src/ui/screens.py` using the Spanish message catalog

**Checkpoint**: At this point, User Stories 1 through 4 should all work independently

---

## Phase 7: User Story 5 - View Reports (Priority: P3)

**Goal**: A user opens the reports section and generates player summaries, frequency charts, game logs, and a TOP 5 ranking.

**Independent Test**: After at least one game is saved, open reports, select each report type, and verify the output is written to a physical `.txt` file with correct data.

### Tests for User Story 5

- [x] T045 [P] [US5] Write unit tests for report aggregations in `tests/test_reports.py`
- [x] T046 [P] [US5] Write unit tests for date-range filtering in `tests/test_reports.py`

### Implementation for User Story 5

- [x] T047 [US5] Implement player summary report in `src/reports/summary.py`
- [x] T048 [US5] Implement Gantt frequency report in `src/reports/gantt.py`
- [x] T049 [US5] Implement game logs report in `src/reports/logs.py`
- [x] T050 [US5] Implement TOP 5 ranking report in `src/reports/ranking.py`
- [x] T051 [US5] Implement `.txt` report export with aligned columns in `src/reports/export.py`
- [x] T052 [US5] Implement reports screen in `src/ui/screens.py` using the Spanish message catalog

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T053 [P] Run full `pytest` suite and fix any failures
- [x] T054 [P] Validate all `quickstart.md` scenarios manually
- [x] T055 [P] Add rotating ODS educational messages during gameplay in `src/ods/messages.py`
- [x] T056 [P] Review all on-screen text to ensure 100% Spanish language compliance
- [x] T057 [P] Run UI performance check for 60 fps during gameplay
- [x] T058 Update `docs/` to reflect final implementation details

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Depends on US1 only for login state, but independently testable with its own login
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - Depends on US1 only for authentication state
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - Depends on US1 and US3
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - Depends on US1 and US4

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Models before services
- Services before UI screens
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task: "T016 [P] [US1] Write unit tests for recursive access-key validator in tests/test_auth.py"
Task: "T017 [P] [US1] Write integration tests for player registration and login persistence in tests/test_persistence.py"

# Launch foundational model tasks together:
Task: "T010 [P] Create Player dataclass in src/auth/player.py"
Task: "T011 [P] Create Card dataclass in src/core/card.py"
Task: "T012 [P] Create Game dataclass in src/core/game.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Demo registration and login if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Demo (MVP!)
3. Add User Story 2 → Test independently → Demo profile management
4. Add User Story 3 → Test independently → Demo card creation
5. Add User Story 4 → Test independently → Demo full game
6. Add User Story 5 → Test independently → Demo reports
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 + User Story 2
   - Developer B: User Story 3 + User Story 4
   - Developer C: User Story 5 + Polish
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
