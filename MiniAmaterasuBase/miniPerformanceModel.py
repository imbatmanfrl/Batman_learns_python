"""This will be just a small program that I can use to track my savings, spending and like project my future financial situation
based on the input and current performance and the projection changes as the performance changes
Alright this program will need a couple of things, what should a financial budget have
I'm starting to see the importance of flowchart and pseudocode"""
#from time import strptime


class BudgetModel:

    def __init__(self,weekly_earnings,weekly_expenditure,weekly_savings,weekly_investments,):
        self.weekly_earnings = weekly_earnings
        self.weekly_expenditure = weekly_expenditure
        self.weekly_savings = weekly_savings
        self.weekly_investments = weekly_investments

import datetime
class WeeksPassed:

    def starting_date(self,start):
        try:
            self.beginning_date = start #maybe I should write this date manually
            with open("StartDate.txt","w")as file:
                file.write(str(self.beginning_date))
                print(self.beginning_date)
            with open("StartDate.txt","r") as file:
                self.the_date = file.read().strip()
                self.get_how_long = datetime.datetime.strptime(self.the_date,"%Y-%m-%d").date()
                self.latest_date = datetime.date.today()
                self.how_long_weeks = (self.latest_date - self.get_how_long)//7
                print(f"You've been budgeting for {self.how_long_weeks} weeks")
        except FileNotFoundError:
            print(f"StartDate.txt does not exist")

#7-16-2025

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
    def weekly_spending(self):
#Here I had to pass in first_week= Nonee as an argument cuz if i said that the compter should write sel.combined_total in one block of code
#then im telling it to append in another i dont think it'll work the way i want, so one block of code where the user manually enters how much
#they spent the first time they used this model which is saved into a file and another block where the saved file is appended with the
#most recent week's spending
        weekly_value = sum(self.cost)
        print(f"You spent #{weekly_value} on {self.weekly} this week")
        once_value = sum(self.tag)
        print(f"You spent #{once_value} on {self.random} this week")
        self.combined_total = weekly_value + once_value
        print(f'You spent #{self.combined_total} this week')
#        first_week_spending = first_week
#        with open ("WeeklySpent.xtx","w") as file:
#            file.write(str(first_week_spending))
        with open("WeeklySpent.xtx","a") as file:
            file.write(str(self.combined_total)+ "\n")


    def weekly_leftover(self):

        whats_left = int(self.weekly_earnings) - self.combined_total
        print(f"You have #{whats_left} left this week")

    def total_spent(self):
        pass


    def total_earned(self,weeks_passed):
        pass

    def total_saved(self):
        pass

    def projections(self):
        pass


