# -*- coding: utf-8 -*-
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

KEYWORD = '手机'
TIMEOUT = 30
PLATFORM = 'Android'
DEVICE_NAME = 'Redmi Note 4X'
DRIVER_SERVER = 'http://localhost:4723/wd/hub'
FLICK_START_X = 300
FLICK_START_Y = 500
FLICK_DISTANCE = 500


class Action:
    def __init__(self):
        # 驱动配置
        self.desired_caps = {
            'platformName': PLATFORM,
            'deviceName': DEVICE_NAME,
            'appPackage': 'com.jingdong.app.mall',
            'appActivity': 'main.MainActivity'
        }
        self.driver = webdriver.Remote(DRIVER_SERVER, self.desired_caps)
        self.wait = WebDriverWait(self.driver, TIMEOUT)

    def comments(self):
        # 同意
        agree = self.wait.until(EC.presence_of_element_located((By.ID, 'com.jingdong.app.mall:id/bv_')))
        agree.click()
        # 两次允许
        allow = self.wait.until(EC.element_to_be_clickable((By.ID, 'android:id/button1')))
        allow.click()
        time.sleep(1)
        allow.click()
        time.sleep(1)
        # 点击进入搜索页面
        search = self.wait.until(EC.presence_of_element_located((By.ID, 'com.jingdong.app.mall:id/ru')))
        search.click()
        # 点击搜索文本
        search_text = self.wait.until(EC.presence_of_element_located((By.ID, 'com.jd.lib.search:id/search_text')))
        search_text.click()
        # 输入搜索文本
        TouchAction(self.driver).tap(x=204, y=1517).perform()
        TouchAction(self.driver).tap(x=650, y=1497).perform()
        TouchAction(self.driver).tap(x=896, y=1352).perform()
        TouchAction(self.driver).tap(x=696, y=1343).perform()
        TouchAction(self.driver).tap(x=745, y=1490).perform()
        TouchAction(self.driver).tap(x=781, y=1359).perform()
        TouchAction(self.driver).tap(x=105, y=1182).perform()
        # 点击搜索按钮
        search_button = self.wait.until(EC.element_to_be_clickable((By.ID, 'com.jingdong.app.mall:id/avw')))
        search_button.click()
        # 点击进入商品详情
        time.sleep(5)
        while True:
            try:
                view1 = self.wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//*[@resource-id="com.jd.lib.search:id/product_list"]/android.widget.RelativeLayout[1]')))
                view1.click()
                break
            except TimeoutException:
                time.sleep(5)
        # 点击进入评论详情
        time.sleep(5)
        while True:
            try:
                self.driver.flick(FLICK_START_X, FLICK_START_Y + 100, FLICK_START_X, FLICK_START_Y)
                tab = self.wait.until(EC.presence_of_element_located((By.ID, 'com.jd.lib.productdetail:id/pd_tab3')))
                tab.click()
                break
            except TimeoutException:
                time.sleep(5)

    def scroll(self):
        while True:
            try:
                # 模拟滑动
                time.sleep(1.5)
                self.driver.flick(FLICK_START_X, FLICK_START_Y + FLICK_DISTANCE, FLICK_START_X, FLICK_START_Y)
                time.sleep(1.5)
                if self.driver.find_element_by_id("com.jd.lib.shareorder:id/default_icon"):
                    print('滑到底端')
                    break
            except NoSuchElementException:
                pass

    def main(self):
        self.comments()
        self.scroll()


if __name__ == '__main__':
    action = Action()
    action.main()


