# keyword arguments =		arguments preceded by an identifier when we pass them to a function.
#				The order of the arguments doesn't matter, unlike positional arguments
#				Python knows the names of the arguments that our function receives

def hello(first, middle, last):
	print("Hello " + first + " " + middle + " " + last)

# Example of Keyword Arguments
# prints "Hello Bro Dude Code"
hello(last = "Code", middle="Dude", first="Bro")

# Example of Positional Arguments
# prints "Hello Code Dude Bro"
hello("Code", "Dude", "Bro")
