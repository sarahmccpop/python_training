class Animal:
    def __init__(self, name, eats, lives_in):
        self.name = name
        self.eats = eats
        self.lives_in = lives_in


class Lion(Animal):
    def __init__(self, name, eats, lives_in, legs=4):
        super().__init__(name, eats, lives_in)
        self.legs = legs

    def make_noise(self):
        return "Lion says roar"


class Dog(Animal):
    def __init__(self, name, eats, lives_in, legs=4):
        super().__init__(name, eats, lives_in)
        self.legs = legs

    def make_noise(self):
        return "Dog says woof"


class Fish(Animal):
    def __init__(self, name, eats, lives_in, tail=1):
        super().__init__(name, eats, lives_in)

    def make_noise(self):
        return "Fisk makes a splash"


lion = Lion("Alex", "meat", "plains", 4)
dog = Dog("Pepper", "everything", "house")
fish = Fish("Nemo", "plankton", "ocean")

print(
    lion.name,
    " is a lion and he eats ",
    lion.eats,
    ". He lives in the",
    lion.lives_in,
    " and has ",
    lion.legs,
    " legs. ",
    lion.make_noise(),
)


def speak(animal):
    print(animal.make_noise())


print(
    f"{dog.name} is a dog and he eats {dog.eats}. He lives in the {dog.lives_in}. {dog.make_noise()}"
)

print(
    f"{fish.name} is a fish and he eats {fish.eats}. He lives in the {fish.lives_in}. {fish.make_noise()}"
)

speak(dog)
speak(lion)
speak(fish)
