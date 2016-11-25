#coding: UTF-8

from bs4 import BeautifulSoup
import urllib.request as url

import re

site = 'https://www.dicio.com.br/'
cidade = input('Forneça o nome da cidade: ')


#Remove os espaços que possam existir em um nome de cidade composto



#Formata a URL da cidade, garantindo que as siglas do estado serão maiúsculas
url2 = site  + cidade.replace(' ','')



print (' > Conectando-se a %s...' % url2)

#Estabelece a conexão, com timeout de 5 segundos
con = url.urlopen(url2 , None , 5)

print (' > Conexão estabelecida. Obtendo código HTML...')

#Obtém o código HTML
HTML = con.read()



print (' > Filtrando informações...\n')


soup = BeautifulSoup(HTML)
#temperatura = re.search(r'[0-9]{2}' , str(soup.find('p', attrs={'id':'significado'})))
temperatura = str(soup.find('p', attrs={'id':'significado'}))
#atualizado = re.search(r'Atualizado às .*[0-9]' , str(soup.find('span', attrs={'class':'updateTime'})))


idxInicio = temperatura.find('</span>')
idxInicio += 13
idxFinal = temperatura.find('</span>', idxInicio)

temperatura = temperatura[idxInicio:idxFinal]

print ('*** Significado de  %s ***' % (cidade.upper()))
print (temperatura)
#print (atualizado.group(0) ,'\n')

