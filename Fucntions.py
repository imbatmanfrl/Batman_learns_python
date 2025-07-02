# A block of code executed only when it is called

#def Batman(first_name,last_name):
#    print("🦇" +first_name+ last_name )
#    print("I'm going to save you")

#my_name = "Awwal"
#Batman(my_name)
#Batman("awwal",21)

#Batman("The ","Batman")

def Batman():
    first_name = input("Your First Name?: ")
    last_name = input("Your Last Name?:")
    full_name = first_name + last_name
    return full_name
#    return ("Your name is:" + first_name + last_name)
#    return first_name and last_name

print(Batman())