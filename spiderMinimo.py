import scrapy

# Criação da classe com o menor nível de spider possível
class SpiderMinimo1(scrapy.Spider):
    """Scrapy spider minimo"""
    name = 'mínimo'

# Executar no terminal o seguinte comando: scrapy runspider spiderMinimo1.py

# Criação da classe com requisições HTTP
class SpiderMinimo2(scrapy.Spider):
    """Scrapy spider minimo"""
    name = 'mínimo'

    def start_requests(self):
        # método 'start_requests' => responsável por iniciar a requisição HTTP
        url = 'https://www.igti.com.br/blog/'       # URL para o crawler ou para o scraping
        return[scrapy.Request(url)]

    def parse(self, response):
        # método para retornar o resultado da busca
        self.log('Acessando a URL: %s' % response.url)

# Executar no terminal o seguinte comando: scrapy runspider spiderMinimo2.py

# Criação da classe com requisições HTTP
class SpiderMinimo(scrapy.Spider):
    """Scrapy spider minimo"""
    name = 'mínimo'

    # Se não for necessária a realização de alguma modificação no método 'start_reques' é possível não defini-lo no script, o Python assumirá que este é o método padrão dentro do framework

    start_urls = ['https://www.igti.com.br/blog/']

    def parse(self, response):
        # método para retornar o resultado da busca
        self.log('Acessando a URL: %s' % response.url)

# Executar no terminal o seguinte comando: scrapy runspider spiderMinimo.py


