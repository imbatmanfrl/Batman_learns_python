#from xml.etree.ElementTree import indent

import requests

import time

import json

latest_tokens = "https://api.dexscreener.com/token-profiles/latest/v1"

#get_pair_using_pair_address = "https://api.dexscreener.com/latest/dex/pairs/{chainId}/{pairId}"

pair = "https://api.dexscreener.com/latest/dex/search"

pool = "https://api.dexscreener.com/token-pairs/v1/{chainId}/{tokenAddress}"

class Api:
    def __init__(self,chainId,tokenAddress):
        self.chainId = chainId
        self.tokenAddress = tokenAddress

    def get_tokens(self):
        url = f"{latest_tokens}"
        response = requests.get(url)
        return response.json()

    def orders(self):
        url = f"https://api.dexscreener.com/orders/v1/{self.chainId}/{self.tokenAddress}"
        response = requests.get(url)
        return response.json()

    get = get_tokens()

    ordr =orders()

    with open("latest_dex.json", "w") as file:
        json.dump(get, file, indent=2)

    with open("orders.json", "w") as file:
        json.dump(ordr, file, indent=2)

    def loading(self):
        #    url = f"https://api.dexscreener.com/token-pairs/v1/{chainId}/{tokenAddress}"
        with open("latest_dex.json", "r") as file:
            self.data = json.load(file)

            for item in self.data:
                self.the_ID = item["chainId"]
                self.the_addy = item["tokenAddress"]
                print(self.the_ID, self.the_addy)

    def evil_laugh(self):
        url = f"https://api.dexscreener.com/token-pairs/v1/{self.the_ID}/{self.the_addy}"
        response = requests.get(url)
        return response.json()

    evil = evil_laugh()

    with open("pool.json", "w") as file:
        json.dump(evil, file, indent=2)


api = Api("solana","2FduXi5zPSyxWpvcxBNsu9NcukhKmXaRpy4RLv5obonk")
api.get_tokens()

#C:\Users\HP\PycharmProjects\BatmanLearnsPython\.venv\Scripts\python.exe C:\Users\HP\PycharmProjects\BatmanLearnsPython\MiniAmaterasu1\GetData.py
#Traceback (most recent call last):
#  File "C:\Users\HP\PycharmProjects\BatmanLearnsPython\MiniAmaterasu1\GetData.py", line 23, in <module>
#    class Api:
#  File "C:\Users\HP\PycharmProjects\BatmanLearnsPython\MiniAmaterasu1\GetData.py", line 35, in Api
#    ordr =orders()
#          ^^^^^^^^
#TypeError: Api.orders() missing 1 required positional argument: 'self'
