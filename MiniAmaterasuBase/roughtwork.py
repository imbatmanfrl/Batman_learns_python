"""Inheritance
Abstract and parent class
super function
walrus operator
storing Iterables
lambda function
map function
object as arguments
python oriented programming
Method Overriding and chaining
assigning functions to variables"""

"""class BudgetModel:

budget = BudgetModel(10000,2000,5000,3000)
budget.weeks_since_start(1)
print(budget.total_earned(1))
budget.expense_list.append("Spotify")
print(budget.expense_list)"""
from miniPerformanceModel import BudgetModel

class Spending:
#I want to spend this night changing from accepting input to accepting arguments
    re_occurring = ["F","Transport","Data","Spotify"]
    """re_occurring = [investments, necessities, must_have]"""

    one_time_purchases = []
    """How do i say "did you invest in x this week? if yes how much " for each item in the list but i dont want to have to type it 
    manually for each item oin the list, it'll be a block of code that will iterate and loop through all the elements in the list 
    using their respective indexes"""

    print(re_occurring)
    occurrence = input("Did all this happen this week?(YES/NO): ").lower()
    if occurrence == "no":


        confirmed_expense = []
#the issue here is that the program can't check if you spelt yes or no wrongly, and theres no way to know if items were paired to
#prie and stuff, and why are we receiving input from the terminak i thought for a gui we pass in arguments in a block of code, this program
#has flaws i don't know what i'm doing anymore
        for item in re_occurring:
            response = input(f"did you spend on {item} this week?(YES/NO): ").lower()
            if response == "yes":
                try:
                    price = float(input(f"How much did you spend on {item}?: "))
                    confirmed_expense= {item,price}
                except ValueError:
                   print("Enter Number not values!")


    else:
        print(f"All re_occurring expenses were made")
        """one time purchases could be more than one in number, so i created a while loop to ask repeatedly so far the user saids yes, 
        bu i also need a ways to collect he cost and make it into a dictionary or something, wtf am i even building ??!"""
    while True:
        anything_else = input("Did yoy make any one time purchase?").lower()
        if anything_else == "yes":
            others = (input("What else?: "))
            for items in others:
                cost=input(f"How much is {items}?: ")
            one_time_purchases.append(others,cost)
            print(one_time_purchases)
        elif anything_else != "yes":
            break


spending = Spending()






#all that is left now is for the user program to be able to update the last_saved function,
# as it is it'll be using the current date of every day as the last saved.
# we want to be able to append that file or idk i think im right

"""budget = BudgetModel(10000,2000,5000,3000)
weeks_passed = WeeksPassed()
weeks_passed.time_since_last_update()
weeks_passed.store()"""
