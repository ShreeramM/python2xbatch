# Ecap
# Inheritance
# poly ( method overiding, loading)


# Abstraction
# Abstraction - OOPs
# Hiding the details and showing the what is required
# Do you know How engine is started?
# How gear box was managed?
# hide the implementation and show only the important details
# 1. Abstract Base Class
# 2. Abstract base Methods

from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass


class Tata(Car):
    def sound(self):
        return "tata car started sound"


class Lambo(Car):
    def sound(self):
        return "Lambo Car started sound "


lambo = Lambo("Rancho")
print(lambo.sound())

tata = Tata("CAT")
print(tata.sound())