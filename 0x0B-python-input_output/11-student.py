#!/usr/bin/python3
""" Define a class called student
"""


class Student:
	""" Representation of class Student """
	def __init__(self, first_name, last_name, age):
		""" An instantiation of Student class
		
		Args:
			first_name (str): students' first_name
			last_nme (str): students' last name
			age (int): student's age
		"""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		
	def to_json(self, attrs=None):
		""" Dictionary rep of a Student instance
		
		Args:
			attrs (list): list of attributes to retrieve
		"""
		new_dict = {}
		if type(attrs) == list:
			a_dict = {k: getattr(self, k) for k in attrs if hasattr(self, k)}
			for k in sorted(a_dict.keys()):
				new_dict[k] = a_dict[k] 
			return (new_dict)
		for k in sorted(self.__dict__.keys()):
			new_dict[k] = self.__dict__[k]
		return new_dict
	
	def reload_from_json(self, json):
		""" Method that replaces all
		attributes of the student instance
		
		Args:
			json (JSON): json object
		"""
		for k, v in json.items():
			setattr(self, k, v)
