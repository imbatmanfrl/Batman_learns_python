class Car:

    wheels = 4 #class variable
    """for class variables, every object that uses this class will have this
    constant attribute whereas for instance variable is a unique atrribute that
    only a particular object has, for exam all cars have 4 wheels and 2 side mirrors
    that is a class variable, a common attribute for all cars, but not all cars are named ford or are from the same year
    those are instance variables!"""
    def __init__(self):#constructor
        self.make = input("Make?: ")# first the attributes  #instance variable
        self.model = input("model?: ") #instance variable
        self.year = input("year?: ")  #instance variable
        self.color = input("color?: ") #instance variable


    def drive(self):#self as in the object using this method
        print(f"This {self.model} {self.year} is driving")
        """print("This " + self.model+ " is driving")"""

    def stop(self):
        print(f"This {self.make} {self.model} is stopped")
        #print("This " + self.model+ str(self.year) +" is stopped")

