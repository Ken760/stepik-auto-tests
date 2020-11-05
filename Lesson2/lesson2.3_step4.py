import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    path = r'C:\Users\Ken\PycharmProjects\stepik-auto-tests\chromedriver.exe'
    browser = webdriver.Chrome(executable_path=path)
    browser.get('http://suninjuly.github.io/alert_accept.html')
    button_magic = browser.find_element(By.CLASS_NAME, 'btn-primary').click()
    alert = browser.switch_to.alert
    alert.accept()
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    browser.find_element_by_id('answer').send_keys(y)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(2)
    browser.quit()
