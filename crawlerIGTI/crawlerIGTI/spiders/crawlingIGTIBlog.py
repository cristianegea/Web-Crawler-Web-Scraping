import scrapy

from crawlerIGTI.items import CrawlerigtiItem

class CrawlingigtiblogSpider(scrapy.Spider):
    name = 'crawlingIGTIBlog'

    # allowed_domains = ['https://www.igti.com.br/blog/']
    start_urls = ['http://https://www.igti.com.br/blog//']

    def parse(self, response):
        self.log('Acessando a URL: %s' % response.url)

        # busca de todas as categorias
        categories = response.xpath("//nav[@class='gridlove-main-navgation']//li//a")

        # criação do item
        item = CrawlerigtiItem()

        for category in categories:
            url = category.xpath('@href').extract.first()       # extração da 1ª url para fazer o crawler, a navegação
            self.log('Categorias %s' % category.xpath('text()').extract_first())

            yield response.follow(url, self.parse_category)
            # o 1º parse somente coletou os dados básicos

        # coleta dos dados
        item['titulo_pagina'] = response.css['title ::text'].extract_first()
        item['url_pagina'] = response.url
        item['categoria'] = 'HOME'      # indicação que é a página inicial

        yield item

    # criação de um parse para as páginas específicas
    def _parse(self, response):
        self.log('Acessando a URL: %s' % response.url)
        item = CrawlerigtiItem()

        item['titulo_pagina'] = response.css['title ::text'].extract_first()
        item['url_pagina'] = response.url
        item['categoria'] = response.xpath("//h1[@class='h2']/text()").extract_first()

        yield item

