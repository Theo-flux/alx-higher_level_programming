#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of rectanlge"""
        return (self.__height * self.__width)

    def perimeter(self):
        """returns the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2*self.__height + 2*self.__width)

    def __str__(self):
        """instance methof for 'inofrmal' rep of object"""
        if self.__height == 0 and self.__width == 0:
            return ""
        i = 0
        val = []
        while i < self.__height:
            val.append("{}".format("#"*self.__width))
            if i != self.__height - 1:
                val.append("\n")
            i = 1 + i
        return("".join(val))
