# Encapsulation describes the concept of bundling data and methods within a single unit e.g. a class.
# A class is an example of encapsulation as it binds all the data members (instance vars) and methods into a single unit


class Employee:
    # constructor
    def __init__(self, name, salary, project):
        # data members
        self.name = name  # public member - accessible within or outside of a class
        self._project = (
            project  # protected member (accessible with the class and it's sub-classes)
        )
        self.__salary = salary  # private member (accessible only within a class)

    # method to display employee's details
    def show(self):
        # accessing public data member
        print("Name: ", self.name, "Salary:", self.__salary)

    # method
    def work(self):
        print(self.name, " is working on ", self._project)


# creating an object of a class
emp = Employee("Jessa", 8000, "NLP")

# calling public method of the class
emp.show()
emp.work()

# We can access private members from outside the class using the following two approaches
# - create public method to access private members e.g in show()
# - use name mangling

# Name mangling is created on an identifier by adding two leading underscores and one trailing underscore,
# like this _classname__dataMember, where classname is the current class, and datamember is the private variable name
print("Salary name mangling", emp._Employee__salary)

# accessing private data mebers
print(
    "Salary", emp.__salary
)  # This will throw an attribute error as salary is a private variable and we can't access private
# variables from outside of that class
