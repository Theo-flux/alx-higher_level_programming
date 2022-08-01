#!/usr/bin/python3
"""Define a derived class"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
	"""Representation of Rectangle"""
	
	def __init__(self, width, height):
		"""Instantiation with width and height
		
		Args:
	             width (int): width of the rectangle
		     height (int): height of the rectangle
		"""
		
		super().integer_validator("width", width)
		self.__width = width
		super().integer_validator("height", height)
		self.__height = height
