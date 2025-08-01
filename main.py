# A PYTHON CODE FOR A SCHOOL SCORE GRADER
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def grade(self):
        if self.score >= 70:
            print("your grade is A")
        elif 60 <= self.score < 70:
            print("your grade is B")
        elif 50<= self.score < 60:
            print("your grade is C" )
        else:
            print("your grade is F")

name = input("Enter your name: \n")
score =int(input("Enter your score: \n"))

my_grade = Student(name , score)

my_grade.grade()