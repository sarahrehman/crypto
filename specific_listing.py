import requests
import json
import pprint

key = {"api_key": "93663a29-1493-4313-8dab-1c3551f2ff23"}
keys = "93663a29-1493-4313-8dab-1c3551f2ff23"
headers = { "secret_key": "mEUH33CJWq9h6RP1a0gEOpUDZ2pAT5LQFJORJhw1hwKaH9GjbrtJsDTKnjCQLxQ8",
  "api_key": key['api_key']}

base_url = 'https://pro-api.coinmarketcap.com'

local_currency = 'GBP'
local_symbol = '£'
symbol = input("1 Enter the symbol of the cryptocurrency for inspection: ").upper()
#symbol_2 = input("1 Enter the symbol of the cryptocurrency for inspection:")
listings_url = base_url + '/v1/cryptocurrency/quotes/latest?convert=' + local_currency + '&symbol=' + symbol #+ ',' + symbol_2

headers = { 
    'Accepts': 'application/json',
    "X-CMC_PRO_API_KEY": key['api_key'] }

results = requests.get(url=listings_url, headers=headers)
data = results.json()
#print(json.dumps(data, sort_keys=True, indent=4))

data = data['data']
currency = data[symbol]
#for currency in data:
name = currency['name']
print('name: ' + name)
    # symbol = currency['symbol']

    # price = currency['quote'][local_currency]['price']
    # percent_change_1h = currency['quote'][local_currency]['percent_change_24h']
    # percent_change_1h = str(round(percent_change_1h, 2)) + '%'
    # price = local_symbol +  '{:,}'.format(price)