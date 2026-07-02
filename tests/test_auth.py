import pytest

from auth.login import login
from auth.player import Player
from auth.profile import delete_profile, get_profile, update_profile
from auth.registration import register
from auth.validator import validate_key
from common.errors import DuplicateCedulaError, PlayerNotFoundError, ValidationError


def test_valid_key():
    valid, failures = validate_key("Aa1*bb")
    assert valid is True
    assert failures == []


def test_invalid_key_missing_uppercase():
    valid, failures = validate_key("aa1*bb")
    assert valid is False
    assert "key_uppercase" in failures


def test_invalid_key_missing_special():
    valid, failures = validate_key("Aa1bbb")
    assert valid is False
    assert "key_special" in failures


def test_invalid_key_too_many_consecutive():
    valid, failures = validate_key("Aaaaa1*bb")
    assert valid is False
    assert "key_consecutive" in failures


def test_invalid_key_too_short():
    valid, failures = validate_key("Aa1*")
    assert valid is False
    assert "key_length" in failures


def test_registration_and_login(tmp_path, monkeypatch):
    monkeypatch.setattr("persistence.players.PLAYERS_FILE", tmp_path / "JUGADORES.bin")
    player = register("123456", "Juan Pérez", "m", "2000-01-01", "CCS", "Aa1*bb")
    assert isinstance(player, Player)
    assert player.cedula == "123456"

    logged = login("123456", "Aa1*bb")
    assert logged.cedula == "123456"


def test_duplicate_cedula(tmp_path, monkeypatch):
    monkeypatch.setattr("persistence.players.PLAYERS_FILE", tmp_path / "JUGADORES.bin")
    register("123456", "Juan Pérez", "m", "2000-01-01", "CCS", "Aa1*bb")
    with pytest.raises(DuplicateCedulaError):
        register("123456", "Otro", "f", "2001-01-01", "CCS", "Bb2*cc")


def test_profile_update_and_delete(tmp_path, monkeypatch):
    monkeypatch.setattr("persistence.players.PLAYERS_FILE", tmp_path / "JUGADORES.bin")
    register("123456", "Juan Pérez", "m", "2000-01-01", "CCS", "Aa1*bb")

    updated = update_profile("123456", {"full_name": "Juan Actualizado"})
    assert updated.full_name == "Juan Actualizado"

    profile = get_profile("123456")
    assert profile.full_name == "Juan Actualizado"

    delete_profile("123456")
    assert get_profile("123456") is None
