# -*- coding: utf-8 -*-
import scrapy


class FakeSpider(scrapy.Spider):
    name = "fake"
    allowed_domains = ["archive-it.org/collections/8142/?show=Sites"]
    start_urls = ['https://www.archive-it.org/collections/8142/?show=Sites/']

    def parse(self, response):
        pass
