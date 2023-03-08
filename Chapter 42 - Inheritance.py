# NOTE: Inheritance allows developers
#       to not copy and paste code because
#       of changing multiple classes that 
#       can be clustered or grouped


# Parent Class
class Animal:
    
    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")


# Subclass
# Rabbit inherits the properties and methods
# of Animal class
# Meaning rabbit can call eat() and sleep()
# from the Animal Cass 
class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")



# Subclass
# Fish inherits the properties and methods
# of Animal class
# Meaning rabbit can call eat() and sleep()
# from the Animal Cass 
class Fish(Animal):
    def swim(self):
        print("This fish is sleeping")


# Subclass
# Hawk inherits the properties and methods
# of Animal class
# Meaning rabbit can call eat() and sleep()
# from the Animal Cass 
class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

# Calling the properties or method
# from the Parent Class
# Demonstrating the inheritance
# print(rabbit.alive)
# fish.eat()
# hawk.sleep()

# Calling the methods unique
# to each subclass
rabbit.run()
fish.swim()
hawk.fly()