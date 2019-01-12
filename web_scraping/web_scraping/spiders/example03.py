import scrapy


class Example03(scrapy.Spider):
    name = "Example03"

    allowed_domains = ['https://scrapy.org']

    def start_requests(self):
        urls = [
            'https://scrapy.org',
            'https://scrapy.org/download/',
            'https://scrapy.org/community/',
            'https://scrapy.org/resources/',
            'https://example.com/',
            'https://scrapy.org/resources/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        title = response.selector.xpath('//title/text()').extract_first()

        filename = 'Example03_ScrapingTitles.txt'
        with open(filename, 'at') as f:
            f.write(title + '\n')
