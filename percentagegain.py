bias = input("LONG or SHORT?: ").upper()
# I want to modify the program in a way where it asks for what pair, and based on what pair for usd it will mulitply pips by 10,000
#and if it were a jpy pair it would multiply by 100 I just need where ill store pair, maybe inside a 2D list

fav_pairs = ["GBPUSD","EURUSD","GBPJPY","ES"]
pair = input("What pair?: ").upper()
account_balance = float (input ("Account Balance?: "))
lots = float (input("Lots?: "))
profit = ""
entry_price = float(input("Entry Price?: "))
exit_Price = float(input("Exit Price?: "))
pips = ""
percentage_gain = ""

if bias == "LONG":
    pips = exit_Price - entry_price
    if pair == "GBPJPY" in fav_pairs:
        pips = pips*100
        print("Total pips: " + str(round (pips,2)))#this will round pps up to 2 decimal places
    elif pair == "GBPUSD" in fav_pairs:
        pips = pips * 10000
        print("Total pips: " + str(round (pips,2)))
    elif pair == "EURUSD" in fav_pairs:
        pips = pips * 10000
        print("Total pips: " + str(round (pips,2)))
    profit = lots * pips * 10
    percentage_gain = (profit / account_balance) * 100
    print("Your profit is: " + str(round(profit, 2)))
    print("You earned: " + str(round(percentage_gain, 2)) + "%")

elif bias == "SHORT":
    pips = entry_price - exit_Price
    if pair == "GBPJPY" in fav_pairs:
        pips = pips * 100
        print("Total pips: " + str(round (pips,2)))
    elif pair == "GBPUSD" in fav_pairs:
        pips = pips * 10000
        print("Total pips: " + str(round (pips,2)))
    elif pair == "EURUSD" in fav_pairs:
        pips = pips * 10000
        print("Total pips: " + str(round(pips, 2)))
    profit = lots * pips * 10
    percentage_gain = (profit / account_balance) * 100
    print("Your profit is: " + str(round(profit,2)))
    print("You earned: "+ str (round(percentage_gain,2))+"%")

