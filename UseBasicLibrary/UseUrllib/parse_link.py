# -*- coding: utf-8 -*-
# urlparse()
# from urllib.parse import urlparse, urlunparse

# result = urlparse('https://www.baidu.com/index.html;user?id=5#comment')
# print(type(result), result)
# # result = urlparse('www.baidu.com/index.html;user?id=5#comment')
# # print(type(result), result)
# # result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme="https")
# # print(type(result), result)
# # result = urlparse('https://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
# # print(type(result), result)
# # result = urlparse('https://www.baidu.com/index.html#comment', allow_fragments=True)
# # print(type(result), result)
# print(result.scheme, result[0], result.netloc, result[1])

# data = ['https', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
# del data
# data = ('https', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment')
# print(urlunparse(data))
#
# from urllib.parse import urlsplit, urlunsplit
# result = urlsplit('https://www.baidu.com/index.html;user?id=5#comment')
# print(type(result), result)
# data = ('https', 'www.baidu.com', 'index.html', 'a=6', 'comment')
# print(urlunsplit(data))

# from urllib.parse import urljoin
# print(urljoin('https://www.baidu.com', 'index.html'))
# print(urljoin('https://www.baidu.com', 'https://cuiqingcai.com/index.html'))
# print(urljoin('https://www.baidu.com/about.html', 'https://cuiqingcai.com/index.html'))
# print(urljoin('https://www.baidu.com/about.html', 'https://cuiqingcai.com/index.html?question=2'))
# print(urljoin('https://www.baidu.com?wd=bc', 'https://cuiqingcai.com/index.html'))
# print(urljoin('https://www.baidu.com', '?category=2#comment'))
# print(urljoin('www.baidu.com', 'index.html'))
# print(urljoin('www.baidu.com', '?category=2#comment'))
# print(urljoin('www.baidu.com?wd=bc#comment', '?category=2'))

# from urllib.parse import urlencode, parse_qs, parse_qsl
#
# params = {
#     'name': 'germey',
#     'age': 22
# }
# base_url = "http://www.baidu.com?"
# url = base_url + urlencode(params)
# print(urlencode(params))
# print(url)
#
# query = "ie=UTF-8&wd=socket"
# dit = parse_qs(query)
# print(dit.items())
# for key in dit.keys():
#     print(key, dit[key])
#
# dit2 = parse_qsl(query)
# print(dit2)

from urllib.parse import quote, unquote

keyword = "壁纸"
url = "https://www.baidu.com/s?wd=" + quote(keyword)
print(url)
url = "https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8"
print(unquote(url))
