import json
import numpy as np
from selenium import webdriver
from time import sleep
import random
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
import pandas as pd


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.fahasa.com/truong-ca-achilles.html?fhs_campaign=CATEGORY')

detail_information = {}

#Get images
images = driver.find_elements(By.CSS_SELECTOR, ".lightgallery .include-in-gallery")
image_hrefs = [image.get_attribute("href") for image in images]

#Get description
more = driver.find_element(By.CSS_SELECTOR, ".fhs_btn_new_default.mobile_link")
sleep(2)
more.click()

description = driver.find_element(By.CSS_SELECTOR, "#product_tabs_description_contents").text

#Get detail information
additional_datas = driver.find_elements(By.CSS_SELECTOR, ".data-table.table-additional tbody tr")

i = 0
for additional_data in additional_datas:
    key = additional_data.find_element(By.CSS_SELECTOR, ".table-label").text
    value = additional_data.find_element(By.CSS_SELECTOR, ".data_{index}".format(index=i)).text
    detail_information[key] = value
    i = i + 1

detail_information['images'] = image_hrefs
detail_information['description'] = description
with open("data/js.json", "w") as f:
    json.dump(detail_information, f, ensure_ascii=False, indent=4)
    f.close()


















