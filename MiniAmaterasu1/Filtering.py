import json

from GetData import Api

class Filter:
    with open("pool.json","r")as file:
        date = json.load(file)