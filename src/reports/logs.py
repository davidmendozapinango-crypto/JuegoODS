from typing import List, Optional

from core.game import Game
from persistence.games import list_games


def game_logs(
    date_from: Optional[str] = None, date_to: Optional[str] = None
) -> List[Game]:
    return list_games(date_from=date_from, date_to=date_to)
