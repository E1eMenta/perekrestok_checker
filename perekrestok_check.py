import time

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def check() -> bool:
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(
        "https://www.perekrestok.ru/catalog/zamorojennye-produkty/ovoschi-i-smesi/mark-perekr-kapusta-bryussel-bzam-400g--309768")

    try:
        skipButtonXPath = '//*[@id="dy-10466948"]/div[3]/button'
        skip_button = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, skipButtonXPath)))
        skip_button.click()
    except selenium.common.exceptions.TimeoutException:
        print("No skip button")

    time.sleep(5)

    check_xpath = '/html/body/div[2]/header/div[2]/div[4]/div'
    check_element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, check_xpath)))
    check_element.click()
    time.sleep(5)

    try:
        available_xpath = '/html/body/div[4]/span'
        available_element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, available_xpath)))
    except selenium.common.exceptions.TimeoutException:
        return True

    result = not ('на данный момент нет доступных дат' in available_element.text)

    driver.close()

    return result
