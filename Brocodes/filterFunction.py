#crreates a complexion of elements from an iterable for which a function retuens true

#filter(function, iterable)

friends=[("Awwal",21),
         ("Batman",35),
         ("Obito",28),
         ("Tony Soprano",50),
         ("Kenpachi Zaraki",1000),
         ("Micheal Corleone",50)]

age = lambda our_age: our_age[1]>=18

we_are_awesome=list(filter(age,friends))

for i in we_are_awesome:
    print(i)
    print("WE ARE FUCKING AWESOME!")
