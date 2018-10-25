
# urllib为内置的http请求库,包含request，error，parse，robotparser四个模块
import urllib.request

response = urllib.request.urlopen("https://www.python.org")
# print(response.status)
# print(type(response))
# print(len(response.read()))
# print(response.read())
print(response.read().decode('utf-8'))
