# -*- coding: utf-8 -*-
import scrapy
from scrapy_fd.items import ScrapyFdItem


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ["dmoz.org"]
    def start_requests(self):
        urls = [
            #'https://list.jd.com/list.html?cat=737,794,965/',
            "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
            "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.logger.info('A response from %s just arrived!!!!!!!!!!!!!', response.url) 
        for sel in response.xpath('//ul/li'):
            item = ScrapyFdItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item
        pass
