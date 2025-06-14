import requests
import sys

res = requests.get(url = f"https://10.10.244.203/api")
print(res)
