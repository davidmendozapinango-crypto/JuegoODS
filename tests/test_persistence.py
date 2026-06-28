import pytest

from auth.player import Player
from common.errors import CorruptedDataError
from core.game import Game
from persistence.games import list_games, save_game
from persistence.players import (
    delete_player,
    find_player,
    list_players,
    register_player,
    update_player,
)


def test_register_and_find_player(tmp_path, monkeypatch):
    monkeypatch.setattr("persistence.players.PLAYERS_FILE", tmp_path / "JUGADORES.bin")
    player = Player("123456", "Juan", "m", "2000-01-01", "CCS", "Aa1*bb")
    register_player(player)
    found = find_player("123456")
    assert found is not None
    assert found.full_name == "Juan"


def test_list_players_empty(tmp_path, monkeypatch):
    monkeypatch.setattr("persistence.players.PLAYERS_FILE", tmp_path / "JUGADORES.bin")
    assert list_players() == []


def test_update_and_delete_player(tmp_path, monkeypatch):
    monkeypatch.setattr("persistence.players.PLAYERS_FILE", tmp_path / "JUGADORES.bin")
    register_player(Player("123456", "Juan", "m", "2000-01-01", "CCS", "Aa1*bb"))
    update_player("123456", {"full_name": "Pedro"})
    assert find_player("123456").full_name == "Pedro"
    delete_player("123456")
    assert find_player("123456") is None


def test_save_and_list_games(tmp_path, monkeypatch):
    monkeypatch.setattr("persistence.players.PLAYERS_FILE", tmp_path / "JUGADORES.bin")
    monkeypatch.setattr("persistence.games.GAMES_FILE", tmp_path / "JUEGOS.bin")
    game = Game.new(
        "123456",
        5,
        1,
        [[1, 2, 3, 4, 5] for _ in range(5)],
        [[6, 7, 8, 9, 10] for _ in range(5)],
    )
    game.drawn_numbers = [1, 2, 3]
    game.winner_card = "main"
    save_game(game)
    games = list_games()
    assert len(games) == 1
    assert games[0].player_id == "123456"
