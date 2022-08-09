#!/usr/bin/python3
""" Define the base class
"""
import json
import csv

class Base:
	""" Representation of Base class
	"""
	__nb_objects = 0
	
	def __init__(self, id=None):
		""" class constructor
		
		Args:
		     id (int): object instance id
		"""
		if id != None:
			self.id = id
		else:
			Base.__nb_objects += 1
			self.id = Base.__nb_objects

	@staticmethod
	def to_json_string(list_dictionaries):
		""" Dictionary to JSON string
		
		Args:
		     	list_dictionaries (list): list of dictionaries

		Returns:
			the JSON string representation of list_dictionaries
		"""
		if list_dictionaries == None or list_dictionaries == []:
			return "[]"
		return json.dumps(list_dictionaries)

	@staticmethod
	def from_json_string(json_string):
		""" converts json to string
		
		Args:
		     json_string (list): is a string representing a list of
		     dictionaries
		
		Returns:
		     list of the JSON string representation
		"""
		if json_string == None  or json_string == []:
			return []
		return json.loads(json_string)	
	
	@classmethod
	def save_to_file(cls, list_objs):
		""" saves lists to file
		
		Args:
		     list_objs (list): list of dictionaries
		"""
		filename = "{}.json".format(cls.__name__)
		with open(filename, mode="w") as f:
			res = ""
			if list_objs == None:
				res = cls.to_json_string([])
			else:
				res = [obj.to_dictionary() for obj in list_objs]
			f.write(cls.to_json_string(res))

	@classmethod
	def create(cls, **dictionary):
		""" create classmethod
		
		Args:
		    **dictionary (keyword args): double pointer to a dictionary
			
		Return:
		    instance with all attributes already set.
		"""
		if dictionary and dictionary != {}:
			if cls.__name__ == "Rectangle":
				dummy = cls(4, 8)
			else:
				dummy = cls(8)
			dummy.update(**dictionary)
			return dummy
	
	@classmethod
	def load_from_file(cls):
		""" load from file
		"""
		filename = "{}.json".format(cls.__name__)
		try:
			with open(filename) as f:
				list_of_obj = cls.from_json_string(f.read())
				list_of_instances = [cls.create(**li) for li in list_of_obj]
				return list_of_instances
		except IOError:
			return []

	@classmethod
	def save_to_file_csv(cls, list_objs):
		"""Write the CSV serialization of a list of objects to a file.
	
		Args:
				list_objs (list): A list of inherited Base instances.
		"""
		filename = cls.__name__ + ".csv"
		with open(filename, "w", newline="") as csvfile:
			if list_objs is None or list_objs == []:
				csvfile.write("[]")
			else:
				if cls.__name__ == "Rectangle":
					fieldnames = ["id", "width", "height", "x", "y"]
				else:
					fieldnames = ["id", "size", "x", "y"]
				writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
				for obj in list_objs:
					writer.writerow(obj.to_dictionary())


	@classmethod
	def load_from_file_csv(cls):
		"""Return a list of classes instantiated from a CSV file.
		Reads from `<cls.__name__>.csv`.
		Returns:
				If the file does not exist - an empty list.
				Otherwise - a list of instantiated classes.
		"""
		filename = cls.__name__ + ".csv"
		try:
			with open(filename, "r", newline="") as csvfile:
				if cls.__name__ == "Rectangle":
					fieldnames = ["id", "width", "height", "x", "y"]
				else:
					fieldnames = ["id", "size", "x", "y"]
				list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
				list_dicts = [dict([k, int(v)] for k, v in d.items()) for d in list_dicts]
				return [cls.create(**d) for d in list_dicts]
		except IOError:
			return []

	@staticmethod
	def draw(list_rectangles, list_squares):
		"""Draw Rectangles and Squares using the turtle module.
		Args:
				list_rectangles (list): A list of Rectangle objects to draw.
				list_squares (list): A list of Square objects to draw.
		"""
		turt = turtle.Turtle()
		turt.screen.bgcolor("#b7312c")
		turt.pensize(3)
		turt.shape("turtle")

		turt.color("#ffffff")
		for rect in list_rectangles:
			turt.showturtle()
			turt.up()
			turt.goto(rect.x, rect.y)
			turt.down()
			for i in range(2):
				turt.forward(rect.width)
				turt.left(90)
				turt.forward(rect.height)
				turt.left(90)
				turt.hideturtle()

		turt.color("#b5e3d8")
		for sq in list_squares:
			turt.showturtle()
			turt.up()
			turt.goto(sq.x, sq.y)
			turt.down()
			for i in range(2):
				turt.forward(sq.width)
				turt.left(90)
				turt.forward(sq.height)
				turt.left(90)
			turt.hideturtle()

		turtle.exitonclick()
