# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode
from ..items import ImageItem
from json import loads


class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['image.so.com']

    def start_requests(self):
        data = {
            'ch': 'photography',
            'listtype': 'new',
            'temp': 1
        }
        base_url = 'http://image.so.com/zj?'
        for page in range(0, self.settings.get('MAX_PAGE')):
            data['sn'] = page * 30
            params = urlencode(data)
            url = base_url + params
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        result = loads(response.text)
        for image in result.get('list'):
            item = ImageItem()
            item['id'] = image.get('index')
            item['imageid'] = image.get('imageid')
            item['title'] = image.get('group_title')
            item['tag'] = image.get('tag')
            item['img_url'] = image.get('qhimg_url')
            yield item