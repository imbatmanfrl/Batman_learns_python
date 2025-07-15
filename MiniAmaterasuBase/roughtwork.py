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

    def one_time_purchases(self,random=None,cost=None):
        self.random = list[random]
        self.cost = list[cost]
        full_list = dict(zip(self.random,self.cost))
        print(f"Your one time purchases are {full_list}")

#append

spend = Spending()
spend.re_occurring("Data","Transport","Spotify","F")
spend.price(1500,800,2000,3500)
spend.expenses()
spend.one_time_purchases(random="FIFA, Workbook, Bread",cost="500, 4250, 500")
#Now we need a way to be able to map the prices to their corresponding expenditure ther than that it looks simple and i lke it.
#there isn't mcuh questions yet ill create a sperate python file that will run the code while this the engine will be in its own file
#initialy, I'd have gone for defining functions like must have and necssities then put them in  a recurring function but too ambiguous
spend.one_time_purchases(None)


#the issue here is that the program can't check if you spelt yes or no wrongly, and theres no way to know if items were paired to
#prie and stuff, and why are we receiving input from the terminal i thought for a gui we pass in arguments in a block of code, this program
#has flaws i don't know what i'm doing anymore

"""budget = BudgetModel(10000,2000,5000,3000)
weeks_passed = WeeksPassed()
weeks_passed.time_since_last_update()
weeks_passed.store()"""
