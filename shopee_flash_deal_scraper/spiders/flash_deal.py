# -*- coding: utf-8 -*-
import scrapy
from ..items import ShopeeFlashDealScraperItem

class FlashDealSpider(scrapy.Spider):
    name = 'flashdeal'
    start_urls = ['http://shopee.ph/']

    def parse(self, response):
        items = ShopeeFlashDealScraperItem()
        
        image = response.css('.flash-sale-item-card__animated-image::attr(style)').extract()
        price = response.css('.item-price-number').css('::text').extract()
        discount = response.css('.shopee-item-card__badge-wrapper .percent').css('::text').extract()
        
        items['image'] = image
        items['price'] = price
        items['discount'] = discount
                
        yield items
        