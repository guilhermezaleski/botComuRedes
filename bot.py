#coding: UTF-8

from bs4 import BeautifulSoup
import urllib.request as url
from datetime import datetime
import re

'''Recebe o a mensagem, uma string,
e identifica qual comando proceder'''
def comando(msg):

   msg = msg.lower()

   if msg == '/autores' :
      return "Esse chat foi desenvolvido por: \n" \
             "Guilherme Zaleski, Juliana Engelmann\n" \
             "e Pablo Tessmann. Para a disciplina de \n" \
             "Redes de Computadores, ministrada pelo \n" \
             "professor Lucas Muller, semestre 2016/2."

   elif msg == '/datahora':

      now = datetime.now()

      hora = str(now.time())

      now = 'Dia ' + str(now.day) + ' de ' + str(now.month) + ' de ' + str(now.year) + \
            '\n          Hora ' + hora[:5]

      return now

   elif msg == '/data':

      now = datetime.now()

      now = 'Dia ' + str(now.day) + ' de ' + str(now.month) + ' de ' + str(now.year)

      return now

   elif msg == '/hora':

      now = datetime.now()

      hora = str(now.time())

      now = 'Hora ' + hora[:5]

      return now

   elif msg[:6] == '/tempo':
      site = 'http://tempo.clic.com.br/'
      cidade = msg[7:-2]
      estado = msg[-3:]
      cidade = cidade.replace(' ' , '')
      estado = estado.replace(' ' , '')
      con = ''

      try:
         url2 = site + estado + '/' + cidade
         con = url.urlopen(url2 , None , 5)

         if con.status == 200 :
            HTML = con.read()

            soup = BeautifulSoup(HTML)
            cidadeTempo = re.search(r'Previsão do tempo em.*no ClicTempo', str(soup.find('meta', attrs={'id':'site-description'})))
            temperatura = re.search(r'[0-9]{2}' , str(soup.find('span', attrs={'class':'temperature_now'})))
            atualizado = re.search(r'Atualizado às .*[0-9]' , str(soup.find('span', attrs={'class':'updateTime'})))

            return cidadeTempo.group(0)+ ' ' + temperatura.group(0) + 'º\n' + atualizado.group(0)

      except Exception as e:

         if str(e) == 'HTTP Error 404: NOT FOUND':
            return 'Não foi possivel localizar\n' \
                   '          essa cidade!'

         return str(e)

   elif msg[:11] == '/dicionario':
      site = 'https://www.dicio.com.br/'
      palavra = msg[12:]
      con = ''

      try:
       url2 = site + palavra.replace(' ', '')
       con = url.urlopen(url2 , None , 5)
       HTML = con.read()

       soup = BeautifulSoup(HTML)
       significado = str(soup.find('p', attrs={'id':'significado'}))

       idxInicio = significado.find('</span>')
       idxInicio += 13
       idxFinal = significado.find('</span>', idxInicio)

       return  significado[idxInicio:idxFinal]


      except Exception as e:

               if str(e) == 'HTTP Error 404: NOT FOUND':
                  return 'Não foi possivel localizar\n' \
                         'essa palavra'
               return str(e)





   else:
      return "Comando não reconhecido!"

'''
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
print (atualizado.group(0) ,'\n')'''

