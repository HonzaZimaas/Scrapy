import scrapy


class Example10(scrapy.Spider):
    name = "Example10"
    start_urls = ['https://nakup.itesco.cz/groceries/cs-CZ/shop/napoje/all?page=1']
    allowed_domains = ['https://nakup.itesco.cz/groceries/']

    def parse(self, response):
        page_number = response.url.split("=")[1]
        self.logger.info("Scraping page number: %s", page_number)

        products = response.css('li.product-list--list-item')

        for product in products:
            value = product.css('span.value::text')[1].extract()
            currency = product.css('span.currency::text')[1].extract()
            weight = product.css('span.weight::text').extract_first()

            product_values = (value, currency, weight)

            yield {
                'productName': product.css('a.product-tile--title.product-tile--browsable::text').extract(),
                'productPrice': product.css('span.value::text')[0].extract(),
                'productUnit': product.css('span.currency::text')[0].extract(),
                'productPriceForUnit': product_values
            }

        if response.url == 'https://nakup.itesco.cz/groceries/cs-CZ/shop/napoje/all?page=1':
            next_page = response.css('a.pagination--button.prev-next::attr(href)').extract_first()
        else:
            next_page = response.css('a.pagination--button.prev-next::attr(href)')[1].extract()

        if next_page is not None:
            self.logger.info("Moving to next Page")
            yield response.follow(next_page, callback=self.parse, dont_filter=True)
        else:
            self.logger.info("There is no other Page")
