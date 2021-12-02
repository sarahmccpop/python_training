class Employee:
    # class variables
    company_name = "McConvilles Coffees"

    # constructor to initialize the object with parameters to constructor
    def __init__(self, name, role, private_salary):
        # instance variables
        self.name = name
        self.role = role
        self.__private_salary = (
            private_salary  # this is not accessible outside of a class.
        )

    # We can achieve encapsulation by using prefix sing underscore and double underscore to control access of variable and method within the python program

    # instance method
    def show(self):
        print(
            "Employee:", self.name, self.role, self.__private_salary, self.company_name
        )


# creating objects of class
emp1 = Employee("Colin Robinson", "barista", 18000)
emp1.show()

emp2 = Employee("Vicky Robinson", "manager", 25000)
emp2.show()

# cannot access private_salary from outside of a class
print(emp1.__private_salary)  # this will throw an AttributeError when run
