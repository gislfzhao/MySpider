# -*- coding: utf-8 -*-
import requests
import logging
import urllib3
# urllib3.disable_warnings()
logging.captureWarnings(True)
r = requests.get("https://www.12306.cn", verify=False)
r.encoding = 'utf-8'
print(r.status_code)
print(r.text)
