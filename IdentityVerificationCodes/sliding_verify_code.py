# -*- coding: utf-8 -*-
from time import sleep
from random import randint
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

EMAIL = 'test@test.com'
PASSWORD = '123456'
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 20)


def get_geetest_button():
    """
    获取初识验证按钮
    :return: 按钮对象
    """
    button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_radar_tip')))
    return button


def get_position():
    """
    获取验证码位置
    :return: 验证码位置元祖
    """
    img = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_img')))
    # 等待一段时间
    sleep(2)
    location = img.location
    size = img.size
    # 使用的电脑缩放为150%，而location，size是以100%得到的, 故需乘以1.5
    top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], \
                               location['x'] + size['width']
    print(top, bottom, left, right)
    return 1.5 * top, 1.5 * bottom, 1.5 * left, 1.5 * right


def get_screenshot():
    """
    获取网页截图
    :return: 截图对象
    """
    screenhot = browser.get_screenshot_as_png()
    screenhot = Image.open(BytesIO(screenhot))
    return screenhot


def get_geetest_image(name='captcha.png'):
    """
    获取验证码图片
    :return: 图片对象
    """
    top, bottom, left, right = get_position()
    print("验证码位置：", top, bottom, left, right)
    screenhot = get_screenshot()
    captcha = screenhot.crop((left, top, right, bottom))
    captcha.save(name)
    return captcha


def get_slider():
    """
    获取滑块
    :return: 返回滑块对象
    """
    slider = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_slider_button')))
    return slider


def is_pixel_equal(image1, image2, x, y):
    """
    判断像素是否相同
    :param image1: 图片1
    :param image2: 图片2
    :param x: 位置x
    :param y: 位置y
    :return: 像素是否相同
    """
    # 去两个图片的像素点
    pixel1 = image1.load()[x, y]
    pixel2 = image2.load()[x, y]
    threshold = 60
    # 判断图片像素点的RGB数据
    if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and \
            abs(pixel1[2] - pixel2[2]) < threshold:
        return True
    else:
        return False


def get_gap(image1, image2):
    """
    获取缺口偏移量
    :param image1: 不带缺口图片
    :param image2: 带缺口图片
    :return:
    """
    left = 100
    for i in range(left, image1.size[0]):
        for j in range(image1.size[1]):
            if not is_pixel_equal(image1, image2, i, j):
                left = i
                return left
    return left


def get_track(distance):
    """
    根据偏移量获取移动轨迹
    :param distance: 偏移量
    :return: 偏移轨迹
    """
    # 移动轨迹列表
    track = []
    # 当前位移
    current = 0
    # 减速阈值
    mid = distance * 4 / 5
    # 初速度
    v = 0

    while current <= distance:
        # 计算间隔
        t = randint(2, 8) / 15
        if current < mid:
            # 加速度为正2
            a = randint(1, 5)
        else:
            # 加速度为负3
            a = -randint(2, 4)
        # 初速度 v0
        v0 = v
        # 当前速度 v = v0 + at
        v = v0 + a * t
        # 移动距离
        move = v0 * t + 1 / 2 * a * t * t
        # 当前位移
        current += move
        track.append(round(move / 1.5))
    print(track)
    return track


def move_to_gap(slider, tracks):
    """
    拖动滑块到缺口处
    :param slider: 滑块
    :param tracks: 轨迹
    :return:
    """
    ActionChains(browser).click_and_hold(slider).perform()
    for x in tracks:
        ActionChains(browser).move_by_offset(xoffset=x, yoffset=0).perform()
        sleep(0.1)
    ActionChains(browser).release().perform()


def main():
    url = 'https://account.geetest.com/login'
    browser.get(url)
    email = wait.until(EC.presence_of_element_located((By.ID, 'email')))
    password = wait.until(EC.presence_of_element_located((By.ID, 'password')))
    email.send_keys(EMAIL)
    password.send_keys(PASSWORD)
    button = get_geetest_button()
    button.click()

    # 获取有滑块的图片
    image1 = get_geetest_image('image1.png')
    # 获取没有滑块的图片
    browser.execute_script("document.getElementsByClassName('geetest_canvas_fullbg')[0].style.display='block'")
    image2 = get_geetest_image('image2.png')
    browser.execute_script("document.getElementsByClassName('geetest_canvas_fullbg')[0].style.display='none'")

    # 获取滑块
    slider = get_slider()
    # slider.click()
    distance = get_gap(image1, image2) - 7
    print(distance)
    tracks = get_track(distance)
    move_to_gap(slider, tracks)


if __name__ == '__main__':
    while True:
        main()
        sleep(3)
        # try:
        #     main()
        # except:
        #     browser.quit()
