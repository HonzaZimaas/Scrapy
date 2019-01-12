import scrapy


class Example02(scrapy.Spider):
    name = "Example02"

    start_urls = [
        'http://scrapy.org'
    ]

    def parse(self, response):
        filename = 'Example02_ScrapingTitle.txt'
        title = response.xpath('//title/text()').extract_first()

        with open(filename, 'wt') as f:
            f.write(title)
