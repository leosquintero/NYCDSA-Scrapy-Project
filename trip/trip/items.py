# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TripItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    reviews = scrapy.Field()
    price = scrapy.Field()
    cuisine = scrapy.Field()
    avg = scrapy.Field()
    rank = scrapy.Field()