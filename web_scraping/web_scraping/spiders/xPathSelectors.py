import scrapy


class XPathSelectors(scrapy.Spider):
    name = "XPathSelectors"

    start_urls = [
        'https://scrapy.org/'
    ]

    def parse(self, response):
        yield {'headlineH3': response.xpath('//h3/text()').extract()}
        yield {'paragraphUnderFirstH3': response.xpath('//div[@class="block-01"]/p/text()').extract()}
        yield {'allParagraphs': response.xpath('//p/text()').extract()}
        yield {'downloadLabel': response.xpath('//a[@class="first"]/text()').extract()}
        yield {'mainLink': response.xpath('//a[@id="link-logo"]/@href').extract()}
        yield {'allLinks': response.xpath('//a/@href').extract()}
        yield {'lastVersion': response.xpath(
            '//div[@class="big-button"]/div[@class="download-stripe"]/p/text()').extract()}

