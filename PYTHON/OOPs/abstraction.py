#partial abstraction = some methods are abstract method
#full abstraction = all methods are abstract methods 

from abc import ABC,abstractmethod
class Dog(ABC):
    def __init__(self, name):
        self.name = name 

    @abstractmethod
    def sound(self):
        pass

    def getName(self):
        return self.name
    
class Labradog(Dog):
    def sound(self):
        print(self.name," labradog bark")
    
d1 = Labradog("Buddy")
d1.sound()
print(d1.getName())