# Quickstart: Initial Project Features

This guide validates that the MVP feature set works end-to-end.

## Prerequisites

- Python 3.11 or newer installed.
- Pygame 2.5 or newer installed.
- pytest installed.
- Repository cloned and branch `001-initial-project-features` checked out.

## Setup

1. Create a virtual environment (recommended):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Linux/macOS
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create the runtime data directory:
   ```bash
   mkdir data
   ```

## Validation Scenarios

### Scenario A: Registration and Login

1. Start the application:
   ```bash
   python -m src.main
   ```
2. Select **Registrarse**.
3. Enter a unique cédula, full name, sex, birthdate, state code, and a valid access key.
4. Confirm the success message is in Spanish.
5. Select **Iniciar sesión** and enter the same cédula and access key.
6. Confirm you reach the main menu.

**Expected outcome**: Player record is saved in `data/JUGADORES.bin` and login succeeds.

### Scenario B: Profile CRUD

1. Log in with an existing player.
2. Select **Perfil**.
3. Update the full name and confirm.
4. Close and reopen the application, then log in again.
5. Verify the updated name appears.
6. Select **Eliminar perfil** and confirm.
7. Try to log in with the deleted cédula.

**Expected outcome**: Updates persist; deleted player cannot log in.

### Scenario C: Card Generation

1. Log in and select **Jugar**.
2. Choose dimension `7` and any ODS theme.
3. Confirm two 7×7 cards appear with unique numbers from 1 to 49.
4. Select an invalid dimension such as `4`.

**Expected outcome**: Valid cards display correctly; invalid dimension shows the Spanish error message.

### Scenario D: Full Game Round

1. Log in and generate cards with dimension `5`.
2. Select a draw speed (e.g., "1 segundo").
3. Start the game.
4. Wait until a card completes the figure.

**Expected outcome**: Game stops, winning card is labeled "GANADOR", the cell sum is shown, and `data/JUEGOS.bin` contains the new record.

### Scenario E: Reports

1. After completing at least one game, select **Reportes**.
2. Generate each report type with a date range that includes today.
3. Check the generated `.txt` files.

**Expected outcome**: Files are created in plain text with aligned columns and correct data.

## Automated Tests

Run the full test suite:

```bash
pytest
```

Run a specific module:

```bash
pytest tests/test_auth.py
pytest tests/test_persistence.py
pytest tests/test_game.py
```

**Expected outcome**: All tests pass; no failures are merged.

## Cleanup

To reset data between validation runs:

```bash
rm data/JUGADORES.bin data/JUEGOS.bin
```

On Windows:

```powershell
Remove-Item data\JUGADORES.bin, data\JUEGOS.bin
```
