# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 12:16:20 2015

@author: Michel_home
"""

import scrapy

class DIYSpider(scrapy.Spider):
    name = "diySpider"
    allowed_domains = ["instructables.com"]
    start_urls = [
        "http://www.instructables.com/tag/type-id/category-technology/"
    ]

    def parse(self, response):
        for sel in response.selector.xpath("//div[@class='cover-info ']/span[@class='title']"): 
            url= sel.xpath("a/@href")
            yield response.Request(url, callback=self.parse_tech_page)
        


#   def parse_tech_page(self, response):
#        for sel in response.xpath('//ul/li'):
#            item =   DomzItem()          
#            item["title"] = sel.xpath('a/text()').extract()
#            item["lists"] = sel.xpath('a/@href').extract()
#            item["author"] = sel.xpath('text()').extract()
#            yield scrapy.Request(url, self.parse_articles_follow_next_page)      
#        
#        
##        filename = response.url.split("/")[-2] + '.html'
#        with open(filename, 'wb') as f:
#            f.write(response.body)