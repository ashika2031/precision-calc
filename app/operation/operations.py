"""Primitive arithmetic operations with basic validation."""

from typing import Iterable, List


def _validate_numbers(values: Iterable[float]) -> List[float]:
    cleaned = []
    for v in values:
        if isinstance(v, (int, float)):
            cleaned.append(float(v))
        else:
            raise TypeError(f"Non-numeric value: {v!r}")
    return cleaned


def add(*args: float) -> float:
    nums = _validate_numbers(args)
    return sum(nums)


def subtract(a: float, b: float) -> float:
    (a1, b1) = _validate_numbers((a, b))
    return a1 - b1


def multiply(*args: float) -> float:
    nums = _validate_numbers(args)
    result = 1.0
    for n in nums:
        result *= n
    return result


def divide(a: float, b: float) -> float:
    (a1, b1) = _validate_numbers((a, b))
    try:
        return a1 / b1
    except ZeroDivisionError as exc:
        raise ZeroDivisionError("Division by zero is not allowed.") from exc
