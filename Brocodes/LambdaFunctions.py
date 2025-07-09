"""A function is written in one line using the lambda keyword
accepts any number of arguments, but on;y has one expression (It's more like a shortcut, useful if needed for a short period of time, Throwaway

 Lambda parameters:expression

def double(x):
    return x * 2

print(double(5))

useful if you need to use a function only once and throw it away"""

double = lambda x:x*2
multiply = lambda x,y: x * y
print(multiply(2,28))
full_name = lambda first_name,last_name: f"{first_name} {last_name}"
age = lambda your_age : True if your_age >= 18 else False
print(age(24))
print(double(5))
print(full_name("TheBatmam","🦇"))

