import csv
import json

data = []

# with open('data/vietnamese_categories.csv') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row['id'])

import requests
import json
import pandas as pd
#Get category based on category_id

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cookie': 'frontend=7f33e2db865d465d82fd1b2f46ba5c51; frontend_cid=53bSalvZ3G3c0MJX; external_no_cache=1',
    'Connection': 'keep-alive'
}

prefix_url = 'https://www.fahasa.com/node_api/flashsale/product'

response = requests.get(prefix_url, headers=headers).json()
print(response)





















