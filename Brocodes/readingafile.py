#try:
#    with open("text") as file:
#        print(file.read())
#except FileNotFoundError:
#    print("File was not found")

text = ("I can't hide it anymore\n saving Gotham aint easy shit \n but imma keep doing it regardless")

with open("test.txt","w") as file:
    file.write(text)