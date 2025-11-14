class Bike:

# Attribute
    Engine = None
    Tyres = None
    Petrol_EV = None
    CC = None
    Speed = None

#Behaviours

# Function 1 => With no parameter and no return
    def High_Speed(self):
        print("Speed is very high")

# Function 2 => Single parameter and no return
    def Low_Speed(self, speed):
        print("Low speed is ", speed)

# Function 3 => Single/Multiple parameter with return
    def EV_Petrol(self, Gear):
        if Gear == "EV":
            return print("Vehical type is EV")
        else:
            return print("Vehical type is Petrol")

# Function 4 => With no parameter and return
    def EngineCC(self):
        return print("150 CC")

Honda = Bike()
Honda.EngineCC()

Yamaha = Bike()
Yamaha.EV_Petrol("Test")

Hero = Bike()
Hero.High_Speed()

Bajaj = Bike()
Bajaj.Low_Speed(30)