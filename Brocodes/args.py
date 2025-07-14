# parameter that pack all arguments into a tuple
# useful for function that can accept a varying amount of arguments

#def add(*args ):
#    sum = 0
#    args = list(args)
#    args[0] = 50
#    for i in args:
#        sum += i
#    return  sum


#print(add(2,8,5,7,80))


class Spending:
    # I want to spend this night changing from accepting input to accepting arguments

    def re_occuring(self, *args):
        self.weekly = [*args]
        print(self.weekly)

    print(f"Did all these happen this week?")

    def yes_or_no(self, answer):
        self.answer = answer

    confirmed_expense = []
    one_time_purchases = []

    def confirm(self, response,price):
        self.response = response
        self.price = price
        if self.answer == "yes":
            for item in self.weekly:
                print(f"did you spend on {item} this week?")
                if self.response == "yes":
                    try:
                        print(f"How much did you spend on {item}?")
#since were passing keyword arguments, we don't need ambiguity like this, we could just put zero in anything in the budget that
#we didn't spend on for that week
                        confirmed_expense = {item, price}
                        return confirmed_expense
                    except ValueError:
                        print("Enter Number not values!")

        else:
            print(f"All re_occurring expenses were made")

spending = Spending()
spending.re_occuring("transport","data","spotify","fifa")
spending.yes_or_no("yes")
spending.confirm("yes")

