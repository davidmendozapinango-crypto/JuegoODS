# Feature Specification: Initial Project Features

**Feature Branch**: `001-initial-project-features`

**Created**: 2026-06-28

**Status**: Draft

**Input**: User description: "Initial project features. The specification must include: 1) Business objective and operational context of the calculation. 2) Command input contract. 3) Decision rules by calculation paths. 4) Required internal dependencies. 5) Handling of business errors with clear messages for each failed precondition. 6) Impact on API endpoint. 7) Verifiable and measurable acceptance criteria. 8) Include the implementation of all necessary tests. 9) Create the branch respective"

## 1. Business Objective and Operational Context

The **SDG Tombola** is an educational bingo-style desktop game developed for the Algorithms and Programming course at Universidad Católica Andrés Bello. Its purpose is to promote the United Nations Sustainable Development Goals (SDGs) while teaching students software engineering fundamentals.

The operational context covers five core challenges:
- Secure player registration and authentication.
- Dynamic generation of N×N themed bingo cards.
- Automated tombola gameplay with random number draws.
- Report generation for players, games, and rankings.
- Integration of SDG images, colors, and slogans throughout the experience.

All calculations (score sums, card filling sequences, winner detection, frequency reports, and access-key validation) must produce correct, reproducible results that can be verified against the project rules.

## Clarifications

### Session 2026-06-28

- **Q**: The spec refers to an SDG "figure pattern" that determines how a card wins, but it does not define what a pattern looks like or how winner detection works. How should a winning figure be defined for the themed cards?  
  **A**: Project-defined figure. The exact figure pattern is defined by the course assignment and MUST be documented in the project source as a configurable grid mask.
- **Q**: The spec assumes all 17 SDGs are available as themes but allows the MVP to start with a subset. How many SDG themes must be implemented for the MVP to be acceptable?  
  **A**: All 17 ODS. The MVP MUST include every Sustainable Development Goal as a selectable theme.
- **Q**: Reports must be saved to physical files, but the spec does not specify the format. What format should the generated reports use?  
  **A**: Plain text (.txt). All reports MUST be saved as UTF-8 text files with aligned columns for human readability.
- **Q**: The spec says the tombola draws numbers automatically but does not state how fast. What draw interval should the game use during gameplay?  
  **A**: Configurable. The player MUST be able to select a draw speed (e.g., manual, 1 second, 2 seconds) before starting the game.
- **Q**: The spec defines player registration but does not say whether a registered player can later update or delete their profile. What player data lifecycle operations should the MVP support?  
  **A**: Full CRUD. Registered players MUST be able to view, update, and delete their own profile after authenticating.

## 2. Command Input Contract

The application receives user actions through the Pygame graphical interface. Each action must provide the inputs defined below:

| Action | Required Inputs | Valid Input Rules |
|---|---|---|
| Register player | Cédula, full name, sex, birthdate, state code, access key | Cédula unique; key 6-10 chars with uppercase, lowercase, number, special char (*, =, %, _) and no more than 3 consecutive identical chars |
| Log in | Cédula, access key | Both must match an existing registered player |
| Manage profile | Updated profile fields or delete confirmation | Player must be authenticated; updated cédula must remain unique |
| Create cards | Card dimension N, SDG theme | N must be odd and 5 ≤ N ≤ 15; theme must exist in the SDG catalog |
| Start game | Confirmation of cards, selected draw speed | Cards must have been generated in the current session; speed must be one of the supported options |
| Generate report | Report type, optional date range | Date range end must not precede start |
| Exit / return | Menu selection | Any available menu option |

## 3. Decision Rules by Calculation Paths

### Access-key validation (recursive)
- Accept if length is 6-10, contains at least one uppercase, one lowercase, one digit, one special character from {*, =, %, _}, and contains no run of more than 3 identical consecutive characters.
- Reject otherwise and indicate which rules are not met.

### Card dimension validation
- Accept if N is odd and 5 ≤ N ≤ 15.
- Reject otherwise.

### Card filling
- Populate each N×N card with unique random numbers from 1 to N×N following the pattern associated with the selected SDG theme.
- Numbers must not repeat within a card.

### Tombola draw
- Draw random, non-repeating numbers from 1 to N×N until a winner is detected.
- Each drawn number must be marked automatically on every card that contains it.

### Winner detection
- A card wins when it completes the SDG figure associated with its theme.
- The exact figure pattern is defined by the course assignment and MUST be documented in the project source as a configurable grid mask.
- The game stops at the first winning card.
- The winning card is labeled "GANADOR" and the sum of all its cells is displayed.

### Report calculations
- Player summary counts total games per player from `JUEGOS.bin`.
- Gantt report shows the 10 most frequent drawn numbers in a date range, sorted high to low.
- TOP 5 ranking lists players by accumulated points in a date range.

## 4. Required Internal Dependencies

The initial feature set requires the following functional capabilities to be available:

- **Player identity management**: registration, login, and profile lookup.
- **Recursive validator**: access-key complexity checking.
- **Card generator**: theme-aware pattern and number placement.
- **Game engine**: random draw, marking, and winner detection.
- **Binary persistence**: read/write players and games to binary files.
- **Report engine**: aggregations, sorting, and file export.
- **SDG content catalog**: names, colors, slogans, and figures for all 17 goals.
- **Pygame user interface**: menus, card rendering, animations, and Spanish text.

## 5. Handling of Business Errors

| Failed Precondition | Clear Spanish Message | Recovery Action |
|---|---|---|
| Cédula already registered | "La cédula ya está registrada. Inicie sesión o use otra cédula." | Return to registration form |
| Access key too short/long | "La clave debe tener entre 6 y 10 caracteres." | Show real-time criteria feedback |
| Access key missing uppercase | "La clave debe incluir al menos una letra mayúscula." | Show real-time criteria feedback |
| Access key missing lowercase | "La clave debe incluir al menos una letra minúscula." | Show real-time criteria feedback |
| Access key missing digit | "La clave debe incluir al menos un número." | Show real-time criteria feedback |
| Access key missing special char | "La clave debe incluir al menos uno de estos caracteres: *, =, %, _." | Show real-time criteria feedback |
| More than 3 consecutive identical chars | "La clave no puede tener más de 3 caracteres iguales seguidos." | Show real-time criteria feedback |
| Invalid login credentials | "Cédula o clave incorrecta. Intente de nuevo." | Return to login form |
| Invalid card dimension | "La dimensión debe ser un número impar entre 5 y 15." | Return to dimension selection |
| Invalid SDG theme | "Seleccione una temática de ODS válida." | Return to theme selection |
| No cards before starting game | "Debe generar los cartones antes de iniciar el juego." | Redirect to card creation |
| Corrupted binary file | "Error al leer los datos guardados. Contacte al administrador." | Log error, continue with empty state |
| Invalid date range in report | "La fecha final no puede ser anterior a la fecha inicial." | Return to report filters |

## 6. Impact on Application Entry Points

**Assumption**: This project is a desktop Pygame application, not a web service. Therefore, the concept of "API endpoint" is interpreted as the application's public entry points and navigable screens.

Impacted entry points:
- Application launch (`main.py`): initializes Pygame, loads assets, and shows the welcome screen.
- Registration screen: new dependency on recursive validator and player persistence.
- Login screen: new dependency on player lookup.
- Card creation screen: new dependency on card generator and SDG catalog.
- Game screen: new dependency on game engine, draw logic, and winner detection.
- Reports screen: new dependency on report engine and binary file readers.

Each entry point must validate its inputs and route to the appropriate screen or error message.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Register and Log In (Priority: P1)

A new user registers with valid personal data and a secure access key, then logs in successfully to access the game.

**Why this priority**: Without registration and authentication, no player can create cards or play. This is the entry gate for all other features.

**Independent Test**: Register a player, verify the binary file stores the record, then log in with the same credentials and reach the main menu.

**Acceptance Scenarios**:

1. **Given** the registration screen is open, **When** the user enters a unique cédula, valid name, sex, birthdate, state code, and a key that meets all complexity rules, **Then** the system saves the player and confirms success in Spanish.
2. **Given** the user has registered, **When** they enter the correct cédula and access key on the login screen, **Then** they are authenticated and reach the main menu.
3. **Given** the user enters a duplicate cédula, **When** they submit the registration form, **Then** the system displays "La cédula ya está registrada" and does not overwrite existing data.

---

### User Story 2 - Manage Player Profile (Priority: P2)

An authenticated player views, updates, or deletes their own profile and access key.

**Why this priority**: Full CRUD was explicitly requested for the MVP. Profile management ensures players can recover from mistakes during registration and maintain their accounts.

**Independent Test**: Log in, update the player's name or access key, verify the changes persist in `JUGADORES.bin`, then delete the profile and confirm it can no longer log in.

**Acceptance Scenarios**:

1. **Given** an authenticated player on the profile screen, **When** they update their full name and confirm, **Then** the system saves the change and shows a Spanish confirmation message.
2. **Given** an authenticated player, **When** they change their access key to a new valid key, **Then** the system updates the stored key and requires the new key on the next login.
3. **Given** an authenticated player, **When** they choose to delete their profile and confirm the action, **Then** the system removes their record from `JUGADORES.bin` and returns to the welcome screen.

---

### User Story 3 - Create Themed Cards (Priority: P2)

An authenticated player chooses a card size and SDG theme, then views the generated main and complement cards before playing.

**Why this priority**: Cards are required before gameplay. This story validates the card generation logic and theme integration.

**Independent Test**: Log in, select dimension 5 and any SDG theme, and verify two valid 5×5 cards are displayed with unique numbers and the selected theme.

**Acceptance Scenarios**:

1. **Given** an authenticated player on the card creation screen, **When** they select N=7 and an SDG theme, **Then** the system generates a 7×7 main card and complement card with unique numbers from 1 to 49.
2. **Given** the user selects N=4, **When** they confirm, **Then** the system rejects the input with "La dimensión debe ser un número impar entre 5 y 15."
3. **Given** valid cards are generated, **When** the user requests the filling sequence, **Then** the system displays the numerical order used to populate the figure.

---

### User Story 4 - Play a Tombola Round (Priority: P2)

An authenticated player with valid cards starts a game, watches the automatic number draw, and sees a winner announcement when a card completes the SDG figure.

**Why this priority**: This is the core game loop and validates draw randomness, marking, winner detection, and persistence.

**Independent Test**: Start a game with two cards and force or observe a completed figure; verify the game stops, labels "GANADOR", shows the cell sum, and saves the game record.

**Acceptance Scenarios**:

1. **Given** valid cards are displayed, **When** the user selects a draw speed and starts the game, **Then** the system draws random non-repeating numbers at the selected pace and marks matching cells automatically.
2. **Given** a number has been drawn, **When** it appears on one or both cards, **Then** the corresponding cells change appearance to indicate they are marked.
3. **Given** a card completes the SDG figure, **When** the winning number is drawn, **Then** the game stops, the card is labeled "GANADOR", the sum of all its cells is shown, and the result is saved.

---

### User Story 5 - View Reports (Priority: P3)

A user opens the reports section and generates player summaries, frequency charts, game logs, and a TOP 5 ranking.

**Why this priority**: Reports demonstrate data persistence and provide visibility into player activity and game statistics.

**Independent Test**: After at least one game is saved, open reports, select each report type, and verify the output is written to a physical file with correct data.

**Acceptance Scenarios**:

1. **Given** at least one player and one game exist, **When** the user requests the player summary, **Then** the system lists all players with their total games played.
2. **Given** games have been played in a date range, **When** the user requests the Gantt report, **Then** the system outputs the 10 most frequent drawn numbers sorted from highest to lowest.
3. **Given** games have been played in a date range, **When** the user requests the TOP 5 ranking, **Then** the system shows up to 5 players sorted by accumulated points.

---

### Edge Cases

- What happens when `JUGADORES.bin` is missing or empty? The system must allow registration and treat the player list as empty.
- What happens when `JUEGOS.bin` is corrupted? The system must report the error gracefully and continue without crashing.
- What happens when a draw reaches the last available number without a winner? The game must end in a draw and offer a new round.
- What happens when both cards win on the same number? The system must label both as "GANADOR" and show both sums.
- What happens when the user closes the application mid-game? Unsaved game progress is lost; saved players remain intact.
- What happens when a player updates their cédula to a value already used by another player? The system must reject the update with "La cédula ya está registrada por otro jugador."
- What happens when a deleted player tries to log in? The system must treat them as unregistered and offer registration.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow a new player to register with cédula, full name, sex, birthdate, state code, and access key.
- **FR-002**: System MUST validate access keys using a recursive algorithm checking length, character classes, and consecutive-character rules.
- **FR-003**: System MUST prevent duplicate cédulas during registration.
- **FR-004**: System MUST authenticate players using cédula and access key.
- **FR-005**: System MUST allow card creation only after successful authentication.
- **FR-006**: System MUST support N×N card dimensions where N is odd and 5 ≤ N ≤ 15.
- **FR-007**: System MUST generate main and complement cards with unique random numbers from 1 to N×N following the selected SDG theme pattern for any of the 17 ODS themes.
- **FR-008**: System MUST draw random, non-repeating numbers from 1 to N×N during gameplay at a player-selected speed.
- **FR-009**: System MUST automatically mark matching numbers on all active cards.
- **FR-010**: System MUST detect when a card completes its SDG figure and stop the game.
- **FR-011**: System MUST display the winning card as "GANADOR" and show the sum of its cells.
- **FR-012**: System MUST save every completed game to `JUEGOS.bin` with date, time, player ID, card sequences, and drawn numbers.
- **FR-013**: System MUST generate player summary, Gantt frequency, game log, and TOP 5 reports.
- **FR-014**: System MUST save generated reports as UTF-8 plain text files (.txt) with aligned columns.
- **FR-015**: System MUST display all graphical text in Spanish.
- **FR-016**: System MUST allow an authenticated player to view their own profile.
- **FR-017**: System MUST allow an authenticated player to update their full name, state code, or access key, preserving cédula uniqueness.
- **FR-018**: System MUST allow an authenticated player to delete their own profile and all associated future login capability.

### Key Entities

- **Player**: Represents a registered user. Attributes: cédula, full name, sex, birthdate, state code, access key.
- **Card**: Represents an N×N bingo card. Attributes: dimension N, SDG theme, cell values, marked cells, filling sequence.
- **Game**: Represents a single tombola session. Attributes: player ID, date/time, main card sequence, complement card sequence, drawn numbers, winner card reference.
- **SDG Theme**: Represents a Sustainable Development Goal. Attributes: number, name, color, slogan, figure pattern.
- **Report**: Represents an exported summary. Attributes: report type, date range, generated output, file path.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A new player can complete registration in under 3 minutes on first attempt.
- **SC-002**: Access-key validation identifies invalid keys in under 1 second and lists all unmet criteria.
- **SC-003**: Card generation produces valid N×N cards for any allowed dimension in under 2 seconds.
- **SC-004**: 100% of drawn numbers are unique within a single game session.
- **SC-005**: Winner detection triggers immediately when the final required cell is marked.
- **SC-006**: Every completed game is persisted before the results screen is shown.
- **SC-007**: Reports generate correctly for any date range containing saved games.
- **SC-008**: 100% of on-screen text visible to players is in Spanish.
- **SC-009**: The application handles corrupted binary files without crashing and shows a clear Spanish error message.
- **SC-010**: Profile updates and deletions are persisted within 1 second and reflected immediately on the next login attempt.

## Assumptions

- The application runs as a single-player desktop application using Python and Pygame.
- "API endpoint impact" is interpreted as impact on application entry points and UI screens because the project is not a web service.
- All 17 ODS are available as themes in the MVP.
- Binary files are stored locally and are not shared across network instances.
- The user has Python 3.x and Pygame installed in the development environment.
- Tests cover unit logic, integration of file persistence, and end-to-end game flow.
