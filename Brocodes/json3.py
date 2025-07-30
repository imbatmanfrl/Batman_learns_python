import json
from textwrap import indent

import requests

dex_url = "https://api.dexscreener.com/token-profiles/latest/v1"

def get_profile():
    url = f"{dex_url}"
    response = requests.get(url)
    return response.json()

get_prof = get_profile()

with open ("Asset_on_dex.json", "w") as file:
    json.dump(get_prof,file,indent=2)

for item in get_prof:
    print(item)

#print(len(get_prof))