# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Images360Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ImageItem(scrapy.Item):
    collection = table = 'images'
    id = scrapy.Field()
    imageid = scrapy.Field()
    title = scrapy.Field()
    tag = scrapy.Field()
    img_url = scrapy.Field()
