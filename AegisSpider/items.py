# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AegisspiderItem(scrapy.Item):
    # define the fields for your item here like:
    question = scrapy.Field()
    standardanswer = scrapy.Field()
    laws = scrapy.Field()
    answer = scrapy.Field()
    content = scrapy.Field()


class AegisrelatedItem(scrapy.Item):
    sim_que = scrapy.Field()
    content = scrapy.Field()
