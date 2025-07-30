#from xml.etree.ElementTree import indent
from itertools import count

import requests

import time

import json

latest_tokens = "https://api.dexscreener.com/token-profiles/latest/v1"

#get_pair_using_pair_address = "https://api.dexscreener.com/latest/dex/pairs/{chainId}/{pairId}"

pair = "https://api.dexscreener.com/latest/dex/search"

pool = "https://api.dexscreener.com/token-pairs/v1/{chainId}/{tokenAddress}"

class Api:
    def __init__(self,chainId,tokenAddress,pairId=None):
        self.chainId = chainId
        self.tokenAddress = tokenAddress
        self.pairId = pairId

    def get_tokens(self):
        url = f"{latest_tokens}"
        response = requests.get(url)
        data = response.json()

        with open("latest_dex.json", "w") as file:
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

    def ids(self):

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

            for group in data:
                for pairs in group:
                    info = {
                        "name": pairs["baseToken"]["name"],
                        "symbol": pairs["baseToken"]["symbol"],
                        "chainId": pairs.get("chainId"),
                        "address": pairs.get("pairAddress"),
                        "price": pairs.get("priceUsd"),
                        "market_cap": pairs.get("fdv"),
                        "liquidity": pairs.get("liquidity"),
                        "volume": pairs.get("volume")
                    }


                pair_info.append(info)
        with open("pair_info.json","w") as file:
            json.dump(pair_info,file,indent=2)

    def run_all(self):
        self.get_tokens()
        self.loading()
        self.ids()
        self.pair_name()


api = Api("solana","2FduXi5zPSyxWpvcxBNsu9NcukhKmXaRpy4RLv5obonk")
api.run_all()
