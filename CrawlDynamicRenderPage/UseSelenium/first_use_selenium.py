# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def search_from_driver():
    browser = webdriver.Chrome()
    try:
        browser.get('https://www.baidu.com')
        iinput = browser.find_element_by_id('kw')
        iinput.send_keys('Python')
        iinput.send_keys(Keys.ENTER)
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
        print(browser.current_url)
        print(browser.get_cookies())
        print(browser.page_source)
    finally:
        browser.close()


def visit_page():
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    input_first = browser.find_element_by_id('q')
    input_second = browser.find_element_by_name('q')
    input_third = browser.find_element_by_css_selector('#q')
    input_forth = browser.find_element_by_xpath('//*[@id="q"]')
    input_fifth = browser.find_element_by_class_name('search-combobox-input')
    input_sixth = browser.find_element_by_tag_name('input')
    input_seventh = browser.find_element(By.ID, 'q')
    print(input_first)
    print(input_second)
    print(input_third)
    print(input_forth)
    print(input_fifth)
    print(input_sixth)
    print(input_seventh)
    lis = browser.find_elements_by_css_selector('.service-bd li')
    print(lis)
    # print(browser.page_source)
    browser.close()


def node_interact():
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    input_text = browser.find_element_by_id('q')
    input_text.send_keys('iPhone')
    time.sleep(1)
    input_text.clear()
    input_text.send_keys('iPad')
    # button = browser.find_element_by_class_name('btn-search')
    # button.click()
    input_text.send_keys(Keys.ENTER)


def action_chain():
    browser = webdriver.Chrome()
    url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    browser.get(url)
    browser.switch_to.frame('iframeResult')
    source = browser.find_element_by_css_selector('#draggable')
    target = browser.find_element_by_css_selector('#droppable')
    actions = ActionChains(browser)
    actions.drag_and_drop(source, target)
    actions.perform()
    time.sleep(2)


if __name__ == '__main__':
    # search_from_driver()
    # visit_page()
    # node_interact()
    action_chain()
