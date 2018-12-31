import scrapy


class DataScrapper(scrapy.Spider):
    name = "SeznamScrapper"
    start_urls = [
        'https://login.szn.cz/'
    ]

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'username': 'WebScrapper', 'password': 'Heslo123456*'},
            callback=self.after_login
        )

    def after_login(self, response):
        if "authentication failed" in str(response.body):
            self.logger.error("Login failed")
            return

        self.logger.info("Login succeed")
        yield scrapy.Request(url='https://seznam.cz', callback=self.scrapy_article)


    def scrapy_article(self,response):
        for article in response.css('div.timeline-article'):
            yield {
                'website': article.css('a.timeline-article__source-name.link.link--gadget-title::text').extract_first(),
                'websiteUrl': article.css(
                    'a.timeline-article__source-name.link.link--gadget-title::attr(href)').extract_first().split('?')[
                    0],
                'headline': article.css('a.link.link--show-visited.timeline-article__title::text').extract_first(),
                'headlineUrl': article.css(
                    'a.link.link--show-visited.timeline-article__title::attr(href)').extract_first().split('?')[0],
            }
