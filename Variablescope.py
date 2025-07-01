#The region that the variable is recognised
# Only available from inside the region it was created

name = "THE" #Golbal scope (available inside and outside a function)

def display_name():
    name = "Batman"   #local scope(only available inside this function)
    print(name)

print(name)
display_name()