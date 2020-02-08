# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst


class SherdogFighterDescription(scrapy.Item):
    name = scrapy.Field(serializer=str)
    nickname = scrapy.Field()
    dob = scrapy.Field()
    height = scrapy.Field()
    wins_total = scrapy.Field()
    loses_total = scrapy.Field()
    draws_total = scrapy.Field()
    nc_total = scrapy.Field()
    affiliation = scrapy.Field()
    nationality = scrapy.Field()
    location_region = scrapy.Field()
    location_city = scrapy.Field()
    weight = scrapy.Field()
    wins_ko = scrapy.Field()
    wins_subs = scrapy.Field()
    wins_dec = scrapy.Field()
    wins_other = scrapy.Field()
    loses_ko = scrapy.Field()
    loses_subs = scrapy.Field()
    loses_dec = scrapy.Field()
    loses_other = scrapy.Field()

def dateDecoder(string):
    months = {'Jan': '01', 'Feb': '02', 'Mar': '03',
                'Apr': '04', 'May': '05', 'Jun': '06',
                'Jul': '07', 'Aug': '08', 'Sep': '09',
                'Oct': '10', 'Nov': '11', 'Dec': '12'}
    new_date = string.split('/')
    return '-'.join([new_date[2].strip(), months[new_date[0].strip()],new_date[1].strip()])

class SherdogFighterBout(scrapy.Item):
    result = scrapy.Field()
    opponent = scrapy.Field()
    event = scrapy.Field()
    date = scrapy.Field(
        input_processor = MapCompose(dateDecoder)
        )
    method = scrapy.Field()
    referee = scrapy.Field()
    roundn = scrapy.Field()
    time = scrapy.Field()
    dc_reason = scrapy.Field()