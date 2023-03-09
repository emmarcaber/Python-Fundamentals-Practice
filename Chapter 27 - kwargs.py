# CHAPTER 27
# **kwargs =	parameter that will pack all arguments into a dictionary
#		useful so that a function can accept a varying aount of keyword arguments

def hello(**kwargs):
	#print("Hello " + kwargs['first'] + " " + kwargs['last'])
	print("Hello", end=" ")
	for key, value in kwargs.items():
		print(value, end=" ")

hello(title="Mr.", first="Embre", middle="Emra",last="Cabe")
