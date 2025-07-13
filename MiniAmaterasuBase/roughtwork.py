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

    re_occurring = ["Forex","Transport","Data","Spotify"]
    """re_occurring = [investments, necessities, must_have]"""

    one_time_purchases = []

    print(re_occurring)
    occurrence = input("Did all this happen this week?(YES/NO): ").lower()
    if occurrence == "no":
       """How do i say "did you invest in x this week? if yes how much " for each item in the list but i dont want to have to type it 
       manually for each item oin the list, it'll be a block of code that will iterate and loop through all the elements in the list 
       using their respective indexes"""
       while True:
           loop = re_occurring

    else:
        print(f"All re_occurring expenses were made")

    anything_else = input("Did yoy make any one time purchase?").lower()
    if anything_else == "yes":
        others = (input("What else?:"))
        one_time_purchases.append(others)
        print(one_time_purchases)

spending = Spending()






#all that is left now is for the user program to be able to update the last_saved function,
# as it is it'll be using the current date of every day as the last saved.
# we want to be able to append that file or idk i think im right

"""budget = BudgetModel(10000,2000,5000,3000)
weeks_passed = WeeksPassed()
weeks_passed.time_since_last_update()
weeks_passed.store()"""
