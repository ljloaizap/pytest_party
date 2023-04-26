"""Module test_main"""
import pytest
from src.UskoKruM2010.main import *


def test_my_sum():
    assert my_sum(2, 5) == 7


def test_is_greater_than():
    assert is_greater_than(10, 2)


@pytest.mark.parametrize(
    ('x', 'y', 'expected'),
    [
        (5, 1, 6),
        (12, 4, 16),
        (12, my_sum(1, 5), 18),
        (9, 3, 12)
    ]
)
def test_my_sum_params(x, y, expected):
    assert my_sum(x, y) == expected


def test_login_pass():
    assert login("admin", "123")


def test_login_fails():
    assert not login("xyz", "000")
