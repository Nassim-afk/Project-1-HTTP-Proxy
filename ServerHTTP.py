#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 11:54:53 2019

@author: nassim
"""

from socket import *

serverPort = 6788
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('server ready')

while True:
      connectionSocket, address = serverSocket.accept()
      message = connectionSocket.recv(2048)
      file = message.split()[1]
      """divise le message de la requete quand y'a des espaces à partir du 1er mot apres le get"""
      """apres test avec le webClient mozilla la requete http est comme suit get /text.txt HTTP1.1"""
      print ("le fichier demander est : ",file.decode('utf-8'))

      """du caractére i=1 jusqu'a la fin """
      file=file[1:]
      print ("le fichier demander est : ",file.decode('utf-8'))
      
      try:
          with open(file ,'rb') as f :
              Message="HTTP/ 1.1 200 OK \r\n\r\n"
              connectionSocket.send(Message.encode('utf-8'))    
              fichier=f.read()
              while fichier:
                  connectionSocket.sendall(fichier)
                  fichier = f.read()
      except:
         MM="HTTP/ 1.1 404 File Not Found\r\n\r\n"
         connectionSocket.send(MM.encode('utf-8'))
          
      connectionSocket.close()

  