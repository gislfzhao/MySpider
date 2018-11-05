# -*- coding: utf-8 -*-
import requests
import random
import json
from bs4 import BeautifulSoup
from User_Agents.UserAgents import USER_AGENTS
from Proxy.Proxies import PROXYIES


def get_user_agent():
    random.choice(USER_AGENTS)


def get_proxy():
    return dict()
    pass


def get_proxies_from_page(page_num):
    try:
        headers = {
            'User-Agent': get_user_agent(),
            'Host': 'www.xicidaili.com',
            'Referer': 'http://www.xicidaili.com/nn/',
        }
        proxies = get_proxy()
        url = 'http://www.xicidaili.com/nn/' + str(page_num)
        response = requests.get(url, headers=headers, proxies=proxies, timeout=60)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            # print(response.text)
            return response.text
    except BaseException as e:
        print("ERROR", e.args)
        return None


def parse_proxies_from_page(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find_all(name='tr', attrs={'class': ['', 'odd']})
    for tr in trs:
        tds = tr.find_all(name='td')
        ip = tds[1].string
        port = tds[2].string
        type = tds[5].string.lower()
        savetime = tds[8].string
        yield {
            'ip': ip,
            'port': port,
            'type': type,
            'savetime': savetime
        }


def validate_proxies(json):
    try:
        headers = {
            'User-Agent': get_user_agent(),
        }
        proxies = dict()
        proxies[json['type']] = json['type'] + '://' + json['ip'] + ':' + json['port']
        response = requests.get('https://www.baidu.com', headers=headers, proxies=proxies)
        if response.status_code == 200:
            return proxies
        else:
            return False
    except BaseException as e:
        print("ERROR", e.args)
        return False


def write_to_txt(proxy_info):
    with open('Proxies.txt', 'a', encoding='utf-8') as f:
        f.writelines(json.dumps(proxy_info, ensure_ascii=False) + ',\n')


def main(num):
    html = get_proxies_from_page(num)
    jsons = parse_proxies_from_page(html)
    for item in jsons:
        if validate_proxies(item):
            write_to_txt(validate_proxies(item))


if __name__ == '__main__':
    for i in range(1, 5):
        main(i)
