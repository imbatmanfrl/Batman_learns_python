import json

from datetime import datetime,timedelta
#from GetData import Api

class Filter:
        def okay(self):
            with open("pair_info.json", "r") as file:
                data = json.load(file)

                for item in data:
                    timestamp_ms = item.get("created_at")
                    pair_time = datetime.strptime(timestamp_ms, "%Y-%m-%d %H:%M:%S")
                    now = datetime.now()
                    check_age = now - pair_time <= timedelta(hours=4)

                    liquidity_data = item.get("liquidity")

                    if isinstance(liquidity_data, dict):
                        usd_liquidity = liquidity_data.get("usd", 0)
                    else:
                        usd_liquidity = 0
                    liquidity = 1000 <= usd_liquidity <= 25000
                    volume_data = item.get("volume")
                    h24_volume = volume_data.get("h24",0)
                    volume = 10000 <= h24_volume <= 50000
                    market_cap_data = item.get("market_cap")
                    market_cap = 10000 <= market_cap_data <= 50000
                    price_data = item.get("priceChange")
                    if isinstance(price_data,dict):
                        h1_price = price_data.get("h1",0)
                    else:
                        h1_price = 0
                    price_change = h1_price > 10
                    chain_Id = item.get("chainId")
                    if chain_Id == "solana":
                        sol_meme = chain_Id

                    if liquidity and volume and market_cap and price_change and sol_meme and check_age:
                        filtered_info = [item]
                        print(filtered_info)

                        print(
                            f"check_age: {check_age}, liquidity: {liquidity}, volume: {volume}, market_cap: {market_cap}, price_change: {price_change}, solana: {sol_meme}")

                        with open ("filtered_pairs.json","w") as file:
                            json.dump(filtered_info,file,indent=2)

filters = Filter()
filters.okay()


#                    print(check_age,usd_liquidity,h24_volume)


#                with open ("testing.json","w")as file:
#                    json.dump(liquidity,file,indent=2)
#                    """liquidity = 1000 <= item.get("liquidity" or {}).get("usd", 0) <= 25000
#                    volume = 10000 <= item.get("volume",{}).get("h24",0) <= 50000
#                    market_cap = 10000 <= item.get("market_cap") <= 50000
#                    price_change = item.get("priceChange",{}).get("h1",0) > 10
#                    chain_Id = item.get("chainId") == "solana"
#                    """

#                    if liquidity and volume and market_cap and price_change and chain_Id and check_age:
#                        filtered_info = [item]
#                        print(filtered_info)
#                    else:
#                        print("Not working properly")
#                        new_info = {
#                            "name": item.get("name"),
#                            "symbol": item.get["baseToken"]["symbol"],
#                            "chainId": item.get("chainId"),
#                            "address": item.get("pairAddress"),
#                            "price": item.get("priceUsd"),
#                            "market_cap": item.get("fdv"),
#                            "liquidity": item.get("liquidity"),
#                            "volume": item.get("volume"),
#                            "created_at": readable_time
#                        }





#        age = data.get("created_at")
#        liquidity = data.get["liquidity"]["usd"]
#


