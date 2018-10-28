# -*- coding: utf-8 -*-
from requests import Request, Session

url = "http://httpbin.org/post"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)'
                  'Chrome/52.0.2743.116 Safari/537.36'
}
data = {
    'name': 'zhao'
}
s = Session()
req = Request('POST', url=url, headers=headers, data=data)
prep = s.prepare_request(req)
r = s.send(prep)
print(r.text)
