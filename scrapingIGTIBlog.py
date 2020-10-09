# Para executar utilize o terminal e execute um dos seguintes comandos:
# scrapy runspider scrapingIGTIBlog.py -t json -o artigos.json
# scrapy runspider scrapingIGTIBlog.py -t csv -o artigos.csv

import scrapy

# Definição dos itens aonde será realizado o scraping
class Items(scrapy.Item):
    # Para cada artigo da página
    categoria = scrapy.Field()
    categoriaUrl = scrapy.Field()
    titulo = scrapy.Field()
    url = scrapy.Field()
    dtPostagem = scrapy.Field()
    comentarios = scrapy.Field()
    visualizacoes = scrapy.Field()

class IGTIBlogSpider(scrapy.Spider):
    name = 'Scraping IGTI Blog'

    # Página alvo: https://www.igti.com.br/blog/

    # A classe é inicializada com a requisição HTTP
    def __init__(self):
        self.start_urls = ['https://www.igti.com.br/blog/']

    # O método 'start_requests' foi omitido

    def parse(self, response):
        # método para retornar o resultado da busca
        self.log('Acessando a URL: %s' % response.url)              # Mensagem do log de saída

        # Criação da variável "artigos" para leitura da estrutura "artigos" dentro da página principal
        artigos = response.xpath('//article')
        count = 0
        self.log('Total de artigos em destaque: %s' %str(len(response.css('article'))))     # registra o total de artigos em destaque
        # função "str" => transforma o valor numérico em string

        from artigo in artigos:         # 'artigo' é um elemento do vetor 'artigos'
            item = Items()
            count += 1

            categorias = artigo.xpath('.//div/div[@class = 'entry-category']//a')

            if len(categorias) == 1:        # o arigo só tem 1 categoria
                item['categoria'] = ''.join(categorias.xpath('text()').extract())
                item['categoriaURL'] = ''.join(categorias.xpath('@href').extract())
            else:
                cat = []
                carUrl = []
                for categoria in categorias:
                    cat.append(''.join(categorias.xpath('text()').extract()))
                    cat.append(', ')
                    cat.append(''.join(categorias.xpath('@href').extract()))
                item['categoria'] = ''.join(cat)
                item['categoriaURL'] = ''.join(carUrl)

            print('Categoria: ', item['categoria'])

            titulo = artigo.xpath('.//h2[@class = 'entry-title h3']//a')

            item['titulo'] = ''.join(titulo.xpath('text()').extract())
            item['url'] = ''.join(titulo.xpath('@href').extract())

            metadata = artigo.xpath('.//div/div[@class = 'entry-meta']')
            data = metadata.xpath('.//div/div[@class = 'entry-item meta-date']/span[@class= 'updated']')
            item['dtPostagem'] = ''.join(data, xpath('text()').get())

            comentario = metadata.xpath('.//div/div[@class = 'meta-item meta-comments']//a//span[@class = 'dsq-]')
            item['comentarios'] = ''.join(comentario, xpath('text()').get())

            visao = metadata.xpath('.//div/div[@class = 'meta-item meta-views']')
            item['visualizacoes'] = ''.join(comentario, xpath('text()').get())

            yield item          # gerador de objeto do tipo item

        self.log('Artigos raspados: %s' % str(count))
    
        self.log('Fim da raspagem')

