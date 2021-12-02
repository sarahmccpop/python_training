# example of polymorphism
# https://pynative.com/python/object-oriented-programming/
class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        # pi x rsquared
        print("Area of circle: ", self.pi * self.radius * self.radius, "cms")


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        print("Area of a rectangle: ", self.length * self.width, "cms")


# creating a common function that can take any shape
def area(shape):
    # call action
    shape.calculate_area()


# creating objects
circle = Circle(5)
rectangle = Rectangle(4, 5)

# calling common function
area(circle)
area(rectangle)
