from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from WbFilt import check_price

import requests
import time


def wb_pars(text, kwargs):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    serv = Service("G:/Drivers/chromedriver-131/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=serv, options=chrome_options)
    prices = check_price(driver, kwargs, text)
    driver.get(f"https://www.wildberries.ru/catalog/0/search.aspx?search={text.replace(' ', '%20')}&sort={kwargs['sort']}&priceU={kwargs['price_low']}00%3B{kwargs['price_high']}00&&fdlvr={kwargs['delivery']}")


def wb_parsx(text, kwargs):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    serv = Service("G:/Drivers/chromedriver-131/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=serv, options=chrome_options)
    prices = check_price(driver, kwargs, text)
    driver.get(f"https://www.wildberries.ru/catalog/0/search.aspx?search={text.replace(' ', '%20')}&sort={kwargs['sort']}&priceU={kwargs['price_low']}00%3B{kwargs['price_high']}00&&fdlvr={kwargs['delivery']}")
    time.sleep(2)
    card_img1 = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/div[2]/div/div/div[4]/div[1]/div[1]/div/article[1]/div/div[1]/div[2]/img[1]')
    img1_src = card_img1.get_attribute("src")
    card_img2 = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/div[2]/div/div/div[4]/div[1]/div[1]/div/article[2]/div/div[1]/div[2]/img[1]')
    img2_src = card_img2.get_attribute("src")
    img1 = requests.get(img1_src)
    img2 = requests.get(img2_src)
    for i in [img1, img2]:
        with open(f"photo/image{[img1, img2].index(i)}.webp", "wb") as f:
            f.write(i.content)

wb_parsx("Футболка", {'sort': 'rate', 'price_low': 1000, 'price_high': 3000, 'delivery': 72})

