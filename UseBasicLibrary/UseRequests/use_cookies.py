# -*- coding: utf-8 -*-
# use cookies
import requests
import re
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)'
                  'Chrome/52.0.2743.116 Safari/537.36',
    'Cookie': '_zap=0a08d404-0b0d-4389-9263-e2bac1269d13; d_c0="ABAj6AaInw2PTjmp8U-s7Z9kL76M4U51IE4=|1526824267"; _'
              'xsrf=eWtxym5t3ApdIDbP7y4wXKERJqp3ITou; l_n_c=1; q_c1=e9b0675660b2474ea696415913d25c90|154055996200'
              '0|1523517675000; r_cap_id="N2IzMjY2MjZhNjFiNDg4OWFhM2Y3NjU1OWRlZWMwOWQ=|1540559962|5de73e9b8f30101ca84'
              '19ea03602b6ff70b112cb"; cap_id="ZTkxZTdhOTFhZTZhNGFmMTkxMWZhZmI3OWVhNGY3NjY=|1540559962|4a57f41ee810a0'
              '7877892568852572faad528f17"; l_cap_id="ODBjZTBkNjc2NWNjNDZhZDkwYjM3YWJiYWJkMGVhNjc=|1540559962|44541f'
              '9db4b5b29fcadfc47155771cb2bf760559"; n_c=1; __utma=51854390.1215083517.1540560499.1540560499.15405604'
              '99.1; __utmc=51854390; __utmz=51854390.1540560499.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=ref'
              'erral|utmcct=/question/22913650; __utmv=51854390.000--|3=entry_date=20180412=1; tgw_l7_route=170010e94'
              '8f1b2a2d4c7f3737c85e98c; capsion_ticket="2|1:0|10:1540564818|14:capsion_ticket|44:YTg2YjVlZTEzZDRiNDE'
              '0ZDg5N2MyZWNjMjYxZGZhZWU=|14a1c99c1a447e8d7aed868fda41f9d009f3b8caf3e373b3c727a2413d3d4c28"; z_c0="2|1'
              ':0|10:1540564831|4:z_c0|92:Mi4xWWlwVkJRQUFBQUFBRUNQb0JvaWZEU1lBQUFCZ0FsVk5YM1hBWEFEWUJpMzYzQzJhX204QjFx'
              'andNelBrV0pxelNB|77f5e35c9a2f6d7a4638568a1b8ef64076e7f7460c9760115057d88e1bd3a6d9"; tst=r',
    'Host': 'www.zhihu.com'
}
r = requests.get("https://www.zhihu.com/explore", headers=headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(titles)
