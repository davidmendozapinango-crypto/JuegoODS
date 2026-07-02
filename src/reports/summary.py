from typing import Any, Dict, List, Optional

from persistence.games import list_games
from persistence.players import list_players


def player_summary(
    date_from: Optional[str] = None, date_to: Optional[str] = None
) -> List[Dict[str, Any]]:
    players = list_players()
    games = list_games(date_from=date_from, date_to=date_to)
    counts = {}
    for game in games:
        counts[game.player_id] = counts.get(game.player_id, 0) + 1

    result = []
    for player in players:
        result.append(
            {
                "cedula": player.cedula,
                "full_name": player.full_name,
                "total_games": counts.get(player.cedula, 0),
            }
        )
    return result
