from operator import index
import requests
import json
import os

coinmarket_api_key = os.environ['coinmarket_api_key']
coinmarket_secret_key = os.environ['coinmarket_secret_key']

key = {"api_key": coinmarket_api_key }
headers = { "secret_key": coinmarket_secret_key,
  "api_key": key['api_key']}

base_url = 'https://pro-api.coinmarketcap.com'

local_currency = 'GBP'
local_symbol = '£'

symbols = ["BTC","ETH","ADA","SOL","DOT","ALGO","LINK"]
x = 0
for i in range(0,4):
    x += 1
    symbols[x]
    print(symbols[x])
    
listings_url_1 = base_url + '/v1/cryptocurrency/quotes/latest?convert=' + local_currency + '&symbol='
listings_url = listings_url_1 + symbols[x]
headers = { 
    'Accepts': 'application/json',
    "X-CMC_PRO_API_KEY": key['api_key'] }

results = requests.get(url=listings_url, headers=headers)
data = results.json()
print(json.dumps(data, sort_keys=True, indent=4))





currency = data["data"][symbols[x]]

#Parameters
crypto_0 = {"Name": str(currency["slug"].capitalize()),
              "Symbol": currency["symbol"]}
#               "Price": local_symbol + '{:,}'.format(data["data"][symbols[0]]['quote'][local_currency]['price']),
#               "1H Change": str(data["data"][symbols[0]]['quote'][local_currency]['percent_change_1h']),
#               "24H Change": str(data["data"][symbols[0]]['quote'][local_currency]['percent_change_24h'])
#             }

# crypto_1 = {"Name": str(currency["slug"].capitalize()),
#               "Symbol": currency["symbol"],
#               "Price": local_symbol + '{:,}'.format(data["data"][symbols[1]]['quote'][local_currency]['price']),
#               "1H Change": str(data["data"][symbols[1]]['quote'][local_currency]['percent_change_1h']),
#               "24H Change": str(data["data"][symbols[1]]['quote'][local_currency]['percent_change_24h'])
#             }

# crypto_2 = {"Name": str(data["data"][symbols[2]]["slug"].capitalize()),
#               "Symbol": data["data"][symbols[2]]["symbol"],
#               "Price": local_symbol + '{:,}'.format(data["data"][symbols[2]]['quote'][local_currency]['price']),
#               "1H Change": str(data["data"][symbols[2]]['quote'][local_currency]['percent_change_1h']),
#               "24H Change": str(data["data"][symbols[2]]['quote'][local_currency]['percent_change_24h'])
#             }

# crypto_3 = {"Name": str(data["data"][symbols[3]]["slug"].capitalize()),
#               "Symbol": data["data"][symbols[3]]["symbol"],
#               "Price": local_symbol + '{:,}'.format(data["data"][symbols[3]]['quote'][local_currency]['price']),
#               "1H Change": str(data["data"][symbols[3]]['quote'][local_currency]['percent_change_1h']),
#               "24H Change": str(data["data"][symbols[3]]['quote'][local_currency]['percent_change_24h'])
#             }


# price0 = data["data"][symbols[0]]['quote'][local_currency]['price']

# price1 = data["data"][symbols[1]]['quote'][local_currency]['price']

# # print(
# #     "Name: " + data["data"][symbols[0]]["slug"] + 
    
# #     "\nPrice: " + local_symbol + str(data["data"][symbols[0]]['quote'][local_currency]['price']))
# # print("Price: " + local_symbol + str(price1))
#     # percent_change_1h = currency['quote'][local_currency]['percent_change_24h']
#     # percent_change_1h = str(round(percent_change_1h, 2)) + '%'
#     # price = local_symbol +  '{:,}'.format(price)


# print("Name: " + crypto_0["Name"] 
#     + "\nSymbol: " + crypto_0["Symbol"] 
#     + "\nPrice: " + crypto_0["Price"] 
#     + "\n24H Change: " + crypto_0["24H Change"] + '%'
#     + "\n1H Change: " + crypto_0["1H Change"] + '%'
#     '\n'
#     + "\nName: " + crypto_1["Name"] 
#     + "\nSymbol: " + crypto_1["Symbol"] 
#     + "\nPrice: " + crypto_1["Price"] 
#     + "\n24H Change: " + crypto_1["24H Change"] + '%'
#     + "\n1H Change: " + crypto_1["1H Change"] + '%'
#     '\n'
#     + "\nName: " + crypto_2["Name"] 
#     + "\nSymbol: " + crypto_2["Symbol"] 
#     + "\nPrice: " + crypto_2["Price"] 
#     + "\n24H Change: " + crypto_2["24H Change"] + '%'
#     + "\n1H Change: " + crypto_2["1H Change"] + '%'
#         '\n'
#     + "\nName: " + crypto_3["Name"] 
#     + "\nSymbol: " + crypto_3["Symbol"] 
#     + "\nPrice: " + crypto_3["Price"] 
#     + "\n24H Change: " + crypto_3["24H Change"] + '%'
#     + "\n1H Change: " + crypto_3["1H Change"] + '%')


# Bitcoin BTC £444
# Ethereum ETH 48
# Solana SOL
# ChainLink LINK
# Polkadot DOT
# Cardano ADA
# VetChain VET
# Synthetic Network Token
# Algorand ALGO
# Stellar Lumens


    