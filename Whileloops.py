#While loops execute a block of code so far the condition remains true

name = ""

while (len(name))==0:
    name = input("Your name?: ")
    if (len(name))==0:
        print("Enter your name you Dipshit")
print("Your name is "+ name)