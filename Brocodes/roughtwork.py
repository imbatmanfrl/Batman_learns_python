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

while True:
    try:
        lots = float(input("Lots?: "))
        continue
    except ValueError:
        print("Enter Numbers not letters!")
    try:
        entry_price = float(input("Entry Price?: "))
        break
    except ValueError:
        print("Enter Numbers not letters!")
    try:
        exit_Price = float(input("Exit Price?: "))
        break
    except ValueError:
        print("Enter Numbers not letters!")
