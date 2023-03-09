# CHAPTER 26
# *args = 	parameter that will pack all arguments into a tuple
#		useful so that a function can accept a varying amount of arguments

def add(*args):
	sum = 0
	args = list(args) 	# convert it to a list, so that you can reassign some values
	args[0] = 0		# assigning index 0 of stuff list equals to 0
	for i in args:
		sum += i
	return sum

print(add(1, 2, 3, 4, 5, 6))
