class Person:
    def __init__(self, name, gender, profession):
        self.name = name
        self.gender = gender
        self.profession = profession

    def show(self):
        print(
            "Name: ",
            self.name,
            "Gender: ",
            self.gender,
            "Profession: ",
            self.profession,
        )

    def work(self):
        print(self.name, "working as a ", self.profession)


person1 = Person("Jessa", "Female", "Software Engineer")
person2 = Person("John", "Male", "Doctor")

person1.show()
person2.show()
person1.work()
person2.work()
