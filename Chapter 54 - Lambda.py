# CHAPTER 54
# Lambda Function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)

# lambda parameters : expression

# Long Method
# def double(x):
#     return x * 2

# Shortcut using Lambda Function
double = lambda x : x * 2
print(double(5))


# Long Method
# def multiply(x, y):
#       return x * y

# Shortcut using Lambda Function
multiply = lambda x, y : x * y
print(multiply(5, 3))


# Long Method
# def add(x, y, z):
#       return x + y + z

# Shortcut using Lambda Function
add = lambda x, y, z : x + y + z
print(add(3, 6, 9))


# Long Method
# def full_name(first_name, last_name):
#       return first_name + " " + last_name

# Shortcut using Lambda Function
full_name = lambda first_name, last_name : first_name + " " + last_name
print(full_name("Emmar", "Caber"))


# Long Method
# def age_check(age):
#       return True if age >= 18 else False

# Shortcut Method using Lambda Function
age_check = lambda age : True if age >= 18 else False
print(age_check(18))