bias = input("LONG or SHORT?: ").upper()
account_balance = input ("Account Balance?: ")
lots = input("Lots?: ")
profit = ""
entry_price = input("Entry Price?: ")
exit_Price = input("Exit Price?: ")
earned_pips = ""
percentage_gain = ""

if bias == "LONG":
    earned_pips = exit_Price - entry_price
    profit = lots * earned_pips
    percentage_gain = (profit/account_balance)*100
    print(earned_pips)
    print("Your profit is: "+profit)
    print("You earned: "+ percentage_gain)

elif bias == "SHORT":
    earned_pips = entry_price - entry_price
    profit = lots * earned_pips
    percentage_gain = (profit / account_balance) * 100
    print(earned_pips)
    print("Your profit is: " + profit)
    print("You earned: " + percentage_gain)


