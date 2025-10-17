#use (parent_name) for inheritance
# 1. use super() key word for access parent class method.
# 2. use parent_name.method_name(self) for access parent class method

class parent:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Parent name is :", self.name)
    
    def pm(slef):
        print("Parent class called")

class child(parent):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def display(self): 
        super().display()
        print("Child name is :", self.name)

print("----------------------------------")
p1 = parent("Super")
p1.display()
p1.pm()

print("\n----------------------------------")
c1 = child("sub")
c1.display()
c1.pm()