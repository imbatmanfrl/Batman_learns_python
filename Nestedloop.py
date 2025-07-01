#Nested loop is a loop within another loop
#Inner loop finishes before the outer loop

rows = int(input("How many rows?:"))
columns = int(input("How many columns?: "))
symbol = input("enter a symbol to use:")

#outer for loop incharge of rows,inner for loop incharge of columns
for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
#not adding end="" to the program will print the symbols on a new line not on the same line
    print()



