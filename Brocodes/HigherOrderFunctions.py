"""They either accept a function as an argument or they return a function (In python, functions can also be treated as objects)

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud)"""

def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide = divisor(2)
print(divide(10))

