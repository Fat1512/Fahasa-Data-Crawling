from unicodedata import category

import requests
import json

from numpy.ma.core import empty

from app.product_detail import get_product_detail
import pandas as pd

#Get all the categories
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

#Fetch data
prefix_url = 'https://www.fahasa.com/fahasa_catalog/product/loadCatalog'
response = requests.get(prefix_url, params=params, headers=headers).json()

#Fetch categories
categories = response['children_categories']
df_category = pd.DataFrame(categories)
df_category.to_csv('vietnamese_categories.csv', index=False)

# for category in categories:
for i in range(6, 7):
    category = categories[i]
    params['category_id'] = category['id']
    category_info_response = requests.get(prefix_url, params=params, headers=headers).json()

    product_list = category_info_response['product_list']
    df_category_product = pd.DataFrame(product_list)
    df_category_product.to_csv("data/category_id_{category_id}.csv".format(category_id=category['id']), index=False)
    empty = []

    for product in product_list:
        empty.append(get_product_detail(url = product['product_url'], category_id = category['id'], product_id=product['product_id']))
    with open("data/product/{category_id}.json".format(category_id=category['id']), "w") as f:
        json.dump(empty, f, ensure_ascii=False, indent=4)
        f.close()


# f = open("categories.json", "w", encoding="utf-8")
# json.dump(categories, f, ensure_ascii=False, indent=4)
# f.close()
