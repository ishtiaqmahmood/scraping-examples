# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlPathSelector
from scrapy.http import Request
from linkedin.items import LinkedinItem


class LinkedinScraperSpider(scrapy.Spider):
    #crawler description
    name = 'linkedin_scraper'
    allowed_domains = ['linkedin.com']

    """
    list_one = (i for i in xrange(1,100))
    list_two = (i for i in xrange(1,100))
    list_three = (i for i in xrange(1,100))
    start_urls = ["http://www.linkedin.com/directory/people-%s-%d-%d-%d"
                  % (alphanum, num_one, num_two, num_three)
                    for alphanum in "abcdefghijklmnopqrstuvwxyz"
                    for num_one in list_one
                    for num_two in list_two
                    for num_three in list_three
                 ]
    """
    start_urls = ["http://www.linkedin.com/directory/people-a-23-23-2"]
    rules = (Rule(LinkExtractor(allow = ('\/pub\/.+')), callback='parse_item'))

    def parse(self, response):
        if response:
            hxs = HtmlXPathSelector(response)
            item = LinkedinItem()

