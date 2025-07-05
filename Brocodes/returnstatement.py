#function that send python values/objects back to caller
# these objects/ values are known as return values

def multiply(num1,num2):
    results = num1 * num2
    return results

print(multiply(10,5))