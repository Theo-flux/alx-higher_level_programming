#!/usr/bin/python3
"""Define a derived class"""


Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
	"""Representation of Square"""
	
	def __init__(self, size):
		"""Instantiation with width and height
		
		Args:
	             size (int): size of the square
		"""
		
		super().integer_validator("size", size)
		self.__size = size
		super().__init__(self.__size, self.__size)

	def area(self):
		"""Area of square"""
		return self.__size**2
