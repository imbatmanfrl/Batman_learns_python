#This will be just a small program that I can use to track my savings, spending and like project my future financial situation
#based on the input and current performance and the projection changes as the performance changes
#Alright this program will need a couple of things, what should a financial budget have
#I'm starting to see the importance of flowchart and pseudocode
#from time import strptime

import datetime
import json
from datetime import timedelta

class BudgetModel:

    def __init__(self):
        self.weekly_earnings = []
        self.weekly_expenditure = []
        self.weekly_savings = []
        self.weekly_investments = []
        self.all_earnings = []
        self.all_expenditure = []
        self.all_savings = []
        self.all_investments = []

    def earn_daily(self, *args):
        earned = list(args)
        earned_today = sum(earned)
        today = datetime.date.today().isoformat()
        print(f"You earned #{earned_today} today")
        self.weekly_earnings.append(earned_today)


        earning_entry = {
            "amount": earned_today,
            "date": today,
            "breakdown": earned
        }
        self.all_earnings.append(earning_entry)
        today_total = sum(entry['amount'] for entry in self.all_earnings if entry['date'] == today)

        with open ("all_earnings.json",'w') as file:
            json.dump(self.all_earnings,file,indent=2)

        return today_total


    def spent_today(self, name, cost):
        item_date = datetime.date.today().isoformat()
        spent = {
            "item": name,
            "cost": cost,
            "date": item_date
        }
        today_date = datetime.date.today()
        self.weekly_expenditure.append(cost)
        print(f"you spent #{total} this week")
        self.all_expenditure.append(spent)
        total = sum(cost for cost in self.all_expenditure if item_date == today_date)

        with open("all_expenditure.json", "w") as file:
            json.dump(self.all_expenditure, file, indent=2)
        return total

    def save_today(self, *args):
        saved = list(args)
        saved_today = sum(saved)
        date = datetime.date.today().isoformat()
        print(f"You Saved #{saved_today} today")
        saved = {
            "amount": saved_today,
            "date": date,
            "breakdown": saved
        }
        self.weekly_savings.append(saved_today)
        self.all_savings.append(saved)

        with open("all_savings.json", "w") as file:
            json.dump(self.all_savings, file, indent=2)

    def invest(self, name, cost):
        date = datetime.date.today().isoformat()
        invested = {
            "name": name,
            "cost": cost,
            "date": date
        }
        self.weekly_investments.append(cost)
        print(f"you invested #{self.weekly_investments} this week")
        self.all_investments.append(invested)
        with open("all_investments.json", "w") as file:
            json.dump(self.all_savings, file, indent=2)


class WeeksPassed:

    def starting_date(self,year,month,day):

        self.year = year
        self.month = month
        self.day = day
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


class Calc(BudgetModel,WeeksPassed):

    def weekly_amounts(self):
        today = datetime.date.today()
        monday = today - timedelta(days=today.weekday())
        monday_str = monday.strftime('%Y-%m-%d')
        with open("all_earnings.json", "r") as file:
            data = json.load(file)

            self.earn_total = 0
            for item in data:
                date = item.get("date", "")
                amount = item.get("amount", 0)
                if date >= monday_str:
                    self.earn_total += amount
                print(self.earn_total)

        with open("all_expenditure.json", "r") as file:
            data1 = json.load(file)

            self.spend_total = 0
            for item1 in data1:
                date1 = item1.get("date", "")
                amount1 = item1.get("cost", 0)
                if date1 >= monday_str:
                    self.spend_total += amount1
                print(self.spend_total)

    def weekly_leftover(self):
        arith = self.earn_total - self.spend_total
        whats_left = arith
        with open("WeeklySpent.json", "a") as file:
            json.dump(whats_left, file, indent=2)

    def tottal_earned(self):
        self.total_earned = 0
        with open("all_earnings.json", "r") as file:
            data = json.load(file)


        for item in data:
            amount = item.get("amount", 0)
            start_date = self.beginning_date
            self.total_earned += amount

            return f"you have earned #{self.total_earned} since {start_date}"

    def tottal_spent(self):
        self.total_spent = 0
        with open("all_expenditure.json", "r") as file:
            data = json.load(file)

        for item in data:
            amount = item.get("cost", 0)
            start_date = self.beginning_date
            self.total_spent += amount
            return f"you have spent #{self.total_spent} since {start_date}"

    def tottal_saved(self):
        self.total_saved = 0
        with open("all_savings.json", "r") as file:
            data = json.load(file)

        for item in data:
            amount = item.get("amount", 0)
            start_date = self.beginning_date
            self.total_saved += amount

            return f"you have saved #{self.total_saved} since {start_date}"

    def tottal_invested(self):
        self.total_invested = 0
        with open("all_investments.json", "r") as file:
            data = json.load(file)

        for item in data:
            amount = item.get("cost", 0)
            start_date = self.beginning_date
            self.total_invested += amount

            return f"you have saved #{self.total_invested} since {start_date}"


    def projections(self, duration):# in weeks
        self.duration = duration
        try:
            projected_spending = (self.total_spent / self.how_long_weeks) * self.duration
            projected_earning = (self.total_earned / self.how_long_weeks) * self.duration
            projected_savings = (self.total_saved/ self.how_long_weeks) * self.duration
            # all these are based on previous performance I guess
            print(f"{duration} weeks from now, you would have earned #{projected_earning},spent #{projected_spending} and saved #{projected_savings}")
        except ZeroDivisionError:
            print(f"Zero weeks has passed since you started")


#int type not iterable