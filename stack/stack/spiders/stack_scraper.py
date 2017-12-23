# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

from stack.items import StackItem

class StackScraperSpider(scrapy.Spider):
    name = 'stack_scraper'
    allowed_domains = ['stackoverflow.com']
    start_urls = ["http://stackoverflow.com/questions?pagesize=50&sort=newest"]

    def parse(self, response):
        question = Selector(response).xpath('//div[@class="summary"]/h3')

        for questions in question:
            item = StackItem()
            item['title'] = question.xpath(
                'a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = question.xpath(
                'a[@class="question-hyperlink"]/@href').extract()[0]
            yield item
