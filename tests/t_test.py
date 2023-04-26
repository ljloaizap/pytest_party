"""DocString"""

import unittest
import pytest
from src import t


# region functions

def test_square():
    assert t.square(5) == 25


def test_square_float():
    assert t.square(3.) == 9.


# # Not recommended. Code smell?
# def test_square_float_approx():
#     assert t.square(3.) == pytest.approx(10.)


@pytest.mark.parametrize(
    ('input_n', 'expected'),
    (
        (5, 25),
        (3., 9.)
    )
)
def test_square_params(input_n, expected):
    print(f'{input_n=}')
    assert t.square(input_n) == expected

# endregion


# region classes

# Note: Better to avoid classes. If need to group, tend to use
# different modules for it.

class TestSquare:
    def test_square(self):
        assert t.square(3) == 9

# endregion


# region Legacy tests with unittest

class TestLegacy(unittest.TestCase):
    def test(self):
        self.assertEqual(t.square(3), 9)

# endregion
