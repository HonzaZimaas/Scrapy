import scrapy


class Example04(scrapy.Spider):
    name = "Example04"
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        list_quotes = response.css('div.quote')
        for quote in list_quotes:
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('span small::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

        next_page = response.css('li.next a::attr(href)').extract_first()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
