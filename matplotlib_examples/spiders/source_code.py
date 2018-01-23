# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy import Request


class SourceCodeSpider(scrapy.Spider):
    name = 'source_code'
    allowed_domains = ['matplotlib.org']
    start_urls = ['https://matplotlib.org/gallery/index.html']

    # 解析index页面
    def parse(self, response):
        for sel in response.css('div.section'):
            section = sel.xpath('./@id').extract_first()
            for url in sel.css('span.caption-text a::attr(href)').extract():
                item = {}
                item['section'] = section
                url = response.urljoin(url)
                yield Request(url, callback=self.parse_example, meta={'_item': item})
        # 获取每个caption
        # le = LinkExtractor(restrict_css='span.caption-text')

        # # for link in le.extract_links(response):
        # #     yield Request(link.url, callback=self.parse_example)
        #
        # yield from (Request(link.url, callback=self.parse_example)
        #                     for link in le.extract_links(response))

    # 解析例子页面
    def parse_example(self, response):
        # 得到parse中的item
        item = response.meta.get('_item')
        url = response.css('a.reference.download.internal::attr(href)').extract_first()
        url = response.urljoin(url)
        # url = [link.url for link in le.extract_links(response)]
        # item = {}
        item['file_urls'] = [url]
        yield item