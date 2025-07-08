""""#sort() method = used with list
#sort() function = used with iterables
# sort() doesn't work with tuples
students = ["Batman","Kenpachi","Obito","Madara","Pain","Luffy","Zoro","Ichigo",]

#students.sort()
#students.sort(reverse=True)#this starts from the reversed alphabetical order

sorted_students = sorted(students)
for i in sorted_students:
    print(i)"""

"""students = [("Batman","A",35),
            ("kenpachi","C",1000),
            ("Obito","A",25),
            ("Goku","E",1000),
            ("Luffy","D",18)]

grade = lambda grades: grades[1]
students.sort(key=grade,reverse=True)

for i in students:
    print(i)"""

students = (("Batman","A",35),
            ("kenpachi","C",1000),
            ("Obito","A",25),
            ("Goku","E",1000),
            ("Luffy","D",18))

age = lambda your_age : your_age[2]
sorted_students = sorted(students,key=age)
for i in sorted_students:
    print(i)