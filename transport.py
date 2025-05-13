class Transport:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Horse(Transport):
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} is galloping 🐎")

class Camel(Transport):
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} is walking steadily through the desert 🐪")

class Car(Transport):
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def move(self):
        print(f"Driving a car powered by {self.fuel_type} fuel 🚗")

class Bicycle(Transport):
    def move(self):
        print("Pedaling the bicycle 🚲")

class SteamTrain(Transport):
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def move(self):
        print(f"Chugging along the tracks using {self.fuel_type} fuel 🚂")

class Airplane(Transport):
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def move(self):
        print(f"Flying through the skies powered by {self.fuel_type} ✈️")

class Sailboat(Transport):
    def move(self):
        print("Sailing on the water using wind power ⛵")

class Rocket(Transport):
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def move(self):
        print(f"Launching into space using {self.fuel_type} 🚀")

# Example usage:
transports = [
    Horse("Spirit"),
    Camel("Sahara"),
    Car("gasoline"),
    Bicycle(),
    SteamTrain("coal"),
    Airplane("jet fuel"),
    Sailboat(),
    Rocket("liquid oxygen and kerosene")
]

for t in transports:
    t.move()
