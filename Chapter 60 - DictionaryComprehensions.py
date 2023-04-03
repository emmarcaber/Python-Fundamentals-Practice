# CHAPTER 60
# Dictionary Comprehensions = create dictionaries using an expression 
#                             can replace for loops and certain lambda functions

# PART 1
# dictionary = {key: expression for (key, value) in iterable}

cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

# First, it gets all the items in cities_in_F dictionary
# Next, it iterates and gets the key-value pair inside each item
# Then, the values are being applied with formula
#       to convert Fahrenheit to Celsius
cities_in_C = {key: round((value -32) * 5/9) for (key, value) in cities_in_F.items()}
print(cities_in_C)



# PART 2
# dictionary = {key: expression for (key, value) in iterable if conditional}

weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': 'cloudy'}

# First, it gets all the items in weather dictionary
# Next, it iterates and gets the key-value pair inside each item
# Then, the value is checked for every item if it is sunny
# IF it is sunny include the item in the sunny_states dictionary
sunny_states = {key: value for (key, value) in weather.items() if value == "sunny"}
print(sunny_states)



# PART 3
# dictionary = {key: (if/else) for (key, value) in iterable}

cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

# IF the value of items in cities is greater than 40, assign WARM 
# ELSE, assign COLD
cities_status = {key: ("WARM" if value >= 40 else "COLD") for (key, value) in cities.items()}
print(cities_status)



# PART 4
# dictionary = {key: function(value) for (key,value) in iterable}

def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"

cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

# Depending on the value of the item in cities dictionary
# It will call a function check_temp() to apply different conditions
# and return corresponding values
cities_status = {key: check_temp(value) for (key, value) in cities.items()}
print(cities_status)
