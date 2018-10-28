# -*- coding: utf-8 -*-
import requests
from requests.auth import HTTPBasicAuth
proxies = {
    'http': 'http://118.190.95.35:9001',
    'https': 'https://125.70.13.77:8080'
}
r = requests.get("https://taobao.com", proxies=proxies, timeout=1)
print(r.status_code)
print(r.text)
