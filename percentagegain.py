
def pair():
    traded_asset = input("What Asset Pair?: ").upper()
    return traded_asset
#(----------------------------------------)
def bias():
    direction = input("LONG or SHORT?: ").upper()
    return direction
#(------------------------------------------)
def account_balance():
    value = float (input ("Account Balance?: "))
    return value
#(-------------------------------------------)
lots = float (input("Lots?: "))
entry_price = float(input("Entry Price?: "))
exit_Price = float(input("Exit Price?: "))
#(--------------------------------------------)
def pips():
    if bias() == "LONG":
        calc_pips = (exit_Price - entry_price)
        return calc_pips
    elif bias() == "SHORT":
        calc_pips = (entry_price - exit_Price)
        return calc_pips
#(--------------------------------------------)
def pip_value():
    value_or_pip = lots * 10
    return value_or_pip
# (--------------------------------------------)
def asset_type():
    if "USD" in pair():
        asset_value = pips() * 10000
        return asset_value
    elif "JPY" in pair():
        asset_value = pips() * 100
        return asset_value
# (--------------------------------------------)
def profit():
    your_prof = pips() * pip_value()
    return your_prof
# (--------------------------------------------)
def percentage_gain():
    gain = (profit()/account_balance()) * 100
    return gain
# (--------------------------------------------)
def output():
    trade_details = ("The Pair you traded is: "+pair()+" and you entered a "+bias()+" position")

    trade_execution = ("Lots Traded: "+ str(round(lots,2))+" Entry Price: "+
                       str(round(entry_price,2))+
                       " Exit Price: "+str(round(exit_Price,2)))

    trade_outcome = ("Pips Traded: "+ str(round(pips(),2))+
                     "\n Profit made: "+ str(round(profit(),2))+
                     "\n Percentage gain: "+str(round(percentage_gain(),2)) )
    return trade_details and trade_execution and trade_outcome
#(-----------------------------------------------------------------------------------------------)
#our code has been written with separate functions performing different task as in modular programming
#now we just need a body of code that would actually carry out this whole code

#currently having trouble with the while loop but im going to try and shorten the code by breaking some parts into functions!
#while True:
#    if bias == "LONG":
#        pips = exit_Price - entry_price
#        if pair == "GBPJPY" in fav_pairs:
#            pips = pips * 100
#            pip_value = lots * 10  # 0.01 lots = 0.1 lots on jpy pairs
#            profit = pips * pip_value
#            percentage_gain = (profit / account_balance) * 100
#            print("Your profit is: " + str(round(profit, 2)))
#            print("You earned: " + str(round(percentage_gain, 2)) + "%")
#            print("Total pips: " + str(round(pips, 2)))  # this will round pps up to 2 decimal places
#        elif pair == "GBPUSD" or "EURUSD" in fav_pairs:
#            pips = pips * 10000
#            pip_value = lots * 10  # 0.01 lots = 0.01 lots on usd pairs
#            profit = pips * pip_value
#            percentage_gain = (profit / account_balance) * 100
#            print("Your profit is: " + str(round(profit, 2)))
#            print("You earned: " + str(round(percentage_gain, 2)) + "%")
#            print("Total pips: " + str(round(pips, 2)))





