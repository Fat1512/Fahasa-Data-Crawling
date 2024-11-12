import requests
import json
import pandas as pd
#Get category based on category_id
params = {
    'category_id': 4,
    'currentPage': 1,
    'limit': 24,
    'order': 'num_orders',
    'series_type': 0
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cookie': 'frontend=7f33e2db865d465d82fd1b2f46ba5c51; frontend_cid=53bSalvZ3G3c0MJX; external_no_cache=1',
    'Connection': 'keep-alive'
}

prefix_url = 'https://www.fahasa.com/fahasa_catalog/product/loadCatalog'

product_list = []
category_id = 20
params['category_id'] = category_id

for i in range(11):
    params['currentPage'] = i + 1
    response = requests.get(prefix_url, params=params, headers=headers).json()['product_list']
    product_list += response

df_product = pd.DataFrame(product_list)
df_product.to_csv('data/product_category_{category_id}.csv'.format(category_id=category_id), index=False)






















