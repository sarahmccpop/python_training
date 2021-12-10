class Vehicle:
    def __init__(self, speed):
        if speed > 240:
            raise Exception("Not Allowed")
        self.speed = speed

    def __del__(self):
        print("Release resources")


# creating an object
car = Vehicle(350)
del car
