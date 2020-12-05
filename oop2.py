# Object Orientated Programming in Python

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 - 100

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        # it's fine that we don't assign attribute to parameter(arg)

    def add_student(self, student):
        # parameter 'student' is gonna be an instance of a Student object
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0 
        for student in self.students:  
            value += student.get_grade()
        return value/len(self.students)


# print(type(1))

s1 = Student('Tom', 18, 70)
s2 = Student('Jerry', 18, 95)
s3 = Student('Jill', 19, 65)

course = Course('Computer Science', 2)

course.add_student(s1)
course.add_student(s2)

print(course.students)
# [<__main__.Student object at 0x7fec62103dc0>, <__main__.Student object at 0x7fec6212ff40>]
# both of these things inside our list are Student objects

print(course.students[0].name)
print(course.get_average_grade())
print(course.add_student(s3))


