#!/usr/bin/python3
"""Define is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
	"""function to check instance of object
	Args:
	    obj (any): object to check instance
	    a_class (type): Type to check obj with
	Return:
	      True if obj and a_class are of sam instances
	      or false
	"""
	if isinstance(obj, a_class):
		return True
	return False
