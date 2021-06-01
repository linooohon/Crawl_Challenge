# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlchallengeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ArticleItem(scrapy.Item):
    url = scrapy.Field()
    author = scrapy.Field()
    social_media = scrapy.Field()
