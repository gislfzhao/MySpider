# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

rules = {
    'china': (
        Rule(LinkExtractor(allow='article/.*.html', restrict_xpaths='//div[@id="left_side"]//div[@class="con_item"]'),
             callback='parse_item', follow=False, process_links='modify_http'),
        # Rule(LinkExtractor(restrict_xpaths='//div[@id="pageStyle"]//a[contains(., "下一页")]'))
    )
}


def modify_http(link_list):
    for item in link_list:
        item.url = item.url.replace('http', 'https')
    return link_list
