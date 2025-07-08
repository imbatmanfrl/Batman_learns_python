"""prevents a user from creating an object of that class
 compels a user to override abstract methods in a child class

abstract class = a class containing one or more abstract methods
abstract method = a method that has a declaration but does not have an implementation"""

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

class Motorcycle(Vehicle):
#the children class always carry the functions and methods in the abstract class
    def go(self):
        print("You ride the motorcycle")

#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()