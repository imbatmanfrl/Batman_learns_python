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

        with open("latest_dex.json", "r") as file:
            self.data = json.load(file)
            self.pairs = []

            for item in self.data:
                chainId = item.get("chainId")
                tokenAdress = item.get("tokenAddress")

                if chainId and tokenAdress:
                    self.pairs.append((chainId,tokenAdress))
                    print(self.pairs)

    def evil_laugh(self):

        all_data = []
        for chainId, tokenAddress in self.pairs:
            url = f"https://api.dexscreener.com/token-pairs/v1/{chainId}/{tokenAddress}"
            response = requests.get(url)
            data = response.json()
            all_data.append(data)

        with open("pool.json", "w") as file:
            json.dump(all_data, file, indent=2)
            for item in all_data:
                return item

    def pair_name(self):
        pair_info = []
        with open("pool.json", "r") as file:
            data = json.load(file)

            for pairs in data:
                name = pairs["baseToken"],["name"]
                symbol = pairs["baseToken"],["symbol"]
                market_cap = pairs["baseToken"],["fdv"]
                price = pairs["baseToken"],["price"]

#                self.name = f"Pair name: {pairs["baseToken"]["name"]}"
#                self.symbol = f"Pair symbol: {pairs["baseToken"]["symbol"]}"
#                self.mc = f"Pair MarketCap: ${pairs["fdv"]}"
#                #self.liquidity = f"Pair liquidity: {pairs["liquidity"]["usd"]}"
#                self.price = f"Pair Current Price: ${pairs["priceUsd"]}"

                data =name,symbol,market_cap,price
                pair_info.append(data)
        with open("pair_info.json","w") as file:
            json.dump(pair_info,file,indent=2)

    def run_all(self):
        self.get_tokens()
        self.orders()
        self.loading()
        self.evil_laugh()
        self.pair_name()


api = Api("solana","2FduXi5zPSyxWpvcxBNsu9NcukhKmXaRpy4RLv5obonk")
api.run_all()
