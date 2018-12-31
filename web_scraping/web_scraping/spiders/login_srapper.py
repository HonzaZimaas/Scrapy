import scrapy


class LoginScrapper(scrapy.Spider):
    name = 'LoginScrapper'

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
