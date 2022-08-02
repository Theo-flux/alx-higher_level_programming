#!/usr/bin/python3
"""Define a derived class from int class"""


class MyInt(int):
	"""Representation of MyInt class"""
	
	def __eq__(self, value):
		return self.real != value

	def __ne__(self, value):
		return self.real == value  
