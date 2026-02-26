class parent:
    def parent_method(self):
        print("this is parent method")

class child1(parent):
    def child_method(self):
        print("this is child method")
class child2(parent):
            def child_method(self):
                print("this is child method")
child1_instance = child1()
child1_instance.parent_method()
child1_instance.child_method()
child2_instance = child2()
child2_instance.parent_method()
child2_instance.child_method()
