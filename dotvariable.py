class MyClass:
    def __init__(self, name):
        self.name = name
    def display_name(self):
        print(f"Name: {self.name}")
obj = MyClass("Rohit Kumar")
print(type(obj))
obj.display_name()