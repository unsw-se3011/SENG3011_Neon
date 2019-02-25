# -*- coding: utf-8 -*-
import scrapy
import fileinput

def get_url(text):
    return "http://www.promedmail.org/post/%s" % text 

class PromedSpider(scrapy.Spider):
    name = 'promed'
    allowed_domains = ['http://www.promedmail.org']

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
