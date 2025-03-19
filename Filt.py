from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time


def wb_check_price(dr, kwargs, text):
    d_links = {
        "00": f"https://www.wildberries.ru/catalog/0/search.aspx?search={'%20'.join(text)}",
        "01": f"https://www.wildberries.ru/catalog/0/search.aspx?search={'%20'.join(text)}&fdlvr={kwargs['delivery']}",
        "10": f"https://www.wildberries.ru/catalog/0/search.aspx?search={'%20'.join(text)}&sort={kwargs['sort']}",
        "11": f"https://www.wildberries.ru/catalog/0/search.aspx?search={'%20'.join(text)}&sort={kwargs['sort']}&fdlvr={kwargs['delivery']}"
    }
    dr.get(d_links[f"{int(bool(kwargs['wb']['sort']))}{int(bool(kwargs['wb']['delivery']))}"])
    time.sleep(9)
    p_filter = dr.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div/div/div[3]/div[4]/div/button/div')
    p_filter.click()
    lw_p = dr.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div[1]/div/label/input')
    lw_pr = int(lw_p.get_attribute('value').replace(" ", ''))
    hg_p = dr.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div[2]/div/label/input')
    hg_r = int(hg_p.get_attribute('value').replace(" ", ''))
    low = max([lw_pr, int(kwargs['price_low'])])
    high = min([hg_r, int(kwargs['price_high'])])
    return [low, high]


def ya_check_price(dr, kwargs, text):
    d_links = {
        "00": f"https://market.yandex.ru/search?text={'%20'.join(text)}",
        "01": f"https://market.yandex.ru/search?text={'%20'.join(text)}&delivery-interval={kwargs['ya']['delivery']}",
        "10": f"https://market.yandex.ru/search?text={'%20'.join(text)}&how={kwargs['ya']['sort']}",
        "11": f"https://market.yandex.ru/search?text={'%20'.join(text)}&how={kwargs['ya']['sort']}&delivery-interval={kwargs['ya']['delivery']}"
    }
    dr.get(d_links[f"{int(bool(kwargs['ya']['sort']))}{int(bool(kwargs['ya']['delivery']))}"])
    time.sleep(5)
    lw_pr = 0
    hg_r = 0
    for i in range(1, 9):
        try:
            lw_pr = dr.find_element(By.XPATH, f'/html/body/div[1]/div/div[2]/div/div[1]/div[4]/div/aside/div[3]/div/div/div/div/div[{i}]/div/fieldset/div/div/div/div[1]/span/div/div/label')
            break
        except NoSuchElementException:
            continue
    for i in range(1, 9):
        try:
            hg_r = dr.find_element(By.XPATH, f'/html/body/div[1]/div/div[2]/div/div[1]/div[4]/div/aside/div[3]/div/div/div/div/div[{i}]/div/fieldset/div/div/div/div[2]/span/div/div/label')
            break
        except NoSuchElementException:
            continue

    low = max([int(lw_pr.text.replace(' ', '')), int(kwargs['price_low'])])
    high = min([int(hg_r.text.replace(' ', '')), int(kwargs['price_high'])])
    return [low, high]

