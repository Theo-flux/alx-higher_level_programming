#!/usr/bin/python3
"""The 0-rectangle module file"""


class Rectangle:
    """A representation of a simple rectangle type"""
    
    def __init__(self, width=0, height=0):
        """The instance method called when a new rectangle is created
        
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get/set the width"""
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
        """Get/set the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height mus be >= 0")
        self.__height =  value
