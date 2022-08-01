#!/usr/bin/python3
"""Define a function is_same_class"""


def is_same_class(obj, a_class):
	"""A function that returns True
	if obj is an exact instance of the specified
	class

	Args:
	    obj: object
	    a_class: class
	"""
	if type(obj) == a_class:
		return True
	return False
