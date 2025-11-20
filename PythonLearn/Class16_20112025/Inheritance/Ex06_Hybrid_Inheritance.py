class Teacher:

    def Math(self):
        print("We are Learning Mathematics")

    def Physics(self):
        print("We are Learing Physics")

    def Science(self):
        print("We are Learning Science")

class Amol_Student(Teacher):
    def Learn(self):
        self.Math()
        self.Physics()
        self.Science()
        print("Explained to 2 more students")
class Tejal_Student(Amol_Student):
    def Learning(self):
        self.Learn()
        print("Prepared for Exam")

class Principal(Tejal_Student, Teacher):

    def Exam(self):
        self.Learning()
        print("Final Exam")


school = Principal()
school.Exam()
