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
            for item in data:
                return item

    def pair_name(self):
        with open("pool.json", "r") as file:
            data = json.load(file)
            for pairs in data:
                self.name = f"Pair name: {pairs["baseToken"]["name"]}"
                self.symbol = f"Pair symbol: {pairs["baseToken"]["symbol"]}"
                self.mc = f"Pair MarketCap: ${pairs["fdv"]}"
                #self.liquidity = f"Pair liquidity: {pairs["liquidity"]["usd"]}"
                self.price = f"Pair Current Price: ${pairs["priceUsd"]}"

                data = self.name,self.symbol,self.mc,self.price
        with open("pair_info.json","w") as file:
            json.dump(data,file,indent=2)

    def run_all(self):
        self.get_tokens()
        self.orders()
        self.loading()
        self.evil_laugh()
        self.pair_name()


api = Api("solana","2FduXi5zPSyxWpvcxBNsu9NcukhKmXaRpy4RLv5obonk")
api.run_all()

#problem im having now is that pool.json isn't getting the tokenomics of all the pairs in latest_dex.json
#and if that happens, pair.info will onnly generate the info on one crypto token
#I need it to be able to do it for all the pairs in latest_dex.json
#and also sometimes in pool.json, it'll pull the token's liquidity, sometimes it wont
#and i'm also not able to get pair age, just 24hr volume,
# like alot of these pairs might be real old already and i've missed out on early buys
#I can't also tell who's the dev yet but im thinking we can use the twitter api to see that,
# also one of these API can check if a token has been bought by CTO but im guessing it can only do it for one pair as well