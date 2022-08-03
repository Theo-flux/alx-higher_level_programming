#!/usr/bin/python3
"""Define a function"""


def write_file(filename="", text=""):
	"""function that writes a string to 
	a text file.
	
	Args:
	     filename (str): name of the file.
	     text (str): content of file.
	"""
	with open(filename, mode="w", encoding="utf-8") as f:
		f.write(text)
		return len(text)
