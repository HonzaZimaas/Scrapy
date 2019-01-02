import scrapy


class SeznamScrapper(scrapy.Spider):
    name = "SeznamScrapper"

    start_urls = ['https://seznam.cz/']

    allowed_domains = ['https://seznam.cz/']

    def parse(self, response):
        self.save_document_object_model(response)

        articles = response.css('div.timeline-article')

        for article in articles:
            yield {
                'website': article.css('a.timeline-article__source-name.link.link--gadget-title::text').extract_first(),
                'websiteUrl': article.css(
                    'a.timeline-article__source-name.link.link--gadget-title::attr(href)').extract_first().split('?')[
                    0],
                'headline': article.css('a.link.link--show-visited.timeline-article__title::text').extract_first(),
                'headlineUrl': article.css(
                    'a.link.link--show-visited.timeline-article__title::attr(href)').extract_first().split('?')[0],
                "countOfLikes": article.css('span.timeline-article-footer__vote-count::text').extract()[1]
            }
            self.logger.info('%s articles was scrapped', len(articles))

    def save_document_object_model(self, response):
        file_name = self.name + '.html'
        with open(file_name, 'wb') as file:
            file.write(response.body)
            self.logger.info('File %s was saved', file_name)
