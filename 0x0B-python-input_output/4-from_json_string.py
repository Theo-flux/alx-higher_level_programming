#!/usr/bin/python3
"""Define a function"""


import json

def from_json_string(my_str):
	"""function that returns the str from json
	
	Args:
	     my_str (json): json str
	
	Returns:
		object
	"""
	return json.loads(my_str)
