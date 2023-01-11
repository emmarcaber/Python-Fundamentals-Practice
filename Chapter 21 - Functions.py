# CHAPTER 21
# function = a block of code which is executed only when it is called

# NOTE: Any code type after function declaration,
#       should be indented first


def hello(first_name, last_name, age):
    print("Hello, " + first_name + " " + last_name + "!")
    print("You are " + str(age) + " years old.")
    print("Have a nice day!")

# Arguments are variables passed in function invocation
# For example below, the string "Emmar" is the argument
# hello("Emmar")

# my_name = "Emmar"
# # An example of using variable as the argument
# hello(my_name)

hello("Emmar", "Caber", 20)