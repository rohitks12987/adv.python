class Student:
    def __init__(self, name, age, section, roll_number, university):
        self.name = name
        self.age = age
        self.section = section
        self.roll_number = roll_number
        self.university = university    
    def display(self):
        print(f"name is {self.name}")
        print(f"age is {self.age}")
        print(f"roll number is {self.roll_number}")
        print(f"section is {self.section}")
        print(f"university is {self.university}")
name = input("enter the name of the student: ")
age = int(input("enter the age of the student: "))
university = input("enter the university of the student: ")
section = input("enter the section of the student: ")
roll_number = int(input("enter the roll number of the student: "))
student = Student(name, age, section, roll_number, university)
student.display()
