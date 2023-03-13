# CHAPTER 48
# Abstract Classes

# Prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# Abstract Class = a class which contains one or more abstract methods
# Abstract Method = a method that has a declaration but does not have an implementation
# THINK OF ABSTRACT CLASS AS A TEMPLATE

# abc is an acronym for Abstract-based Class
from abc import ABC, abstractmethod

# By inheriting the ABC class
# You declare the Vehicle as an abstract class
class Vehicle(ABC):

    # @abstractmethod is a decorator to
    # declare an abstract method
    @abstractmethod
    def go(self):
        pass

# If you create an object of this class
# Without this class having any go() method implementation
# It will result to an error
# Since Car class inherits from Vehicle class
# Vehicle class compels Car class
# to create  go() method implementation
class Car(Vehicle):

    def go(self):
        print("You drive a car")

    # You can add methods to Abstract Child Class
    # Just remember to always implement the abstract method
    # From the parent abstract class
    def stop(self):
        print("This car is stopped")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride a motorcycle")
    
    def stop(self):
        print("This motorcycle is stopped")


# vehicle = Vehicle() # Error since this is an abstract class
car = Car()
motorcycle = Motorcycle()

car.go()
motorcycle.go()

car.stop()
motorcycle.stop()