from selenium.webdriver.common.by import By
import time


def check_price(dr, kwargs, text):
    dr.get(f"https://www.wildberries.ru/catalog/0/search.aspx?search={text.replace(' ', '%20')}&sort={kwargs['sort']}&fdlvr={kwargs['delivery']}")
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
