class Company:
    # This type of constructor is used to initialize each object with default values

    # This constructor doesn't accept the arguments during object creation. Instead, it initializes every object with the same set of values

    # no-argument constructor
    def __init__(self):
        self.name = "PYnative"
        self.address = "ABC Street"

    # a method for printing data members
    def show(self):
        print("Name:", self.name, "Address:", self.address)


# creating object of the class
cmp = Company()

# calling the instance method using the object
cmp.show()

# second object will have the same values
cmp2 = Company()
cmp2.show()
