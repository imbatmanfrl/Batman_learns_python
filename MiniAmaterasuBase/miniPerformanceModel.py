"""This will be just a small program that I can use to track my savings, spending and like project my future financial situation
based on the input and current performance and the projection changes as the performance changes
Alright this program will need a couple of things, what should a financial budget have
I'm starting to see the importance of flowchart and pseudocode"""

#First will be all the input needed to be able to generate output

class BudgetModel:

# Attributes, What a budget has like to get a budget you need like income/earnings, expenditures, monthly finances/bills
#This program we're trying something different, we're going to be passing input as parameters not passing it through the terminal
    def __init__(self,weekly_earnings,weekly_expenditure,weekly_savings,weekly_investments,):
        self.weekly_earnings = weekly_earnings
        self.weekly_expenditure = weekly_expenditure
        self.weekly_savings = weekly_savings
        self.weekly_investments = weekly_investments

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

#Methods, Actions that the budget model can do like the prediction after x number of months, total saved, total invested,
# total expenditure, a method function that counts weeks

class Spending:
#I want to spend this night changing from accepting input to accepting arguments

    def re_occurring(self,*args):
        self.weekly = list(args)
        print(self.weekly)

    def price(self,*args):
        self.cost = list(args)

    def expenses(self):
        compiled = dict(zip(self.weekly,self.cost))
        print(compiled)

    def one_time_purchases(self,random= None ,cost=None):
        self.random = list(random)
        self.cost = list(cost)
        the_zip = zip(self.random,self.cost)
        miscelieous = dict(the_zip)
        print(miscelieous)

class Calc(BudgetModel,WeeksPassed,Spending):
    def weekly_leftover(self):
        pass

    def total_earned(self,weeks_passed):
        pass

    def total_saved(self):
        pass

    def total_inested(self):
        pass

    def projections(self):
        pass



