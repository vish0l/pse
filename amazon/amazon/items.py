# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    product_name=scrapy.Field()
    #subname of the product like black,white or 8gb , 1gb etc
    product_tag=scrapy.Field()
    product_url=scrapy.Field()
    product_price=scrapy.Field()
    product_specs=scrapy.Field()
    product_desc=scrapy.Field()
    product_pmode=scrapy.Field()