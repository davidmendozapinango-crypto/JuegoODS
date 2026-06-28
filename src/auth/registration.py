from auth.player import Player
from auth.validator import validate_key
from common.errors import ValidationError
from config import STATE_CODES
from persistence.players import register_player as persist_player


def register(
    cedula: str,
    full_name: str,
    sex: str,
    birthdate: str,
    state_code: str,
    access_key: str,
) -> Player:
    cedula = cedula.strip()
    full_name = full_name.strip()
    sex = sex.strip().lower()
    state_code = state_code.strip().upper()
    access_key = access_key.strip()

    if not cedula:
        raise ValidationError("La cédula es obligatoria")
    if not full_name:
        raise ValidationError("El nombre es obligatorio")
    if sex not in ("m", "f"):
        raise ValidationError("Sexo inválido")
    if state_code not in STATE_CODES:
        raise ValidationError("Código de estado inválido")

    valid, failures = validate_key(access_key)
    if not valid:
        raise ValidationError(f"Clave inválida: {', '.join(failures)}")

    player = Player(
        cedula=cedula,
        full_name=full_name,
        sex=sex,
        birthdate=birthdate,
        state_code=state_code,
        access_key=access_key,
    )
    persist_player(player)
    return player
