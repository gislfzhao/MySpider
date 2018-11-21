# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq

# html = '''
# <div id="container">
# <ul class="list">
# <li class="item-0">first item</li>
# <li class="item-1"><a href="link2.html">second item</a></li>
# <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
# <li class="item-1 active"><a href="link4.html">fourth item</a></li>
# <li class="item-0"><a href="link5.html">fifth item</a></li>
# </ul>
# </div>
# '''
#
# doc = pq(html)
# print(type(doc('li')))
#
# del doc
# doc = pq(url="https://cuiqingcai.com")
#
# del doc
# import requests
# doc = pq(requests.get(url="https://cuiqingcai.com").text)
# # print(doc('title').text())
#
# del doc
# doc = pq(html)
# # print(doc('li'))
# print(doc("#container .list li"))
# print(type(doc("#container .list li")))
# items = doc('.list')
# print("\n\n\n")
# print(items)
# lis = items.find('li')
# print(lis)
# del lis
# lis = items.children('.active')
# print("nihaonihao")
# print(lis)
# print(lis.parents())
# del lis
# print("nihaonihao")
# li = doc('.list .item-0.active')
# print(li)
# print(li.siblings())
#
# print("nihaonihao")
# lis = doc('li').items()
# print(type(lis))
# print(type(doc('li').html()))
# print(type(doc('li').text()))
# for item in lis:
#     print(item, type(item))
#     print(item.attr.href)
#     print(type(item.html()))
#     print(item.text())
#
# print("nihaonihao\n")
# print(html)
# li = doc('li:first-child')
# print(li)
# del li
# li = doc('li:last-child')
# print(li)
# del li
# li = doc('li:nth-child(2)')
# print(li)
# del li
# li = doc('li:gt(2)')
# print(li)
# del li
# li = doc('li:nth-child(2n)')
# print(li)
# del li
# li = doc('li:contains(second)')
# print(li)
# del li
# li = doc('.item-0').items()
# print(type(li))
# del li
# li = doc.find('li').items()
# print(li)
# del li
# print("ninininini")
# del doc
with open('test2.html', encoding='utf-8') as f:
    content = f.read()
doc = pq(content)
print("测试")
toplist = doc('#toplist')
print(toplist)
print("kaishiceshi")
toplistname1 = toplist('#toplist > div.g-sd3.g-sd3-1 > div > h2:nth-child(1)').text()
toplistname2 = toplist('.n-minelst > h2:nth-child(3)').text()
print(toplistname1)
print(toplistname2)
lists1 = toplist('.n-minelst > ul:nth-child(2) li.mine').items()
for item in lists1:
    result = {
        'toplist': toplistname1,
        'id': item.attr('data-res-id'),
        'name': item('.name > a').text(),
        'link': 'https://music.163.com' + item('.name > a').attr('href'),
        'update': item('p.s-fc4').text()
    }
    print(result)

lists2 = toplist('.n-minelst > ul:nth-child(4) li.mine').items()
for item in lists2:
    result = {
        'toplist': toplistname2,
        'id': item.attr('data-res-id'),
        'name': item('.name > a').text(),
        'link': 'https://music.163.com' + item('.name > a').attr('href'),
        'update': item('p.s-fc4').text()
    }
    print(result)

song_list_div = doc('#song-list-pre-cache')
toplist = doc('#toplist > div.g-mn3 > div > div.g-wrap > div > div.cnt > div > div.hd.f-cb > h2').text()
songs = song_list_div('.m-table > tbody > tr').items()
for song in songs:
    result = {
            'toplist': toplist,
            'id': song.attr('id'),
            'songname': song('td:nth-child(2) .ttc b').attr('title'),
            'song_link': song('td:nth-child(2) .ttc a').attr('href'),
            'duration': song('span.u-dur').text(),
            'artist': song('td:nth-child(4) span').attr('title'),
            'artist-link': song('td:nth-child(4) a').attr('href')
        }
    print(result['songname'])
    print(result)
