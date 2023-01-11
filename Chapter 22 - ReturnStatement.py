# CHAPTER 22
# return statement = functions send Python values/objects back to the caller.
#                    These values/objects are known as the function's return value

def multiply(number1, number2):
    result = number1 * number2
    return result

# You can also do this
# def multiply(number1, number2):
#     return number1 * number2

x = multiply(6,8)
print(x) # Output: 48

# You can also just do this
# print(multiply(6, 8))