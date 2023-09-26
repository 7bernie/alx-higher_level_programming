#!/usr/bin/python3
"""Square generation module for Python Size validation
"""


class Square:
    """class defined for square generation
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
