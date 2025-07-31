import json

from datetime import datetime,timedelta
#from GetData import Api

class Filter:
    with open("pair_info.json","r")as file:
        data = json.load(file)

        for item in data:
            timestamp_ms = item.get("created_at")  # Replace with your actual timestamp
            timestamp_sec = timestamp_ms / 1000
            pair_time = datetime.fromtimestamp(timestamp_sec)
            now = datetime.now()
            if now - pair_time <= timedelta(hours=4):
                print("This pair is less than 3 hours")


#        age = data.get("created_at")
#        liquidity = data.get["liquidity"]["usd"]
#        market_cap = data.get("market_cap")
#        chain_Id = data.get("chainId")


