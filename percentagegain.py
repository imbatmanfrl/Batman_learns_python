def bias():
    direction = input("LONG or SHORT?: ").upper()
    return direction
#(----------------------------------------)
def pair():
    traded_asset = input("What Asset Pair?: ").upper()
    return traded_asset
#(------------------------------------------)
def account_balance():
    value = float (input ("Account Balance?: "))
    return value
#(-------------------------------------------)
lots = float (input("Lots?: "))
entry_price = float(input("Entry Price?: "))
exit_Price = float(input("Exit Price?: "))
#(--------------------------------------------)
def output():
#    pip_value
    profit =
    pips
    percentage_gain




#if "usd" in pair
# I want to modify the program in a way where it asks for what pair, and based on what pair for usd it will mulitply pips by 10,000
#and if it were a jpy pair it would multiply by 100 I just need where ill store pair, maybe inside a 2D list

fav_pairs = ["GBPUSD","EURUSD","GBPJPY","ES"]


#currently having trouble with the while loop but im going to try and shorten the code by breaking some parts into functions!
while True:
    if bias == "LONG":
        pips = exit_Price - entry_price
        if pair == "GBPJPY" in fav_pairs:
            pips = pips * 100
            pip_value = lots * 10  # 0.01 lots = 0.1 lots on jpy pairs
            profit = pips * pip_value
            percentage_gain = (profit / account_balance) * 100
            print("Your profit is: " + str(round(profit, 2)))
            print("You earned: " + str(round(percentage_gain, 2)) + "%")
            print("Total pips: " + str(round(pips, 2)))  # this will round pps up to 2 decimal places
        elif pair == "GBPUSD" or "EURUSD" in fav_pairs:
            pips = pips * 10000
            pip_value = lots * 10  # 0.01 lots = 0.01 lots on usd pairs
            profit = pips * pip_value
            percentage_gain = (profit / account_balance) * 100
            print("Your profit is: " + str(round(profit, 2)))
            print("You earned: " + str(round(percentage_gain, 2)) + "%")
            print("Total pips: " + str(round(pips, 2)))


    elif bias == "SHORT":
        pips = entry_price - exit_Price
        if pair == "GBPJPY" in fav_pairs:
            pips = pips * 100
            pip_value = lots * 10  # 0.01 lots = 0.1 lots on jpy pairs
            profit = pips * pip_value
            percentage_gain = (profit / account_balance) * 100
            print("Your profit is: " + str(round(profit, 2)))
            print("You earned: " + str(round(percentage_gain, 2)) + "%")
            print("Total pips: " + str(round(pips, 2)))  # this will round pps up to 2 decimal places
        elif pair == "GBPUSD" or "EURUSD" in fav_pairs:
            pips = pips * 10000
            pip_value = lots * 10  # 0.01 lots = 0.01 lots on usd pairs
            profit = pips * pip_value
            percentage_gain = (profit / account_balance) * 100
            print("Your profit is: " + str(round(profit, 2)))
            print("You earned: " + str(round(percentage_gain, 2)) + "%")
            print("Total pips: " + str(round(pips, 2)))

    elif bias == "Stop":
        print("End of session")


