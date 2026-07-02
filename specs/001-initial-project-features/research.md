# Research: Initial Project Features

## 1. Pygame Screen/State Management

**Decision**: Use a screen-state manager with a dictionary of screen objects and an active-screen pointer.

**Rationale**:
- Pygame does not provide a built-in scene/screen framework. A lightweight state manager keeps screen transitions explicit and testable.
- Each screen (welcome, registration, login, profile, menu, card creation, game, results, reports) becomes a class with `handle_event`, `update`, and `draw` methods.
- The main loop delegates to the active screen, simplifying navigation and reducing coupling between UI and game logic.

**Alternatives considered**:
- Single-loop with global state flags: simpler for tiny prototypes but becomes unmanageable with 9+ screens.
- External scene library (e.g., pygame-menu): adds a dependency and reduces control over Spanish text rendering and SDG theming.

## 2. Binary File Persistence Pattern

**Decision**: Use fixed-length record packing with `struct` and append-only writes for `JUEGOS.bin`; rewrite-on-modify for `JUGADORES.bin` updates/deletes.

**Rationale**:
- `struct` provides deterministic binary encoding/decoding, which satisfies the constitution's requirement for fixed, documented record structures.
- Append-only for games matches the natural append behavior of match history and avoids overwriting previous records.
- Player updates and deletes require rewriting `JUGADORES.bin` because records change size or are removed; the file is small enough for full rewrite.

**Alternatives considered**:
- `pickle`: convenient but not human-readable, version-fragile, and poses security risks when loading untrusted data.
- `sqlite`: violates the project constraint of using binary files for persistence.

## 3. Recursive Access-Key Validation

**Decision**: Implement validation as a pure recursive function over the key string, with helper predicates for each rule.

**Rationale**:
- The project explicitly requires a recursive algorithm. A single recursive traversal can check length, character classes, and consecutive-character runs.
- Keeping validation pure (no side effects) makes it trivial to unit test.
- Real-time feedback is achieved by calling the validator on each keystroke and mapping rule results to UI indicators.

**Alternatives considered**:
- Iterative regex-based validation: would be shorter but violates the recursive requirement.
- Mixed recursive/iterative approach: acceptable but harder to reason about and test.

## 4. Figure Pattern Representation

**Decision**: Represent each ODS figure as an N×N boolean grid mask where `True` cells are the winning positions.

**Rationale**:
- A grid mask scales naturally with any allowed dimension (5×5 to 15×15).
- Winner detection reduces to checking whether all mask positions on a card are marked.
- The mask is configurable per ODS theme and can be documented in the source catalog.

**Alternatives considered**:
- Coordinate list: also workable but less visually aligned with the card grid.
- Hardcoded win conditions per dimension: does not scale and duplicates logic.

## 5. Configurable Draw Speed

**Decision**: Offer three modes: manual (space/click to draw), 1 second per number, and 2 seconds per number.

**Rationale**:
- Three discrete options are easy to render in the UI and simple to implement with a Pygame timer.
- Manual mode supports testing and demos; automatic modes support relaxed gameplay.
- This satisfies the clarification answer: "configurable" with concrete examples.

**Alternatives considered**:
- Free numeric input (e.g., 0.5s to 5s): more flexible but harder to validate and test consistently.
- Single fixed speed: does not meet the clarified requirement.
