# -*- coding: utf-8 -*-
from urllib import request,error

try:
    res = request.urlopen("https://cuiqingcai.com/index.htm")
except error.HTTPError as e:
    print(e.code, e.reason, e.headers, sep="\n")
    # print(e)
    # print(e.reason)
    # print(e.headers)
