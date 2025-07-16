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

budget = BudgetModel(10000,2000,5000,3000)
budget.weeks_since_start(1)
print(budget.total_earned(1))
budget.expense_list.append("Spotify")
print(budget.expense_list)"""

from miniPerformanceModel import BudgetModel,WeeksPassed,Spending

class Calc(BudgetModel,Spending,WeeksPassed):
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

    def total_spent(self):
#I dont know if this code I wrote works 😅😂 what i did was from the Weekly spent txt file i created,
#I got like all the amount i spent each week then I used summ to add everything and then multiplied by how many weeks passed since start

        with open ("WeeklySpent.xtx","r") as file:
            weekly_spent_str = file.read().strip()
            summm = sum(weekly_spent_str)
            converted = float(summm)
        tottal_spent = converted * self.how_long_weeks
        print(f"So far, you have spent #{tottal_spent} since you strted budgetting")

#this method calculated how much i've spent sine i started using the model
#write the date of which we started inside of  file,
#read read the contents for that file and turn it into like an int or float value
#append multiply by recent weekly spending and append back into the file
#then the following week ou start with read
#or better yet, since we now have a function that can tell us how long its been since weve started, all we need now is for this total_spent
#funcoin to be able to store how much we spend each week since start into a file and multiply it by weeks that have passed since strat
#        with open("StartDate.txt","r")as file:
#            start_week = file.read()

    def total_earned(self,weeks_passed):
        pass

    def total_saved(self):
        pass

    def projections(self):
        pass

#append
"""budget = BudgetModel(10000,2000,5000,3000)
week =WeeksPassed
spend = Spending()
spend.re_occurring("Data","Transport","Spotify","F")
spend.price(1500,800,2000,3500)
spend.expenses()
spend.one_time_purchases(random=["FIFA","Workbook","Bread"],cost=[500,4250,500])"""
#sine Calc inherits from all the classes, you can pass all the arguments into calc
calc = Calc(1000,2000,5000,3000)
calc.re_occurring("Data","Transport","Spotify","F")
calc.price(1500,800,2000,3500)
calc.one_time_purchases(random=["FIFA","Workbook","Bread"],cost=[500,4250,500])
calc.weekly_leftover()
#Now we need a way to be able to map the prices to their corresponding expenditure ther than that it looks simple and i lke it.
#there isn't mcuh questions yet ill create a sperate python file that will run the code while this the engine will be in its own file
#initialy, I'd have gone for defining functions like must have and necssities then put them in  a recurring function but too ambiguous


#the issue here is that the program can't check if you spelt yes or no wrongly, and theres no way to know if items were paired to
#prie and stuff, and why are we receiving input from the terminal i thought for a gui we pass in arguments in a block of code, this program
#has flaws i don't know what i'm doing anymore

"""budget = BudgetModel(10000,2000,5000,3000)
weeks_passed = WeeksPassed()
weeks_passed.time_since_last_update()
weeks_passed.store()"""
