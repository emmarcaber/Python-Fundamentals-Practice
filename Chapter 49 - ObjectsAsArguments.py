# CHAPTER 49
# Objects as Arguments

class Car:

    color = None

# Function with car objects as arguments
def change_car_color(car, color):

    # Changes the color of the object argument
    car.color = color

car_1 = Car()  
car_2 = Car()
car_3 = Car()

# Passing the different car objects as arguments
change_car_color(car_1, "red")
change_car_color(car_2, "green")
change_car_color(car_3, "blue")

print(car_1.color)
print(car_2.color)
print(car_3.color)
