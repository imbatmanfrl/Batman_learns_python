#from xml.etree.ElementTree import indent

import requests

import time

import json

latest_tokens = "https://api.dexscreener.com/token-profiles/latest/v1"

#check_orders = "https://api.dexscreener.com/orders/v1/{chainId}/{tokenAddress}"

#get_pair_using_pair_address = "https://api.dexscreener.com/latest/dex/pairs/{chainId}/{pairId}"

#search_for_specific_pairs = "https://api.dexscreener.com/latest/dex/search"

def get_tokens():
    url = f"{latest_tokens}"
    response = requests.get(url)
    return response.json()

def orders(chainId,tokenAddress):
    url = f"https://api.dexscreener.com/orders/v1/{chainId}/{tokenAddress}"
    response = requests.get(url)
    return response.json()

get = get_tokens()
ord = orders("solana","A55XjvzRU4KtR3Lrys8PpLZQvPojPqvnv5bJVHMYy3Jv")

with open ("latest_dex.json","w") as file:
    json.dump(get,file,indent=2)

with open ("orders.json","w")as file:
    json.dump(ord,file,indent=2)

#for item in get:
#    print(get)