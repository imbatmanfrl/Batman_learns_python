#A dictionary is a changeable, unordered collection of unique key value pairs
#Uses hashing with allows us to access a value quickly

capitals = {"USA":"Washington DC",
            "India":"New Dehli",
            "China":"Beijing",
            "Russia":"Moscow"}

capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Wall Street"})

#print(capitals["Russia"])
#print(capitals.get("Nigeria"))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

#for x in capitals:
#    print(capitals)
#    break

for x,y in capitals.items():
    print(x,y)