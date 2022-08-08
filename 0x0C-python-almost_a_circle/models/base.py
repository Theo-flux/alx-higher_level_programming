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

	@staticmethod
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

	@staticmethod
	def from_json_string(json_string):
		""" converts json to string
		
		Args:
		     json_string (list): is a string representing a list of
		     dictionaries
		
		Returns:
		     list of the JSON string representation
		"""
		import json
		if json_string == None  or json_string == []:
			return []
		return json.loads(json_string)	
	
	@classmethod
	def save_to_file(cls, list_objs):
		""" saves lists to file
		
		Args:
		     list_objs (list): list of dictionaries
		"""
		filename = "{}.json".format(cls.__name__)
		with open(filename, mode="w") as f:
			res = ""
			if list_objs == None:
				res = cls.to_json_string([])
			else:
				res = [obj.to_dictionary() for obj in list_objs]
			f.write(cls.to_json_string(res))

	@classmethod
	def create(cls, **dictionary):
		""" create- classmethod
		
		Args:
		    **dictionary (keyword args): double pointer to a dictionary
			
		Return:
		    instance with all attributes already set.
		"""
		if dictionary and dictionary != {}:
			if cls.__name__ == "Rectangle":
				dummy = cls(4, 8)
			else:
				dummy = cls(8)
			dummy.update(**dictionary)
			return dummy
