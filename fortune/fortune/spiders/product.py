# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#from fortune.items import FortuneItem

class ProductSpider(scrapy.Spider):
    name = 'product'
    allowed_domains = ['http://fortune.com/']
    start_urls = ['http://fortune.com/fortune500/list/']
    
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.wait =  WebDriverWait(self.driver, 10)

    def scroll_until_loaded(self):
        check_height = self.driver.execute_script("return document.body.scrollHeight;")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                self.wait.until(lambda driver: self.driver.execute_script("return document.body.scrollHeight;")  > check_height)
                check_height = self.driver.execute_script("return document.body.scrollHeight;") 
            except TimeoutException:
                break

    def parse(self, response):
        self.driver.get(response.url)
        self.scroll_until_loaded()
        
        for item in self.driver.find_elements_by_css_selector(".company-list li.row"):
            name = item.find_element_by_css_selector(".company-title").text
            revenue = item.find_element_by_css_selector(".company-revenue").text
            yield {"Title":name,"Revenue":revenue}
