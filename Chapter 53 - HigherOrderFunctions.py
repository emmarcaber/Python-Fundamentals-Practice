# CHAPTER 53
# Higher Order Functions
# A function that either:
#   1. Accepts a function as argument
#   2. Returns a function
#   (In Python, functions are also treated as objects)


# Part 1 Demonstration
# Functions that accepts a function as argument

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

# This is the higher order functions
def hello(func):
    text = func("Hello")
    print(text)

# prints "HELLO"
# loud function is pass to hello function
# then inside the hello function:
#       text = loud("Hello")
# now, print the text
hello(loud)

# prints "hello"
# loud function is pass to hello function
# then inside the hello function:
#       text = quiet("Hello")
# now, print the text
hello(quiet)
