#!/usr/bin/python3
"""Define a function"""


def append_write(filename="", text=""):
	"""function to append to a file
	
	Args:
	     filename (str): name of file.
	     text (str): text to append to file.
	"""
	with open(filename, mode="a", encoding="utf-8") as f:
		return f.write(text)
