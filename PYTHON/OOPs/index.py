# note : The self parameter is a reference to the current instance of the class,
# and is used to access variables that belong to the class.
# multiple constructor not support --> __init__(self)
# use 'pass' statement for without body class,function,conditional statements,loopign statements etc...

class Student:
    def __init__(self, name): #constructor
        self.name = name
    
    def __str__(self): # object name 
        return f"my name is {self.name}" 
    
    def displayName(self):
        print(self.name)

s1 = Student("ABCD")
s2 = s1 # it makes copy of original one

s1.displayName()
print(s1)

s1.name = "XYZ"

#deleting Object
del s1
