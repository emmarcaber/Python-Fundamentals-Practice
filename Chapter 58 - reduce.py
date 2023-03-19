# CHAPTER 58
# reduce() = apply a function to an iterable and reduce it to a single cumulative value
#            performs function on first two elements and repeats process until 1 value remains

# Remember that reduce() is in functools library,
# So you must import the functools
# reduce(function, iterable)

import functools

letters = ["H", "E", "L", "L", "O"]

# First Iteration: HE
# Second Iteration: HEL
# Third Iteration: HELL
# Fourth Iteration HELLO
word = functools.reduce(lambda x, y : x + y, letters)
print(word)


factorial = [5, 4, 3, 2, 1]

# First Iteration: 5 * 4 = 20
# Second Iteration: 20 * 3 = 60
# Third Iteration: 60 * 2 = 120
# Fourth Iteration: 120 * 1 = 120
result = functools.reduce(lambda x, y : x * y, factorial)
print(result)

