import csv
import json

data = []

with open('data/vietnamese_categories.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['id'])