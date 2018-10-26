# urllib为内置的http请求库,包含request，error，parse，robotparser四个模块

# response = urllib.request.urlopen("https://www.python.org")
# print(response.status)
# print(type(response))
# print(len(response.read()))
# print(response.getheaders())
# print(response.getheader('Server'))
# # print(response.read().decode('utf-8'))

# data = bytes(urllib.parse.urlencode({"word": "hello"}), encoding="utf-8")
# response = urllib.request.urlopen("https://httpbin.org/post", data=data)
# print(response.read())

# import urllib.request
# response = urllib.request.urlopen("https://www.jianshu.com")
# print(response.read())

# request = urllib.request.Request("https://www.python.org")
# response = urllib.request.urlopen(request)
# print(response.read().decode("utf-8"))

from urllib import request, error, parse

url = "https://httpbin.org/post"
headers = {
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)",
    "Host": 'httpbin.org'
}
dict1 = {
    'word': "Zhao"
}
data = bytes(parse.urlencode(dict1), encoding="utf-8")
req = request.Request(url, data=data, method="POST")
req.add_header("User-Agent", "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)")
res = request.urlopen(req)
print(res.read().decode("utf-8"))

# 构建验证
# from urllib.error import URLError
# from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
#
# username = 'username'
# password = 'password'
# url = "http://localhost:4000/"
#
# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None, url, username, password)
# auth_handler = HTTPBasicAuthHandler(p)
# opener = build_opener(auth_handler)
#
# try:
#     result = opener.open(url)
#     html = result.read().decode("utf-8")
#     print(html)
# except URLError as e:
#     print(e.reason)

# # 使用代理
# from urllib.request import ProxyHandler, build_opener, getproxies
# from urllib.error import URLError
#
# proxy_handler = ProxyHandler({
#     # 'http': 'http://127.0.0.1:9743',
#     # 'https': 'https://127.0.0.1:9743',
#     'http': 'http://114.113.126.82:80',
#     'https': 'https://125.70.13.77:8080',
#     'socks5': 'socks5://182.33.217.116:6666'
# })
# opener = build_opener(proxy_handler)
# try:
#     res = opener.open("https://docs.python.org", timeout=10)
#     print(res.getheaders())
#     print(proxy_handler.proxies.keys())
#     print(res.read().decode("utf-8"))
# except URLError as e:
#     print(e.reason)

# 使用和保存Cookies
# import http.cookiejar
# import urllib.request
#
# # cookie = http.cookiejar.CookieJar()
# filename = "cookies2.txt"
# # cookie = http.cookiejar.MozillaCookieJar(filename)
# cookie = http.cookiejar.LWPCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# res = opener.open("http://www.baidu.com")
# cookie.save(ignore_discard=True, ignore_expires=True)
# # print(cookie)
# # for item in cookie:
# #     print(item.name + " = " + item.value + "  " + item.domain)

# 利用cookie
import http.cookiejar
import urllib.request
cookie = http.cookiejar.LWPCookieJar()
cookie.load("cookies2.txt", ignore_expires=True, ignore_discard=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
res = opener.open("http://www.baidu.com")
print(res.read().decode("utf-8"))
