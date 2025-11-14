class Name:
    F_Name = None
    L_Name = None
    Address = None

    def __init__(self,FN,LN):
        self.F_Name = FN
        self.L_Name = LN
        # self.Address = Add

    def FullName(self,address):
        print("My Full Name is",self.F_Name, self.L_Name,"And my addess is", address)

MyName = Name("Amol","Sonar")
MyName.FullName("Dindoli Surat")