#!/usr/bin/python3
"""Defines a class TestRectangleMethods"""

from unittest.mock import patch
import unittest
import json
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle

class TestRectangleMethods(unittest.TestCase):
    """ Defines tests for Rectangle class """

    @classmethod
    def setUp(self):
        """ Runs for each test """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ Cleans up after each test """
        pass

    # ... (existing test methods)

    def test_width_zero(self):
        """ Test creating Rectangle with width equal to 0 """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_height_zero(self):
        """ Test creating Rectangle with height equal to 0 """
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)

if __name__ == "__main__":
    unittest.main()

