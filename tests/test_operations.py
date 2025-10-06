import pytest
from app.operation import add, subtract, multiply, divide


@pytest.mark.parametrize(
    "inputs,expected",
    [
        ((1, 2, 3), 6.0),
        ((-1, 1), 0.0),
        ((2.5, 2.5), 5.0),
        ((), 0.0),
    ],
)
def test_add(inputs, expected):
    assert add(*inputs) == pytest.approx(expected)


@pytest.mark.parametrize("a,b,expected", [(5, 3, 2.0), (0, 10, -10.0), (2.5, 0.5, 2.0)])
def test_subtract(a, b, expected):
    assert subtract(a, b) == pytest.approx(expected)


@pytest.mark.parametrize(
    "inputs,expected",
    [
        ((2, 3, 4), 24.0),
        ((-1, 5), -5.0),
        ((2.5, 0), 0.0),
        ((1,), 1.0),
    ],
)
def test_multiply(inputs, expected):
    assert multiply(*inputs) == pytest.approx(expected)


def test_divide_ok():
    assert divide(8, 2) == 4.0


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


@pytest.mark.parametrize("bad", [None, "x", object()])
def test_non_numeric_raises(bad):
    with pytest.raises(TypeError):
        add(1, bad)
