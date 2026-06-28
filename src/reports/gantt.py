from collections import Counter
from typing import List, Optional, Tuple

from persistence.games import list_games


def gantt_frequencies(
    date_from: Optional[str] = None, date_to: Optional[str] = None, top: int = 10
) -> List[Tuple[int, int]]:
    games = list_games(date_from=date_from, date_to=date_to)
    counter = Counter()
    for game in games:
        for number in game.drawn_numbers:
            counter[number] += 1
    return counter.most_common(top)
