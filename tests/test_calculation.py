import pytest

from calculator.calculation import Calculation
from calculator.operations import Operations


def test_add():
    calculation = Calculation(10, 5, Operations.add)
    assert calculation.get_result() == 15


def test_instances_have_their_own_operands():
    first = Calculation(10, 5, Operations.add)
    second = Calculation(100, 50, Operations.add)

    first.a = 20

    assert first.get_result() == 25
    assert second.a == 100
    assert second.b == 50
    assert second.get_result() == 150


def test_negative_operand():
    calculation = Calculation(-10, 5, Operations.add)
    assert calculation.get_result() == -5


def test_zero_operand():
    calculation = Calculation(0, 0, Operations.add)
    assert calculation.get_result() == 0


def test_add_does_not_change_operands():
    calculation = Calculation(8, -3, Operations.add)

    assert calculation.get_result() == 5
    assert calculation.a == 8
    assert calculation.b == -3


def test_subtract():
    calculation = Calculation(20, 7, Operations.subtract)
    assert calculation.get_result() == 13


def test_subtract_negative_result():
    calculation = Calculation(5, 10, Operations.subtract)
    assert calculation.get_result() == -5


def test_multiply():
    calculation = Calculation(4, 5, Operations.multiply)
    assert calculation.get_result() == 20


def test_divide():
    calculation = Calculation(10, 4, Operations.divide)
    assert calculation.get_result() == pytest.approx(2.5)


def test_different_operations_use_same_calculation_class():
    calculations = [
        Calculation(10, 5, Operations.add),
        Calculation(20, 7, Operations.subtract),
        Calculation(4, 5, Operations.multiply),
        Calculation(10, 2, Operations.divide),
    ]

    results = [calculation.get_result() for calculation in calculations]

    assert results == [15, 13, 20, 5]


def test_multiple_calculations():
    calculations = [
        Calculation(12, 8, Operations.add),
        Calculation(3, 9, Operations.subtract),
        Calculation(-4, 10, Operations.add),
    ]

    results = [calculation.get_result() for calculation in calculations]

    assert results == [20, -6, 6]


def test_decimal_addition():
    calculation = Calculation(0.1, 0.2, Operations.add)
    assert calculation.get_result() == pytest.approx(0.3)


def test_decimal_subtraction():
    calculation = Calculation(1.5, 0.25, Operations.subtract)
    assert calculation.get_result() == pytest.approx(1.25)


def test_subtract_two_negative_operands():
    calculation = Calculation(-10, -5, Operations.subtract)
    assert calculation.get_result() == -5


def test_subtract_zero_operands():
    calculation = Calculation(0, 0, Operations.subtract)
    assert calculation.get_result() == 0



def test_rejects_non_finite_result():
    def infinite_result(a, b):
        return float("inf")

    calculation = Calculation(1, 2, infinite_result)

    with pytest.raises(ValueError, match="Result is outside the supported range."):
        calculation.get_result()