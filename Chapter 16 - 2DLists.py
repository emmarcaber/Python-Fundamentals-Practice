# CHAPTER 16
# 2D lists = a list of lists
# also known as multi-dimensional lists

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
desserts = ["cake", "ice cream"] 

foods = [drinks, dinner, desserts]

# show all the elements of the list
# prints [['coffee', 'soda', 'tea'], ['pizza', 'hamburger', 'hotdog'], ['cake', 'ice cream']]
print(foods) 

# show the first list element of foods which is the drinks
# prints [['coffee', 'soda', 'tea']
print(foods[0])

# show the first element of drinks which is "coffee"
print(foods[0][0])

# show the third element of dinner which is "hotdog"
print(foods[1][2])

# this is an IndexError
# since there are only two elements inside the desserts list
# print(foods[2][2])