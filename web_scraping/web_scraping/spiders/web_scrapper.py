import scrapy


class WebScrapper(scrapy.Spider):
    name = "WebScrapper"

    start_urls = [
        'http://scrapy.org'
    ]

    def parse(self, response):
        filename = 'WebScrapper.html'

        with open(filename, 'wb') as f:
            f.write(response.body)


