import json
#json boolean uses lowercase true/false
#load method loads a file while load(s) loads a string
people_string = '''
{
    "people":[
        {
            "name": "Batman",
            "phone": "555",
            "emails": ["batmansofficialmail@gmail.com"],
            "has_licence": true 
        },
        {
            "name": "obito",
            "phone": "10",
            "emails": null,
            "has_licence": false
        }
    ]
}
'''

data = json.loads(people_string)

print(type(data['people']))
print(f"{data}")

for person in data['people']:
    del person['phone']

new_string = json.dumps(data, indent=2, sort_keys=True)

print(new_string)