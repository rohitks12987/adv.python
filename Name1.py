class stu:
    def __init__(self,name,age):
        self.name = name
        self._age = age
        self.__rollno = 543   
    def get_rollno(self):
        return self.__rollno
class myClass(stu):
    def __init__(self,name,age):
        super().__init__(name,age)
        print("It is the derived class of the stu class")
s = stu("Rohit  Kumar", 20)
print(s.name) # this is the public variable of the stu class
print(s._age) # this is the protected variable of the stu class
print(s.get_rollno()) # this is the private variable of the stu class

m = myClass("Kishore Chandra", 25)
print(m.name) # this is the public variable of the myClass class which is inherited from the stu class
print(m._age) # this is the protected variable of the myClass class which is inherited
print(m.get_rollno()) # this is the private variable of the myClass class which is inherited from the stu class but we can access it through the public method of the stu class which is get_rollno() method.