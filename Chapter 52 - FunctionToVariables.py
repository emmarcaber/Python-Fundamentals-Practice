# CHAPTER 52
# Function to Variables

def hello():
    print("Hello")

print(hello) # prints the memory address of function hello

hi = hello

# prints also the memory address of function hello
# since hello function is assigned to hi variable
print(hi) 

hi() # prints "Hello"

say = print
# Just imagine that the variable
# is like an alias for the function
say("Hello, World!")