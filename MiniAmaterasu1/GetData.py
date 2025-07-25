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
        data = response.json()

        with open("latest_dex.json", "w") as file:
            json.dump(data, file, indent=2)
        return data

    def orders(self):
        url = f"https://api.dexscreener.com/orders/v1/{self.chainId}/{self.tokenAddress}"
        response = requests.get(url)
        data =response.json()

        with open("orders.json", "w") as file:
            json.dump(data, file, indent=2)
        return data

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
        data = response.json()

        with open("pool.json", "w") as file:
            json.dump(data, file, indent=2)
        return data

    def run_all(self):
        self.get_tokens()
        self.orders()
        self.loading()
        self.evil_laugh()

api = Api("solana","2FduXi5zPSyxWpvcxBNsu9NcukhKmXaRpy4RLv5obonk")
api.run_all()
