import scrapy
from scrapy.loader import ItemLoader

from web_scraping.web_scraping.items import WebScrapingItem


class ItemScrapper(scrapy.Spider):
    name = "itemScrapper"

    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        loader = ItemLoader(item=WebScrapingItem, response=response)
        loader.add_css('text', 'span.text::text')
        loader.add_css('author', 'span small::text')
        loader.add_css('tags', 'div.tags a.tag::text')
        return loader.load_item()

