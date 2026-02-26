class grandparent:
    def grandparent_method(self):
        print("This is the grandparent method.")
class parent(grandparent):
    def parent_method(self):
        print("This is the parent method.")
class child(parent):
    def child_method(self):
        print("This is the child method.")
child_instance = child()
child_instance.grandparent_method()
child_instance.parent_method()
child_instance.child_method()
