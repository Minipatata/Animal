#Write a program to implement abstraction on animal class (base class). 
# The abstract method will be move will display what subclasses can do. 
# Subclasses can be something like - Human, Dog.
from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("The dog barks")
a=Dog()
a.sound()