from dataclasses import dataclass, field
from typing import List, Tuple
import random


@dataclass
class Card:
    dimension: int
    theme_id: int
    cells: List[List[int]] = field(default_factory=list)
    marked: List[List[bool]] = field(default_factory=list)
    filling_sequence: List[Tuple[int, int]] = field(default_factory=list)
    figure_mask: List[List[bool]] = field(default_factory=list)

    def __post_init__(self):
        if not self.cells:
            self._generate()

    def _generate(self):
        n = self.dimension
        numbers = list(range(1, n * n + 1))
        random.shuffle(numbers)

        self.cells = [[0] * n for _ in range(n)]
        self.marked = [[False] * n for _ in range(n)]
        self.filling_sequence = []
        idx = 0
        for i in range(n):
            for j in range(n):
                self.cells[i][j] = numbers[idx]
                self.filling_sequence.append((i, j))
                idx += 1

        self.figure_mask = self._build_figure_mask()

    def _build_figure_mask(self) -> List[List[bool]]:
        n = self.dimension
        return [[True] * n for _ in range(n)]

    def mark_number(self, number: int) -> bool:
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.cells[i][j] == number:
                    self.marked[i][j] = True
                    return True
        return False

    def is_winner(self) -> bool:
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.figure_mask[i][j] and not self.marked[i][j]:
                    return False
        return True

    def sum_cells(self) -> int:
        return sum(sum(row) for row in self.cells)

    @classmethod
    def create_pair(cls, dimension: int, theme_id: int) -> Tuple["Card", "Card"]:
        main = cls(dimension=dimension, theme_id=theme_id)
        complement = cls(dimension=dimension, theme_id=theme_id)
        return main, complement
