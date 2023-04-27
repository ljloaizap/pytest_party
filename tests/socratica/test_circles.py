"""Placeholder module"""

import unittest
from math import pi
from src.socratica.circles import get_circle_area


class TestCircleArea(unittest.TestCase):
    """Placeholder class"""

    def test_area(self):
        """Placeholder function"""
        # Test areas when radius >= 0
        self.assertAlmostEqual(get_circle_area(1), pi)
        self.assertAlmostEqual(get_circle_area(0), 0)
        self.assertAlmostEqual(get_circle_area(2.1), pi * 2.1**2)

    def test_values(self):
        """Placeholder function"""
        # Make sure value errors are raised when necessary
        self.assertRaises(ValueError, get_circle_area, -2)

    def test_types(self):
        """Placeholder function"""
        # Make sure type errors are raised when necessary
        self.assertRaises(TypeError, get_circle_area, 3+5j)
        self.assertRaises(TypeError, get_circle_area, True)
        self.assertRaises(TypeError, get_circle_area, "radius")
