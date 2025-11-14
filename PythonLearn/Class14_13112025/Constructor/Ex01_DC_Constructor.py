class Mobile:
#Attribute

    size = None
    camera = None
    charging = None
    simslot = None

# Contructor will always run first
    def __init__(self):  # => DC -> Default Constructor -> Default with no argument - DC
        print("It is a DC Constructor")

#Behavious
    def talk(self):
        print("Talking")

    def chat(self):
        print("Chating")

    def snap(self):
        print("Photo shoot")


Vivo = Mobile()
Vivo.talk()
Vivo.chat()
Vivo.snap()