#applies a function to each item in an iterable (list, tuple, e.t.c)

#map(function,iterable)

store = [("Shirt",20.00),
         ("Pants",25.00),
         ("Jacket",50.00),
         ("Socks",10.00)]

to_euros = lambda euros: (euros[0],euros[1]*0.82)
to_dollars = lambda euros: (euros[0],euros[1]/0.82)

store_dollars = list(map(to_dollars,store))
store_euros = list(map(to_euros,store))

for i in store_euros:
    print(i)

for i in store_dollars:
    print(i)
