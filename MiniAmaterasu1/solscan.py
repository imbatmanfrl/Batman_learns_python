import requests

import json


scanning = "https://pro-api.solscan.io/v2.0/token/latest?page=1&page_size=10"

def solscan():
    url = f"{scanning}"
    response = requests.get(url)
    return response

sol = solscan()

with open ("solscan.json","w")as f:
    json.dump(sol,f,indent=2)

"""C:\Users\HP\PycharmProjects\BatmanLearnsPython\.venv\Scripts\python.exe C:\Users\HP\PycharmProjects\BatmanLearnsPython\MiniAmaterasu1\solscan.py 
Traceback (most recent call last):
  File "C:\Users\HP\PycharmProjects\BatmanLearnsPython\MiniAmaterasu1\solscan.py", line 16, in <module>
    json.dump(sol,f,indent=2)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python312\Lib\json\__init__.py", line 179, in dump
    for chunk in iterable:
  File "C:\Users\HP\AppData\Local\Programs\Python\Python312\Lib\json\encoder.py", line 439, in _iterencode
    o = _default(o)
        ^^^^^^^^^^^
  File "C:\Users\HP\AppData\Local\Programs\Python\Python312\Lib\json\encoder.py", line 180, in default
    raise TypeError(f'Object of type {o.__class__.__name__} '
TypeError: Object of type Response is not JSON serializable"""