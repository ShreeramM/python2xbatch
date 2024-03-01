# Single Inheritance

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


Tata = Car()
Tata.vehicle_start()  # Car class function is getting invoked, if car is not having any function then it will call
# Vehicle functions
Tata.vehicle_stop()  # its calling vehicle class function
