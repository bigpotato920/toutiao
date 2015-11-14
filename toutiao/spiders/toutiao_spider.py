#!/usr/bin/env python
# encoding: utf-8

import scrapy
from toutiao.items import ToutiaoItem


class TouTiaoSpider(scrapy.Spider):
    name = "toutiao"
    allowed_domains = ["toutiao.io"]
    start_urls = ["http://toutiao.io/"]

    def parse(self, response):
        date = response.xpath('//div[@class="daily"]/h3/small/text()').extract()
        index = 1
        for post in response.xpath('//div[@class="daily"]/div[@class="posts"]/div[@class="post"]'):
            item = ToutiaoItem()

            title = post.xpath('.//div[@class="content"]/h3/a/text()').extract()
            url = post.xpath('.//div[@class="content"]/h3/a/@href').extract()
            summary = post.xpath('.//p[@class="summary"]/a/text()').extract()

            item['date'] = date[0].encode('utf-8').strip()
            item['title'] = title[0].encode('utf-8').strip()
            item['url'] = url[0].encode('utf-8').strip()
            if len(summary) > 0:
                item['summary'] = summary[0].encode('utf-8').strip()
            else:
                item['summary'] = ""
            self.debug_item(index, item)
            index += 1
            yield item

    def debug_item(self, index, item):
        print '第%d个头条，时间：%s，标题：%s，url：%s，总结：%s' \
            % (index, item['date'], item['title'], item['url'], item['summary'])
