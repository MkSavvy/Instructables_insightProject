# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 12:16:20 2015

@author: Michel_home
"""

import scrapy

from DIYprojects.items import DiyprojectsItem

class DIYSpider(scrapy.Spider):
    name = "diySpider"
    allowed_domains = ["instructables.com"]
    start_urls = [
        "http://www.instructables.com/tag/type-id/category-technology/"
    ]
    
    def parse(self, response):
        for sel in response.selector.xpath("//div[@class='projects']/ul[@class='h-list explore-covers-list clearfix']/li"):
            item = DiyprojectsItem()          
            item["projectURL"] = sel.xpath(".//div[@class='cover-info ']/span[@class='title']/a/@href").extract()
            item["projectName"] = sel.xpath(".//div[@class='cover-stats']/span/text()").extract()
            item["views"] = sel.xpath(".//span[@class='views']/text()").extract()
            item["favorites"] = sel.xpath(".//span[@class='tutorials']/text()").extract()
            yield item
            
        next_page = response.xpath("//div[@class='pagination fr']/ul/li[last()]/a/@href")
        if(next_page):
            scrapy.Request(next_page
#    def parse_tech_page(self, response):
#        for sel in response.xpath('//div[@id="instructable-steps"]'):
#            print sel.url
#            item = DiyprojectsItem()          
#            item["projectURL"] = sel.xpath('a/text()').extract()
#            item["lists"] = sel.xpath('a/@href').extract()
#            item["views"] = sel.xpath('text()').extract()
#            item["favorites"] = sel.xpath('text()').extract()
#            yield scrapy.Request(url, self.parse_articles_follow_next_page)      
#        
#        
##        filename = response.url.split("/")[-2] + '.html'
#        with open(filename, 'wb') as f:
#            f.write(response.body)