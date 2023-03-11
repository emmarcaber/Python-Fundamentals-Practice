# CHAPTER 45
# Method Overriding

class Animal:

    def eat(self):
        print("This animal is eating")

# Method Overriding
class Rabbit(Animal):
    
    # Method which overrides the eat() method
    # of Animal class
    def eat(self):
        print("This rabbit is eating")


rabbit = Rabbit()

# Prints "This rabbit is eating"
# Instead of, "This animal is eating"
rabbit.eat()