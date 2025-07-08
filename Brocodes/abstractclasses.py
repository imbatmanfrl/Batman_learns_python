"""prevents a user from creating an object of that class
 compels a user to override abstract methods in a child class

abstract class = a class containing one or more abstract methods
abstract method = a method that has a declaration but does not have an implementation

The major difference between this and a normal parent class is that a normal parent class will already be instantiated, and you dont need
any special like derived method for the child class I mean in the parent class i can say alive = True so after declaring like 50
animals i Don't need to create an alive function inside each one of them, but all of them will have access to that method if i chosse to call
the method for each child class but in an abstract class, one i declare an abstract method in the abstract parent class, I mustn't
write any code within that abstract method and I have to write 50 different methods using the abstract method as a blueprint and it's a must"""


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