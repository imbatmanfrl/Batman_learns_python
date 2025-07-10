from MiniAmaterasuBase.MA0_5 import Trade

while True:
    trade = Trade()
    trade.output()

    again =input("Do you want to Continue?: ").lower()
    if again == "no":
        break