"""This will be just a small program that I can use to track my savings, spending and like project my future financial situation
based on the input and current performance and the projection changes as the performance changes
Alright this program will need a couple of things, what should a financial budget have
I'm starting to see the importance of flowchart and pseudocode"""

class BudgetModel:

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

class Spending:

    def re_occurring(self, *args):
        self.weekly = list(args)
        print(self.weekly)

    def price(self, *args):
        self.cost = list(args)

    def expenses(self):
        self.compiled = dict(zip(self.weekly, self.cost))
        print(self.compiled)

    def one_time_purchases(self, random=None, cost=None):
        self.random = list(random)
        self.tag = list(cost)
        the_zip = zip(self.random, self.tag)
        miscelieous = dict(the_zip)
        print(f"one-time purchases {miscelieous}")








class Calc(BudgetModel,WeeksPassed,Spending):
#now we want to calculate how much we have at the end of each week, how much we've saved so far,
# how much money we actually earned before expenses
#how much money we've spent on expenses up until now
#how much we'll have earned after x number of years, only problem is
# i want this part to be dynamic as spending and earning frequency may vary
    def weekly_leftover(self):

        weekly_value = sum(self.cost)
        print(f"You spent #{weekly_value} on {self.weekly} this week")
        once_value = sum(self.tag)
        print(f"You spent #{once_value} on {self.random} this week")
        combined_total = weekly_value + once_value
        whats_left = int(self.weekly_earnings) - combined_total
        print(f"You have #{whats_left} left this week")

    def total_spent(self):
        pass


    def total_earned(self,weeks_passed):
        pass

    def total_saved(self):
        pass

    def projections(self):
        pass


