#tuple is an ordered and unchangeable collection

nigga = ("Batman", 21, " Male")

print(nigga.index("Batman")) #index show the position of "batman" in our program
print(nigga.count(21))# count shows how many times 21 appeared in our tuple

for x in nigga:
    print(x, end="")

if "Batman" in nigga:
    print("It's the Batman!!")