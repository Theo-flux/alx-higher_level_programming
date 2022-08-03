#!/usr/bin/python3
"""Define a function"""


import json

def load_from_json_file(filename):
	"""Create object from JSON file"""
	with open(filename, encoding="utf-8") as f:
		return json.dumps(f.read(), sort_keys=True)
