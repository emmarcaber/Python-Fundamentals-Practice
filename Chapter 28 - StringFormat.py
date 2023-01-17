# str.format() =	optional method that gives users
#	                more control when displaying output

animal = "cow"
item = "moon"

#print("The " + animal + " jumped over the " + item)									          # tedious way
print("The {} jumped over the {}".format(animal, item))								          # easy and beautiful way
print("The {1} jumped over the {0}".format(animal, item)) 								      # positional argument
print("The {item} jumped over the {anim}".format(anim="dog", item="pillow")) 		# keyword argument

name="Bro"
print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name)) # formatting for spaces

number = 3.14159
number2 = 1000
print("The number pi is {:.2f}".format(number)) 	# formating floating values to display
print("The number pi is {:,}".format(number2)) 		# comma for every three digits
print("The number pi is {:b}".format(number2))	  # displaying in binary
print("The number pi is {:o}".format(number2)) 	  # displaying in octal
print("The number pi is {:X}".format(number2)) 	  # displaying in hexadecimal
print("The number pi is {:E}".format(number2))		# displaying in scientific notation 


print(f"The {animal} jumped over the {item}") 		# the amazing way
