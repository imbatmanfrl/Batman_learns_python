"""A trade as an object,it will have attributes(what it has) and methods(what it can do)
question is what will be in the parent class and what would be in the abstract class or do I even need an abstract class

On second thought fuck it, i dont yet understand enough to create a huge program like that
 so instead let it work on fx trades only """
class Trade:#this will be a parent class as a trade could be stock, forex or crypto or even futures, they all have this feature

    def __init__(self):
        def fxasset():
            while True:
                traded_asset = input("What Asset Pair?: ").upper()
                if "USD" in traded_asset or "JPY" in traded_asset:
                    return traded_asset
                else:
                    print("Enter a valid pair")
        self.asset = fxasset()
# since I want my program to be able to validate input, I had to create a method before creating attribute which
 # i didn't even know was allowed impressive, it's much easier that the shit i had going on in my head
        # (----------------------------------------)
        def fxbias():
            while True:
                direction = input("LONG or SHORT?: ").upper()
                if "LONG" not in direction and "SHORT" not in direction:
                    print("Enter Long or Short")
                else:
                    return direction
        self.bias = fxbias()
        # (----------------------------------------)
        def fxaccount_balance():
            while True:
                try:
                    value = float(input("Account Balance?: "))
                    return value
                except ValueError:
                    print('Enter "1,2,3..." not "A,B,C..."')
        self.account_balance = fxaccount_balance()
        while True:
            try:
                lots = float(input("Lots?: "))
                entry_price = float(input("Entry Price?: "))
                exit_price = float(input("Exit Price?: "))
                break
            except ValueError:
                print("Enter Numbers not letters!")
        self.entry_price = entry_price
        self.exit_price = exit_price
        self.lots = lots
        # (----------------------------------------)
        def fxpips():
            if self.bias == "LONG":
                calc_pips = (self.exit_price - self.entry_price)
                return calc_pips
            elif self.bias == "SHORT":
                calc_pips = (self.entry_price - self.exit_price)
                return calc_pips
        self.pips = fxpips()

"""from abc import ABC, abstractmethod
class TradeCalcs:

    def pips(self):
        pass

    def pip_value(self):
        pass

    def asset_type(self):
        pass

    def profit(self):
        pass

    def percentage_gain(self):
        pass


class ForexTrades(Trade,TradeCalcs):
    pass"""


#trade = ForexTrades
"""while True:
#The try blocks should be inside the function
#Try blocks are not needed, use an if statement instead
        def pairf():
            while True:
                traded_asset = input("What Asset Pair?: ").upper()
                if "USD" in traded_asset or  "JPY" in traded_asset:
                    return traded_asset
                else:
                    print("Enter a valid pair")
        pair = pairf()
        # (----------------------------------------)
        def biasf():
            while True:
                direction = input("LONG or SHORT?: ").upper()
                if "LONG" not in direction and "SHORT" not in direction:
                    print("Enter Long or Short")
                else:
                    return direction
        bias = biasf()
        # (------------------------------------------)
        def account_balancef():
            while True:
                try:
                    value = float(input("Account Balance?: "))
                    return value
                except ValueError:
                    print('Enter "1,2,3..." not "A,B,C..."')
        account_balance = account_balancef()
        # (-------------------------------------------)
        while True:
            try:
                lots = float(input("Lots?: "))
                entry_price = float(input("Entry Price?: "))
                exit_Price = float(input("Exit Price?: "))
                break
            except ValueError:
                print("Enter Numbers not letters!")
        # (--------------------------------------------)
        def pipsf():
            if bias == "LONG":
                calc_pips = (exit_Price - entry_price)
                return calc_pips
            elif bias == "SHORT":
                calc_pips = (entry_price - exit_Price)
                return calc_pips
        pips = pipsf()
        # (--------------------------------------------)
        def pip_valuef():
            value_or_pip = lots * 10
            return value_or_pip
        pip_value = pip_valuef()
        # (--------------------------------------------)
        def asset_typef():
            if "USD" in pair:
                asset_value = pips * 10000
                return asset_value
            elif "JPY" in pair:
                asset_value = pips * 100
                return asset_value
        asset_type = asset_typef()
        # (--------------------------------------------)
        def profitf():
            your_prof = asset_type * pip_value
            return your_prof
        profit = profitf()
        # (--------------------------------------------)
        def percentage_gainf():
            gain = (profit / account_balance) * 100
            return gain
        percentage_gain = percentage_gainf()
        # (--------------------------------------------)
        def output():
            trade_details = (" The Pair you traded is: " + pair + " and you entered a " + bias + " position")

            trade_execution = (" Lots Traded: " + str(round(lots, 2)) + "\n Entry Price: " +
                               str(round(entry_price, 2)) +
                               "\n Exit Price: " + str(round(exit_Price, 2)))

            trade_outcome = (" Pips Traded: " + str(round(pips, 2)) + " pips"
                             "\n Profit made: $" + str(round(profit, 2)) +
                             "\n Percentage gain: " + str(round(percentage_gain, 2))+"%")
            print(trade_details)
            print(trade_execution)
            print(trade_outcome)
        # (-----------------------------------------------------------------------------------------------)
        output()
        again = input("Do you want to continue?").lower()
        if again == "no":
            break"""

# blueprint
#while True:  👈🏾 The main gate. Start here.
#    1. Ask for input (call functions)
#    2. Do the calculations
#    3. Show the results
#    4. Ask: “Do you want to continue?”
#    5. If user says “no” → break

#I ust found out that everytime I call a function within another function it will always ask for input, functions are maily just
#used to print functions multiple times without repeating too much lines of code
#what i should do id store the return value of the function inside another variable
#our code has been written with separate functions performing different task as in modular programming
#now we just need a body of code that would actually carry out this whole code
#while statement should come before the declaring functions so the program can ask for new inputs
#"I learnt alot tonight, It's important to practice what you learn and gather data yourself,
# i wish i'm able to gather this much data and info in forex too"






