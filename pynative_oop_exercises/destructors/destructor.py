# Destructor is a special method that is called when an object gets destroyed

# in python destructor is not called manually but completley automatic. destructor gets called in the following two cases
# - when an object goes out of scope
# - the reference counter of the object reaches 0

# the magic method __del__() is used as the deconstructor in python. The method is automatically called by python when the instance is about to be destroyed

import time


class Student:

    # constructor
    def __init__(self, name):
        print("Inside constructor")
        self.name = name
        print("Object initialized")

    def show(self):
        print("Hello my name is ", self.name)

    # destructor
    def __del__(self):
        print("Inside destructor")
        print("Object destroyed")


# create object
s1 = Student("Emma")
s2 = s1
s1.show()

# delete object
del s1

time.sleep(5)
print("After sleep")
s2.show()
