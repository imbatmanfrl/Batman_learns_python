class Car:

    def __init__(self,make,model,year,color):#constructor
        self.make = make# first the attributes
        self.model = model
        self.year = year
        self.color = color


    def drive(self): #self as in the object using this method
        print("This " + self.model+ " is driving")

    def stop(self):
        print("This " + self.model+" is stopped")

