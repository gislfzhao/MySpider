# -*- coding: utf-8 -*-

import re

content = "Hello 1234567 World_This is a Regex Demo"
# print(len(content))
# pattern = "^Hello\s\d\d\d\s\d{4}\s\w{10}"
# result1 = re.match(pattern, content)
# print(result1)
# print(result1.group())
# print(result1.span())

pattern = "^Hello\s(\d+)\s(World)"
result = re.match(pattern, content)
# print(result)
# print(result.group())
# print(result.group(1))
# print(result.group(2))
# print(result.span())

result1 = re.match("^Hello.*?(\d+).*Demo$", content)
# print(len(content))
# print(result1)
# print(result1.group(1))
# print(result1.span())

# content2 = "http://weibo.com/comment/zhao"
# result2 = re.match("http.*?comment/(.*?)", content2)
# result3 = re.match("http.*?comment/(.*)", content2)
# print(type(result2))
# print(result3.group(1))

result5 = re.match("\s\d+\s", "456 123 789 ")
if result5 in [None]:
    print("没有结果")
else:
    print(result5)

# content = '(百度)www.baidu.com'
# result4 = re.match('\(百度\)www.baidu\.com', content)
# print(result4)
