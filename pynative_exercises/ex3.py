# https://pynative.com/python-object-oriented-programming-oop-exercise/
# OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

    def show(self):
        print(
            f"Vehicle Name: {self.name} Speed: {self.max_speed} Mileage: {self.mileage}"
        )


bus = Bus("School Volvo", 180, 12)
bus.show()
