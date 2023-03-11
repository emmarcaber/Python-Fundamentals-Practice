# CHAPTER 44
# Multiple Inheritance = when a child class is derived from more than one parent class

# Parent class to inherit
class Prey:

    def flee(self):
        print("This animal flees")

# Parent class to inherit
class Predator:
    
    def hunt(self):
        print("This animal is hunting")

# Example of Single Inheritance
class Rabbit(Prey):
    pass

# Another eample of Single Inheritance
class Hawk(Predator):
    pass

# Example of Multiple Inheritance
class Fish(Prey, Predator):
    pass

# Testing the Single Inheritance
rabbit = Rabbit()
rabbit.flee()
hawk = Hawk()
hawk.hunt()

# Testing the Multiple Inheritance
fish = Fish()
fish.hunt()
fish.flee()