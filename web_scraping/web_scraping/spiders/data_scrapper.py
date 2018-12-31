import scrapy


class DataScrapper(scrapy.Spider):
    name = "DataScrapper"
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('span small::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

        next_page = response.css('li.next a::attr(href)').extract_first()
        print(next_page)
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


