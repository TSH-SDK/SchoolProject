from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from Filt import wb_check_price

import time


def wb_pars(text, kwargs):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    items = {}

    d_links = {
        "00": f"https://www.wildberries.ru/catalog/0/search.aspx?search={'%20'.join(text)}",
        "01": f"https://www.wildberries.ru/catalog/0/search.aspx?search={'%20'.join(text)}&fdlvr={kwargs['wb']['delivery']}",
        "10": f"https://www.wildberries.ru/catalog/0/search.aspx?search={'%20'.join(text)}&sort={kwargs['wb']['sort']}",
        "11": f"https://www.wildberries.ru/catalog/0/search.aspx?search={'%20'.join(text)}&sort={kwargs['wb']['sort']}&fdlvr={kwargs['wb']['delivery']}"
    }
    serv = Service("G:/Drivers/chromedriver-134/chromedriver-win64/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=serv, options=chrome_options)
    if kwargs['price_low']:
        prices = wb_check_price(driver,kwargs, text)
        driver.get(d_links[f"{int(bool(kwargs['wb']['sort']))}{int(bool(kwargs['wb']['delivery']))}"]+f"&priceU={prices[0]}00%3B{prices[1]}00")
    else:
        driver.get(
            d_links[f"{int(bool(kwargs['wb']['sort']))}{int(bool(kwargs['wb']['delivery']))}"])
    time.sleep(10)
    for i in range(1, 4):
        d_price = driver.find_element(By.XPATH,
                                      f'/html/body/div[1]/main/div[2]/div[2]/div[2]/div/div/div[4]/div[1]/div[1]/div/article[{i*2}]/div/div[3]/div/span/ins')
        r_price = driver.find_element(By.XPATH,
                                      f'/html/body/div[1]/main/div[2]/div[2]/div[2]/div/div/div[4]/div[1]/div[1]/div/article[{i*2}]/div/div[3]/div/span/del')
        name_tag = driver.find_element(By.XPATH,
                                       f'/html/body/div[1]/main/div[2]/div[2]/div[2]/div/div/div[4]/div[1]/div[1]/div/article[{i*2}]/div/a')
        name = name_tag.get_attribute('aria-label')
        rate = driver.find_element(By.XPATH,
                                   f'/html/body/div[1]/main/div[2]/div[2]/div[2]/div/div/div[4]/div[1]/div[1]/div/article[{i*2}]/div/div[4]/p[1]/span[1]')
        link_tag = driver.find_element(By.XPATH,
                                       f'/html/body/div[1]/main/div[2]/div[2]/div[2]/div/div/div[4]/div[1]/div[1]/div/article[{i*2}]/div/a')
        link = link_tag.get_attribute('href')
        photo_tag = driver.find_element(By.XPATH,
                                        f'/html/body/div[1]/main/div[2]/div[2]/div[2]/div/div/div[4]/div[1]/div[1]/div/article[{i*2}]/div/a')
        photo = photo_tag.get_attribute('href')

        deliver_time = driver.find_element(By.XPATH, f"/html/body/div[1]/main/div[2]/div[2]/div[2]/div/div/div[4]/div[1]/div[1]/div/article[{i*2}]/div/div[4]/p[2]/a/span[2]")

        items[i] = {"name": name,
                    "r_price": r_price.text,
                    "d_price": d_price.text,
                    "rate": rate.text,
                    "link": link,
                    "photo": photo,
                    "delivery_time": deliver_time.text
                    }
    return items

