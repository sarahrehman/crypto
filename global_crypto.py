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
global_url = base_url + '/v1/global-metrics/quotes/latest?convert=' + local_currency

headers = { 
    'Accepts': 'application/json',
    "X-CMC_PRO_API_KEY": key['api_key'] }

response = requests.get(url=global_url, headers=headers)
data = json.loads(response.text)
print(json.dumps(data, sort_keys=True, indent=4))
