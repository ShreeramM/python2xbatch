#Hiding of data members

class LamboVehicle():

    name = "Tata"
    _carnumber = 123
    __engineno = 123444

    def public_car(self):
        print("Public Car function")

    def _protected_car(self):
        print("Protected Car function")

    def __private_car(self):
        print("Privare Car function")

v = LamboVehicle()
v.public_car()
v._protected_car()
# v.__private_car()
v.name