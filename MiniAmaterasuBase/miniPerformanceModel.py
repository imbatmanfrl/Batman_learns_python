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
        print(f"You've spent a total of #{combined_total} this week")
        whats_left = int(self.weekly_earnings) - combined_total
        print(f"You have #{whats_left} left this week")


    def total_earned(self):
        with open("TotalEarned.txt", "a") as file:
            file.write(str(self.weekly_earnings) + "\n")
        with open("TotalEarned.txt", "r") as file:
            liness = file.readline()
            earns = [float(line.strip()) for line in liness if line.strip()]
            self.earned_total = sum(earns)
            print(f"You have earned #{self.earned_total} since {self.beginning_date}")


    def total_spent(self):
    # I dont know if this code I wrote works 😅😂 what i did was from the Weekly spent txt file i created,
    # I got like all the amount i spent each week then I used summ to add everything and then multiplied by how many weeks passed since start

        with open("WeeklySpent.xtx", "r") as file:
            lines = file.readline()  # reads each line file into a list
            weekly_values = [float(line.strip()) for line in lines if line.strip()]  # turns all lines into numbers
            """weekly_spent_str = file.read().strip()
            summm = sum(weekly_spent_str)
            converted = float(summm)"""
            self.tottal_spent = sum(weekly_values)  # I dont need to multiply by weeks_passes since im appending the spending of every week
             # into a file line by line
            print(f"So far, you have spent #{self.tottal_spent} since {self.beginning_date}")


    def total_saved(self):
        with open("TotalEarned.txt", "a") as file:
            file.write(str(self.weekly_savings) + "\n")
        with open("TotalEarned.txt", "r") as file:
            linesss = file.readline()
            savedd = [float(line.strip()) for line in linesss if line.strip()]
            self.saved_total = sum(savedd)
            print(f"You have earned #{self.saved_total} since {self.beginning_date}")


    def projections(self, duration):  # in weeks
        self.duration = duration
        projected_spending = self.duration * self.tottal_spent
        projected_earning = self.duration * self.earned_total
        projected_savings = self.duration * self.saved_total
        # all these are based on previous performance I guess
        print(f"{duration} weeks from now, you would have earned #{projected_earning},spent #{projected_spending} and saved #{projected_savings}")


