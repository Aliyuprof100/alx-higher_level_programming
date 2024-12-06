#!/usr/bin/python3
"""This is the header of the files"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """Instantiation method"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width of the parent class"""
        return self.__width

    @property
    def height(self):
        """Height"""
        return self.__height

    @width.setter
    def width(self, value):
        """ width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setting height property"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value