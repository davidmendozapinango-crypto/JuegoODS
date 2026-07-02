from typing import List


def card_sum(cells: List[List[int]]) -> int:
    return sum(sum(row) for row in cells)
