class Car:

	# Below are attributes
	# make = None
	# model = None
	# year = None
	# color = None
	
	# This is a special method
	# It is known as constructor in other
	# programming languages
	def __init__(self, make, model, year, color):
		self.make = make
		self.model = model
		self.year = year
		self.color = color
		
	# NOTE: You don't need to pass an argument 
	# 		  in the self parameter
	
	# Below are methods 
	# Methods are simply functions 
	# that belongs to a class
	def drive(self):
		print(f"This {self.model} is driving")
		
	def stop(self):
		print(f"This {self.model} is stopped")
