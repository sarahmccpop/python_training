# https://pynative.com/python-object-oriented-programming-oop-exercise/
# Create a Class with instance attributes
# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.


class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


vehicle1 = Vehicle(150, 100000)
print(
    f"Vehicle 1 max speed is {vehicle1.max_speed} miles per hour and the current mileage is {vehicle1.mileage}"
)
