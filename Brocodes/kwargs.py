# parameter that will pack all arguments into a dictionary
# useful so a function can accept varying amount f keyword arguments

def hello(**kwargs):
    #print("Hello"+" "+kwargs["first"]+" "+kwargs["last"]+" "+kwargs["symbol"])
    print("Hello ",end="")
    for key,value in kwargs.items():
        print(value,end="")


hello(last="Batman",first="THE",symbol="🦇" )