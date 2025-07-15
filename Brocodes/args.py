# parameter that pack all arguments into a tuple
# useful for function that can accept a varying amount of arguments
#from MiniAmaterasuBase.roughtwork import spending


#def add(*args ):
#    sum = 0
#    args = list(args)
#    args[0] = 50
#    for i in args:
#        sum += i
#    return  sum


#print(add(2,8,5,7,80))


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
        self.random = list[cost]
        self.cost = list[cost]
        full_list = dict(zip(self.random,self.cost))
        print(f"Your one time purchases are {full_list}")



spend = Spending()
spend.re_occurring("Data","Transport","Spotify","F")
spend.price(1500,800,2000,3500)
spend.expenses()
spend.one_time_purchases(random="FIFA, Workbook, Bread",cost="500, 4250, 500")
#Now we need a way to be able to map the prices to their corresponding expenditure ther than that it looks simple and i lke it.
#there isn't mcuh questions yet ill create a sperate python file that will run the code while this the engine will be in its own file
#initialy, I'd have gone for defining functions like must have and necssities then put them in  a recurring function but too ambiguous