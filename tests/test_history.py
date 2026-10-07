import pytest

from calculator.calculation import Calculation
from calculator.history import History
from calculator.operations import Operations


def test_empty_history():
    assert History().get_history() == []


def test_mixed_calculations_keep_their_order():
    history = History()

    first = Calculation(10, 5, Operations.add)
    second = Calculation(20, 7, Operations.subtract)

    first_result = first.get_result()
    second_result = second.get_result()

    history.add(first, first_result)
    history.add(second, second_result)

    assert history.get_history() == [
        (first, first_result),
        (second, second_result),
    ]


def test_returned_list_is_a_copy():
    history = History()

    calculation = Calculation(10, 5, Operations.add)
    result = calculation.get_result()

    history.add(calculation, result)

    snapshot = history.get_history()
    snapshot.clear()

    assert history.get_history() == [(calculation, result)]


def test_histories_are_independent():
    first_history = History()
    second_history = History()

    calculation = Calculation(10, 5, Operations.add)
    result = calculation.get_result()

    first_history.add(calculation, result)

    assert second_history.get_history() == []


def test_reject_non_calculation():
    history = History()

    with pytest.raises(TypeError):
        history.add("not a calculation", 15)

    assert history.get_history() == []


def test_clear_history():
    history = History()

    first = Calculation(1, 2, Operations.add)
    second = Calculation(5, 1, Operations.subtract)

    history.add(first, first.get_result())
    history.add(second, second.get_result())

    history.clear()

    assert history.get_history() == []