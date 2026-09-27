import pytest 

from calculator.calculation import Add, Calculation, Subtract

def test_add():
    calculation = Add(10, 5)
    result = calculation.get_result()
    assert result == 15


def test_instances_have_their_own_operands():
    first = Add(10, 5)
    second = Add(100, 50)

    first.a = 20

    assert first.get_result() == 25
    assert second.a == 100
    assert second.b == 50   
    assert second.get_result() == 150


def test_negative_operand():
    assert Add(-10, 5).get_result() == -5   


def test_zero_operand():
    assert Add(0,0).get_result() == 0


def test_add_does_not_change_operands():
    calculation = Add(8, -3)

    assert calculation.get_result() == 5
    assert calculation.a == 8
    assert calculation.b == -3   



def test_subtract():
    assert Subtract(20,7).get_result() == 13


def test_subtract_negative_result():
    assert Subtract(5, 10).get_result() == -5



def test_calculation_is_abstract():
    with pytest.raises(TypeError):
        Calculation(10, 5)

def test_polymorphism():
    calculations = [Add(10, 5), Subtract(20, 7)]
    results = []

    for calculation in calculations:
        results.append(calculation.get_result())

    assert results == [15, 13]



def test_multiple_calculations():
    calculations = [
        Add(12,8),
        Subtract(3,9),
        Add(-4,10)
    ]

    results = []

    for calculation in calculations:
        results.append(calculation.get_result())

    assert results == [20, -6, 6]