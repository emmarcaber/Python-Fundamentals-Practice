# CHAPTER 47
# super() = function used to give access to the methods of a parent class
#           returns a temporary object of a parent class when used

class Rectangle:

    # Constructor class or __init__ method in Python
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Rectangle):


    def __init__(self, length, width):
        
        # self.length = length
        # self.height = height
        # This is repeated and in programming,
        # we don't want that
        # so use the super()
        super().__init__(length, width)

    def area(self):
        return self.length * self.width


class Cube(Rectangle):

    def __init__(self, length, width, height):
        # self.length = length
        # self.height = height
        # This is repeated and in programming,
        # we don't want that
        # so use the super()
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.width * self.length * self.height



square = Square(3, 3)
cube = Cube(3, 3, 3)

# Testing if the super() works
print(square.area())
print(cube.volume())