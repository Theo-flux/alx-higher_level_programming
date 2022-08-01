#!/usr/bin/python3
"""Define MyList class"""

class MyList(list):
	"""Representation of MyList class"""
	
	def print_sorted(self):
		"""print list in sorted order"""
		print(sorted(self))
