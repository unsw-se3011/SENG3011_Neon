# -*- coding: utf-8 -*-
import scrapy
from .FuzzTime import FuzzTime
from datetime import datetime
import re

import cssselect


def filter_str(s):
    if "adsbygoogle" in s:
        return ''
    if "disease news and information" in s:
        return ''
    if "the Infectious Disease News Facebook page" in s:
        return ''
    if 'Image/' in s:
        return ''
    return s


def replace_unicode(s):
    # some character of unicode dosen't need to show
    # and then stip it
    return str(s).replace('\u00a0', ' ').replace('\\u2019', "'")\
        .replace('\u2018', '').replace('\xa0', '').strip()


listen_filter = re.compile('^LISTEN')


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

        # edge_urls=[
        #     'http://outbreaknewstoday.com/possible-ebola-exposure-arrive-nebraska-47761/',
        #     'http://outbreaknewstoday.com/cdcs-frieden-zika-infections-appear-to-be-increasing-rapidly-in-puerto-rico-51464/',
        #     'http://outbreaknewstoday.com/invasive-asian-longhorn-tick-confirmed-pennsylvania-86598/',
        #     'http://outbreaknewstoday.com/chikungunya-2nd-travel-associated-case-reported-dallas-45898/',
        #     'http://outbreaknewstoday.com/caribbean-island-countries-trained-to-respond-rapidly-to-imported-measles-58466/',
        #     'http://outbreaknewstoday.com/african-swine-fever-vietnam-reports-1st-outbreaks-guangxi-province-china-55191/'
        # ]
        
        # for url in edge_urls:
        #     yield scrapy.Request(url=url, callback=self.parse_article)
            

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

        # all the text
        text = response.css('div.postcontent *::text').getall()

        # text need to remove
        bad = response.css('ul li strong a::text').getall()
        # script is not needed
        bad += response.css('script *::text').getall()
        # listen link is not needed
        bad += response.css('p strong::text').getall()
        # # power press link should remove 
        bad += response.css('p.powerpress_links *::text').getall()
        bad += response.css('div.powerpress_player *::text').getall()

        # filter out
        text = [t for t in text if t not in bad]

        # listen link is not needed
        bad = response.css('p strong::text').getall()
        bad = filter(listen_filter.search, bad)
        # filter out
        text = [t for t in text if t not in bad]

        # trim
        text = [t for t in map(
            lambda el: filter_str(
                replace_unicode(el)
            ), text
        )]

        # reduce empty
        text = [t for t in text if len(t) > 0]

        # fetch img 


        yield {
            'headline': replace_unicode(response.css('div.posttitle h1::text').get()),
            'date_of_publication':  str(FuzzTime(date, hour=True)),
            'main_text': ' '.join(text),
            # 'all_text': ' '.join(
            #     map(lambda x: replace_unicode(x), response.css(
            #         'div.postcontent *::text').getall()
            #         )
            # ),
            'url': response.url,
            'img': response.css('div.postcontent figure>img::attr(src)').get() or ''
        }
