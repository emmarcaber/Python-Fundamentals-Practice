# logical operatores (and, or, not)
# = are used to check if two or more conditional statements
#   true

temp = int(input("What is the temperature outside? "))

# AND OPERATORS
# returns true if both of the conditions are true
if temp >= 0 and temp <= 30:
    print("The temperature is bad today!")
    print("Stay inside!")

# OR OPERATORS
# returns true if one of the conditions are true
elif temp < 0 or temp > 30:
    print("The temperature is good today!")
    print("Go outside!")

# NOT OPERATORS
# reverses the conditioanl statement
# FOR EXAMPLE:
"""
    x = True
    y = False

    # Return false since x is True
    result = not x
    print(result)

    # Return true since y is False
    result = not y
    print(result)
"""