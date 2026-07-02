# UI Screen Contracts

Each screen in the Pygame application implements the same interface contract so the main loop can manage navigation uniformly.

## Screen Interface

Every screen MUST provide:

- `__init__(app, state)`
  - `app`: reference to the main application object.
  - `state`: shared session state (current player, generated cards, game in progress, etc.).

- `handle_event(event)`
  - Receives a Pygame event.
  - Returns the name of the next screen to navigate to, or `None` to stay on the current screen.
  - May mutate `state`.

- `update(delta_time)`
  - Called once per frame.
  - `delta_time`: milliseconds since last frame.
  - Updates animations, timers, and automatic draw pacing.

- `draw(surface)`
  - `surface`: Pygame surface representing the window.
  - Renders all visible elements in Spanish.

## Navigation Contract

- Screen names are unique lowercase strings: `welcome`, `register`, `login`, `profile`, `menu`, `card_creation`, `game`, `results`, `reports`.
- A screen MAY push a transient overlay (e.g., confirmation dialog) but the underlying screen name remains unchanged.
- Returning `"quit"` from `handle_event` terminates the application.
- The application MUST call `pygame.quit()` only after the main loop exits.

## Shared State Contract

The `state` object passed to screens MUST expose at least:

| Field | Type | Description |
|---|---|---|
| `current_player` | Player or None | Authenticated player, if any |
| `cards` | tuple(Card, Card) or None | Generated main and complement cards |
| `selected_speed` | string or None | "manual", "1s", or "2s" |
| `current_game` | Game or None | In-progress or completed game |
| `message_catalog` | dict | Spanish text lookup by key |

Screens MUST NOT assume fields are populated; they MUST validate and show errors via the message catalog.

## Error Rendering Contract

- Error messages MUST be drawn using keys from the centralized message catalog.
- Error text MUST be in Spanish.
- Error displays MUST remain visible until the user acknowledges them or navigates away.
