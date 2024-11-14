import json
import numpy as np
from selenium import webdriver
from time import sleep
import random
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
import pandas as pd

def get_product_detail(url, category_id, product_id):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('{url}?fhs_campaign=CATEGORY'.format(url=url))

    detail_information = {}

    #Get images
    try:
        images = driver.find_elements(By.CSS_SELECTOR, ".lightgallery .include-in-gallery")
        image_hrefs = [image.get_attribute("href") for image in images]
        detail_information['images'] = image_hrefs
    except Exception:
        print("Cannot click")

    #Get description
    try:
        more = driver.find_element(By.CSS_SELECTOR, ".fhs_btn_new_default.mobile_link")
        sleep(2)
        more.click()
    except Exception:
        print("Cannot click")

    try:
        description = driver.find_element(By.CSS_SELECTOR, "#product_tabs_description_contents").text
        detail_information['description'] = description
    except Exception:
        print("Cannot find description")

    #Get detail information
    additional_datas = driver.find_elements(By.CSS_SELECTOR, ".data-table.table-additional tbody tr")

    i = 0
    for additional_data in additional_datas:
        key = additional_data.find_element(By.CSS_SELECTOR, ".table-label").text
        value = additional_data.find_element(By.CSS_SELECTOR, ".data_{index}".format(index=i)).text
        detail_information[key] = value
        i = i + 1

    detail_information['product_id'] = product_id
    detail_information['category_id'] = category_id
    return detail_information
    # with open("data/product/{category_id}_{product_id}.json".format(product_id=product_id, category_id=category_id), "w") as f:
    #     json.dump(detail_information, f, ensure_ascii=False, indent=4)
    #     f.close()


















