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
from budgetModel import BudgetModel

import datetime
class WeeksPassed:

    def time_since_last_update(self):
        # this now turns the date of that external txt file into a data type which can be subtracted from todays date to show
        # you how ong it has been since you logged in a budget
        try:
            with open("last_update.txt", "r") as file:
                stored_date_str = file.read().strip()
                stored_date = datetime.datetime.strptime(stored_date_str, "%Y-%m-%d").date()
                today = datetime.date.today()
                days_passed = (today - stored_date) // 7
                print(f"{days_passed} weeks has passed since you last budgeted!")

        except FileNotFoundError:
            print("No saved date appeared yet!")

#I can turn current_date and updt into one block of code that san read today's date and save it into an external file
    def store(self):
        update = input("Do you want to update your Budget?(YES/NO): ").lower()
        if update != "no":
            # this stores that date in an external txt file
            stored = datetime.date.today()
            with open("last_update.txt", "w") as file:
                file.write(str(stored))
                print(stored)
        elif update == "no":
            print("Have a great day then!")


#all that is left now is for the user program to be able to update the last_saved function,
# as it is it'll be using the current date of every day as the last saved.
# we want to be able to append that file or idk i think im right

budget = BudgetModel(10000,2000,5000,3000)
weeks_passed = WeeksPassed()
weeks_passed.time_since_last_update()
weeks_passed.store()
