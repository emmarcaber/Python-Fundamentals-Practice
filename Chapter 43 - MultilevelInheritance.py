# CHAPTER 43
# Multilevel Inheritance = when a derived (child) class inherits another derived (child) class 
# Imagine a family tree which inherits the characteristics from grandfather to the grandson

# Super Parent Class
class Organism:
    alive = True

# Parent Class of Dog
# but a Child class of Animal
class Animal(Organism):

    def eat(self):
        print("This animal is eating")

# Child class of Animal
class Dog(Animal):

    def bark(self):
        print("This dog is barking")


# Testing the inheritance
dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()