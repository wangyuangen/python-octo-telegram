# -*- coding: utf-8 -*-
from selenium import webdriver

def setUp():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('http://www.baidu.com')
    driver.find_element_by_link_text("登录").click()

if __name__ == '__main__':
    setUp()