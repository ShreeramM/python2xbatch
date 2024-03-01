# Polymorphism

# Overloading is not possible in python
# Overriding - same name in parent & child but definition will be different

class A():


    def __init__(self):
     pass

    def print_information(self):
        return "A information is printed"


class B(A):
    def print_information(self):
        return "B information is printed"


B = B()
print(B.print_information())
