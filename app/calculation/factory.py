"""Factory to build Calculation objects from user-intent strings."""

from typing import List, Callable, Dict
from app.operation import add, subtract, multiply, divide
from .calculation import Calculation


class CalculationFactory:
    _OPS: Dict[str, Callable[..., float]] = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    @classmethod
    def create(cls, op_name: str, operands: List[float]) -> Calculation:
        op_name = (op_name or "").strip().lower()
        if op_name not in cls._OPS:
            raise ValueError(f"Unknown operation: {op_name!r}")
        return Calculation(operation=cls._OPS[op_name], operands=operands)
