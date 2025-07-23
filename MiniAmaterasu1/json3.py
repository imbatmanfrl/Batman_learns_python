import json

import requests

dex_url = "https://api.dexscreener.com/token-profiles/latest/v1"

def get_profile():
    url = f"{dex_url}"
    response = requests.get(url)
    return response

get_prof = get_profile()

data = json.loads(str(get_prof))

#with open ("Asset_on_dex","w") as file:
#    json.dumps(data,file,indent=2)

print(json.dumps(data,indent=2))