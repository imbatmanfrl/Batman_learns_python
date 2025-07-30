import json
import requests

#a1cd384b910a4640b5d562d60b9f9d53
class Track:
    def start(self):
        url = f"https://public-api.birdeye.so/defi/v2/tokens/new_listing"

        headers = {
            "X-API-KEY": "a1cd384b910a4640b5d562d60b9f9d53"
        }

        response = requests.get(url, headers=headers)
        data = response.json()
        print(data)

        with open ("more_tokens.json","w") as file:
            json.dump(data,file,indent=2)

track = Track()
track.start()


"""def orders(self):
    url = f"https://api.dexscreener.com/orders/v1/{self.chainId}/{self.tokenAddress}"
    response = requests.get(url)
    data = response.json()

    with open("orders.json", "w") as file:
        json.dump(data, file, indent=2)
    return data"""