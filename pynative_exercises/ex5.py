# https://pynative.com/python-object-oriented-programming-oop-exercise/
# Define a property that must have the same value for every class instance (object)
# Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.
# Use the following code for this exercise.


class Vehicle:
    def __init__(self, name, max_speed, mileage, colour="White"):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.colour = colour


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


bus = Bus("School Volvo", 180, 12)
car = Car("Audi Q5", 240, 18)
print(
    f"Colour : {bus.colour}, Vehicle name: {bus.name}, Speed: {bus.max_speed}, Mileage: {bus.mileage}"
)
print(
    f"Colour : {car.colour}, Vehicle name: {car.name}, Speed: {car.max_speed}, Mileage: {car.mileage}"
)
