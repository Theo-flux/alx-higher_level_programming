#!/usr/bin/python3
"""Define inherits_from function"""


def inherits_from(obj, a_class):
	"""A function that checks if an object
	is an instance of a class
	
	Args:
	    	obj (any): obj to check
		a_class (type): class to check obj with
	
	Returns:
		True if obj is an instance of a_class or false
	"""
	if (issubclass(type(obj), a_class) and type(obj) != a_class):
		return True
	return False
