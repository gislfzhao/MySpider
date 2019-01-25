# -*- coding: utf-8 -*-
import scrapy


class TrafficSpider(scrapy.Spider):
    name = 'traffic'
    allowed_domains = ['www.nitrafficindex.com']
    start_urls = ['http://www.nitrafficindex.com/']

    def parse(self, response):
        print(response.text)
        pass
