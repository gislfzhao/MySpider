# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import NewsItem
from ..utils import get_config
from ..rules import rules
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, SelectJmes, Compose


class NewsLoader(ItemLoader):
    default_output_processor = TakeFirst()


class ChinaLoader(NewsLoader):
    text_out = Compose(Join(), lambda s: s.strip())
    source_out = Compose(Join(), lambda s: s.strip())


class UniversalSpider(CrawlSpider):
    name = 'universal'

    def __init__(self, name, *args, **kwargs):
        config = get_config(name)
        self.config = config
        self.rules = rules.get(config.get('rules'))
        self.start_urls = config.get('start_urls')
        self.allowed_domains = config.get('allowed_domains')
        super(UniversalSpider, self).__init__(*args, **kwargs)

    def modify_http(self, link_list):
        for item in link_list:
            item.url = item.url.replace('http', 'https')
        return link_list

    def parse_item(self, response):
        item = self.config.get('item')
        if item:
            cls = eval(item.get('class'))()
            loader = eval(item.get('loader'))(item=cls, response=response)
            # 动态获取属性配置
            for key, value in item.get('attrs').items():
                for extractor in value:
                    if extractor.get('method') == 'xpath':
                        loader.add_xpath(key, *extractor.get('args'), **{'re': extractor.get('re')})
                    elif extractor.get('method') == 'css':
                        loader.add_css(key, *extractor.get('args'), **{'re': extractor.get('re')})
                    elif extractor.get('method') == 'attr':
                        loader.add_value(key, getattr(response, *extractor.get('args')))
                    elif extractor.get('method') == 'value':
                        loader.add_value(key, *extractor.get('args'), **{'re': extractor.get('re')})
            yield loader.load_item()
