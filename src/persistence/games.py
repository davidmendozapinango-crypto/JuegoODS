import struct
from datetime import datetime
from typing import List, Optional

from common.errors import CorruptedDataError, ValidationError
from config import GAMES_FILE
from core.game import Game


def _write_text(f, text: str):
    data = text.encode("utf-8")
    if len(data) > 255:
        raise ValidationError("Texto demasiado largo")
    f.write(struct.pack("B", len(data)))
    f.write(data)


def _read_text(f) -> str:
    length_data = f.read(1)
    if not length_data:
        raise CorruptedDataError("Fin inesperado del archivo")
    length = struct.unpack("B", length_data)[0]
    data = f.read(length)
    if len(data) != length:
        raise CorruptedDataError("Registro de texto incompleto")
    return data.decode("utf-8")


def _read_grid(f, n: int) -> List[List[int]]:
    grid = []
    for _ in range(n):
        row = []
        for _ in range(n):
            value = struct.unpack("H", f.read(2))[0]
            row.append(value)
        grid.append(row)
    return grid


def _write_grid(f, grid: List[List[int]]):
    for row in grid:
        for value in row:
            f.write(struct.pack("H", value))


def _write_record(f, game: Game):
    _write_text(f, game.player_id)
    _write_text(f, game.played_at)
    f.write(struct.pack("B", game.dimension))
    f.write(struct.pack("B", game.theme_id))
    _write_grid(f, game.main_card_cells)
    _write_grid(f, game.complement_card_cells)
    f.write(struct.pack("H", len(game.drawn_numbers)))
    for number in game.drawn_numbers:
        f.write(struct.pack("H", number))
    f.write(struct.pack("B", len(game.winner_card)))
    f.write(game.winner_card.encode("ascii"))
    f.write(struct.pack("I", game.main_card_sum))
    f.write(struct.pack("I", game.complement_card_sum))


def _read_record(f) -> Game:
    try:
        player_id = _read_text(f)
        played_at = _read_text(f)
        dimension = struct.unpack("B", f.read(1))[0]
        theme_id = struct.unpack("B", f.read(1))[0]
        main_card_cells = _read_grid(f, dimension)
        complement_card_cells = _read_grid(f, dimension)
        drawn_count = struct.unpack("H", f.read(2))[0]
        drawn_numbers = [struct.unpack("H", f.read(2))[0] for _ in range(drawn_count)]
        winner_len = struct.unpack("B", f.read(1))[0]
        winner_card = f.read(winner_len).decode("ascii")
        main_card_sum = struct.unpack("I", f.read(4))[0]
        complement_card_sum = struct.unpack("I", f.read(4))[0]
        return Game(
            player_id=player_id,
            played_at=played_at,
            dimension=dimension,
            theme_id=theme_id,
            main_card_cells=main_card_cells,
            complement_card_cells=complement_card_cells,
            drawn_numbers=drawn_numbers,
            winner_card=winner_card,
            main_card_sum=main_card_sum,
            complement_card_sum=complement_card_sum,
        )
    except (struct.error, UnicodeDecodeError, ValueError) as exc:
        raise CorruptedDataError("Registro de juego corrupto") from exc


def list_games(
    date_from: Optional[str] = None, date_to: Optional[str] = None
) -> List[Game]:
    if not GAMES_FILE.exists():
        return []
    games = []
    with open(GAMES_FILE, "rb") as f:
        while True:
            try:
                games.append(_read_record(f))
            except CorruptedDataError as exc:
                if "Fin inesperado" in str(exc):
                    break
                raise

    if date_from or date_to:

        def _parse(dt: str) -> datetime:
            return datetime.fromisoformat(dt)

        filtered = []
        for game in games:
            game_dt = _parse(game.played_at)
            if date_from and game_dt < _parse(date_from):
                continue
            if date_to and game_dt > _parse(date_to):
                continue
            filtered.append(game)
        games = filtered
    return games


def games_for_player(cedula: str) -> List[Game]:
    return [game for game in list_games() if game.player_id == cedula]


def save_game(game: Game):
    GAMES_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(GAMES_FILE, "ab") as f:
        _write_record(f, game)
