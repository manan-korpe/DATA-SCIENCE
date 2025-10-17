class Parent:
    def __init__(self):
        self.name = "super"
        
    def display(self):
        print("Parnet name is : ", self.name)
    
class Child(Parent):
    def __init__(self):
        self.name = "sub"
    
    def display(self):
        print("child name is : ", self.name)

    def parentDisplay(self):
        super().display()

p1 = Parent()
p1.display()

c1 = Child()
c1.display()
c1.parentDisplay()

