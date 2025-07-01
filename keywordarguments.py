#preceeded by an identifier when we pass a function to them
# the order of argument doesn't matter, unlike positional arguments
# python knows the name of the argument that our function receives

def hello(first, middle , last):
    print("Hello " + first +middle+last)

hello(middle="The",last=" Batman",first=" 🦇")
