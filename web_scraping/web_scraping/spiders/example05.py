import scrapy


class Example05(scrapy.Spider):
    name = "Example05"

    start_urls = [
        'https://scrapy.org/'
    ]

    def parse(self, response):
        yield {'headlineH3': response.css('h3::text').extract()}
        yield {'paragraphUnderFirstH3': response.css('div.block-01 p::text').extract()}
        yield {'allParagraphs': response.css('p::text').extract()}
        yield {'downloadLabel': response.css('li.first::text').extract()}
        yield {'mainLink': response.css('a#link-logo::attr(href)').extract()}
        yield {'allLinks': response.css('a::attr(href)').extract()}
        yield {'lastVersion': response.css('div.big-button div.download-stripe p::text').extract()}

