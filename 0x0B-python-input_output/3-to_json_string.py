#!/usr/bin/python3
"""Define a function"""


import json

def to_json_string(my_obj):
	"""function that returns the JSON representation
	of an object (string)
	
	Args:
	     my_obj (str): string object
	
	Returns:
		JSON
	"""
	return json.dumps(my_obj)
