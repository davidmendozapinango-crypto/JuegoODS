from collections import defaultdict
from typing import List, Optional, Tuple

from persistence.games import list_games


def top_players(
    date_from: Optional[str] = None, date_to: Optional[str] = None, top: int = 5
) -> List[Tuple[str, int]]:
    games = list_games(date_from=date_from, date_to=date_to)
    points = defaultdict(int)
    for game in games:
        if game.winner_card in ("main", "both"):
            points[game.player_id] += game.main_card_sum
        if game.winner_card in ("complement", "both"):
            points[game.player_id] += game.complement_card_sum
    return sorted(points.items(), key=lambda x: x[1], reverse=True)[:top]
