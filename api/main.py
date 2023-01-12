import json
import os
import re
import unicodedata
from time import sleep

import chromedriver_autoinstaller
import schedule
from bs4 import BeautifulSoup
# Firefox & Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By


class Main:
    def livelo(self):
        self.driver.get(
            'https://www.livelo.com.br/ganhe-pontos-compre-e-pontue')
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        cards = soup.find_all('div', {'class': 'parity__card'})
        while len(cards) == 0:
            sleep(1)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            cards = soup.find_all('div', {'class': 'parity__card'})
        for card in cards:
            nome = card.find(
                'img', {'class': 'parity__card--img'}).attrs.get('alt')
            valor = ''
            pontos = card.find(
                'span', {'data-bind': 'text: $data.parity'}).text
            real = card.find('span', {'data-bind': 'text: $data.value'}).text

            valor = 'Até ' + pontos + ' pontos por R$' + real

            url = card.find(
                'a', {'class': 'button__knowmore--link gtm-link-event'}).attrs.get('href')
            img = 'https://www.livelo.com.br' + \
                card.find(
                    'img', {'class': 'parity__card--img'}).attrs.get('src')
            if nome in self.dicionario:
                self.dicionario[nome]['valor']['livelo'] = valor
                self.dicionario[nome]['url']['livelo'] = url
                self.dicionario[nome]['nLojas'] += 15
            else:
                self.dicionario[nome] = {
                    'nome': nome,
                    'img': img,
                    'nLojas': 15,
                    'valor': {'livelo': valor,
                              'smiles': '',
                              'curteai': '',
                              'latampass': '',
                              'esfera': ''},
                    'url': {'livelo': url,
                            'smiles': '',
                            'curteai': '',
                            'latampass': '',
                            'esfera': ''}
                }

    def esfera(self):
        self.driver.get(
            'https://www.esfera.com.vc/c/junte-pontos/junte-pontos/esf02163#page=8')
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        cards = soup.find_all('div', {
            'class': 'col-xs-6 col-sm-3 col-lg-2 PartnerShopv2List-partners__marginPartners'})
        while len(cards) == 0:
            sleep(1)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            cards = soup.find_all('div', {
                'class': 'col-xs-6 col-sm-3 col-lg-2 PartnerShopv2List-partners__marginPartners'})

        for card in cards:
            nome = card.find('div', {'class': '-partnerName'}).text
            img = 'https://www.esfera.com.vc' + \
                card.find('img').attrs.get('src')
            url = 'https://www.esfera.com.vc' + \
                card.find('a').attrs.get('href')
            points = card.find(
                'div', {'class': '-partnerPoints'}).find_all('span')
            condicao = card.find(
                'div', {'class': 'textPoints'}).text + ' '
            valor = points[0].text + " " + points[1].text + " " + condicao
            valor = valor.replace('  ', ' ').replace('a cada dolar', '= U$1').replace(
                'a cada real', '= R$1').removesuffix(' ')
            if nome in self.dicionario:
                self.dicionario[nome]['valor']['esfera'] = valor
                self.dicionario[nome]['url']['esfera'] = url
                self.dicionario[nome]['nLojas'] += 11
            else:
                self.dicionario[nome] = {
                    'nome': nome,
                    'img': img,
                    'nLojas': 11,
                    'valor': {'livelo': '',
                              'smiles': '',
                              'curteai': '',
                              'latampass': '',
                              'esfera': valor
                              },
                    'url': {'livelo': '',
                            'smiles': '',
                            'curteai': '',
                            'latampass': '',
                            'esfera': url
                            }
                }

    def latampass(self):
        self.driver.get(
            'https://latampass.latam.com/pt_br/junte-pontos/parceiros')
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        cards = soup.find_all('div', {
            'class': 'item bancos col-md-3 name '})
        while len(cards) == 0:
            sleep(1)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            cards = soup.find_all(
                'div', {'class': 'item bancos col-md-3 name'})
        for card in cards:
            nome = card.find(
                'span', {'class': 'sistema-de-busca'}).text.strip()
            img = card.find('img').attrs.get('src')
            url = 'https://latampass.latam.com/pt_br/junte-pontos/' + nome.lower().replace(' ','-')
                    #card.find('a').attrs.get('href')
            texto = card.find('p', {'class': 'sc-furwcr jxGPMc'}).text
            # valor = texto.replace('em comprasGanhe', '=').replace(' LATAM Pass', '').replace('dólar em hospedagem', 'dolar').replace(
            #    'em diariaGanhe', '=').replace('em compras  Ganhe até', '=').replace('R$ ', 'R$').replace('até', '=').replace('em serviçosGanhe', '=').replace('')
            if len(re.findall('[0-9]', texto)) > 0:
                valor = 'R$ ' + \
                    re.findall('[0-9]', texto)[0] + ' = ' + \
                    re.findall('[0-9]', texto)[1] + ' pontos Latam Pass'
            else:
                valor = texto
            if len(re.findall('dólar', texto)) > 0:
                valor = 'U$ ' + \
                    re.findall('[0-9]', texto)[0] + ' = ' + \
                    re.findall('[0-9]', texto)[1] + ' pontos Latam Pass'
            if nome in self.dicionario:
                self.dicionario[nome]['valor']['latampass'] = valor
                self.dicionario[nome]['url']['latampass'] = url
                self.dicionario[nome]['nLojas'] += 12
            else:
                self.dicionario[nome] = {
                    'nome': nome,
                    'img': img,
                    'nLojas': 12,
                    'valor': {'livelo': '',
                              'smiles': '',
                              'curteai': '',
                              'latampass': valor,
                              'esfera': ''
                              },
                    'url': {'livelo': '',
                            'smiles': '',
                            'curteai': '',
                            'latampass': url,
                            'esfera': ''
                            }
                }

    def curteai(self):
        urls = ["https://curtai.com.br/ganhe-pontos/fornecedor/polishop?modalidade=ac&produtoHome=false&relevancia=PRECO_FORNECEDOR_DESC&page=1",
                "https://curtai.com.br/ganhe-pontos/fornecedor/casasbahia?modalidade=ac&produtoHome=false&relevancia=PRECO_FORNECEDOR_DESC&page=1",
                "https://curtai.com.br/ganhe-pontos/fornecedor/pontofrio?modalidade=ac&produtoHome=false&relevancia=PRECO_FORNECEDOR_DESC&page=1",
                "https://curtai.com.br/ganhe-pontos/fornecedor/extra?modalidade=ac&produtoHome=false&relevancia=PRECO_FORNECEDOR_DESC&page=1",
                "https://curtai.com.br/ganhe-pontos/fornecedor/fastshop?modalidade=ac&produtoHome=false&relevancia=PRECO_FORNECEDOR_DESC&page=1",
                "https://curtai.com.br/ganhe-pontos/fornecedor/magazineluiza?modalidade=ac&produtoHome=false&relevancia=PRECO_FORNECEDOR_DESC&page=1"]
        for url in urls:
            self.driver.get(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            cards = soup.find_all('mkt-produto-card-pointed',
                                  {'class': 'ng-star-inserted'})
            while len(cards) == 0:
                sleep(1)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                cards = soup.find_all('mkt-produto-card-pointed',
                                      {'class': 'ng-star-inserted'})
            for card in cards:
                nome = card.find('lib-dynamically-img',
                                 {'class', 'logo-fornecedor'}).a.img.attrs.get('alt')
                if nome == 'Ponto Frio':
                    nome = 'Ponto'
                valor = card.find(
                    'span', {'class': 'ng-star-inserted'}).text.removeprefix(' ').removesuffix(' ').replace(' pts', '').replace('.', '')
                valor = 'Até ' + valor + ' pontos'
                img = card.find('img', {'class', 'img-fluid'}).attrs.get('src')
                if nome in self.dicionario:
                    if self.dicionario[nome]['valor']['curteai'] == '':
                        self.dicionario[nome]['valor']['curteai'] = valor
                        self.dicionario[nome]['url']['curteai'] = url
                        self.dicionario[nome]['nLojas'] += 13
                    elif int(valor.removeprefix('Até ').removesuffix(' pontos')) > int(self.dicionario[nome]['valor']['curteai'].removeprefix('Até ').removesuffix(' pontos')):
                        self.dicionario[nome]['valor']['curteai'] = valor
                        self.dicionario[nome]['url']['curteai'] = url
                        self.dicionario[nome]['nLojas'] += 13
                else:
                    self.dicionario[nome] = {
                        'nome': nome,
                        'img': img,
                        'nLojas': 13,
                        'valor': {'livelo': '',
                                  'smiles': '',
                                  'curteai': valor,
                                  'latampass': '',
                                  'esfera': ''
                                  },
                        'url': {'livelo': '',
                                'smiles': '',
                                'curteai': url,
                                'latampass': '',
                                'esfera': ''
                                }
                    }

    def smiles(self):
        urls = ["https://www.shoppingsmiles.com.br/smiles/fornecedor.jsf?f=85&n=renner&o=PRECO_FORNECEDOR_DESC",
                "https://www.shoppingsmiles.com.br/smiles/fornecedor.jsf?f=57&n=polishop&o=PRECO_FORNECEDOR_DESC",
                "https://www.shoppingsmiles.com.br/smiles/fornecedor.jsf?f=7&n=casas-bahia&o=PRECO_FORNECEDOR_DESC",
                "https://www.shoppingsmiles.com.br/smiles/fornecedor.jsf?f=73&n=zattini&o=PRECO_FORNECEDOR_DESC",
                "https://www.shoppingsmiles.com.br/smiles/fornecedor.jsf?f=72&n=netshoes&o=PRECO_FORNECEDOR_DESC",
                "https://www.shoppingsmiles.com.br/smiles/fornecedor.jsf?f=58&n=topstore&o=PRECO_FORNECEDOR_DESC",
                "https://www.shoppingsmiles.com.br/smiles/fornecedor.jsf?f=3&n=extra&o=PRECO_FORNECEDOR_DESC",
                "https://www.shoppingsmiles.com.br/smiles/fornecedor.jsf?f=4&n=ponto-frio&o=PRECO_FORNECEDOR_DESC",
                "https://www.shoppingsmiles.com.br/smiles/fornecedor.jsf?f=76&n=camicado&o=PRECO_FORNECEDOR_DESC",
                "https://www.shoppingsmiles.com.br/smiles/fornecedor.jsf?f=81&n=luxury-loyalty&o=PRECO_FORNECEDOR_DESC",
                "https://www.shoppingsmiles.com.br/smiles/fornecedor.jsf?f=8&n=magazine-luiza&o=PRECO_FORNECEDOR_DESC",
                "https://www.shoppingsmiles.com.br/smiles/fornecedor.jsf?f=35&n=fast-shop&o=PRECO_FORNECEDOR_DESC",
                ]
        for url in urls:
            self.driver.get(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            cards = soup.find_all('span', {'class': 'box-produto'})
            while len(cards) == 0:
                sleep(1)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                cards = soup.find_all('span', {'class': 'box-produto'})

            for card in cards:
                nome = soup.findAll(
                    'a', {'class', 'ui-link ui-widget'})[-1].text
                if nome == 'Ponto Frio':
                    nome = 'Ponto'
                valor = 'Até ' + re.sub('[^0-9]', '', card.find(
                    'span', {'class': 'clube-subsection'}).text) + ' pontos'
                img = soup.find(
                    'img', {'class', 'fornecedor-logo'}).attrs.get('src')

                if nome in self.dicionario:
                    if self.dicionario[nome]['valor']['smiles'] == '':
                        self.dicionario[nome]['valor']['smiles'] = valor
                        self.dicionario[nome]['url']['smiles'] = url
                        self.dicionario[nome]['nLojas'] += 14
                    elif int(valor.removeprefix('Até ').removesuffix(' pontos')) > int(self.dicionario[nome]['valor']['smiles'].removeprefix('Até ').removesuffix(' pontos')):
                        self.dicionario[nome]['valor']['smiles'] = valor
                        self.dicionario[nome]['url']['smiles'] = url
                        self.dicionario[nome]['nLojas'] += 14
                else:
                    self.dicionario[nome] = {
                        'nome': nome,
                        'img': img,
                        'nLojas': 14,
                        'valor': {'livelo': '',
                                  'smiles': valor,
                                  'curteai': '',
                                  'latampass': '',
                                  'esfera': ''
                                  },
                        'url': {'livelo': '',
                                'smiles': url,
                                'curteai': '',
                                'latampass': '',
                                'esfera': ''
                                }
                    }

    def melhor(self):
        print('melhor')

    def toFile(self):
        json_object = json.dumps(
            list(self.dicionario.values()), ensure_ascii=False)

        filePath = os.path.split(os.path.abspath(""))[
            0] + "/default/src/assets/data/data.json"
        with open(filePath, "w", encoding='utf-8') as outfile:
            outfile.write(json_object)

        print('escrito no arquivo')

    def __init__(self, json_object, dicionario, driver):
        self.json_object = json_object
        self.dicionario = dicionario
        self.driver = driver
        schedule.every(10).seconds.do(self.livelo)
        schedule.every(10).seconds.do(self.smiles)
        schedule.every(10).seconds.do(self.curteai)
        schedule.every(10).seconds.do(self.latampass)
        schedule.every(10).seconds.do(self.esfera)
        # schedule.every(10).seconds.do(self.melhor)
        schedule.every(10).seconds.do(self.toFile)


if __name__ == '__main__':
    chromedriver_autoinstaller.install()
    json_object = ""
    b = 1
    dicionario = {}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("start-manimized")
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    a = Main(json_object, dicionario, driver)
    while True:
        schedule.run_pending()
        sleep(schedule.idle_seconds() if schedule.idle_seconds() > 0 else 0)
