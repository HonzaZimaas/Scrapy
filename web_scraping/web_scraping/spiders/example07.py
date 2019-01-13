import scrapy


class Example07(scrapy.Spider):
    name = 'Example07'

    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'username': 'john', 'password': 'secret'},
            callback=self.after_login
        )

    def after_login(self, response):
        if "authentication failed" in str(response.body):
            self.logger.error("Login failed")
            return
        self.logger.info("Login succeed")

        list_quotes = response.css('div.quote')
        for quote in list_quotes:
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('span small::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
