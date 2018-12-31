import scrapy


class WebScrapperTitle(scrapy.Spider):
    name = "WebScrapperTitle"

    start_urls = [
        'http://scrapy.org'
    ]

    def parse(self, response):
        filename = 'WebScrapperTitle.txt'
        title = response.xpath('//title/text()').extract_first()

        with open(filename, 'wt') as f:
            f.write(title)
