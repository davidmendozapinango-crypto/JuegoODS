import struct
from io import BytesIO
from typing import List, Optional

from auth.player import Player
from common.errors import (
    CorruptedDataError,
    DuplicateCedulaError,
    PlayerNotFoundError,
    ValidationError,
)
from config import PLAYERS_FILE


def _encode_text(text: str) -> bytes:
    data = text.encode("utf-8")
    if len(data) > 255:
        raise ValidationError("Texto demasiado largo")
    return data


def _write_text(f, text: str):
    data = _encode_text(text)
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


def _validate_player(player: Player):
    if not player.cedula:
        raise ValidationError("La cédula es obligatoria")
    if not player.full_name:
        raise ValidationError("El nombre es obligatorio")
    if player.sex not in ("m", "f"):
        raise ValidationError("Sexo inválido")
    if len(player.state_code) != 3:
        raise ValidationError("Código de estado inválido")


def _write_record(f, player: Player):
    _validate_player(player)
    _write_text(f, player.cedula)
    _write_text(f, player.full_name)
    f.write(struct.pack("B", 1))
    f.write(player.sex.encode("ascii"))
    f.write(player.birthdate.encode("ascii"))
    f.write(player.state_code.encode("ascii"))
    _write_text(f, player.access_key)


def _read_record(f) -> Player:
    try:
        cedula = _read_text(f)
        full_name = _read_text(f)
        sex_len = struct.unpack("B", f.read(1))[0]
        sex = f.read(sex_len).decode("ascii")
        birthdate = f.read(10).decode("ascii")
        state_code = f.read(3).decode("ascii")
        access_key = _read_text(f)
        return Player(
            cedula=cedula,
            full_name=full_name,
            sex=sex,
            birthdate=birthdate,
            state_code=state_code,
            access_key=access_key,
        )
    except (struct.error, UnicodeDecodeError, ValueError) as exc:
        raise CorruptedDataError("Registro de jugador corrupto") from exc


def list_players() -> List[Player]:
    if not PLAYERS_FILE.exists():
        return []
    players = []
    with open(PLAYERS_FILE, "rb") as f:
        while True:
            try:
                players.append(_read_record(f))
            except CorruptedDataError as exc:
                if "Fin inesperado" in str(exc):
                    break
                raise
    return players


def find_player(cedula: str) -> Optional[Player]:
    for player in list_players():
        if player.cedula == cedula:
            return player
    return None


def register_player(player: Player):
    _validate_player(player)
    if find_player(player.cedula) is not None:
        raise DuplicateCedulaError("La cédula ya está registrada")
    PLAYERS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(PLAYERS_FILE, "ab") as f:
        _write_record(f, player)


def _rewrite_players(players: List[Player]):
    PLAYERS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(PLAYERS_FILE, "wb") as f:
        for player in players:
            _write_record(f, player)


def update_player(cedula: str, changes: dict) -> Player:
    players = list_players()
    target = None
    for idx, player in enumerate(players):
        if player.cedula == cedula:
            target = idx
            break
    if target is None:
        raise PlayerNotFoundError("Jugador no encontrado")

    new_cedula = changes.get("cedula", players[target].cedula)
    if new_cedula != players[target].cedula:
        for player in players:
            if player.cedula == new_cedula:
                raise DuplicateCedulaError(
                    "La cédula ya está registrada por otro jugador"
                )

    updated = Player(
        cedula=new_cedula,
        full_name=changes.get("full_name", players[target].full_name),
        sex=changes.get("sex", players[target].sex),
        birthdate=changes.get("birthdate", players[target].birthdate),
        state_code=changes.get("state_code", players[target].state_code),
        access_key=changes.get("access_key", players[target].access_key),
    )
    _validate_player(updated)
    players[target] = updated
    _rewrite_players(players)
    return updated


def delete_player(cedula: str):
    players = list_players()
    filtered = [p for p in players if p.cedula != cedula]
    if len(filtered) == len(players):
        raise PlayerNotFoundError("Jugador no encontrado")
    _rewrite_players(filtered)
