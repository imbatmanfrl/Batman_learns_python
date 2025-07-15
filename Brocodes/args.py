# parameter that pack all arguments into a tuple
# useful for function that can accept a varying amount of arguments


def add(*args ):
    sum = 0
    args = list(args)
    args[0] = 50
    for i in args:
        sum += i
    return  sum


print(add(2,8,5,7,80))
