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