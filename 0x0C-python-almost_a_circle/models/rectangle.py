#!/usr/bin/python3
""" Define a Rectangle class
"""
from models.base import Base

class Rectangle(Base):
	""" Representation of Rectangle
	Child class to Base class
	"""
	
	def __init__(self, width, height, x=0, y=0, id=None):
		""" Class constructor
		
		Args:
		     width (int): width of rectangle
		     height (int): height of rectangle
		     x (int): x coordinate of rectangle
		     y (int): y coordinate of rectangle
		     id (int): id of rectangle
		"""
		super().__init__(id)
		if type(width) != int:
			raise TypeError("width must be an integer")
		if type(height) != int:
			raise TypeError("height must be an integer")
		if type(x) != int:
			raise TypeError("x must be an integer")
		if type(y) != int:
			raise TypeError("y must be an integer")
		if width <= 0:
			raise ValueError("width must be > 0")
		if height <= 0:
			raise ValueError("height must be > 0")
		if x < 0:
			raise ValueError("x must be >= 0")
		if y < 0:
			raise ValueError("y must be >= 0")
		
		self.__width = width
		self.__height = height
		self.__x = x
		self.__y = y
		
	@property
	def width(self):
		return self.__width
	
	@width.setter
	def width(self, value):
		if type(value) != int:
			raise TypeError("width must be an integer")
		if value <= 0:
			raise ValueError("width must be > 0")	
		self.__width = value
	
	@property
	def height(self):
		return self.__height
	
	@height.setter
	def height(self, value):
		if type(value) != int:
			raise TypeError("height must be an integer")
		if value <= 0:
			raise ValueError("height must be > 0")	
		self.__height = value
	
	@property
	def x(self):
		return self.__x
	
	@x.setter
	def x(self, value):
		if type(value) != int:
			raise TypeError("x must be an integer")
		if value < 0:
			raise ValueError("x must be >= 0")		
		self.__x = value

	@property
	def y(self):
		return self.__y

	@y.setter
	def y(self, value):
		if type(value) != int:
			raise TypeError("y must be an integer")
		if value < 0:
			raise ValueError("y must be >= 0")
		self.__y = value
	
	def area(self):
		return self.__width*self.__height
	
	def display(self):
		for _ in range(0, self.__height):
			print("{}".format("#"*self.__width), end="\n")
