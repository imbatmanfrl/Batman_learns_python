import requests

"""base_url = "https://api.dexscreener.com/token-profiles/latest/v1"

def get_token_profiles():
    url = f"{base_url}"
    response = requests.get(url)

    if response.status_code == 200:
        asset_profile = response.json()
        for item in asset_profile:
            print(item)
    else:
        print(f"Failed to retrieve data {response.status_code}")

get_token_profiles()
"""

def get_latest_dexs(chainId,pairId):
    url = f"https://api.dexscreener.com/latest/dex/pairs/{chainId}/{pairId}"
    response= requests.get(url)

    if response.status_code == 200:
        asset_data = response.json()
        return asset_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

asset_chainId = "solana"
asset_pairId = "JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"
asset_info = get_latest_dexs(asset_chainId,asset_pairId)

if asset_info:
    print(f"{asset_info}")

#{'schemaVersion': '1.0.0', 'pairs': None, 'pair': None}