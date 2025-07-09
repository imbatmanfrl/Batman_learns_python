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

"""class Trade:
# Attributes
    def __init__(self):
        def fxasset():
            while True:
                traded_asset = input("What Asset Pair?: ").upper()
                if "USD" in traded_asset or "JPY" in traded_asset:
                    return traded_asset
                else:
                    print("Enter a valid pair")
        self.asset = fxasset()

# (----------------------------------------------------------------)
        def fxbias():
            while True:
                direction = input("LONG or SHORT?: ").upper()
                if "LONG" not in direction and "SHORT" not in direction:
                    print("Enter Long or Short")
                else:
                    return direction
        self.bias = fxbias()
# (-------------------------------------------------------)
        def fxaccount_balance():
            while True:
                try:
                    value = float(input("Account Balance?: "))
                    return value
                except ValueError:
                    print('Enter "1,2,3..." not "A,B,C..."')
        self.account_balance = fxaccount_balance()
# (-----------------------------------------------------)
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
# (------------------------------------------------------)
        def fxpips():
            if self.bias == "LONG":
                calc_pips = (self.exit_price - self.entry_price)
                return calc_pips
            elif self.bias == "SHORT":
                calc_pips = (self.entry_price - self.exit_price)
                return calc_pips
        self.pips = fxpips()

trade = Trade()
print(trade.pips)
"""

while True:
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

        print(pips)
        again =input("Do you want to Continue?: ").lower()
        if again == "no":
            break