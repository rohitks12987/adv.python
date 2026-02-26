class Student:
    def __init__(self, name, age, section, roll_number):
        self.name = name
        self.age = age
        self.section = section
        self.roll_number = roll_number

    def display(self):
        print(f"name is {self.name}")
        print(f"age is {self.age}")
        print(f"roll number is {self.roll_number}")
        print(f"section is {self.section}")

name = input("enter the name of the student: ")
age = int(input("enter the age of the student: "))
section = input("enter the section of the student: ")
roll_number = int(input("enter the roll number of the student: "))
student = Student(name, age, section, roll_number)
student.display()
