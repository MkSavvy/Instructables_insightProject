# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 12:16:20 2015

@author: Michel_home
"""

import scrapy

from DIYcontent.items import DiycontentItem
import json

class contentSpider(scrapy.Spider):
    name = "diycontent"
    allowed_domains = ["instructables.com"]
    
    
    def _url_add_ALLSTEPS(fileh):
        with open(fileh,'rb') as f:
            middle = json.load(f)
            base = "http://www.instructables.com"
            end = "?ALLSTEPS"
            for mid in middle:
                full_url = base + mid["projectURL"][0] + end
                yield full_url
                
                
    start_urls = [url for url in _url_add_ALLSTEPS('../projlist0.json')]
            
            
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
        item["award"]  = response.selector.xpath("//*[@id='ible-awards-bar']/meta[@itemprop='award']/@content").extract()   
        item["relatedURL"] = response.selector.xpath("//div[@id='related-instructables']/ul/li[position()<5]/div/a/@href").extract()  
#       
        body_path = response.selector.xpath("//div[@id='main-content']")        
        item["descr"] = body_path.xpath(".//div[@class='txt step-body']/p/text()").extract()
        item["scripts"] = body_path.xpath(".//div[@class='txt step-body']/pre/text()").extract()
        item["comments"] = body_path.xpath(".//*[@class='txt comment-txt']//text()").extract()
#        item["tools"]  = body_path.xpath(".//*[@id='instructable-steps']/div/div/table/tbody/tr/td/text()").extract()
        item["Nimages"] = body_path.xpath(".//div[@class='photoset']//a/div[@class='photo-container']/img/@src").extract()
        item["Nvideos"] = body_path.xpath(".//div[@class='video-container']").extract()  # will want len() of this list
        item["contentExtra"] = response.selector.xpath("//div[@class='step-container ']//div[@class='entryExtra']/a/span/text()").extract()
        item["Nlinks"] = body_path.xpath(".//div[@id='instructable-steps']/div/div/p/a/@href").extract()
        yield item
               
   