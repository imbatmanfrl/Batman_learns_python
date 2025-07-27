import json
import requests


from GetData import Api

class Track(Api):

    def particular_pair(self):

        chainId = input(f"Enter the chainId: ")
        tokenAddress = input(f"Enter the tokenAddress: ")
        url = f"https://api.dexscreener.com/token-pairs/v1/{chainId}/{tokenAddress}"
        response = requests.get(url)
        data = response.json()

        with open("currentTokenomics.json", "w") as file:
            json.dump(data, file, indent=2)
            for item in data:
                print(item)

    def tracker(self):
        pair_info = []
        with open("currentTokenomics.json", "r") as file:
            data = json.load(file)

            if isinstance(data,dict) and "pair" in data:
                for item in data:
                    pairs = item.get("pair")
                    if not pairs:
                        continue
                    tokenomics = {
                        "name": pairs["baseToken"]["name"],
                        "symbol": pairs["baseToken"]["symbol"],
                        "chainId": pairs.get("chainId"),
                        "address": pairs.get("pairAddress"),
                        "price": pairs.get("priceUsd"),
                        "market_cap": pairs.get("fdv"),
                        "liquidity": pairs.get("liquidity"),
                        "volume": pairs.get("volume")
                    }

                    pair_info.append(tokenomics)
        with open("pair_info.json", "w") as file:
            json.dump(pair_info, file, indent=2)

    def start_tracking(self):
        self.particular_pair()
        self.tracker()


tracker = Track("solana","ELQrbSfE9J2xPnxDGGfboGchw8QY7ua7NjsDtJYi4qt9")
#tracker = Track("solana","ELQrbSfE9J2xPnxDGGfboGchw8QY7ua7NjsDtJYi4qt9")
tracker.start_tracking()
