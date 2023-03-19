# CHAPTER 56
# map() = applies a function to each item in an iterable (list, tuple, etc)
# map(function, iterables)

store = [
    ("shirt", 20.00),
    ("pants", 25.00),
    ("jacket", 50.00),
    ("socks", 10.00),
]

# Get all the tuple element in the store list
# Convert the second element which is price into euro
to_euros = list(map(lambda data : (data[0], data[1] * 0.82), store))

to_dollars = list(map(lambda data: (data[0], round(data[1] / 0.82, 2)), store))

print(*to_euros, sep="\n")
print()
print(*to_dollars, sep="\n")