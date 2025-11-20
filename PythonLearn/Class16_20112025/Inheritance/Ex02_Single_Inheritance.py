class ClassRoom1:
    def room1student(self, students):
        return students

class ClassRoom2(ClassRoom1):
    def room2student(self):
        print("Class 2 students and",self.room1student("Class 1 students"), "are merged")

classroom = ClassRoom2()
classroom.room2student()
