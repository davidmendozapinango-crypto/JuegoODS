# Data Model: Initial Project Features

## Entities

### Player

Represents a registered user of the game.

| Field | Type | Constraints | Notes |
|---|---|---|---|
| cédula | string | Unique, non-empty | Primary identifier |
| full_name | string | Non-empty | Player display name |
| sex | string | "m" or "f" | Single character |
| birthdate | date | Valid calendar date | Stored as ISO string (YYYY-MM-DD) |
| state_code | string | 3 uppercase chars | Must exist in recognized state catalog |
| access_key | string | 6-10 chars, validated recursively | Stored after validation; not plaintext secret |

**Validation rules**:
- `cédula` must be unique across all players.
- `access_key` must pass recursive validation: length 6-10, at least one uppercase, one lowercase, one digit, one special character from {*, =, %, _}, and no run of more than 3 identical consecutive characters.
- Updates that change `cédula` must preserve uniqueness.

**Lifecycle**:
- Created during registration.
- Read during login and profile view.
- Updated during profile management.
- Deleted during profile deletion; associated future logins are rejected.

### Card

Represents a single N×N bingo card.

| Field | Type | Constraints | Notes |
|---|---|---|---|
| dimension | integer | Odd, 5 ≤ N ≤ 15 | Card size |
| theme_id | integer | 1-17 | References ODS theme |
| cells | list[list[int]] | N×N, unique values 1..N×N | Populated numbers |
| marked | list[list[bool]] | N×N | Marks matching drawn numbers |
| filling_sequence | list[tuple[int, int]] | Length N×N | Order in which cells are conceptually filled |
| figure_mask | list[list[bool]] | N×N | Winning positions for this theme |

**Validation rules**:
- All numbers in `cells` must be unique within the card.
- All numbers must be in range 1..N×N.
- `marked` starts as all `False` and updates as numbers are drawn.

**Lifecycle**:
- Generated after player selects dimension and theme.
- Used during a single game session.
- Discarded after game unless persisted as part of `Game` record.

### Game

Represents a completed tombola session.

| Field | Type | Constraints | Notes |
|---|---|---|---|
| player_id | string | References Player.cédula | Who played |
| played_at | datetime | Valid timestamp | ISO format with timezone |
| dimension | integer | Odd, 5 ≤ N ≤ 15 | Card size used |
| theme_id | integer | 1-17 | ODS theme used |
| main_card_cells | list[list[int]] | N×N | Main card number layout |
| complement_card_cells | list[list[int]] | N×N | Complement card number layout |
| drawn_numbers | list[int] | Unique, 1..N×N | Order of numbers drawn |
| winner_card | string | "main", "complement", "both", or "none" | Which card(s) completed the figure |
| main_card_sum | integer | Computed | Sum of all main card cells |
| complement_card_sum | integer | Computed | Sum of all complement card cells |

**Validation rules**:
- `drawn_numbers` must contain no duplicates.
- Each drawn number must be in range 1..N×N.
- `winner_card` must match the actual figure completion state.

**Lifecycle**:
- Created when a game starts.
- Updated after each draw.
- Persisted to `JUEGOS.bin` immediately when the game ends.

### ODS Theme

Represents a Sustainable Development Goal theme.

| Field | Type | Constraints | Notes |
|---|---|---|---|
| number | integer | 1-17 | ODS identifier |
| name | string | Non-empty | Spanish name (e.g., "Fin de la pobreza") |
| color | string | Hex color | Theme color for UI |
| slogan | string | Non-empty | Short educational message |
| figure_mask | list[list[bool]] | N×N (parameterized) | Winning cell pattern |

**Validation rules**:
- `number` must be unique.
- `figure_mask` must be applicable to any allowed dimension.

### Report

Represents a generated report output.

| Field | Type | Constraints | Notes |
|---|---|---|---|
| report_type | string | One of: player_summary, gantt, logs, top5 | Report category |
| date_from | date | Optional | Filter start |
| date_to | date | Optional | Filter end |
| content | string | UTF-8 text | Aligned-column output |
| file_path | string | Ends with .txt | Destination path |

**Validation rules**:
- If both dates are provided, `date_to` must not precede `date_from`.
- `file_path` must use `.txt` extension.

## Relationships

- **Player 1..* Game**: A player can play many games; each game belongs to one player.
- **Game 1..2 Card**: Each game uses exactly one main card and one complement card.
- **Card *..1 ODS Theme**: Each card is themed by one ODS; each ODS can theme many cards.
- **Report *..* Game / Player**: Reports aggregate data from multiple games and players.

## Binary Record Layout (high-level)

### JUGADORES.bin

Each record encodes:
- cédula length (1 byte) + cédula bytes
- full_name length (1 byte) + full_name bytes (UTF-8)
- sex (1 byte)
- birthdate (10 bytes, ISO YYYY-MM-DD)
- state_code (3 bytes)
- access_key length (1 byte) + access_key bytes

Records are written sequentially. Updates/deletes trigger a full file rewrite.

### JUEGOS.bin

Each record encodes:
- player_id length (1 byte) + player_id bytes
- played_at (ISO datetime string with length prefix)
- dimension (1 byte)
- theme_id (1 byte)
- main_card_cells as N×N integers
- complement_card_cells as N×N integers
- drawn_numbers count (2 bytes) + numbers
- winner_card (1 byte code)
- main_card_sum (4 bytes)
- complement_card_sum (4 bytes)

Records are appended only.
