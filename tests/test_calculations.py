import pytest
from app.calculation.factory import CalculationFactory
from app.calculation.history import History
from app.operation import add, subtract, multiply, divide


@pytest.mark.parametrize(
    "op,nums,fn",
    [
        ("add", [1, 2, 3], add),
        ("+", [1, 2], add),
        ("subtract", [5, 1], subtract),
        ("-", [5, 1], subtract),
        ("multiply", [2, 3, 4], multiply),
        ("*", [2, 3], multiply),
        ("divide", [8, 2], divide),
        ("/", [9, 3], divide),
    ],
)
def test_factory_builds_correct_operation(op, nums, fn):
    calc = CalculationFactory.create(op, nums)
    assert calc.operation is fn
    assert calc.operands == nums
    assert isinstance(str(calc.execute()), str)


def test_factory_unknown_operation():
    with pytest.raises(ValueError):
        CalculationFactory.create("pow", [2, 3])


def test_history_add_and_list_and_clear():
    h = History()
    c1 = CalculationFactory.create("add", [1, 2])
    c2 = CalculationFactory.create("multiply", [2, 3])

    h.add(c1)
    h.add(c2)
    items = h.all()
    assert len(items) == 2
    assert items[0].execute() == 3
    assert items[1].execute() == 6

    h.clear()
    assert h.all() == []


def test_cli_handle_line_happy_paths():
    from app.calculator.cli import CalculatorCLI
    cli = CalculatorCLI()

    # help text (new header "Commands:"), not the old "Calculator REPL"
    assert "Commands:" in cli.handle_line("help")
    assert cli.handle_line("add 2 3") == "5.0"
    assert "1. add" in cli.handle_line("history")
    assert cli.handle_line("divide 8 2") == "4.0"
    assert cli.handle_line("exit") == "Goodbye!"


def test_cli_handle_line_errors():
    from app.calculator.cli import CalculatorCLI
    cli = CalculatorCLI()
    assert "Error:" in cli.handle_line("add two three")     # invalid numbers
    assert "Unknown operation" in cli.handle_line("pow 2 3") # invalid op
    assert "Please provide numbers" in cli.handle_line("add")# missing args


def test_cli_edge_paths():
    from app.calculator.cli import CalculatorCLI
    cli = CalculatorCLI()
    assert cli.handle_line("") == ""                          # empty input
    assert cli.handle_line("history") == "(history is empty)" # empty history


def test_cli_aliases_and_symbols():
    from app.calculator.cli import CalculatorCLI
    cli = CalculatorCLI()
    assert "Commands:" in cli.handle_line("h")                # help alias
    assert "Commands:" in cli.handle_line("?")                # help alias '?'
    assert cli.handle_line("+ 1 2 3") == "6.0"                # symbol op
    assert cli.handle_line("* 2 3 4") == "24.0"               # symbol op
    assert cli.handle_line("/ 9 3") == "3.0"                  # symbol op
    assert cli.handle_line("quit") == "Goodbye!"              # quit alias


def test_cli_whitespace_and_case():
    from app.calculator.cli import CalculatorCLI
    cli = CalculatorCLI()
    assert cli.handle_line("   ADD   1   2   ") == "3.0"      # spaces + case
    assert cli.handle_line("   ") == ""                       # whitespace-only -> empty
