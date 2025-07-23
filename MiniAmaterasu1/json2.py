import json

with open("people.json","r") as file:
    data = json.load(file)

for item in data:
    del item["isEmployed"]

with open("new_states.json","w") as file:
    json.dump(data, file,indent=2)  


#    print(item["name"],item["age"])