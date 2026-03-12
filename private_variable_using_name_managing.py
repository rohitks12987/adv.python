class Student:
    def __init__(self):
        self.__marks = 90

s = Student()
print("Accessing private variable:", s._Student__marks)