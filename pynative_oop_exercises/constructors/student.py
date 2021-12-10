# https://pynative.com/python-constructors/

# A constructor is a special method used to create and initialize an object of a class. This method is defined in the class.

# __init__() Method: It is a reserved method. This method gets called as soon as an object of a class is instantiated.
# self: The first argument self refers to the current object. It binds the instance to the __init__() method. It’s usually named self to follow the naming convention.


class Student:

    # if no constructor is declared, it's a default constructor

    # this is a non-parametrized constructor
    # def __init__(self);

    # this is a parametrized constructor, as another parameter other than self is passed to it
    # initialize instance variable
    def __init__(self, name):
        print("Inside constructor")
        self.name = name
        print("All variables initialized")

    # instance method
    def show(self):
        print("Hello, my name is", self.name)


s1 = Student("Emma")
s1.show()
