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
	
	def to_json_string(list_dictionaries):
		""" Dictionary to JSON string
		
		Args:
		     	list_dictionaries (list): list of dictionaries

		Returns:
			the JSON string representation of list_dictionaries
		"""
		import json

		if list_dictionaries == None or list_dictionaries == []:
			return "[]"
		return json.dumps(list_dictionaries)
		
