# -*- coding: utf-8 -*-
import scrapy
from ..items import JdProductItem
from urllib.parse import quote
from lxml import etree


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['www.jd.com']
    base_url = 'https://search.jd.com/Search?keyword='

    def start_requests(self):
        for keyword in self.settings.get('KEYWORDS'):
            for page in range(1, self.settings.get('MAX_PAGE') + 1):
                url = self.base_url + quote(keyword)
                yield scrapy.Request(url=url, callback=self.parse, meta={'page': page}, dont_filter=True)

    def parse(self, response):
        products = response.xpath('//*[@id="J_goodsList"]/ul/li[@class="gl-item"]')
        for product in products:
            item = JdProductItem()
            item['image'] = 'https:' + product.xpath('.//div[@class="p-img"]//img/@src').extract_first('')
            item['price'] = ''.join(product.xpath('.//div[@class="p-price"]//text()').extract()).strip()
            item['title'] = ''.join(product.xpath(
                './/div[@class="p-name p-name-type-2"]/a/em//text()').extract()).strip()
            item['comment'] = product.xpath('.//div[@class="p-commit"]/strong/a/text()').extract_first('')
            item['shop'] = product.xpath('.//div[@class="p-shop"]//a/text()').extract_first('')
            yield item
