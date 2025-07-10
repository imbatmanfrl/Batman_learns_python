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

    expense_list = []

"""class Expenditure:

    def __init__(self,expenditure,cost,interval):
        self.expenditure = expenditure
        self.cost = cost
        self.interval = interval

    def total_expenditure(self):
        pass"""

#Methods, Actions that the budget model can do like the prediction after x number of months, total saved, total invested,
# total expenditure, a method function that counts weeks

class Calc(BudgetModel):
    def weekly_leftover(self):
        earnings_left = f"You have {self.weekly_earnings - (self.weekly_expenditure + self.weekly_savings + self.weekly_investments)} left!"
        return earnings_left

    def weeks_since_start(self,weeks_passed):
        current_week = f"{weeks_passed + 1} week(s) has passed since you started!"
        return current_week

    def total_earned(self,weeks_passed):
        earned = f"You earned #{self.weekly_earnings*weeks_passed} after {weeks_passed} week(s)!"
        return earned

    def total_saved(self):
        pass

    def total_inested(self):
        pass

    def projections(self):
        pass



