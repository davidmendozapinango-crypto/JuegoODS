# Persistence Contracts

The persistence layer exposes deterministic read/write operations for `JUGADORES.bin` and `JUEGOS.bin`. All callers interact through the functions below rather than accessing files directly.

## Player Repository Contract

### `register_player(player: Player) -> None`

- Stores a new player record.
- Raises `DuplicateCedulaError` if the cédula already exists.
- Raises `ValidationError` if the player data fails field validation.

### `find_player(cedula: str) -> Player | None`

- Returns the player matching `cedula`, or `None` if not found.
- Raises `CorruptedDataError` if the file cannot be parsed.

### `list_players() -> list[Player]`

- Returns all registered players.
- Returns an empty list if the file is missing.
- Raises `CorruptedDataError` if the file cannot be parsed.

### `update_player(cedula: str, changes: dict) -> Player`

- Applies allowed changes (`full_name`, `state_code`, `access_key`).
- If `cedula` is in `changes`, verifies uniqueness before updating.
- Raises `PlayerNotFoundError` if the player does not exist.
- Raises `DuplicateCedulaError` if the new cédula conflicts with another player.

### `delete_player(cedula: str) -> None`

- Removes the player record.
- Does not delete game history.
- Raises `PlayerNotFoundError` if the player does not exist.

## Game Repository Contract

### `save_game(game: Game) -> None`

- Appends a completed game record to `JUEGOS.bin`.
- Raises `ValidationError` if required fields are missing or invalid.

### `list_games(date_from=None, date_to=None) -> list[Game]`

- Returns all games, optionally filtered by date range.
- Returns an empty list if the file is missing.
- Raises `CorruptedDataError` if the file cannot be parsed.

### `games_for_player(cedula: str) -> list[Game]`

- Returns all games played by the specified player.
- Returns an empty list if none exist.

## Error Types

| Exception | Meaning | Caller Responsibility |
|---|---|---|
| `DuplicateCedulaError` | Cédula already in use | Show "La cédula ya está registrada" |
| `PlayerNotFoundError` | Player does not exist | Treat as unregistered or show error |
| `ValidationError` | Field-level validation failed | Show field-specific Spanish message |
| `CorruptedDataError` | Binary file unreadable | Show "Error al leer los datos guardados" and continue with empty state |

## File Safety Contract

- `JUGADORES.bin` writes MUST complete before the UI confirms the operation.
- `JUEGOS.bin` writes MUST be append-only.
- Temporary files or backups SHOULD be used during rewrite operations to prevent data loss on crash.
