import json
import requests

class Track:
    def particular_asset(self, chainId, pairId):
        url = f"https://api.dexscreener.com/latest/dex/pairs/{chainId}/{pairId}"
        response = requests.get(url)
        data = response.json()
        print(data)

        with open("currentTokenomics.json", "w") as file:
            json.dump(data, file, indent=2)

    def tracking(self):
        tokenomics = []

        with open("currentTokenomics.json","r") as file:
            data = json.load(file)
            for pairs in data["pairs"]:
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

                tokenomics.append(info)
        with open ("Track_info.json","w") as file:
            json.dump(tokenomics,file,indent=2)


track = Track()
track.particular_asset("solana","E9bBxD7UnrPNdiN7VqaPmrQ1uhVHXHoQoiLQ1usdSccS")
track.tracking()
#tracker = Track("solana","ELQrbSfE9J2xPnxDGGfboGchw8QY7ua7NjsDtJYi4qt9")

