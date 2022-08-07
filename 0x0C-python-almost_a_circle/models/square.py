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
	
	def update(self, *args, **kwargs):
        	"""Update the Square.
	
        	Args:
            	    *args (ints): New attribute values.
                    - 1st argument represents id attribute
                    - 2nd argument represents size attribute
                    - 3rd argument represents x attribute
                    - 4th argument represents y attribute
            	    **kwargs (dict): New key/value pairs of attributes.
        	"""
       		if args and len(args) != 0:
            		a = 0
            		for arg in args:
                		if a == 0:
                    			if arg is None:
                        			self.__init__(self.size, self.x, self.y)
                    			else:
                        			self.id = arg
                		elif a == 1:
                    			self.size = arg
                		elif a == 2:
                    			self.x = arg
                		elif a == 3:
                    			self.y = arg
                		a += 1

        	elif kwargs and len(kwargs) != 0:
            		for key, value in kwargs.items():
                		if key == "id":
                    			if value is None:
                        			self.__init__(self.size, self.x, self.y)
                    			else:
                        			self.id = value
                		elif key == "size":
                    			self.size = value
                		elif key == "x":
                    			self.x = value
                		elif key == "y":
                    			self.y = value


	def __str__(self):
		return "[{}] ({}) {}/{} - {}"\
			.format(self.__class__.__name__,\
			self.id, self.x, self.y, self.size)
