class Car:

    wheels = 4 #class variable
    """for class variables, every object that uses this class will have this
    constant attribute whereas for instance variable is a unique atrribute that
    only a particular object has, for exam all cars have 4 wheels and 2 side mirrors
    that is a class variable, a common attribute for all cars, but not all cars are named ford or are from the same year
    those are instance variables!"""
    def __init__(self,make,model,year,color):#constructor
        self.make = make# first the attributes  #instance variable
        self.model = model #instance variable
        self.year = year  #instance variable
        self.color = color #instance variable


    def drive(self):#self as in the object using this method
        print(f"This {self.model} {self.year} is driving")
        """print("This " + self.model+ " is driving")"""

    def stop(self):
        print("This " + self.model+ str(self.year) +" is stopped")

