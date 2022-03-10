import requests
import json


key = {"api_key": "93663a29-1493-4313-8dab-1c3551f2ff23"}
keys = "93663a29-1493-4313-8dab-1c3551f2ff23"
headers = { "secret_key": "mEUH33CJWq9h6RP1a0gEOpUDZ2pAT5LQFJORJhw1hwKaH9GjbrtJsDTKnjCQLxQ8",
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
