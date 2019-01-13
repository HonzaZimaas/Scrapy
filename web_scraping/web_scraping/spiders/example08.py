import scrapy
from scrapy.loader import ItemLoader


class Example08(scrapy.Spider):
    name = "Example08"

    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        from web_scraping.web_scraping.items import WebScrapingItem
        loader = ItemLoader(item=WebScrapingItem, response=response)
        loader.add_css('text', 'span.text::text')
        loader.add_css('author', 'span small::text')
        loader.add_css('tags', 'div.tags a.tag::text')
        return loader.load_item()
