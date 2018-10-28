# -*- coding: utf-8 -*-

import requests

requests.get('http://httpbin.org/cookies/set/number/1234567890987654321')
r = requests.get('http://httpbin.org/cookies')
print(r.text)

s = requests.session()
r = s.get('http://httpbin.org/cookies/set/number/1234567890987654321')
print(r.text)
r = s.get('http://httpbin.org/cookies')
print(r.text)
