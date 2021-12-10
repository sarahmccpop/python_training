# https://pynative.com/python-classes-and-objects/


class Fruit:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def show(self):
        print("Fruit is", self.name, "and colour is", self.colour)


# creating object of the class
obj = Fruit("Apple", "red")
# Modifying the object properties
obj.name = "Strawberry"

# calling the instance method using the object obj
obj.show()

# deleting object properties
# use del keyword
del obj.name

# Accessing object properties after deleting
print(obj.name)
# Error printed after deletion is = AttributeError: 'Fruit' object has no attribute 'name'

# deleting an object
del obj
obj.show()
print(obj)
# NameError: name 'obj' is not defined
