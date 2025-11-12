class Person:
#Attribute
    name = None
    age = None
    DOB = None
    Location = None
    HouseNumber = None

#Behaviour
    #Function In side the class called as Method
    def wakeup(self):
        print("Wakeup")

    def eat(self):
        print("Eat")

    def walk(self):
        print("Walk")

    def work(self):
        print("Work")

    def sleep(self):
        print("Sleep")


amol = Person()
tejal = Person()
amol.wakeup()
tejal.sleep()


#Function out side the class is called Function
def cooking():
    print("Cooking")

cooking()