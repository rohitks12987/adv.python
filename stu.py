class stu :
    def __init__(self,name,age):
        self.name = name
        self._age = age
        self.__section = 'i'   
    def get_section(self):
        return self.__section
class myClass(stu):
    def show(self):
        self.name()
        self._age()
        self.__section
i=myClass("Rohit Kumar", 20)
print(i.name) # this is the public variable of the stu class
print(i._age) # this is the protected variable of the stu class
print(i.get_section()) # this is the private variable of the stu class