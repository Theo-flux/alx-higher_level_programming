#!/usr/bin/python3
"""Define a function"""


def read_file(filename=""):
	"""function to read from a file
	
	Args:
	     filename (str): name of the file
	"""
	with open(filename, mode="r", encoding="UTF-8") as f:
		text = f.read()
		print(text)
