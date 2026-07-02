from typing import List

from ods.data import get_ods_themes


def get_rotating_messages() -> List[str]:
    return [theme["slogan"] for theme in get_ods_themes()]


def get_message_for_theme(theme_id: int) -> str:
    from ods.data import get_theme

    return get_theme(theme_id)["slogan"]
