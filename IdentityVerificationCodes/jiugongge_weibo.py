# -*- coding: utf-8 -*-
import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

USERNAME = '13466221033'
PASSWORD = '13466221033'


class CrackWeiboSlide:
    def __init__(self):
        self.url = "https://passport.weibo.cn/signin/login"
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.username = USERNAME
        self.password = PASSWORD

    def open(self):
        """
        打开网页并输入用户名和密码并点击
        :return: None
        """
        self.browser.get(self.url)
        username = self.wait.until(EC.presence_of_element_located((By.ID, 'loginName')))
        password = self.wait.until(EC.presence_of_element_located((By.ID, 'loginPassword')))
        submit = self.wait.until(EC.element_to_be_clickable((By.ID, 'loginAction')))
        username.send_keys(self.username)
        password.send_keys(self.password)
        submit.click()
        time.sleep(1)

    def get_position(self):
        """
        获取验证码的位置
        :return: 验证码位置元组
        """
        try:
            img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'patt-shadow')))
        except TimeoutException:
            print("未出现验证码")
            self.open()
        time.sleep(2)
        # 调整电脑显示设置中缩放比例为100%, 不然location会出现偏差
        location = img.location
        size = img.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
            'width']
        return top, bottom, left, right

    def get_screenshot(self):
        """
        获取网页截图
        :return: 截图对象
        """
        screenhot = self.browser.get_screenshot_as_png()
        screenhot = Image.open(BytesIO(screenhot))
        return screenhot
        pass

    def get_image(self, name='captcha.png'):
        """
        获取验证码图片
        :return: 图片对象
        """
        top, bottom, left, right = self.get_position()
        print("验证码位置：", top, bottom, left, right)
        screenhot = self.get_screenshot()
        captcha = screenhot.crop((left, top, right, bottom))
        captcha.save(name)
        return captcha

    def main(self):
        """
        批量获取验证码
        :return: 图片对象
        """
        count = 0
        for i in range(6):
            try:
                self.open()
                time.sleep(1)
            except:
                print()
                time.sleep(1)

        while True:
            self.open()
            self.get_image(str(count) + ".png")
            count += 1


if __name__ == '__main__':
    crack = CrackWeiboSlide()
    crack.main()
