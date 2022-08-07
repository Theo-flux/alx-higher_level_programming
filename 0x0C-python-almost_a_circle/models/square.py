#!/usr/bin/python3
""" Define Square class
"""


from models.rectangle import Rectangle
class Square(Rectangle):
	""" A represntation of Square
	"""
	def __init__(self, size, x=0, y=0, id=None):
		""" Class constructor
		
		Args:
		     x (int): x coordinate
		     y (int): y coordinate
		     size (int): length of square
		     id (int): identity for square instance
		"""
		super().__init__(size, size, x, y, id)
		self.size = size
	
	@property
	def size(self):
		return self.height
	
	@size.setter
	def size(self, value):
		self.width = value
		self.height = value

	def __str__(self):
		return "[{}] ({}) {}/{} - {}"\
			.format(self.__class__.__name__,\
			self.id, self.x, self.y, self.size)
