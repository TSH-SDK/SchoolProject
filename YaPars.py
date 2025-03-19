from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from Filt import ya_check_price

import re
import time


def ya_pars(text, kwargs):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    items = {}
    d_links = {
        "00": f"https://market.yandex.ru/search?text={'%20'.join(text)}",
        "01": f"https://market.yandex.ru/search?text={'%20'.join(text)}&delivery-interval={kwargs['ya']['delivery']}",
        "10": f"https://market.yandex.ru/search?text={'%20'.join(text)}&how={kwargs['ya']['sort']}",
        "11": f"https://market.yandex.ru/search?text={'%20'.join(text)}&how={kwargs['ya']['sort']}&delivery-interval={kwargs['ya']['delivery']}"
    }
    serv = Service("G:/Drivers/chromedriver-134/chromedriver-win64/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=serv, options=chrome_options)
    if kwargs['price_low']:
        prices = ya_check_price(driver, kwargs, text)
        driver.get(d_links[
                       f"{int(bool(kwargs['ya']['sort']))}{int(bool(kwargs['ya']['delivery']))}"] + f"&pricefrom={prices[0]}&priceto={prices[1]}")
    else:
        driver.get(
            d_links[f"{int(bool(kwargs['ya']['sort']))}{int(bool(kwargs['ya']['delivery']))}"])
    time.sleep(3)
    info = driver.find_elements(By.CLASS_NAME, '_2rw4E')

    items = {}

    for i, j in enumerate(info[11:14]):
        photo = re.split('img class="w7Bf7"|srcset', j.get_attribute("outerHTML"))[1][6:-2]
        links = re.split('<a href="|target="', j.get_attribute("outerHTML"))
        true_link = "https://market.yandex.ru"
        print(photo)
        for k in set(links):
            if k[0] == "/":
                true_link += k
                print(true_link)
        items[i] = {"name": '',
                    "link": true_link,
                    "photo": photo
                    }
    return items