# import importlib
# importlib.reload(cars)


class Vehicle:
    def __init__(self, make, model, fuel="Petrol"):
        self.make = make
        self.model = model
        self.fuel = fuel

    def is_eco_friendly(self):
        if self.fuel == "Petrol":
            return False
        else:
            return True


# this is inheritance
# you pass in the class you want to inherit from
class Car(Vehicle):
    def __init__(self, make, model, fuel="Petrol", num_wheels=4):
        super().__init__(make, model, fuel)
        self.num_wheels = num_wheels
