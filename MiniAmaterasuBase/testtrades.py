from MiniAmaterasuBase.percentagegain import Trade

while True:
    trade = Trade()
    trade.output()

    again =input("Do you want to Continue?: ").lower()
    if again == "no":
        break