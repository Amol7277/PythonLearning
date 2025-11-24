from abc import ABC, abstractmethod

class ExcelReader(ABC):

    @abstractmethod
    def excelreader(self):
        pass

class Browser(ABC):

    @abstractmethod
    def open(self):
        pass

    def close(self):
        pass

class TC(ExcelReader,Browser):

    def excelreader(self):
        print("Read my excel file")

    def open(self):
        print("Open my browser")

    def close(self):
        print("Close the browser")

    def runTC(self):
        self.open()
        self.excelreader()
        self.close()

case = TC()
case.runTC()