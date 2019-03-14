# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractor import LinkExtractor
from scrapy.selector import HtmlXPathSelector
import re

class CleanmediaItem(scrapy.Item):
    headline = scrapy.Field()
    link = scrapy.Field()


class HindustanSpider(CrawlSpider):
    name = "hindustan"
    allowed_domains = ["www.hindustantimes.com"]
    start_urls = ['hindustantimes.com']
    rules = (Rule(LinkExtractor(allow="hindustantimes",), callback ='parse_page', follow=False),)

    def parse_page(self, response):
        st = response.url
        print(st)
        st = re.sub('https://www.hindustantimes.com/[a-z-]*/','',st)
        st = re.sub('/story(.*)',"",st)
        st = re.sub('-'," ",st)
        print(st)
        if (len(st)>15) :

            ndtvitem = CleanmediaItem(headline= st,link=response.url)
            yield ndtvitem
