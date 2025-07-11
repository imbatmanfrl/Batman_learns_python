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

import datetime
class WeeksPassed:

    def __init__(self,weeks):
        self.weeks = weeks

    def last_saved(self):
        date = datetime.date.today()
        return date

    def store(self):
        stored = self.last_saved()
        with open("last_update.txt", "w") as file:
            file.write(str(stored))
        print(self.last_saved())

    from datetime import datetime, date
    def time_since_last_update(self):
        try:
            with open("last_update.txt","r") as file:
                stored_date_str = file.read().strip()
                stored_date = datetime.strptime(stored_date_str,"%Y-%m-%d").date()
                today = datetime.date.today()
                days_passed = today - stored_date
                return f"{days_passed} days has passed since you last budgeted!"
        except FileNotFoundError:
            print("No saved date appeared yet!")
            """calc = int(updated) - int(todays_date)
            return calc
        finally:
            print(f"This is when you last updated your budget {self.time_since_last_update()}")"""

weeks_passed = WeeksPassed(2)
weeks_passed.store()
weeks_passed.time_since_last_update()