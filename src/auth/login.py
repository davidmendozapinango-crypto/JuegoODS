from auth.player import Player
from common.errors import ValidationError
from persistence.players import find_player


def login(cedula: str, access_key: str) -> Player:
    cedula = cedula.strip()
    access_key = access_key.strip()

    if not cedula or not access_key:
        raise ValidationError("Cédula y clave son obligatorias")

    player = find_player(cedula)
    if player is None or player.access_key != access_key:
        raise ValidationError("Cédula o clave incorrecta")
    return player
