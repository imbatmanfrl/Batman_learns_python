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

    def re_occuring(self, *args):
        self.weekly = [*args]
        print(self.weekly)

    print(f"Did all these happen this week?")

    def yes_or_no(self,answer):
        self.answer = answer
    confirmed_expense = []
    one_time_purchases = []

    def confirm(self,response):
        self.response = response
        if self.answer == "yes":
            for item in self.weekly:
                print(f"did you spend on {item} this week?")
                if self.response == "yes":
                    try:
                        price = float(input(f"How much did you spend on {item}?: "))
                        confirmed_expense = {item, price}
                        return confirmed_expense
                    except ValueError:
                        print("Enter Number not values!")

        else:
            print(f"All re_occurring expenses were made")

    while True:
        anything_else = input("Did yoy make any one time purchase?").lower()
        if anything_else == "yes":
            others = (input("What else?: "))
            for items in others:
                cost = input(f"How much is {items}?: ")
                one_time_purchases.append(others)
            print(one_time_purchases)
        elif anything_else != "yes":
            break
"""one time purchases could be more than one in number, so i created a while loop to ask repeatedly so far the user saids yes, 
bu i also need a ways to collect he cost and make it into a dictionary or something, wtf am i even building ??!"""

#the issue here is that the program can't check if you spelt yes or no wrongly, and theres no way to know if items were paired to
#prie and stuff, and why are we receiving input from the terminak i thought for a gui we pass in arguments in a block of code, this program
#has flaws i don't know what i'm doing anymore




spending = Spending("Forex","Fifa","Transport","Food","Data",answer="yes")
spending.response("yes")






#all that is left now is for the user program to be able to update the last_saved function,
# as it is it'll be using the current date of every day as the last saved.
# we want to be able to append that file or idk i think im right

"""budget = BudgetModel(10000,2000,5000,3000)
weeks_passed = WeeksPassed()
weeks_passed.time_since_last_update()
weeks_passed.store()"""
