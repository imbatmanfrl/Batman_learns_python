#from xml.etree.ElementTree import indent

import requests

import time

import json

latest_tokens = "https://api.dexscreener.com/token-profiles/latest/v1"

#get_pair_using_pair_address = "https://api.dexscreener.com/latest/dex/pairs/{chainId}/{pairId}"

pair = "https://api.dexscreener.com/latest/dex/search"

pool = "https://api.dexscreener.com/token-pairs/v1/{chainId}/{tokenAddress}"

def get_tokens():
    url = f"{latest_tokens}"
    response = requests.get(url)
    return response.json()

def orders(chainId,tokenAddress):
    url = f"https://api.dexscreener.com/orders/v1/{chainId}/{tokenAddress}"
    response = requests.get(url)
    return response.json()

def loading():
#    url = f"https://api.dexscreener.com/token-pairs/v1/{chainId}/{tokenAddress}"
    with open("latest_dex.json","r") as file:
        json.load(file)


get = get_tokens()
ord = orders("solana","A55XjvzRU4KtR3Lrys8PpLZQvPojPqvnv5bJVHMYy3Jv")


with open ("latest_dex.json","w") as file:
    json.dump(get,file,indent=2)

with open ("orders.json","w")as file:
    json.dump(ord,file,indent=2)


#for item in get:
#    print(get)