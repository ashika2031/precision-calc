"""Calculation entity & behavior."""

from dataclasses import dataclass
from typing import Callable, List


@dataclass(frozen=True)
class Calculation:
    """Represents a single calculation with an operation and operands."""
    operation: Callable[..., float]
    operands: List[float]

    def execute(self) -> float:
        return self.operation(*self.operands)
