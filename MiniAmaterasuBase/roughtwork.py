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
from miniPerformanceModel import BudgetModel

class Spending:
#I want to spend this night changing from accepting input to accepting arguments

    def re_occurring(self,*args):
        self.weekly = {args}
        print(self.weekly)

    def price(self,*args):
        self.cost = {args}
        for item in self.weekly:
            try:
                print(f"How much did you spend on {item}?")
                the_price = {item:self.cost}
                print(the_price)
            except ValueError:
                print("Enter Number not values!")

    def one_time_purchases(self,*args):
        self.random = {args}
        print(self.random)



spend = Spending()
spend.re_occurring("Data","Transport","Spotify","F")
spend.price(1500,800,2000,3500)
#Now we need a way to be able to map the prices to their corresponding expenditure ther than that it looks simple and i lke it.
#there isn't mcuh questions yet ill create a sperate python file that will run the code while this the engine will be in its own file
#initialy, I'd have gone for defining functions like must have and necssities then put them in  a recurring function but too ambiguous
spend.one_time_purchases(None)

"""else:
        print(f"All re_occurring expenses were made")
    while True:
        anything_else = input("Did yoy make any one time purchase?").lower()
        if anything_else == "yes":
            others = (input("What else?: "))
            for items in others:
                cost = input(f"How much is {items}?: ")
                one_time_purchases.append(others)
            print(one_time_purchases)
        elif anything_else != "yes":
            break"""
"""one time purchases could be more than one in number, so i created a while loop to ask repeatedly so far the user saids yes, 
bu i also need a ways to collect he cost and make it into a dictionary or something, wtf am i even building ??!"""

#the issue here is that the program can't check if you spelt yes or no wrongly, and theres no way to know if items were paired to
#prie and stuff, and why are we receiving input from the terminak i thought for a gui we pass in arguments in a block of code, this program
#has flaws i don't know what i'm doing anymore




spending = Spending("Forex","Fifa","Transport","Food","Data",answer="yes")
spending.response("yes")






#all that is left now is for the user program to be able to update the last_saved function,
# as it is it'll be using the current date of every day as the last saved.
# we want to be able to append that file or idk i think im right

"""budget = BudgetModel(10000,2000,5000,3000)
weeks_passed = WeeksPassed()
weeks_passed.time_since_last_update()
weeks_passed.store()"""
