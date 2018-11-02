# -*- coding: utf-8 -*-
import requests
from pyquery import PyQuery as pq
from UseBasicLibrary.CrawlWebPage.UserAgents import USER_AGENTS
import random

url = "https://www.zhihu.com/explore"
headers = dict()
headers['User-Agent'] = random.choice(USER_AGENTS)
html = requests.get(url, headers=headers).text
doc = pq(html)
# print(doc)
items = doc('.explore-tab .feed-item').items()
print(items)
for item in items:
    print(item)
    print("\n" + "=" * 50 + "\n")
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    answer = pq(item.find('.content').html()).text()    # html()：获取节点内部的html文本
    file = open("explore.txt", 'a', encoding='utf-8')
    file.write('\n'.join([question, author, answer]))
    file.write("\n" + '='*60 + "\n")
    file.close()

