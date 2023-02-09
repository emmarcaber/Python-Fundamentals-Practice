# class = template of objects
# objects = instance of a class

# Attributes = is/has of an object e.g. name, age, height
# Methods = actions e.g. eating, dancing, watching youtube

# It is a convention that classes are always in PascalCase

from car import Car

# creating an object called car_1 of class Car
car_1 = Car("Chevy", "Corvette", 2021, "blue")

# creating another object of class Car called car_2
car_2 = Car("Ford", "Mustang", 2022, "red")

# Printing all the attributes of car_1
# print(car_2.make)
# print(car_2.model)
# print(car_2.year)
# print(car_2.color)

# Calling all of its methods
car_2.drive()
car_2.stop()
