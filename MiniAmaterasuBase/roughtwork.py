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
# I want to combine both re_occurring expenses and one_time_purchase into one list
        pass

    def total_spent(self):
        pass

    def total_earned(self,weeks_passed):
        pass

    def total_saved(self):
        pass

    def projections(self):
        pass

#append
"""calc = Calc
calc.weekly_leftover()"""
spend = Spending()
spend.re_occurring("Data","Transport","Spotify","F")
spend.price(1500,800,2000,3500)
spend.expenses()
spend.one_time_purchases(random=["FIFA","Workbook","Bread"],cost=[500,4250,500])
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
