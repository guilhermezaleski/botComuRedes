#coding: UTF-8

from bs4 import BeautifulSoup
import urllib.request as url

import re

site = 'http://tempo.clic.com.br/'
cidade = input('Forneça o nome da cidade: ')
estado = input('Forneça a sigla do estado: ')

#Remove os espaços que possam existir em um nome de cidade composto
cidade = cidade.replace(' ' , '')

#Aborta a execução caso a sigla do estado tenha mais de dois caracteres

if len(estado) != 2:
   print ('\nA sigla do estado deve ter duas letras!\n')
   exit(1)

#Formata a URL da cidade, garantindo que as siglas do estado serão maiúsculas
url2 = site + estado + '/' + cidade.replace(' ','')



print (' > Conectando-se a %s...' % url2)

#Estabelece a conexão, com timeout de 5 segundos
con = url.urlopen(url2 , None , 5)

print (' > Conexão estabelecida. Obtendo código HTML...')

#Obtém o código HTML
HTML = con.read()



print (' > Filtrando informações...\n')


soup = BeautifulSoup(HTML)
temperatura = re.search(r'[0-9]{2}' , str(soup.find('span', attrs={'class':'temperature_now'})))
atualizado = re.search(r'Atualizado às .*[0-9]' , str(soup.find('span', attrs={'class':'updateTime'})))

print ('*** CONDIÇÃO CLIMÁTICA EM %s - %s ***' % (cidade.upper() , estado.upper()))
print (temperatura.group(0) + 'º')
print (atualizado.group(0) ,'\n')

