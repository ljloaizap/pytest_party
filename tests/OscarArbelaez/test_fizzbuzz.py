"""Module test_fizzbuzz """
import pytest
from src.OscarArbelaez.fizzbuzz.algorithm import fizzbuzz


@pytest.mark.parametrize(
    'example',
    [3, 6, 9, 12]
)
def test_returns_fizz_for_multiple_of_3(example):
    """Placeholder docString"""
    assert fizzbuzz(example) == 'fizz'


@pytest.mark.parametrize(
    'example',
    [5, 10, 20, 25]
)
def test_returns_buzz_for_multiple_of_5(example):
    """Placeholder docString"""
    assert fizzbuzz(example) == 'buzz'


@pytest.mark.parametrize(
    'example',
    [15, 30, 45, 60]
)
def test_returns_buzz_for_multiple_of_15(example):
    """Placeholder docString"""
    assert fizzbuzz(example) == 'fizzbuzz'


def test_returns_number_for_any_other_number():
    """Placeholder docString"""
    assert fizzbuzz(2) == 2
