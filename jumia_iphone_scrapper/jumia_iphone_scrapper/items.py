# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
class JumiascraperItem(scrapy.Item):
# define the fields for your item here like:
    phone_name = scrapy.Field()
    phone_price = scrapy.Field()
    units_left = scrapy.Field()
    delivery_type = scrapy.Field()
    verified_ratings = scrapy.Field()
    seller_name = scrapy.Field()
    seller_score = scrapy.Field()
    seller_followers = scrapy.Field()
    seller_shipping_speed = scrapy.Field()
    seller_quality_score = scrapy.Field()
    seller_customer_rating = scrapy.Field()