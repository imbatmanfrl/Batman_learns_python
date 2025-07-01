#import  random
from logging import exception

#x = random.randint(1,4)
#y = random.random()

#my_list = ["rock","paper","scissors"]
#z = random.choice(my_list)

#cards = [1,2,3,4,5,6,7,8,9,"j","q","A"]
#random.shuffle(cards)
#print(cards)

# exception handling is an event detected during execution that interrupt the normal flow of a program

#try:
#    1/0
#except Exception as e:
#    print("caught an error:", e)

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by:"))
    result = numerator / denominator
except ZeroDivisionError as e :
    print(e)
    print("You can't divide by zero dipshit!")
except ValueError as e:
    print(e)
    print("Did you not pay attention when they were teaching you in school?")
except exception as e:
    print(e)
    print("Something went wrong")
else:
    print(result)
finally:
    print("This will always execute ")