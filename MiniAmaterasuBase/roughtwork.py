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

# Attributes, What a budget has like to get a budget you need like income/earnings, expenditures, monthly finances/bills
#This program we're trying something different, we're going to be passing input as parameters not passing it through the terminal
    def __init__(self,weekly_earnings,weekly_expenditure,weekly_savings,weekly_investments,):
        self.weekly_earnings = weekly_earnings
        self.weekly_expenditure = weekly_expenditure
        self.weekly_savings = weekly_savings
        self.weekly_investments = weekly_investments

    expense_list = []

#Methods, Actions that the budget model can do like the prediction after x number of months, total saved, total invested,
# total expenditure, a method function that counts weeks

    def weeks_since_start(self,weeks_passed):
        current_week = weeks_passed + 1
        return current_week

    def total_earned(self,weeks_passed):
        earned = f"You earned #{self.weekly_earnings*weeks_passed} after {weeks_passed} weeks"
        return earned


budget = BudgetModel(10000,2000,5000,3000)
budget.weeks_since_start(1)
print(budget.total_earned(1))
budget.expense_list.append("Spotify")
print(budget.expense_list)"""
from miniPerformanceModel import BudgetModel

class Spending:
    investments = [("Forex",3500)]

    necessities = [("Data",1500),
                   ("Transport",800)]

    must_have = [("Spotify Premium",2000)]

    re_occurring = {"Investments":investments,
                    "Necessities":necessities,
                    "Must Have": must_have}
    """re_occurring = [investments, necessities, must_have]"""

    one_time_purchases = []

    occurrence = input("Did all this happen this week?(YES/NO): ").lower()
    if occurrence == "no":

        skipped_items = []
        left_spent_on = []
        """for i in re_occurring:
            print(f"Which of these did you alter {i}")"""


#all that is left now is for the user program to be able to update the last_saved function,
# as it is it'll be using the current date of every day as the last saved.
# we want to be able to append that file or idk i think im right

"""budget = BudgetModel(10000,2000,5000,3000)
weeks_passed = WeeksPassed()
weeks_passed.time_since_last_update()
weeks_passed.store()"""
