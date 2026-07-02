import pytest

from auth.player import Player
from auth.registration import register
from core.card import Card
from core.game import Game
from persistence.games import list_games
from persistence.players import find_player


def test_game_new():
    game = Game.new(
        "123456",
        5,
        1,
        [[1, 2, 3, 4, 5] for _ in range(5)],
        [[6, 7, 8, 9, 10] for _ in range(5)],
    )
    assert game.player_id == "123456"
    assert game.dimension == 5
    assert game.main_card_sum == 75


def test_full_game_flow(tmp_path, monkeypatch):
    monkeypatch.setattr("persistence.players.PLAYERS_FILE", tmp_path / "JUGADORES.bin")
    monkeypatch.setattr("persistence.games.GAMES_FILE", tmp_path / "JUEGOS.bin")

    register("123456", "Juan", "m", "2000-01-01", "CCS", "Aa1*bb")
    assert find_player("123456") is not None

    main, complement = Card.create_pair(5, 1)
    game = Game.new("123456", 5, 1, main.cells, complement.cells)

    numbers = list(range(1, 26))
    for number in numbers:
        main.mark_number(number)
        complement.mark_number(number)
        game.drawn_numbers.append(number)
        if main.is_winner() or complement.is_winner():
            break

    game.winner_card = "main" if main.is_winner() else "complement"
    from persistence.games import save_game

    save_game(game)

    games = list_games()
    assert len(games) == 1
    assert games[0].winner_card in ("main", "complement")
