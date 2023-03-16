# CHAPTER 51
# Walrus Operator :=
# Assignement Expression a.k.a Walrus Operator
# Assign Values to Variable as Part of Larger Expression


# TO understand better the Walrus Operator
# Just remember to evaluate first the expression
# Then assign the result to the variable

# foods = list()
# while True:
#     food = input("What food do you like? ")
#     if food == "quit":
#         break
#     foods.append(food)


foods = list()
while food := input("What food do you like? ")  != "quit":
    foods.append(food)

print(foods)

print(happy := True)
print(happy)