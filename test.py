import os
import json
import datetime

from binance import Client

api_key = os.environ.get("binance_api")
api_secret = os.environ.get("binance_secret")

client_2 = Client(api_key, api_secret)
client_2.api_url = 'https://testnet.binance.vision/api'

account_data = client_2.get_account()

print(account_data)
#print(json.dumps(account_data, indent=4))

# print(account_data)
# print(account_data.dtype)