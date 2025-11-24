# Python does not support method overloading 
class Bike:

    def honda(self):
        print("Honda shine")

    def honda(self, name = None):
        print("Honda Unicorn", name)

bike = Bike()
bike.honda("Black")