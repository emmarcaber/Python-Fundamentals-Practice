# CHAPTER 9
# if statement = a block of code that will execute if it's
#                it's condition is true

age = int(input("How old are you? ")) 

# IF age is exactly 100, proceed to this block
if age == 100:
    print("You are a century old!")

# ELIF age is great than or equal to 18
# proceed to this block
elif age >= 18:
    print("You are an adult!")

# ELIF age is less than 0
# proceed to this block
elif age < 0:
    print("You haven't been born yet!")

# ELSE, proceed to this block
else:
    print("You are a child!")


# NOTE: Indention is important here because 
#       if you indent your next statements after
#       a conditional statement, it will result to an error