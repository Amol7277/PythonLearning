import random


class Bank:
    Name = None
    AC_Number = None
    __Balance = random.randint(1, 100)

    def __init__(self):
        print("Bank Of Baroda")
        self.AC_Number = int(input("Enter account number "))

    def Account_Number(self):
        if self.AC_Number == 123456789:
            print("Valid Account", "Account Number", self.AC_Number, "Balance ", self.__Balance, sep=" | ")
        else:
            print("Invalid Account")

myBank = Bank()
myBank.Account_Number()


