#an object is an instance of a class
#attributes = what as object is or has
# methods = actions/ what an object can do
# class = blueprint for an object

from car import Car

car_1 = Car("Ferrari","LaFerrari","2015","Silver")
car_2 = Car("Pagani","Zonda","2018","Black")

#print(car_2.make)
#print(car_2.model)
#print(car_2.year)
#print(car_2.color)

car_1.drive()
car_2.stop()