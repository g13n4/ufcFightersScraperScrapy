# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from ufcFightersScraper.items import SherdogFighterBout, SherdogFighterDescription

shr_site = "https://www.sherdog.com"

class SherdogSpider(scrapy.Spider):
    name = 'sherdog'
    allowed_domains = ['sherdog.com']
    start_urls = ["https://www.sherdog.com/organizations/Ultimate-Fighting-Championship-UFC-2/recent-events/1"]

    def parse(self, response):
        for event in response.css("div#recent_tab table.event").xpath('tr[@onclick]//a'):
            yield scrapy.Request(url=shr_site + event.attrib['href'], callable=self.parse_event)
            #yield {event.css('span::text').get():shr_site + event.attrib['href']}
        for footer in response.css('span.pagination a'):
            if "Older" in footer.css('a::text').get():
                yield response.follow(shr_site + footer.attrib['href'], self.parse)    
    
    def parse_event(self, response):
        to_parse_fighters_page = lambda elem: response.follow(shr_site + elem.attrib['href'], self.parse_fighters_page)
        for main_event_fighter in response.css('div.module.fight_card div.fighter>a'):
            yield to_parse_fighters_page(main_event_fighter)
        for other_fighter in response.css("div.module.event_match a[href^='/fighter/']"):
            yield to_parse_fighters_page(other_fighter)

    def parse_fighters_page(self,response):
        fighter_loader = ItemLoader(item=SherdogFighterDescription(), response=response)
        fighter_loader.add_xpath('name', '//h1/span[@class="fn"]/text()')
        fighter_loader.add_xpath('nickname', '//h1/span[@class="nickname"]/em/text()')
        fighter_loader.add_css('dob', "div.bio span.birthday span::text") 
        fighter_loader.add_css('height', 'div.bio span.height::text') #need to be processed
        fighter_loader.add_css('weight', 'div.bio span.weight::text') #need to be processed
        fighter_loader.add_css('nationality', 'div.bio span.item.birthplace strong::text')
        fighter_loader.add_css('affiliation', 'div.size_info strong a.association span::text')
        
        _ = response.css('div.bio span.adr span::text').get()
        fighter_loader.add_value('location_city', _[0])
        fighter_loader.add_value('location_region', _[1] if len(_) > 2 else '')
        
        _ = 
        fighter_loader.add_xpath('wins_total', )
        fighter_loader.add_xpath('loses_total', )
        fighter_loader.add_xpath('draws_total', )
        fighter_loader.add_xpath('nc_total', )
        
        _ = response.css('div.left_side div:first-child span.graph_tag')  
        fighter_loader.add_xpath('wins_ko', )
        fighter_loader.add_xpath('wins_subs', )
        fighter_loader.add_xpath('wins_dec', )
        fighter_loader.add_xpath('wins_other', )
        _ = response.css('div.left_side div:last-child span.graph_tag')  
        fighter_loader.add_xpath('loses_ko', )
        fighter_loader.add_xpath('loses_subs', )
        fighter_loader.add_xpath('loses_dec', )
        fighter_loader.add_xpath('loses_other', )

        