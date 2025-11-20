class GrandFather:

    def __init__(self):
        print("Father properties")

    def houes(self):
        print("5 houses")

    def cars(self):
        print("4 cars")

class Father:

    def gold(self):
        print("1kg gold")

    def farms(self):
        print("1 acer farm")

class Children(GrandFather, Father):

    def donate(self):
        self.houes()
        self.cars()
        self.gold()
        self.farms()

child = Children()
child.donate()

