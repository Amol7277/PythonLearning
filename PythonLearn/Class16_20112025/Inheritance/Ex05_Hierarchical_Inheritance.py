class Teacher:

    def Math(self):
        print("We are Learning Mathematics")

    def Physics(self):
        print("We are Learing Physics")

    def Science(self):
        print("We are Learning Science")


class ClassRoom1(Teacher):

    def Study1(self):
        self.Math()
        self.Physics()
        self.Science()

class ClassRoom2(Teacher):

    def Study2(self):
        self.Science()
        self.Physics()
        self.Math()

class1 = ClassRoom1()
class1.Study1()

print("===========================================")

class2 = ClassRoom2()
class2.Study2()


