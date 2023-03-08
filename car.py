class Car:

	# Below are attributes
	# make = None
	# model = None
	# year = None
	# color = None
	
	# An example of class variable
	# A variable that solely belongs to the class
	wheels = 4

	# This is a special method
	# It is known as constructor in other
	# programming languages
	def __init__(self, make, model, year, color):
		self.make = make 				# instance variable
		self.model = model				# instance variable
		self.year = year				# instance variable
		self.color = color				# instance variable

	# NOTE: Instance variables are variables 
	# 		that will be changed for a specific object
		
	# NOTE: You don't need to pass an argument 
	# 		  in the self parameter
	
	# Below are methods 
	# Methods are simply functions 
	# that belongs to a class
	def drive(self):
		print(f"This {self.model} is driving")
		
	def stop(self):
		print(f"This {self.model} is stopped")
