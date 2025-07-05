#Inheritance
"""class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Owl(Animal):#Bat is the child class and animal is the parent class
    def fly(self):
        print("This Bat is flying")

class Fish(Animal):
    def swim(self):
        print("This fish is swimming")

class Cheetah(Animal):
    def run(self):
        print("This Cheetah is runnig")


owl = Owl()
fish = Fish()
cheetah = Cheetah()

#print(owl.alive)
#print(fish.eat())
#print(cheetah.sleep())

owl.fly()
fish.swim()
cheetah.run()"""

#Multilevel Inheritance- when a derived class (child class) inherits from another derived class

"""class Organism:

    alive = True

class Animal(Organism):

    def eat(self):
        print("This animal is eating")

class Owl(Animal):

    def hoot(self):
        print("This owl,🦉 is hooting")


owl = Owl()
print(owl.alive)
print(owl.eat())
print(owl.hoot())"""

#Multiple Inheritance- A child class is derived from more than one parent class

class Prey:

    def flee(self):
        print("This Animal is fleeing!")


class Predator:

    def hunt(self):
        print("This animal is hunting!")


class Rabbit(Prey):
    pass

class Owl(Predator):
    pass

class Fish(Predator,Prey):
    pass

rabbit = Rabbit()
owl =Owl()
fish = Fish()


rabbit.flee()
owl.hunt()
fish.hunt()
fish.flee()