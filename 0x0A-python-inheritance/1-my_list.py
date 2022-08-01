#!/usr/bin/python3
"""Define MyList class"""

class MyList(list):
	"""A representation of MyList data type"""
    
	def print_sorted(self):
        	"""Public instance method that prints the
        	list in ascending order
        	"""
        	print(sorted(self))
