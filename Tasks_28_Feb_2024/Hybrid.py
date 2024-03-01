class Vehicle:
    name = None
    color = None

    def vehicle_start(self):
        print("Vehicle Started")

    def vehicle_stop(self):
        print("Vehicle Stopped")


class Car(Vehicle):

    def car_start(self):
        print("Car Started")


class Scooter(Vehicle):
    def scooter_start(self):
        print("Scooter Started")

class Bicyle(Scooter,Car,Vehicle):
    def bicycle_start(self):
        print("Bicycle Started")

cycle = Bicyle()
cycle.bicycle_start()
cycle.scooter_start()
cycle.car_start()
cycle.vehicle_start()
cycle.vehicle_stop()