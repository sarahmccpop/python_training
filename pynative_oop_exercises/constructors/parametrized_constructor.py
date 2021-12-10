class Employee:
    # A constructor with defined parameters or arguments is called a parameterized constructor.
    # We can pass different values to each object at each tme of creation using a parameterized constructor

    # The first parameter to the constructor is self that is a reference to the being constructed, and the
    # rest of the arguments are provided by the programmer. A parameterized constructor can have any number of
    # arguments.

    # For example, consider a company that contains thousands of employees. In this case, while creating each employee
    # object, we need to pass a different name, age and salary. In such cases, use the parametrized constructor.

    count = 0

    # parametrized constructor
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        Employee.count = Employee.count + 1  # += doesn't work here

    # display object
    def show(self):
        print(self.name, self.age, self.salary)


# creating the object of the Employee class
emma = Employee("Emma", 23, 7500)
emma.show()

kelly = Employee("Kelly", 25, 8500)
kelly.show()

# to count the number of objects in a class call the count
print("The number of employees ", Employee.count)
