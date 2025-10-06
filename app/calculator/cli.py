"""User-facing CLI (REPL) for the calculator."""

from typing import List
from app.calculation.factory import CalculationFactory
from app.calculation.history import History


HELP_TEXT = """
Commands:
  add 2 3              -> 5
  subtract 10 4        -> 6
  multiply 2 3 4       -> 24
  divide 8 2           -> 4

Special:
  help                 -> show this help
  history              -> show calculation history
  exit / quit          -> leave the program
""".strip()


class CalculatorCLI:
    def __init__(self) -> None:
        self.history = History()

    @staticmethod
    def _parse_numbers(parts: List[str]) -> List[float]:
        nums: List[float] = []
        for p in parts:
            try:
                nums.append(float(p))
            except ValueError as exc:
                raise ValueError(f"Invalid number: {p!r}") from exc
        return nums

    def handle_line(self, line: str) -> str:
        line = (line or "").strip()
        if not line:
            return ""

        lower = line.lower()
        if lower in {"help", "h", "?"}:
            return HELP_TEXT
        if lower in {"exit", "quit"}:
            return "Goodbye!"
        if lower == "history":
            if not self.history.all():
                return "(history is empty)"
            rows = []
            for i, c in enumerate(self.history.all(), start=1):
                rows.append(f"{i}. {c.operation.__name__}{tuple(c.operands)} = {c.execute()}")
            return "\n".join(rows)

        parts = line.split()
        op_name, arg_strings = parts[0], parts[1:]
        if not arg_strings:
            return "Please provide numbers, e.g.,: add 2 3"

        try:
            numbers = self._parse_numbers(arg_strings)
            calc = CalculationFactory.create(op_name, numbers)
            result = calc.execute()
            self.history.add(calc)
            return str(result)
        except Exception as exc:
            return f"Error: {exc}"

    def repl(self) -> None:
        print("Calculator — type 'help' for commands. Ctrl+C to exit.")  # pragma: no cover
        while True:  # pragma: no cover
            try:  # pragma: no cover
                line = input("> ")  # pragma: no cover
            except KeyboardInterrupt:  # pragma: no cover
                print("\nGoodbye!")  # pragma: no cover
                break  # pragma: no cover
            out = self.handle_line(line)  # pragma: no cover
            print(out)  # pragma: no cover
            if out == "Goodbye!":  # pragma: no cover
                break  # pragma: no cover
