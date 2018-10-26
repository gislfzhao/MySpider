# -*- coding: utf-8 -*-
from urllib.robotparser import RobotFileParser
from urllib import request

rp = RobotFileParser()
# rp.set_url("https://www.jianshu.com/robots.txt")
# rp.read()
rp.parse(request.urlopen("https://www.baidu.com/robots.txt").read().decode("utf-8").split("\n"))
print(rp.can_fetch('*', 'https://wenku.baidu.com/search?lm=0&od=0&ie=utf-8&word=%E7%AE%80%E4%B9%A6'))
print(rp.can_fetch('*', 'https://www.jianshu.com'))

# url = "https://www.jianshu.com/p/13b9b146e0db"
# headers = {
#     "User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)",
# }
# req = request.Request(url, headers=headers)
# res = request.urlopen(req)
# print(res.read().decode("utf-8"))
