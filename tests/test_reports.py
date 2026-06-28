import pytest

from auth.player import Player
from core.game import Game
from persistence.games import save_game
from persistence.players import register_player
from reports.export import export_report


def test_export_reports(tmp_path, monkeypatch):
    monkeypatch.setattr("persistence.players.PLAYERS_FILE", tmp_path / "JUGADORES.bin")
    monkeypatch.setattr("persistence.games.GAMES_FILE", tmp_path / "JUEGOS.bin")
    monkeypatch.setattr(
        "reports.export.export_report",
        lambda rt, fp, date_from=None, date_to=None: str(tmp_path / f"{rt}.txt"),
    )

    register_player(Player("123456", "Juan", "m", "2000-01-01", "CCS", "Aa1*bb"))
    game = Game.new(
        "123456",
        5,
        1,
        [[1, 2, 3, 4, 5] for _ in range(5)],
        [[6, 7, 8, 9, 10] for _ in range(5)],
    )
    game.winner_card = "main"
    save_game(game)

    for report_type in ["player_summary", "gantt", "logs", "top5"]:
        path = export_report(report_type, str(tmp_path / f"{report_type}.txt"))
        assert path.endswith(f"{report_type}.txt")
