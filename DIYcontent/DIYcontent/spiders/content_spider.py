# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 12:16:20 2015

@author: Michel_home
"""

import scrapy

from DIYcontent.items import DiycontentItem

class contentSpider(scrapy.Spider):
    name = "diycontent"
    allowed_domains = ["instructables.com"]
    start_urls = [
        "http://www.instructables.com/id/Musical-RGB-Lamp/?ALLSTEPS", 
        "http://www.instructables.com/id/System-For-Automatically-Limiting-TV-Time/?ALLSTEPS",
        "http://www.instructables.com/id/Raspberry-Pi-Based-Wireless-Microphone/?ALLSTEPS"
    ]
    
    def parse(self, response):
        item = DiycontentItem()
        item["title"] = response.selector.xpath("//head/title/text()").extract()
        item["projectID"] = response.url
        
        head_path = response.selector.xpath("//div[@class='header-bar']")
        item["date"]  = head_path.xpath("./meta[@itemprop='datePublished']/@content").extract()
        item["keywords"]  =  head_path.xpath("./meta[@itemprop='keywords']/@content").extract()
        item["views"]  =  head_path.xpath("./meta[@itemprop='interactionCount']/@content").extract()
        
        item["author"]  = response.selector.xpath("//span[@class='author']/text()").extract()
        item["Nsteps"]  = response.selector.xpath("//*[@id='jump-to-step-btn']/text()").extract()
        item["tags"]  = response.selector.xpath("//div[@class='ible-tags']/div/a/text()").extract()  
        item["award"]  = scrapy.Field()   
        item["relatedURL"] = response.selector.xpath("//div[@id='related-instructables']/ul/li[position()<5]/div/a/@href").extract()  
#       
        body_path = response.selector.xpath("//div[@id='main-content']")        
        item["descr"] = body_path.xpath(".//div[@class='txt step-body']/p/text()").extract()
        item["scripts"] = body_path.xpath(".//div[@class='txt step-body']/pre/text()").extract()
        item["comments"] = body_path.xpath(".//*[@class='txt comment-txt']//text()").extract()
        item["tools"]  = body_path.xpath(".//*[@id='instructable-steps']/div/div/table/tbody/tr/td/text()").extract()
#       item["Nimages"]  = scrapy.Field()
#       item["Nvideos"]  = scrapy.Field()
#       item["Nlink"]  = scrapy.Field()
#        yield item
               
   