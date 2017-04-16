# -*- coding: utf-8 -*-
import scrapy


class FakeSpider(scrapy.Spider):
    name = "fake"
    allowed_domains = ["archive-it.org", "wayback.archive-it.org"]
    start_urls = ['https://www.archive-it.org/collections/8142/?show=Sites/']

    def parse(self, response):
        links = response.xpath('//*[@class="url"]/a/@href').extract()
        # print links

        for link in links:
            # go to that page and scrape all data from each site, 
            # for now we can look at only the most recent archive
            yield scrapy.http.Request(link, callback=self.parse_wayback)

        # yield scrapy.http.Request(links[0], callback=self.parse_wayback)

    def parse_wayback(self, response):
        list_of_archives = response.xpath('//*[@class="mainBody"]/a/@href').extract()

        # print list_of_archives

        for archive_link in list_of_archives:
            archive_link = 'http:' + archive_link
            yield scrapy.http.Request(archive_link, callback=self.parse_wayback_archive)
        
        # yield scrapy.http.Request(url, callback=self.parse_wayback_archive)

    def parse_wayback_archive(self, response):
        yield {
            'headlines': response.xpath('//h2/a/text()').extract_first()
        } 




