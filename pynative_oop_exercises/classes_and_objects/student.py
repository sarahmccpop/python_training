# https://pynative.com/python-classes-and-objects/

# Class names in UpperCaseCamelCase convention


class Student:
    # class variables
    school_name = "ABC School"

    # constructor
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

    # instance method
    def show(self):
        # access instance variables and class variables
        print("Student: ", self.name, self.age, Student.school_name)

    # instance method
    def change_age(self, new_age):
        # modify instance variables
        self.age = new_age

    # class method
    @classmethod
    def modify_school_name(cls, new_name):
        # modify class variable
        cls.school_name = new_name


s1 = Student("Harry", 12)
# access instance variables
print(f"Student: {s1.name}, {s1.age}")

# call instance methods
s1.show()
s1.change_age(14)
s1.show()
# access class variables
print("School name: ", Student.school_name)

# Modify instance variables
s1.name = "Jessa"
s1.age = 14
print("Student: ", s1.name, s1.age)

# Modify class variables
Student.school_name = "XYZ School"
print("School name: ", Student.school_name)
# call instance method
s1.show()
