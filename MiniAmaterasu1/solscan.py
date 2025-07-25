import requests

import json


scanning = "https://pro-api.solscan.io/v2.0/token/latest?page=1&page_size=10"
headers = {
    "accept": "application/json",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjcmVhdGVkQXQiOjE3NTM0MDIxMzcxNzQsImVtYWlsIjoiYmF0bWFuc29mZmljaWFsbWFpbEBnbWFpbC5jb20iLCJhY3Rpb24iOiJ0b2tlbi1hcGkiLCJhcGlWZXJzaW9uIjoidjIiLCJpYXQiOjE3NTM0MDIxMzd9.5AHXCUgFtvDMEYQUoUV7i90Up5V01NKJMOPjAtd93Sw"
}

def solscan():
    url = f"{scanning}"
    response = requests.get(url,headers=headers)
    return response.json()

sol = solscan()

with open("solscan.json", "w") as f:
    json.dump(sol, f, indent=2)
