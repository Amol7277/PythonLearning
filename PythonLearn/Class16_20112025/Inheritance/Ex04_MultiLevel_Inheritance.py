class Requirement:

    def project_requirement(self):
        print("Step1 - Requirement document")

class Development(Requirement):

    def project_development(self):
        print("step2 - Developing the Project")

class Testing(Development):

    def project_testing(self):
        self.project_requirement()
        self.project_development()
        print("Step3 - Testing the Project")

project = Testing()
project.project_testing()

