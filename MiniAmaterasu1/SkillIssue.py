import json
import requests

class Track:
    def particular_asset(self,chainId,tokenAddress,pairedwith):
        url = f"https://api.dexscreener.com/token-pairs/v1/{chainId}/{tokenAddress}"
        response = requests.get(url)
        data = response.json()
        print(data)

        with open("currentTokenomics.json","w") as file:
            json.dump(data,file,indent=2)

track = Track()
track.particular_asset("solana","6AJcP7wuLwmRYLBNbi825wgguaPsWzPBEHcHndpRpump")