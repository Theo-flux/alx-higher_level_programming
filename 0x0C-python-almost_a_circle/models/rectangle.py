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
		for _ in range (0, self.__y):
			print("".format(), end="\n")
		for _ in range(0, self.__height):
			print("{}{}".format(" "*self.__x, "#"*self.__width), end="\n")
	
	def update(self, *args, **kwargs):
		""" Update class

		Args:
		     *args (non-keyword arguments):
			1st argument should be the id attribute
			2nd argument should be the width attribute
			3rd argument should be the height attribute
			4th argument should be the x attribute
			5th argument should be the y attribute

		      **kwargs (keyword arguments):
			each key represents the the attribute to the instance
		"""
		if args and len(args) != 0:
			a = 0
			for arg in args:
				if a == 0:
					self.id = arg
				elif a == 1:
					self.__width = arg
				elif a == 2:
					self.__height = arg
				elif a == 3:
					self.__x = arg
				elif a == 4:
					self.__y = arg
				a += 1
		elif kwargs and len(kwargs) != 0:
			for key, value in kwargs.items():
				if key == "id":
					self.id = value
				elif key == "width":
					self.__width = value
				elif key == "height":
					self.__height = value
				elif key == "x":
					self.__x = value
				elif key == "y":
					self.__y = value


	def __str__(self):
		stringified = "[{}] ({}) {}/{} - {}/{}"\
				.format(self.__class__.__name__,\
				self.id, self.__x, self.__y,\
				self.__width, self.__height)
		return stringified
