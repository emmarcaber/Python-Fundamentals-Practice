# CHAPTER 49
# Objects as Arguments

class Car:

    color = None

class Motorcycle:

    color = None

# Function with car objects as arguments
def change_color(car, color):

    # Changes the color of the object argument
    car.color = color

car_1 = Car()  
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()

# Passing the different car objects as arguments
change_color(car_1, "red")
change_color(car_2, "green")
change_color(car_3, "blue")

change_color(bike_1, "black")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)
