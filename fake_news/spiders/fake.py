# -*- coding: utf-8 -*-
import scrapy


class FakeSpider(scrapy.Spider):
    name = "fake"
    allowed_domains = ["archive-it.org/collections/8142/?show=Sites"]
    start_urls = ['https://www.archive-it.org/collections/8142/?show=Sites/']

    def parse(self, response):
        links = response.xpath('//*[@class="url"]/a/@href').extract()
        print links

        for link in links:
        	# go to that page and scrape all data from each site, 
        	# for now we can look at only the most recent archive
        	# yield scrapy.http.Request(link)
        	pass