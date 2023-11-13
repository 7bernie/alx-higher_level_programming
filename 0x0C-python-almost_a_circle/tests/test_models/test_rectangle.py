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

    def test_docstring(self):
        """ Test if docstring is present """
        self.assertIsNotNone(Rectangle.__doc__)

    def test_randos_id(self):
        """ Test random arguments passed """
        # ... (existing test code)

    def test_width_height_1(self):
        """ Test for width and height types"""
        # ... (existing test code)

    def test_width_height_2(self):
        """ Test for width and height ranges"""
        # ... (existing test code)

    def test_zero_width_height(self):
        """ Test for width or height being zero """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 0)

    def test_area_1(self):
        """ Test area """
        # ... (existing test code)

    def test_area_2(self):
        """ Checking the return value of area method """
        # ... (existing test code)

    def test_basic_display(self):
        """ Test display without x and y """
        # ... (existing test code)

    def test_basic_display_2(self):
        """ Test string printed """
        # ... (existing test code)

    # ... (other existing test methods)

    def test_load_from_file_1(self):
        """ Test load from file if file non-existent """
        # ... (existing test code)

if __name__ == '__main__':
    unittest.main()

