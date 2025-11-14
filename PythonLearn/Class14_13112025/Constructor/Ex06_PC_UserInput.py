class Human:
    Hand = None
    Leg = None
    Eye = None
    Nose = None
    Brain = None
    Heart = None

    def __init__(self):
        self.Hand = int(input("How many Hands you have "))
        self.Leg = int(input("How many leg you have " ))
        self.Eye = int(input("How many Eye you have " ))
        self.Nose = int(input("How many Nose you have "))
        self.Brain = int(input("How many Brain you have "))
        self.Heart = int(input("How many Heart you have "))
        print("==========================================================")

    def mybodypart(self):
        # print(f"I Have", self.Heart, "Heart", self.Brain, "Brain", self.Eye, "Eye", self.Hand, "Hands", self.Leg,
        #       "Legs", self.Nose, "Nose", sep=",", end=".")
        print(
            f"I Have {self.Heart} Heart, "
            f"{self.Brain} Brain, "
            f"{self.Eye} Eye, "
            f"{self.Hand} Hands, "
            f"{self.Leg} Legs, "
            f"{self.Nose} Nose."
        )

Body = Human()
Body.mybodypart()
