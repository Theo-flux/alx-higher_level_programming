#!/usr/bin/python3
""" Define the base class
"""


class Base:
	""" Representation of Base class
	"""
	__nb_objects = 0
	
	def __init__(self, id=None):
		""" class constructor
		
		Args:
		     id (int): object instance id
		"""
		if id != None:
			self.id = id
		else:
			Base.__nb_objects += 1
			self.id = Base.__nb_objects
