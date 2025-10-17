class Student:
    def __init__(self,rollNo, name, age):
        self.__rollno = rollNo #private variable
        self._name = name # protected variable
        self.age = age  # public variable

    def getRollNo(self):
        print("Roll no : ",self.__rollno)

    def display(self):
        print("name : ",self._name,"\nage :",self.age)
    
s1 = Student(102,"ABCD",21)

s1.getRollNo()
s1.display()