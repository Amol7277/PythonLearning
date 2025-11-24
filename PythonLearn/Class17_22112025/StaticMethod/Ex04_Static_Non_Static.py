class ExcelReader:
    # Static Method
    @staticmethod
    def readExcelFile():
        print("Reading from Excel")
class MYSQLDBConnection:
    # Static Method
    @staticmethod
    def readMySQLFile():
        print("Reading from MySQL")

class TC1:
    # Non - Static Method
    def runTC(self):
        ExcelReader.readExcelFile()
        MYSQLDBConnection.readMySQLFile()
        print("Hi")

class TC2:

    # Non - Static Method
    def runTC(self):
        ExcelReader.readExcelFile()
        MYSQLDBConnection.readMySQLFile()
        print("Hi")

tc1 = TC1()
tc2 = TC1()
tc1.runTC()
tc2.runTC()