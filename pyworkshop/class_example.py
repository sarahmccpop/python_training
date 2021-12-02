class Vehicle:
    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel


# number_of_wheels = 4


class Car(Vehicle):
    number_of_wheels = 4


class Truck(Vehicle):
    number_of_wheels = 6

    def __init__(self, make, model, fuel="diesel"):
        super().__init__(make, model, fuel=fuel)


daily_driver = Car("Subaaru", "Crosstrek")
daily_driver.number_of_wheels = 3
# By default, this is how python represents our object
print(daily_driver)

# The variables we saved to the instance are available like this:
# Instance variables
print(
    f"I drive a {daily_driver.make} {daily_driver.model}. It runs on {daily_driver.fuel} and has {daily_driver.number_of_wheels} wheels."
)

truck = Truck("Ford", "F350")
print(
    f"I also have a {truck.make} {truck.model}."
    f"It uses {truck.fuel} and has {truck.number_of_wheels} wheels."
)

# Class variables
# print(f"Most vehicles have {Vehicle.number_of_wheels} wheels.")


print(f"My daily driver is a {type(daily_driver)} and my truck is a {type(truck)}")
print(f"Is my daily a driver a car? {isinstance(daily_driver, Car)}")
print(f"Is my truck a vehicle? {isinstance(truck, Vehicle)}")
print(f"Is my truck a car? {isinstance(truck, Car)}")

print(f"Is a Truck a subclass of vehicle? {issubclass(Truck, Vehicle)}")
print(f"Is a Car a subclass of vehicle? {issubclass(Car, Vehicle)}")
print(f"Is a Car a subclass of vehicle? {issubclass(Car, Truck)}")


class GitHubRepo:
    def __init__(self, name, language, num_stars):
        self.name = name
        self.language = language
        self.num_stars = num_stars

    def __str__(self):
        return f"-> {self.name} is a {self.language} repo with {self.num_stars} stars"


vue = GitHubRepo(name="Vue", language="JavaScript", num_stars=50000)
print(vue)
