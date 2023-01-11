# dictionary = a changeable, unordered collection of unique key:value pairs
#              Fast because they use hashing, allow us to access value quickly

capitals = {
    'USA': 'Washington DC',
    'India': 'New Delhi',
    'China': 'Beijing',
    'Russia': 'Moscow'
}


capitals.update({'Germany': 'Berlin'}) # adds a new key:value pair
capitals.update({'USA': 'Las Vegas'}) # updates a new key:value pair
capitals.pop('China') # removes a key:value pair
capitals.clear() # clears all key:value pairs in the dictionary

# print(capitals['Russia'])

# a much safer way to get a value from a dictionary
# print(capitals.get('Germany'))

# print(capitals.keys()) # prints all the keys of capitals dictionary
# print(capitals.values()) # prints all the values of capitals dictionary

# One item is equal to one key:value pair
# print(capitals.items()) # prints all the items inside capitals dictionary

# prints all the items in your dictionary
for key,value in capitals.items():
    print(key,value)

# this is an error since there is no
# "Germany" key in the capitals dictionary
# print(capitals['Germany'])