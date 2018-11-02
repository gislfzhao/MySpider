# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

# soup = BeautifulSoup("<p>Hello</p>", "lxml")
# print(soup.p)
# print(soup.p.string)

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and 
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())
print(type(soup.title.string), soup.title.string)
print(type(soup.title), soup.title)
print(type(soup.head), soup.head)
print(soup.p)
print(soup.title.name)
print(soup.title.attrs)
print(soup.p.attrs)
print(soup.p.attrs["name"])
print(soup.p["name"])
print(soup.head.title)

del html, soup
html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><span><!-- Elsie --></span></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and 
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">...</p>
'''
from collections import Generator, Iterator

soup = BeautifulSoup(html, 'lxml')
print(soup.p.contents)
print(soup.p.children)
# for i, child in enumerate(soup.p.children):
#     print(i, child)
print(soup.p.descendants)
print(isinstance(soup.p.children, Generator))
print(isinstance(soup.p.descendants, Iterator))
for i, child in enumerate(soup.p.descendants):
    print(i, child)

del html, soup
html = '''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        "http://www.w3.org/TR/html4/loose.dtd">
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><span><!-- Elsie --></span></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and 
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">...</p>
'''
soup = BeautifulSoup(html, "lxml")
print("nihao")
print(soup.a)
print(soup.a.parent)
print("\n")
print(type(soup.a.parents))
print(list(soup.a.parents))


del html, soup
html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><span><!-- Elsie --></span></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and 
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">...</p>
'''
print("\n\n")
soup = BeautifulSoup(html, "lxml")
print("Next Sibling", soup.a.next_sibling)
print("Pre_Sibling", soup.a.previous_sibling)
print("Next_Siblings", type(soup.a.next_siblings), list(soup.a.next_siblings))
print("Pre_Siblings", type(soup.a.previous_siblings), list(soup.a.previous_siblings))

del html, soup
html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="story">
    Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Bob</a><a href="http://example.com/lacie" class="sister"
 id="link2">Lacie</a>
</p>
'''
soup = BeautifulSoup(html, "lxml")
print("\n\n")
b = soup.a
print(b.next_sibling.string)
print(list(soup.a.parents)[0].attrs)

del html, soup
html = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
<div class="panel-body">
    <ul class="list" id="list-1">
        <li class="Element">Foo</li>
        <li class="Element">Bar</li>
        <li class="Element">Jay</li>
    </ul>
    <ul class="list list-small" id="list-2">
        <li class="Element">Foo</li>
        <li class="Element">Bar</li>
    </ul>
</div>
    </div>
'''
print("\n\n\n")
soup = BeautifulSoup(html, "lxml")
# print(soup.find_all(name="ul"))
# for ul in soup.find_all(name="ul"):
#     print(ul.find_all(name="li"))
#     for li in ul.find_all(name="li"):
#         print(li.string)
print(soup.find_all(attrs={'id': 'list-1'}))
print(type(soup.find_all(attrs={'class': ['Element']})[0]))
import re
del html, soup
print("\n\n\n\n")
html = '''
<div class="panel">
    <div class="panel-heading">
        <a>Hello, this is a link</a>
        <a>Hello, this is a link, too</a>
    </div>
'''
soup = BeautifulSoup(html, 'lxml')
print(type(soup.find_all(text=re.compile("link"))[0]))
print(type(soup.find(text="Hello, this is a link")))

print("\n\n\n\n")
del html, soup
html = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
<div class="panel-body">
    <ul class="list" id="list-1">
        <li class="Element">Foo</li>
        <li class="Element">Bar</li>
        <li class="Element">Jay</li>
    </ul>
    <ul class="list list-small" id="list-2">
        <li class="Element">Foo</li>
        <li class="Element">Bar</li>
    </ul>
</div>
    </div>
'''
soup = BeautifulSoup(html, "lxml")
print(soup.li)
# print(soup.select('.panel .panel-heading')[0].attrs['class'])
# print(type(soup.select('.panel .panel-heading')))
# print(soup.select('ul li'))
# print(soup.select("#list-2 .Element"))
# for ul in soup.select('ul'):
#     for li in ul.select('li'):
#         print(li.get_text())
#         print(li.string)
