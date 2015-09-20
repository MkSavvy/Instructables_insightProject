# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 12:16:20 2015

@author: Michel_home
"""

import scrapy

from DIYcontent.items import DiycontentItem

class contentSpider(scrapy.Spider):
    name = "diySpider"
    allowed_domains = ["instructables.com"]
    start_urls = [
        "http://www.instructables.com/id/Musical-RGB-Lamp/?ALLSTEPS", 
        "http://www.instructables.com/id/System-For-Automatically-Limiting-TV-Time/",
        "http://www.instructables.com/id/Raspberry-Pi-Based-Wireless-Microphone/"
    ]
    
    def parse(self, response):
        item = DiycontentItem()
        item["projectID"] = response.selector.xpath("")
        item["title"] = response.selector.xpath("")
#       item["author"]  = scrapy.Field()
#       item["date"]  = scrapy.Field()
#       item["keywords"]  = scrapy.Field()
#       item["award"]  = scrapy.Field()    
#       item[""] tags = scrapy.Field()
#       item[""]relatedURL = scrapy.Field()
#       item[""]descr = scrapy.Field()
#       item[""]comments = scrapy.Field()
#       item[""] tools = scrapy.Field()
#       item[""] Nsteps = scrapy.Field()
#       item[""] Nimages = scrapy.Field()
#       item[""] Nvideos = scrapy.Field()
#       item[""] Nlink = scrapy.Field()
#        yield item
               
   