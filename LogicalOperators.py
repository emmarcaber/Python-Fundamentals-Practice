# logical operatores (and, or, not)
# = are used to check if two or more conditional statements
#   true

temp = int(input("What is the temperature outside? "))

# AND OPERATORS
# returns true if both of the conditions are true
if temp >= 0 and temp <= 30:
    print("The temperature is good today!")
    print("Go outside!")

# OR OPERATORS
# returns true if one of the conditions are true
elif temp < 0 or temp > 30:
    print("The temperature is bad today!")
    print("Stay inside!")