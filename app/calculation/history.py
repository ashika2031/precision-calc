"""In-memory history for the current calculator session."""

from typing import List
from .calculation import Calculation


class History:
    def __init__(self) -> None:
        self._items: List[Calculation] = []

    def add(self, calculation: Calculation) -> None:
        self._items.append(calculation)

    def all(self) -> List[Calculation]:
        return list(self._items)

    def clear(self) -> None:
        self._items.clear()

    def __len__(self) -> int:  # pragma: no cover
        return len(self._items)
