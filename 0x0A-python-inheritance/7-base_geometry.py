#!/usr/bin/python3
"""Define an empty class"""


class BaseGeometry:
	"""Representation of BaseGeometry data type"""
	
	def area(self):
		"""Public instance method"""
		raise Exception("area() is not implemeneted")
	
	def integer_validator(self, name, value):
		"""Public instance method that validates value
		
		Args:
	             name (str): name variable
		     value (int): value variable
		"""
		if type(value) != int:
			raise TypeError("{} must be an integer".format(name))
		
		if value <= 0:
			raise ValueError("{} must be greater than 0".format(name))
