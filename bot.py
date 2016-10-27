#coding: UTF-8

import requests
import json
import urllib as url
import re

site = 'http://tempoagora.uol.com.br/previsaodotempo.html/brasil/'
cidade = input('Forneça o nome da cidade: ')
estado = input('Forneça a sigla do estado: ')

#Remove os espaços que possam existir em um nome de cidade composto
cidade = cidade.replace(' ' , '')

#Aborta a execução caso a sigla do estado tenha mais de dois caracteres

if len(estado) != 2:
   print ('\nA sigla do estado deve ter duas letras!\n')
   exit(1)

#Formata a URL da cidade, garantindo que as siglas do estado serão maiúsculas
url2 = site + cidade + '-' + estado.upper()



print (' > Conectando-se a %s...' % url2)

#Estabelece a conexão, com timeout de 5 segundos
con = url.request(url2 , None , 5)

print (' > Conexão estabelecida. Obtendo código HTML...')

#Obtém o código HTML
HTML = con.read()



print (' > Filtrando informações...\n')

#Valida a página buscando o padrão "cidade - estado", que só é exibido em páginas válidas
#EXEMPLO HTML: Barbacena - MG
if re.search(r'[A-Z][^-]+- [A-Z]{2}' , HTML) == None:
   print ('Cidade inválida!\n')
   exit(1)

#Busca a condição climática, que é informada entre os fragmentos de tags %;\"> e <
#EXEMPLO HTML: <div style="float:left; width:450px; height:100%;">Predomínio de sol, apenas com pouca variação de nuvens</div>
status = re.search(r'%;\">(.*?)<' , HTML)

#Obtém a data e a hora da última atualização
#EXEMPLO HTML: <p>Atualizado em: 14/09/2009 @ 20:30:00</p>
atualizado = re.search(r'Atualizado em: .*[0-9]' , HTML)

print ('*** CONDIÇÃO CLIMÁTICA EM %s - %s ***' % (cidade.upper() , estado.upper()))
print (status.group(1))
print (atualizado.group(0) , '\n')

