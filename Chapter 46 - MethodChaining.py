# CHAPTER 46
# Method Chaining = calling multiple methods sequentially
#                   each call performs an action on the same object and returns self

class Car:
    
    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self


car = Car()

# Simple method calling
# car.turn_on()
# car.drive()

# Method chaining example
# This will only work
# IF the method returns self
# EXPLANATION: 
# car.turn_on() will return car
# so you can do another method car.drive()
# car.turn_on().drive()

# car.brake().turn_off()

# Supreme example of method chaining (not recommended format)
# Since what if there are multiple methods to chain?
# car.turn_on().drive().brake().turn_off()

# Recommended format
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()