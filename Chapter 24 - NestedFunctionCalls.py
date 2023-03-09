# CHAPTER 24
# nested function calls = 		function calls inside other functioncalls
# 								            innermost function calls are resolved first
#								              returned value is used as argument for the next outer function

# No Nested Function Calls
# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num) 

# Demo of Nested Function Calls
# First, it will ask about the input
# Then, convert to a float data type
# Next, apply the absolute value
# Now, round the result and print it 
print(round(abs(float(input("Enter a whole positive number: ")))))
