while True:
    try:
        lots = float(input("Lots?: "))
        entry_price = float(input("Entry Price?: "))
        exit_Price = float(input("Exit Price?: "))
        break
    except ValueError:
        print("Enter Numbers not letters!")