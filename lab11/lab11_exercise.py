"""
Miguel Castillo
Lab 11: Classes Exercise
April 29, 2025
"""


class Student:
    grade = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def add_grade(self, subject: str, grade: float):
        self.grade[subject] = grade

    def get_average_grade(self):
        if not (len(self.grade)):
            return 0

        sum = 0

        for key in self.grade:
            sum += self.grade[key]

        return sum / len(self.grade)


student1 = Student("Miguel", 26)
student1.add_grade("Math", 100)
student1.add_grade("Science", 50)
print(student1.get_average_grade())
