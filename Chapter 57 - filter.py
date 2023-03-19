# CHAPTER 57
# filter() = creates a collection of elements from an 
#           iterable for which a function returns true
# filter(function, iterable)

friends = [
    ("Rachel", 19), 
    ("Monica", 18), 
    ("Phoebe", 17), 
    ("Joey", 16), 
    ("Chandler", 21), 
    ("Ross", 20), 
]

# Get the second element of every tuple element in friends list
# Then check if it is greater than or equal to 18
# If true, add it to the drinking_buddies list
# ELSE, don't
drinking_buddies = list(filter(lambda data : data[1] >= 18, friends))

print(*drinking_buddies, sep="\n")

