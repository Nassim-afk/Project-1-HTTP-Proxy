#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 18:07:24 2019

@author: nassim
"""

from socket import *
from threading import *
import time
import os

Proxyport=4566
Serverport=6788
Servername='127.0.0.1'
ProxySocket=socket(AF_INET,SOCK_STREAM)
ProxySocket.bind(('',Proxyport))
ProxySocket.listen(5)
print('proxy ready')

def handle_client(clientSocket):
    
    while True :
        received=clientSocket.recv(4096)
        if not received :
            clientSocket.close()
        else :
            #ProxySocket=socket(AF_INET,SOCK_STREAM)
            """create a socket to connect with the server socket"""
            
            tempSocket=socket(AF_INET,SOCK_STREAM)
            
            #ProxySocket.connect((Servername,Serverport))
            tempSocket.connect((Servername,Serverport))
            """cette socket temporaire ici envoie la requete reçu depuis le CLIENT"""
            #ProxySocket.send(received)
            tempSocket.send(received)
            """elle recoit le message modifié depuis le server"""
            #message=ProxySocket.recv(4096)
            message=tempSocket.recv(4096)
            loggeur(received)
            """sendall message""""""ici la socket qui joue le role le plus important est Clientsocket"""
            """la socket temporaire joue le role de client BIS qui etabli la connexion et recoit la comm"""
            #to_send = message.decode('utf-8').upper().encode('utf-8')
            clientSocket.sendall(message)
            #ProxySocket.close()
            """fermer la socket temporaire"""
            tempSocket.close()

    clientSocket.close()
#******************************************************************************     
def loggeur (received) :
    file=received.split()[1]
    file=str(file[1:].decode('utf_8'))
    log=time.strftime("%A %d %B %Y %H:%M:%S") #date de la requete GET
    received=received.decode('utf_8')
    indx=0
    r=""
    size=str(os.path.getsize(file)) #taille du fichier reçu en réponse 
    
    while indx<5 :
        r+=str(received.split()[indx]+"_")
        indx=indx+1
    f=open("date.txt","a")
    f.write(r+"---------------->"+log+"  size  :"+size+" Bytes \n")
    f.close()
#******************************************************************************
while True :
    
    connectionSocket, address=ProxySocket.accept()
    #Thread(target=handle_client,args=(connectionSocket,)).start()
    handle_client(connectionSocket)
    #ConnectionSocket.close()