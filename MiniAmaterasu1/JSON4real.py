import json

people_string = '''
{
    "people":[
        {
            "name": "Batman",
            "phone": "555",
            "emails": ["batmansofficialmail@gmail.com"],
            "has_licence": true (json true or false starts with small letter )
        },
        {
            "name": "obito",
            "phone": "10",
            "emails": ["obitohaskamuii@gmail.com"],
            "has_licence": false
        }
    ]
}
'''

data = json.loads(people_string)

print(data)