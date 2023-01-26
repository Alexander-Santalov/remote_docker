import time

from selenium import webdriver
from selenium.webdriver.common.by import By


link = "https://ya.ru"

capabilities = {"browserName": 'chrome', "browserVersion": "109.0", "platformName": "Linux"}

wd = webdriver.Remote(command_executor=f"http://95.163.236.225:4444/wd/hub", desired_capabilities=capabilities)

def test_ya():
    wd.get(link)
    wd.find_element(By.CSS_SELECTOR, "input.search3__input").send_keys("Проверка докера")
    time.sleep(10)
