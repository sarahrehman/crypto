import os
import json
import csv
import requests
from prettytable import PrettyTable
from colorama import Fore, Back, Style
import os

coinmarket_api_key = os.environ['coinmarket_api_key']
coinmarket_secret_key = os.environ['coinmarket_secret_key']

key = {"api_key": coinmarket_api_key }
headers = { "secret_key": coinmarket_secret_key,
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