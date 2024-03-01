class Vehicle:
    name = None
    color = None

    def vehicle_start(self):
        print("Vehicle Started")

    def vehicle_stop(self):
        print("Vehicle Stopped")


class Car(Vehicle):

    def vehicle_start(self):
        print("Car Started")


class Scooter(Vehicle):
    def vehicle_start(self):
        print("Scooter Started")

Scooty = Scooter()
Scooty.vehicle_start()