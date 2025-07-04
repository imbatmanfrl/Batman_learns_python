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
            break

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





