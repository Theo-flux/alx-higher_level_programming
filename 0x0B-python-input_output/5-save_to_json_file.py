#!/usr/bin/python3
"""Define a function"""


import json

def save_to_json_file(my_obj, filename):
	"""function that writes an object to a
	text file, using JSON representation
	
	Args:
	     my_obj (object): obj
	     filename: name of file to write to.
	"""
	
	with open(filename, mode="w") as f:
		f.write(json.dumps(my_obj, sort_keys=True))
