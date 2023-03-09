# CHAPTER 30
# exception =   events detected during execution that interrupts the flow of a program

# The code below can result to an exception
# since when you provided 0 to denominator, the exception
# will be caught which is ZeroDivisionError

# numerator = int(input("Enter a number to divide: "))
# denominator = int(input("Enter a number to divide by: "))
# result = numerator / denominator
# print(result)

# To solve this problem, we use exception handling

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator

# Handles the exception ZeroDivisionError only
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero! Idiot!")

# Handles the exception ValueError
except ValueError as e:
    print(e)
    print("Enter only number plz!")

# Catches all exception
except Exception as e:
    print(e)
    print("something went wrong")

# If there are no exceptions, print the result
else:
    print(result)

# Whether or not there is exception
# this line of code will be always executed
finally:
    print("This will always execute")