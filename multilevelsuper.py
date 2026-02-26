class Grandparent:
    def grandparent_method(self):
        print("This is the grandparent method.")
class Parent(Grandparent):
    def parent_method(self):
        print("This is the parent method.")
class Child(Parent):
    def child_method(self):
        print("This is the child method.")
child_instance = Child()
child_instance.grandparent_method()
child_instance.parent_method()
child_instance.child_method()
