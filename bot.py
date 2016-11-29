#coding: UTF-8

from bs4 import BeautifulSoup
import urllib.request as url
from datetime import *
import re
from unicodedata import normalize

diasemana = ['segunda-feira','terceira-feira','quarta-feira',
                          'quinta-feira','sexta-feira','sabado','domingo']
meses =['janeiro','fevereiro','março','abril','maio','junho',
                 'julho','agosto','setembro','outubro','novembro','dezembro']

'''Recebe a mensagem, uma string,
e identifica qual comando proceder e
retorna uma string '''
def comando(msg):

   msg = msg.lower() # passa mesagem para minusculo

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

      now = datetime.now() # recebe data e hora do sistema

      hora = str(now.time())

      now = 'Dia ' + str(now.day) + ' de ' + str(meses[now.month - 1]) + ' de ' + str(now.year) + \
            '\n          Hora ' + hora[:5] + ' ' + str(diasemana[int(now.strftime('%w'))])

      return now

   elif msg[:5] == '/data':

      now = datetime.now()

      now = 'Dia ' + str(now.day) + ' de ' + str(meses[now.month - 1]) + ' de ' + str(now.year) +\
            '\n          ' + str(diasemana[int(now.strftime('%w'))])

      return now

   elif msg[:5] == '/hora':

      now = datetime.now()

      hora = str(now.time())

      now = 'Hora ' + hora[:5]

      return now

   elif msg[:6] == '/tempo':

      site = 'http://tempo.clic.com.br/'

      cidade = msg[7:-2] # extrai cidade da mensagem conforme padrão estabelecido
      estado = msg[-3:]  # extrai estado

      cidade = cidade.replace(' ' , '')  # remove espaços se houves
      estado = estado.replace(' ' , '')

      cidade = normalize('NFKD', cidade).encode('ASCII','ignore').decode('ASCII') # remove acentos das palavras
      estado = normalize('NFKD', estado).encode('ASCII','ignore').decode('ASCII')

      con = ''

      try:
         url2 = site + estado + '/' + cidade
         con = url.urlopen(url2 , None , 7) # acessa o endereço com time out de 7s

         if con.status == 200 :
            HTML = con.read() # recebe o HTML da página

            soup = BeautifulSoup(HTML, 'html.parser') # trata o HTML para realizar a busca

            cidadeTempo = re.search(r'Previsão do tempo em.*no ClicTempo',
                                    str(soup.find('meta', attrs={'id':'site-description'}))) # faz busca no HTML

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
      palavra = normalize('NFKD', palavra).encode('ASCII','ignore').decode('ASCII')
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



