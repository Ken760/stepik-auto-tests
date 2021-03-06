import os
from selenium import webdriver

path = r'C:\Users\Ken\PycharmProjects\stepik-auto-tests\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path)
browser.get('http://suninjuly.github.io/file_input.html')

file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.txt')

if not os.path.exists(file_path):
    with open(file_path, 'w') as f:
        pass

inputs = ['test', 'test', 'test@gmail.com', file_path]

for element, value in zip(browser.find_elements_by_tag_name('input'), inputs):
    element.send_keys(value)

browser.find_element_by_css_selector('button.btn').click()

