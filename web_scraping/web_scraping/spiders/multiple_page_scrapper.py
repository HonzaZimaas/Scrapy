import scrapy


class MultiplePageScrapper(scrapy.Spider):
    name = "MultiplePageScrapper"

    allowed_domains = ['https://scrapy.org']

    def start_requests(self):
        urls = [
            'https://scrapy.org',
            'https://scrapy.org/download/',
            'https://scrapy.org/community/',
            'https://scrapy.org/resources/',
            'https://example.com'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        title = response.selector.xpath('//title/text()').extract_first()

        filename = 'MultiplePageScrapper.txt'
        with open(filename, 'at') as f:
            f.write(title + '\n')
