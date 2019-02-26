# -*- coding: utf-8 -*-
import scrapy
from .FuzzTime import FuzzTime
from datetime import datetime


class OutebreaknewsSpider(scrapy.Spider):
    name = 'OutbreakNews'
    # allowed_domains = ['http://outbreaknewstoday.com/']

    def start_requests(self):
        urls = [
            'http://outbreaknewstoday.com/category/us-news/',
            'http://outbreaknewstoday.com/category/latin-america-and-the-caribbean/',
            'http://outbreaknewstoday.com/category/animal-diseases/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_site)

    def parse_site(self, response):
        """ 
        use for pase the links array to article
        """
        for link in response.css('div.posttitle h2 a::attr(href)').getall():
            # yield{
            #     'link': link
            # }
            yield scrapy.Request(
                url=response.urljoin(link),
                callback=self.parse_article
            )
        for link in response.css("a.next.page-numbers::attr(href)").getall():
            yield scrapy.Request(
                url=response.urljoin(link),
                callback=self.parse_site
            )

    def parse_article(self, response):
        """
        Use for pase the article 
        """
        article = response.css('div.content')

        # parse the time
        date = article.css('div.datsingle::text').get()
        date = datetime.strptime(date, '%B %d, %Y')
        yield {
            'headline': str(response.css('div.posttitle h1::text').get().strip()),
            'date_of_publication':  str(FuzzTime(date, day=True)),
            'main_text': ' '.join(
                response.css('div.content div.postcontent')
                .css('div.content div.postcontent p::text,span::text')
                .getall()
            ),
            'url': response.url
        }
