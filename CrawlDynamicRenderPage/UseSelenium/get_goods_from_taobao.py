# -*- coding: utf-8 -*-
import json
from time import sleep
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from urllib.parse import quote

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
KEYWORD = 'iPad'


def index_page(page):
    """
    抓取索引页
    :param page: 页码
    :return:
    """
    print('正在爬取第', page, '页')
    try:
        url = "https://s.taobao.com/search?q=" + quote(KEYWORD)
        browser.get(url)
        sleep(1)
        if page > 1:
            input_page = wait.until(EC.presence_of_element_located((
                By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
            submit = wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
            input_page.clear()
            input_page.send_keys(page)
            submit.click()
            sleep(2)
        # 判断页面是否加载完毕
        wait.until(EC.text_to_be_present_in_element((
            By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, 'div.m-itemlist div.items div.item')))
        # 获取商品信息
        products = get_products()
        for item in products:
            write_to_file(item)
    except TimeoutException:
        index_page(page)
    except BaseException as e:
        print("ERROR", e.args)


def get_products():
    """
    提取商品信息
    :return: 商品信息迭代器
    """
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image_url': item.find('.pic .img').attr('data-src'),
            'link': item.find('.pic .pic-link').attr('href'),
            'price': item.find('.price').text(),
            'deal': item.find('.ctx-box .row-1.g-clearfix .deal-cnt').text(),
            'title': item.find('.ctx-box > .row-2.title').text(),
            'shop': item.find('.ctx-box > .row-3.g-clearfix > .shop').text(),
            'locate': item.find('.ctx-box > .row-3.g-clearfix > .location').text()
        }
        print(product)
        yield product


def write_to_file(product):
    with open(KEYWORD + '_goods_result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(product, ensure_ascii=False) + "\n")


def main():
    """
    遍历每一页
    :return:
    """
    for i in range(1, 101):
        index_page(i)
        print("已完成：{:.2%}".format(i / 100))
        sleep(1)
    sleep(2)
    browser.quit()
    pass


if __name__ == '__main__':
    main()
