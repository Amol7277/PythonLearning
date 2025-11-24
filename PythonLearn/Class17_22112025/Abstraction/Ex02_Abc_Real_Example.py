from abc import ABC, abstractmethod

class Browser_Manager(ABC):

    @abstractmethod
    def Open(self):
        pass

    def Close(self):
        print("Close the Browser")

class Chrome_Manager(Browser_Manager):

    def Open(self):
        print("Open the Browser")

    def Run_URL(self):
        print("Open my URL")

b = Chrome_Manager()
b.Open()
b.Run_URL()
b.Close()