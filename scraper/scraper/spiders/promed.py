# -*- coding: utf-8 -*-
import scrapy


class PromedSpider(scrapy.Spider):
    name = 'promed'
    allowed_domains = ['http://www.promedmail.org']
    start_urls = ['http://http://www.promedmail.org/']

    def parse(self, response):
        pass
