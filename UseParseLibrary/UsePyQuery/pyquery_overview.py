# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq

html = '''
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''

doc = pq(html)
print(type(doc('li')))

del doc
doc = pq(url="https://cuiqingcai.com")

del doc
import requests
doc = pq(requests.get(url="https://cuiqingcai.com").text)
# print(doc('title').text())

del doc
doc = pq(html)
# print(doc('li'))
print(doc("#container .list li"))
print(type(doc("#container .list li")))
items = doc('.list')
print("\n\n\n")
print(items)
lis = items.find('li')
print(lis)
del lis
lis = items.children('.active')
print("nihaonihao")
print(lis)
print(lis.parents())
del lis
print("nihaonihao")
li = doc('.list .item-0.active')
print(li)
print(li.siblings())

print("nihaonihao")
lis = doc('li').items()
print(type(lis))
print(type(doc('li').html()))
print(type(doc('li').text()))
for item in lis:
    print(item, type(item))
    print(item.attr.href)
    print(type(item.html()))
    print(item.text())

print("nihaonihao\n")
print(html)
li = doc('li:first-child')
print(li)
del li
li = doc('li:last-child')
print(li)
del li
li = doc('li:nth-child(2)')
print(li)
del li
li = doc('li:gt(2)')
print(li)
del li
li = doc('li:nth-child(2n)')
print(li)
del li
li = doc('li:contains(second)')
print(li)
