import scrapy


class Example01(scrapy.Spider):
    name = "Example01"

    start_urls = [
        'http://scrapy.org'
    ]

    def parse(self, response):
        filename = 'Example01_Scraping.html'

        with open(filename, 'wb') as f:
            f.write(response.body)
