# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


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


def execute_javascript():
    browser = webdriver.Chrome()
    browser.get('https://www.zhihu.com/explore')
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    browser.execute_script('alert("To Bottom")')
    time.sleep(1)


def get_element_attribute():
    browser = webdriver.Chrome()
    browser.get('https://www.zhihu.com/explore')
    print(browser.page_source)  # 获取源码
    logo = browser.find_element_by_id('zh-top-link-logo')
    print(logo.get_attribute('class'))


def get_element_text():
    browser = webdriver.Chrome()
    browser.get('https://www.zhihu.com/explore')
    input_question = browser.find_element_by_class_name('zu-top-add-question')
    print(input_question.id)
    print(input_question.get_attribute('id'))
    print(input_question.location)
    print(input_question.tag_name)
    print(input_question.size)
    print(input_question.text)


def switch_to_frame():
    browser = webdriver.Chrome()
    url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    browser.get(url)
    browser.switch_to.frame('iframeResult')
    try:
        logo = browser.find_element_by_class_name('logo')
    except exceptions.NoSuchElementException:
        print("NO LOGO")
    browser.switch_to.parent_frame()
    logo = browser.find_element_by_class_name('logo')
    print(logo)
    print(logo.text)


def implicit_wait_to_find():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get('https://www.zhihu.com/explore')
    input = browser.find_element_by_class_name('zu-top-add-question')
    print(input)


def explicit_wait_to_find():
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    wait = WebDriverWait(browser, 10)
    try:
        inputt = wait.until(EC.presence_of_element_located((By.ID, 'qq')))
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
        print(inputt, button)
    except exceptions.TimeoutException as e:
        print("ERROR", e)


def forward_and_back():
    browser = webdriver.Chrome()
    browser.get('https://www.baidu.com')
    browser.get('https://www.taobao.com')
    browser.get('https://www.zhihu.com')
    time.sleep(1)
    browser.back()
    time.sleep(1)
    browser.forward()
    time.sleep(1)
    browser.close()


def use_cookies():
    browser = webdriver.Chrome()
    browser.get('https://www.zhihu.com/explore')
    print(browser.get_cookies())
    browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
    print(browser.get_cookies())
    browser.delete_all_cookies()
    print(browser.get_cookies())


def tabs_management():
    browser = webdriver.Chrome()
    browser.get('https://www.baidu.com')
    browser.execute_script('window.open()')
    print(browser.window_handles)
    browser.switch_to.window(browser.window_handles[1])
    browser.get('https://www.taobao.com')
    time.sleep(1)
    browser.switch_to.window(browser.window_handles[0])
    browser.get('https://www.jianshu.com')
    time.sleep(1)
    browser.close()


def get_traffic_data():
    browser = webdriver.Chrome()
    browser.get('http://www.nitrafficindex.com/')
    browser.switch_to.frame('mainIframe')
    time.sleep(3)
    # 获取道路实时交通指数点击框
    road_update_button = browser.find_element_by_css_selector('#div_traffic > div.tabs-header.tabs-header-noborder >'
                                                              ' div.tabs-wrap > ul > li:nth-child(3)')
    road_update_button.click()
    time.sleep(3)
    page_options = browser.find_element_by_css_selector('.pagination-page-list')
    s1 = Select(page_options)
    s1.select_by_visible_text('50')
    time.sleep(2)
    panel = browser.find_element_by_css_selector('#div_traffic > div.tabs-panels.tabs-panels-noborder > '
                                                 'div:nth-child(3)')
    road_panel = panel.find_element_by_css_selector('#road_tpi_data > div.panel.datagrid')
    road_body = road_panel.find_element_by_css_selector('div.datagrid-view > div.datagrid-view2 > div.datagrid-body > '
                                                        'table.datagrid-btable > tbody')
    for item in road_body.find_elements_by_css_selector('tr'):
        tds = item.find_elements_by_css_selector('td div')
        name = tds[0].text
        startname = tds[1].text
        endname = tds[2].text
        cindex = tds[3].text
        avgspeed = tds[4].text
        roadgrade = tds[5].text
        print(name, startname, endname, cindex, avgspeed, roadgrade)
    browser.quit()


if __name__ == '__main__':
    # search_from_driver()
    # visit_page()
    # node_interact()
    # action_chain()
    # execute_javascript()
    # get_element_attribute()
    # get_element_text()
    # switch_to_frame()
    # implicit_wait_to_find()
    # browser = webdriver.Chrome()
    # browser.get('http://www.nitrafficindex.com/')
    # browser.switch_to.frame('mainIframe')
    # print(browser.page_source)
    # explicit_wait_to_find()
    # forward_and_back()
    # use_cookies()
    # tabs_management()
    # brwser.quit()     # quit()退出后会删除文件，进程中不会出现webdriver
    get_traffic_data()
    # browser.close()
