# -*- coding: utf-8 -*-
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener
from urllib import request
from selenium import webdriver
import socket
import socks
import requests
import time


def use_http():
    proxy = '36.48.73.16:80'
    proxy_handler = ProxyHandler({
        'http': 'http://' + proxy,
        'https://': 'https://' + proxy
    })
    headers = ("User-Agent",
               "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.168 "
               "Safari/537.36")
    opener = build_opener(proxy_handler)
    opener.addheaders = [headers]
    try:
        response = opener.open('http://httpbin.org/get')
        print(response.read().decode('utf-8'))
    except URLError as e:
        print(e.reason)


def use_sock():
    socks.set_default_proxy(socks.SOCKS5, '117.69.98.216', 6666)
    socket.socket = socks.socksocket
    try:
        response = request.urlopen('http://httpbin.org/get')
        print(response.read().decode('utf-8'))
    except URLError as e:
        print(e.reason)


def use_requests():
    proxy = '36.48.73.16:80'
    proxies = {
        'http': 'http://' + proxy,
        'https': 'https://' + proxy
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/64.0.3282.168 Safari/537.36"
    }
    try:
        response = requests.get('http://httpbin.org/get', proxies=proxies, headers=headers)
        print(response.text)
    except requests.exceptions.ConnectionError as e:
        print("Error", e.args)
    pass


def use_selenium():
    proxy = '36.48.73.16:80'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=http://' + proxy)
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get('http://httpbin.org/get')
    time.sleep(10)
    browser.quit()


if __name__ == '__main__':
    # use_http()
    # use_sock()
    # use_requests()
    use_selenium()
