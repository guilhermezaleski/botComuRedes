# botComuRedes

Manual de utilização - Servidor de Chat Bot


Como trabalho acadêmico da disciplina de redes de computadores, foi implementado uma aplicação Bot.


1 - Para o ambiente de desenvolvimento foi utilizado Python 3.5.2 juntamente com a biblioteca beautifulsoup4 4.5.1. 
A IDE utilizada foi a pycharm, versão 2016.3.


2 - Passos para configurar a execução da aplicação:
1º Fazer download do interpretador Python 3: https://www.python.org/ftp/python/3.5.2/python-3.5.2.exe e realizar a instalação.


2º Fazer download da biblioteca beautifulsoup4:

 https://pypi.python.org/pypi/beautifulsoup4 

Descompactar o download e realizar sua instalação da seguinte forma:

//python setup.py install

3º Acessar o prompt de comando e mapear onde a pasta da aplicação está. Logo executar o seguinte comando para o servidorTcp.py: 

//python servidorTcp.py

Logo após, abrir um novo prompt de comando, ou em qualquer outra máquina da rede, e executar o clienteTcp.py:

//python clienteTcp.py

Aplicação Cliente
Primeiro passo - Iniciar a conexão com o servidor iremos clicar em Conectar, situado na barra superior direita. 
Pode-se escolher localhost ou se estiver em uma mesma rede, o IP ou nome do outro computador.

Para realizar consultas, devemos digitar no campo de mensagem, com a barra “/” e mais o que queira solicitar.
A aplicação está prevista os seguintes comandos:


Comandos
/autores                         // Autores do Chat
/datahora                        // Data e hora atual
/data                            // Data atual
/hora                            // Hora atual
/tempo -cidade -sigla do estado  // Previsão do tempo para a cidade
/dicionario -palavra             // Significado da palavra


Há também uma opção de HELP que lista os possíveis comandos:


Para finalizar a conexão com o servidor, clique no botão Desconectar, situado na barra superior direita.


A aplicação do servidor desenvolvida gera um arquivo log, gravando as consultas realizadas e também em casos de erros, irá informar quais erros ocorreram. O arquivo gerado é encontrado dentro da pasta da aplicação, nomeado como servidorLog.txt.


Link para demonstração: https://goo.gl/Yt824H
