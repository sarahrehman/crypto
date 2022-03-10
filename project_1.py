import os
import json
import csv
import requests
from prettytable import PrettyTable
from colorama import Fore, Back, Style


key = {"api_key": "93663a29-1493-4313-8dab-1c3551f2ff23"}
keys = "93663a29-1493-4313-8dab-1c3551f2ff23"
headers = { "secret_key": "mEUH33CJWq9h6RP1a0gEOpUDZ2pAT5LQFJORJhw1hwKaH9GjbrtJsDTKnjCQLxQ8",
  "api_key": key['api_key']}

base_url = 'https://pro-api.coinmarketcap.com'

local_currency = 'GBP'

headers = { 
    'Accepts': 'application/json',
    "X-CMC_PRO_API_KEY": key['api_key'] }


print('\nMY PORTFOLIO\n')

portfolio_value = 0.00

table = PrettyTable(['Asset', 'Amount Owned', 'Value', 'Price', '1h', '24', '7d', '90d'])

#Open CSV with portfolio numbers
with open('my_portfolio.csv', "r") as csv_file:
    csv_reader = csv.reader(csv_file) #csv_reader object to loop through csv file to pull data from file
    for line in csv_reader:
        if '\ufeff' in line[0]:
            line[0] = line[0][1:].upper()
        else:
            line[0] = line[0].upper()

        symbol = line[0]
        amount = line[1]

        quote_url = base_url + '/v1/cryptocurrency/quotes/latest?convert=' + local_currency + '&symbol=' + symbol

        request = requests(url=quote_url, headers=headers)
        results = json.loads(request.text)