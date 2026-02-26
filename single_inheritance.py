class parent:
    def parent_method(self):
        print("this is parent method")

class child(parent):
    def child_method(self):
        print("this is child method")

child_instance = child()
child_instance.parent_method()
child_instance.child_method()

