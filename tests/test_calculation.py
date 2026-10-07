import pytest

from calculator.calculation import Calculation
from calculator.operations import Operations


def test_construction_defers_execution_and_snapshots_inputs():
    calls = []

    def operation(a, b):
        calls.append((a, b))
        return a + b

    values = [2, 3]

    calculation = Calculation(values, operation)

    values.clear()

    assert calls == []
    assert calculation.get_result() == 5
    assert calls == [(2, 3)]


def test_zero_division_occurs_during_execution():
    calculation = Calculation([1, 0], Operations.divide)

    with pytest.raises(ZeroDivisionError):
        calculation.get_result()


def test_reject_nonfinite_result():
    calculation = Calculation(
        [1e308, 1e308],
        Operations.multiply,
    )

    with pytest.raises(ValueError, match="range"):
        calculation.get_result()