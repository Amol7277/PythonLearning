class Car:
    def __init__(self, car_Name, car_Make):
        self.Name = car_Name    #Public Variable
        self.__Make = car_Make  #Private Variable

    def ourcar(self, color):
        print("Car Make by", self.__Make, "Mycar color is", color)


mycar = Car("BMW","BMWCompany")
print(mycar.Name)
mycar.ourcar("Black")

