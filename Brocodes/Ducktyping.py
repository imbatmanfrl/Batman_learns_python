"""Duck typing is where the class of an object is less important than the method/ attribute the class has. Class type
is not checked if minimum methods/ attributes are present. If it walks and quacks like a duck then it's a duck!"""

from abc import  ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def talk(self):
        pass

class Duck(Animal):

    def walk(self):
        print("This Duck is walking")

    def talk(self):
        print("This duck is Quacking ")

class Chicken(Animal):

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking ")

class Person():

    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("You've caught the critter!")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)
#since chicken also has a walk and talk method like the duck object, python will run the program without any errors!
#If i were to remove either a walk or talk method from the chicken function I will get an error 
chicken.walk()
#chicken.talk()