# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy_fd.items import ScrapyFdItem


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ["dmoz.org"]
    def start_requests(self):
        urls = [
            'https://www.jd.com/allSort.aspx',
            #"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
            #"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_category)

    def parse(self, response):
        self.logger.info('A response from %s just arrived!!!!!!!!!!!!!', response.url) 
        """
        for sel in response.xpath('//ul/li[@class="gl-item"]'):
            item = ScrapyFdItem()
            item['name'] = sel.xpath('div[@class="p-name"]//a//em/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item
        pass
        """

    def parse_category(self, response):
        """获取分类页"""
        try:
            texts = response.xpath('//div[@class="category-item m"]/div[@class="mc"]/div[@class="items"]/dl/dd/a').extract()
            for text in texts:
                items = re.findall(r'<a href="(.*?)" target="_blank">(.*?)</a>', text)
                for item in items:
                    if item[0].split('.')[0][2:] in key_word:
                        if item[0].split('.')[0][2:] != 'list':
                            yield scrapy.Request(url='https:' + item[0], callback=self.parse_category)
                        else:
                            categoriesItem = CategoriesItem()
                            categoriesItem['name'] = item[1]
                            categoriesItem['url'] = 'https:' + item[0]
                            categoriesItem['_id'] = item[0].split('=')[1].split('&')[0]
                            yield categoriesItem
                            yield scrapy.Request(url='https:' + item[0], callback=self.parse_list)
        except Exception as e:
            print('error:', e)
