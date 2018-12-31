# import scrapy
# from scrapy.loader import ItemLoader
#
# from web_scraping.web_scraping.items import WebScrapingItem
#
#
# class ItemScrapper(scrapy.Spider):
#     name = "itemScrapper"
#
#     start_urls = [
#         'http://quotes.toscrape.com/'
#     ]
#
#     def parse(self, response):
#         loader = ItemLoader(item=WebScrapingItem(), response=response)
#         loader.add_css('text', 'span.text::text')
#         loader.add_css('author', 'span small::text')
#         loader.add_css('tags', 'div.tags a.tag::text')
#         return loader.load_item()
#
#     from scrapy.spiders import XMLFeedSpider
#     # from myproject.items import TestItem
#     #
#     # class MySpider(XMLFeedSpider):
#     #     name = 'example.com'
#     #     allowed_domains = ['example.com']
#     #     start_urls = ['http://www.example.com/feed.xml']
#     #     iterator = 'iternodes'  # This is actually unnecessary, since it's the default value
#     #     itertag = 'item'
#     #
#     #     def parse_node(self, response, node):
#     #         self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.extract()))
#     #
#     #         item = TestItem()
#     #         item['id'] = node.xpath('@id').extract()
#     #         item['name'] = node.xpath('name').extract()
#     #         item['description'] = node.xpath('description').extract()
#     #         return item
