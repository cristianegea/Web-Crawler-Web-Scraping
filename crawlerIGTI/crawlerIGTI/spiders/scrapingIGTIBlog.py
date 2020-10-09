import scrapy

# importação dos itens
from crawlerIGTI.items import ScraperigtiItem

class ScrapingigtiblogSpider(scrapy.Spider):
    name = 'scrapingIGTIBlog'

    # allowed_domains = ['https://www.igti.com.br/blog/']
    # start_urls = ['http://https://www.igti.com.br/blog//']

    # método de inicialização
    def __init__(self):
        self.start_urls = ['http://https://www.igti.com.br/blog//']

    # Método parse => o parse coleta os dados da internet
    def parse(self, response):
        self.log('Acessando a URL: %s' % response.url)

        # criação de item a partir da classe de itens
        item = ScraperigtiItem()

        # extração do título da página
        item['titulo_pagina'] = response.css("title ::text").extract_first()

        # extração da url da página inicial
        item['url_pagina'] = response.url

        # busca as informações a respeito de cada artigo
        articles = response.xpath('//article')
        count_article = 0

        for article in articles:
            count_article += 1
            self.log('Artigo %s' % str(count_article))

            categories = article.xpath(".//div/div[@class = 'entry-category']//a")

            if len(categories) == 1:                # quando tiver exatamente 1 categoria
                item['categoria_artigo'] = ''.join(categories.xpath('text()').get())
                item['categoria_URL'] = ''.join(categories.xpath('@href').get())
            elif len(categories) > 1:               # quando tiver mais de 1 categoria
                item['categoria_artigo'] = []       # as categorias formaram uma lista
                item['categoria_URL'] = []
                i = 0

                while i < len(categories):
                    item['categoria_artigo'].append(''.join(categories.xpath('text()')[i].get()))
                    item['categoria_URL'].append(''.join(categories.xpath('@href')[i].get()))
                    item += 1

            title = article.xpath(".//h2[@class='entry-title h3']//a")

            item['titulo_artigo'] = ''.join(categories.xpath('text()').get())
            item['titulo_URL'] = ''.join(categories.xpath('@href').get())

            metadata = article.xpath(".//div/div[@class='entry-meta']")
            data = metadata.xpath(".//div[@class='meta-item meta-date']/span[@class='updated']")
            item['dtPostagem_artigo'] = ''.join(data.xpath('text()').get())

            comentario = metadata.xpath(".//div[@class='meta-item meta-comments']/span[@class='dsq-postid']")
            item['comentarios_artigo'] = ''.join(comentario.xpath('text()').get())

            visao = metadata.xpath(".//div[@class='meta-item meta-views']")
            item['visualizacoes_artigo'] = ''.join(visao.xpath('text()').get())

            yield item