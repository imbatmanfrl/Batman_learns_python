#Walrus operator :=, it's an assignment expression
from heapq import heappush

#assigns values to variables as part of a larger expression

#happy = True
#print(happy)

#print(happy := True)

#foods = list()
#while True:
#    food = input("What food do you like?: ").capitalize()
#    if food == "Quit":
#        break
#    foods.append(food)
#print(foods)

foods = list()
#food = ""
while food := input("What food you like?: ").capitalize() != "Quit":
    foods.append(food)
