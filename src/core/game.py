from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class Game:
    player_id: str
    played_at: str
    dimension: int
    theme_id: int
    main_card_cells: List[List[int]] = field(default_factory=list)
    complement_card_cells: List[List[int]] = field(default_factory=list)
    drawn_numbers: List[int] = field(default_factory=list)
    winner_card: str = "none"
    main_card_sum: int = 0
    complement_card_sum: int = 0

    @classmethod
    def new(
        cls,
        player_id: str,
        dimension: int,
        theme_id: int,
        main_card_cells: List[List[int]],
        complement_card_cells: List[List[int]],
    ) -> "Game":
        return cls(
            player_id=player_id,
            played_at=datetime.now().isoformat(),
            dimension=dimension,
            theme_id=theme_id,
            main_card_cells=main_card_cells,
            complement_card_cells=complement_card_cells,
            drawn_numbers=[],
            winner_card="none",
            main_card_sum=sum(sum(row) for row in main_card_cells),
            complement_card_sum=sum(sum(row) for row in complement_card_cells),
        )
