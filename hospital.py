class Hospital:
    def __init__(self, name, age, medical_history):
        self.__name = name
        self.__age = age
        self.__medical_history = medical_history

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_medical_history(self):
        return self.__medical_history

    def set_medical_history(self, medical_history):
        self.__medical_history = medical_history
patient = Hospital("vivek", 30, "No known allergies")
print(patient.get_name())  
print(patient.get_age()) 
print(patient.get_medical_history()) 
patient.set_name("Vivek Kumar")
patient.set_age(28)
patient.set_medical_history("Diabetic")
print(patient.get_name())  
print(patient.get_age()) 
print(patient.get_medical_history())