"""This will be just a small program that I can use to track my savings, spending and like project my future financial situation
based on the input and current performance and the projection changes as the performance changes
Alright this program will need a couple of things, what should a financial budget have
I'm starting to see the importance of flowchart and pseudocode"""
#from time import strptime


class BudgetModel:

    def earn_daily(self, *args):
        self.weekly_earnings = []
        earned = list(args)
        earned_today = sum(earned)
        print(f"You earned #{earned_today} today")
        self.weekly_earnings.append(earned_today)

    def spent_today(self, name, cost):
        item_name = list(name)
        item_cost = list(cost)
        the_zip = zip(item_name, item_cost)
        self.weekly_expenditure = dict(the_zip)
        print(self.weekly_expenditure)

    def save_today(self,*args):
        self.weekly_savings = []
        saved = list(args)
        saved_today = sum(saved)
        print(f"You Saved #{saved_today} today")
        self.weekly_savings.append(saved_today)

    def invest(self,name,cost):
        item_name = list(name)
        item_cost = list(cost)
        the_zip = zip(item_name, item_cost)
        self.weekly_investments = dict(the_zip)


import datetime
class WeeksPassed:

    def starting_date(self,year,month,day):
        self.year = int(input("Enter starting year!: "))
        self.month = int(input("Enter starting month!: "))
        self.day = int(input("Enter starting date!: "))

        year = self.year
        month = self.month
        day = self.day
        try:
            self.beginning_date = datetime.date(year,month,day) #maybe I should write this date manually
            with open("StartDate.txt","w")as file:
                file.write(str(self.beginning_date))
                print(self.beginning_date)
            with open("StartDate.txt","r") as file:
                self.the_date = file.read().strip()
                self.get_how_long = datetime.datetime.strptime(self.the_date,"%Y-%m-%d").date()
                self.latest_date = datetime.date.today()
                delta = self.latest_date - self.get_how_long
                self.how_long_weeks = delta.days //7
                print(f"You've been budgeting for {self.how_long_weeks} week(s)")
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
                beta = today - stored_date
                days_passed = beta.days // 7
                print(f"{days_passed} weeks has passed since you last budgeted!")

        except FileNotFoundError:
            print("No saved date appeared yet!")

    def store(self,update):
        self.update = update
        if self.update != "no":
            # this stores that date in an external txt file
            stored = datetime.date.today()
            with open("last_update.txt", "w") as file:
                file.write(str(stored))
                print(stored)
        elif self.update == "no":
            print("Have a great day then!")

class Calc(BudgetModel,WeeksPassed):
#now we redo the calculatons, this since things like weekly expenditure are dictionaries now
# were going to have to seperate the values needed fir arithmetic operations
    def weekly_leftover(self):
        weekly_value = sum(self.cost)
        print(f"You spent #{weekly_value} on {self.weekly} this week")
        once_value = sum(self.tag)
        print(f"You spent #{once_value} on {self.random} this week")
        combined_total = weekly_value + once_value
        print(f"You've spent a total of #{combined_total} this week")
        whats_left = int(self.weekly_earnings) - combined_total
        print(f"You have #{whats_left} left this week")
        with open("WeeklySpent.txt","a") as file:
            file.write(str(combined_total)+"\n")


    def total_earned(self):
        with open("TotalEarned.txt", "a") as file:
            file.write(str(self.weekly_earnings)+"\n")
        with open("TotalEarned.txt", "r") as file:
            lines = file.readlines()
            earns = [float(line.strip()) for line in lines if line.strip()]
            self.earned_total = sum(earns)
            print(f"You have earned #{self.earned_total} since {self.beginning_date}")


    def total_spent(self):
        with open("TotalSaved.txt","a") as file:
            file.write(str(self.weekly_savings)+"\n")
        with open("TotalSaved.txt", "r") as file:
            lines = file.readlines()  # reads each line file into a list
            weekly_values = [float(line.strip()) for line in lines if line.strip()]  # turns all lines into numbers
            self.tottal_spent = sum(weekly_values)  # I dont need to multiply by weeks_passes since im appending the spending of every week
             # into a file line by line
            print(f"So far, you have spent #{self.tottal_spent} since {self.beginning_date}")


    def total_saved(self):
        with open("TotalSaved.txt", "a") as file:
            file.write(str(self.weekly_savings) + "\n")
        with open("TotalSaved.txt", "r") as file:
            linesss = file.readlines()
            savedd = [float(line.strip()) for line in linesss if line.strip()]
            self.saved_total = sum(savedd)
            print(f"You have saved #{self.saved_total} since {self.beginning_date}")


    def projections(self, duration):  # in weeks
        self.duration = duration
        try:
            projected_spending = (self.tottal_spent / self.how_long_weeks) * self.duration
            projected_earning = (self.earned_total / self.how_long_weeks) * self.duration
            projected_savings = (self.saved_total / self.how_long_weeks) * self.duration
            # all these are based on previous performance I guess
            print(f"{duration} weeks from now, you would have earned #{projected_earning},spent #{projected_spending} and saved #{projected_savings}")
        except ZeroDivisionError:
            print(f"Zero weeks has passed since you started")

