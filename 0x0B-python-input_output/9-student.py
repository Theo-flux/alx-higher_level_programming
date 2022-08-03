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
		
	def to_json(self):
		""" Dictionary rep of a Student instance
		"""
		return self.__dict__
