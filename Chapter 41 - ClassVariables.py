from car import Car

car1 = Car("Chevy", "Corvette", 2021, "blue")
car2 = Car("Ford", "Mustang", 2022, "red")

# Changes all the value of wheels variables to 2
# Since the wheels belongs to the class
# All objects of Car classes will be affected
Car.wheels = 2

print(car1.wheels)
print(car2.wheels)