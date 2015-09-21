# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DiycontentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    projectID = scrapy.Field()
    title = scrapy.Field()    
    author = scrapy.Field()
    views = scrapy.Field()
    date = scrapy.Field()
    keywords = scrapy.Field()
    award = scrapy.Field()    
    tags = scrapy.Field()
    relatedURL = scrapy.Field()
    descr = scrapy.Field()
    contentExtra = scrapy.Field()
    scripts = scrapy.Field()
    comments = scrapy.Field()
    tools = scrapy.Field()
    Nsteps = scrapy.Field()
    Nimages = scrapy.Field()
    Nvideos = scrapy.Field()
    Nlinks = scrapy.Field()
    pass
