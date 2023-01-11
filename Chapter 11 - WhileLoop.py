# CHAPTER 11
# while loop = a statement that will execute it's block of code,
#              as long as it's condition remains true

# this will result to an infinite loop,
# since the condition is always true
# while 1==1:
#    name = print("Help! I'm stuck in a loop!")

name = ""

while len(name) == 0:
    name = input("Enter your name: ")

# NOTE: You can also conditional operators in a while loop
# while not name:
# 	name = input("Enter your name: ")
# It is the same in the example above

print("Hello " + name)  
