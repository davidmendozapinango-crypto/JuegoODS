from typing import Optional

from auth.player import Player
from auth.validator import validate_key
from common.errors import ValidationError
from config import STATE_CODES
from persistence.players import delete_player, find_player, update_player


def get_profile(cedula: str) -> Optional[Player]:
    return find_player(cedula)


def update_profile(cedula: str, changes: dict) -> Player:
    allowed = {"full_name", "state_code", "access_key", "cedula"}
    filtered = {k: v for k, v in changes.items() if k in allowed}

    if "access_key" in filtered:
        valid, failures = validate_key(filtered["access_key"])
        if not valid:
            raise ValidationError(f"Clave inválida: {', '.join(failures)}")

    if "state_code" in filtered:
        if filtered["state_code"].upper() not in STATE_CODES:
            raise ValidationError("Código de estado inválido")
        filtered["state_code"] = filtered["state_code"].upper()

    return update_player(cedula, filtered)


def delete_profile(cedula: str):
    delete_player(cedula)
