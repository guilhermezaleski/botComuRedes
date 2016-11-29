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

   elif msg[:5] == '/help':
       return '--HELP\n' \
              '        Comandos:\n' \
              '      /autores  Autores do chat;\n' \
              '      /datahora  Data e hora atual;\n' \
              '      /data  Data atual;\n' \
              '      /hora  Hora atual;\n' \
              '      /tempo -cidade -sigla estado;\n' \
              '            Previsão do tempo para a cidade;\n' \
              '      /dicionario -palavra\n' \
              '            Significado da palavra;\n'

   elif msg[:9] == '/datahora':
      now = datetime.now()

      hora = str(now.time())

      now = 'Dia ' + str(now.day) + ' de ' + str(now.month) + ' de ' + str(now.year) + \
            '\n          Hora ' + hora[:5]

      return now

   elif msg[:5] == '/data':

      now = datetime.now()

      now = 'Dia ' + str(now.day) + ' de ' + str(now.month) + ' de ' + str(now.year)

      return now

   elif msg[:5] == '/hora':

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

            soup = BeautifulSoup(HTML, 'html.parser')
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
      site = 'https://dicionariodoaurelio.com/'
      palavra = msg[12:]
      con = ''

      try:
       url2 = site + palavra.replace(' ', '')
       con = url.urlopen(url2 , None , 5)
       HTML = con.read()

       soup = BeautifulSoup(HTML, 'html.parser')
       significado = str(soup.find('meta', attrs={'name':'description'}))

       idxInicio = significado.find(':')
       idxInicio += 1
       idxFinal = significado.find('.', idxInicio)

       return  significado[idxInicio:idxFinal]


      except Exception as e:

               if str(e) == 'HTTP Error 404: NOT FOUND':
                  return 'Não foi possivel localizar\n' \
                         'essa palavra'
               return str(e)

   else:
      return "Comando não reconhecido!\n" \
             "          Use /help para ajuda."



