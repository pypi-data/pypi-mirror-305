# school_management/course.py

class Course:
    def __init__(self, name, course_id):
        self.name = name
        self.course_id = course_id
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students = [s for s in self.students if s != student]

    def list_students(self):
        return [student.name for student in self.students]
    

