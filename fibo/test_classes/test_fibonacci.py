import pytest
from support_classes.Fibonacci import generateFibonacci_ForLoop

@pytest.mark.jirapi
def test_positive():
    expected = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    assert generateFibonacci_ForLoop(10) == expected


@pytest.mark.jirapi
def test_0():
    expected = []
    assert generateFibonacci_ForLoop(0) == expected


@pytest.mark.jirapi
def test_minus_int():
    expected = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    assert generateFibonacci_ForLoop(-15) == expected


@pytest.mark.jirapi
def test_not_valid_type():
    expected = "please, enter int number"
    assert generateFibonacci_ForLoop("22") == expected
