# -*- coding: utf-8 -*-
from lxml import etree

text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
# html = etree.HTML(text)
# result = etree.tostring(html)
# print(type(html))
# print(type(result), result)
# print(type(result), result.decode("utf-8"))

html = etree.parse('test.html', etree.HTMLParser())
# result = etree.tostring(html)
result = html.xpath("//*")
print(result)
del result
result = html.xpath("//li")
print(result)
print(result[0])
del result
result = html.xpath("//li/a")
print(result)
del result
result = html.xpath("//ul/a")
print(result)
del result
result = html.xpath("//ul//a")
print(result)
del result
result = html.xpath('//a[@href="link3.html"]/parent::*/@class')
print(result)
del result
result = html.xpath('//a[@href="link3.html"]')
print(result)
del result
result = html.xpath('//li[@class="item-0"]')
print(result)
del result
result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)
del result
result = html.xpath('//li/a/@href')
print(result)

text = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''
del html
html = etree.HTML(text)
del result
result = html.xpath('//li[contains(@class, li)]/a/text()')
# result = html.xpath('//li[@class="li li-first"]/a/text()')
print(result)

del html, result
del text
text = '''
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(result)

del html, result, text
html = etree.parse('test.html', etree.HTMLParser())
result = html.xpath('//li|//a')
print(result)

del result
result = html.xpath('//li[1]/a/text()')
print(result)

del result
result = html.xpath('//li[last()]/a/text()')
print(result)

del result
result = html.xpath('//li[last()-2]/a/text()')
print(result)

del result
result = html.xpath('//li[position()<3]/a/text()')
print(result)

del result
result = html.xpath('//li[1]/ancestor::*')
print(result)

del result
result = html.xpath('//li[1]/ancestor::div')
print(result)

del result
result = html.xpath('//li[1]/attribute::*')
print(result)

del result
result = html.xpath('//li[1]/child::*')
print(result)

del result
result = html.xpath('//ul/child::li[@class="item-0"]')
print(result)

del result
result = html.xpath('//li[1]/descendant::*')
print(result)

del result
result = html.xpath('//li[1]/descendant::span')
print(result)

del result
result = html.xpath('//li[1]/following::*[1]')
print(result)

del result
result = html.xpath('//li[1]/following-sibling::*')
print(result)

# del result
# result = html.xpath('//li')
# print(result)
# li_result =result[0]
# print(li_result)
# result2 = li_result.xpath('//span/text()')
# print(result2)

del html, result
html = etree.parse('test2.html', etree.HTMLParser(encoding='utf-8'))
# etree.tostring(html, encoding='utf-8').decode('utf-8')
content = html.xpath('//dd')
print(content[0])
# index = content[0].xpath('/*')
index = content[0].xpath('//dd/i[contains(@class, "board-index")]/text()')
print(eval(str(index[0])))
image_url = content[0].xpath('//dd/a/img[@class="board-img"]/@data-src')
print(str(image_url[0]))
name = content[0].xpath(u'//dd/div//p[@class="name"]/a/text()')
print(str(name[0]))
star = content[0].xpath(u'//dd/div//p[@class="star"]/text()')
print(str(star[0]).strip().strip("主演："))
time = content[0].xpath(u'//dd/div//p[@class="releasetime"]/text()')
print(str(time[0]).strip("上映时间："))
score = content[0].xpath(u'//dd//div[contains(@class, "score-num")]//i/text()')
print(float(str(score[0]) + str(score[1])))

