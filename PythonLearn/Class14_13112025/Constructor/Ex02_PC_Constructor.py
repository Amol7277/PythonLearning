class Mobile:
#Attribute

    size = None
    camera = None
    charging = None
    simslot = None

# Contructor will always run first
    def __init__(self, a, b):  # => PC -> Parameterized Constructor ->  with argument - PC
        self.size = a
        self.camera = b
        print("It is a PC Constructor",self.size + self.camera)
        print("It is a PC Constructor",a+b)

#Behavious
    def talk(self):
        print("Talking")

    def chat(self):
        print("Chating", self.size + self.camera)

    def snap(self):
        print("Photo shoot")


Vivo = Mobile(10, 2.5)

Vivo.talk()
Vivo.chat()
Vivo.snap()