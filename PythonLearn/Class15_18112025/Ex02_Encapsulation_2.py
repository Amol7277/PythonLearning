class Family:

    def __init__(self, MyMummy, MyPapa, MyWife):
        self.mummy = MyMummy        #Public Variable
        self.papa = MyPapa          #Public Variable
        self.__wife = MyWife        #Private Variable(start from __)

    def Mom(self, Child):
        print(Child)
        self.__Wife()
        print(self.papa)
        print(self.mummy)
        print(self.__wife)
    def __Wife(self):
        print(self.__wife)

myfamily = Family("Mummy Can Access","Papa Can Access","Wife Can Access")
myfamily.Mom("Amol")
# myfamily.Mom()



