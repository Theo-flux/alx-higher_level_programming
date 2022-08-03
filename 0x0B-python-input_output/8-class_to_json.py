#!/usr/bin/python3
""" Defines a function
"""


def class_to_json(obj):
	""" A function that returns the dictionary
	description with simple data structure
	(list, dictionary, string, integer and boolean)
	for JSON serialization of an object
	
	Args:
		obj (class instance): instance of a
	"""
	return (obj.__dict__)
