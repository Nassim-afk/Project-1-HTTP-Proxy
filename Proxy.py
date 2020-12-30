#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 18:19:31 2019

@author: nassim
"""

from socket import *
from threading import *

Proxyport=3030
Serverport=8965
Servername='127.0.0.1'
ProxySocket=socket(AF_INET,SOCK_STREAM)
#ProxySocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
#ClientSocket=socket(AF_INET,SOCK_STREAM)
ProxySocket.bind(('',Proxyport))
ProxySocket.listen(5)
print('proxy ready')




def handle_client(clientScocket):
    while True :
        received=clientScocket.recv(4096)
        if not received :
            clientScocket.close()
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
            """sendall message""""""ici la socket qui joue le role le plus important est Clientsocket"""
            """la socket temporaire joue le role de client BIS qui etabli la connexion et recoit la comm"""
            #to_send = message.decode('utf-8').upper().encode('utf-8')
            clientScocket.sendall(message)
            #ProxySocket.close()
            """fermer la socket temporaire"""
            tempSocket.close()

while True :
    """connectionSocket accept de renvoyer les données obtenue vers le client {joue le role d'un server ici} """
    connectionSocket, address=ProxySocket.accept()
    #for i in range(10) :
    """le thread prends en argument la fonction qui établi la comm avec le server comme étant un client BIS"""
    """et renvoie ce qu'elle recoit vers la socket connection"""
    #Thread(target=handle_client,args=(connectionSocket,)).start()
    handle_client(connectionSocket)
    #ConnectionSocket.close()
    



    #Thread(target=clientSocket.sendall(message),args=(connectionSocket,)).start()
"""
while True :
    
    clientSocket=socket(AF_INET,SOCK_STREAM)

    clientSocket.connect((Servername,Serverport))
    received=clientSocket.recv(4096)

    clientSocket.send(received)
    message=clientSocket.recv(4096)
    clientSocket.sendall(message)
    clientSocket.close()
"""


#while True :
    
    #ConnectionSocket, address=ServerSocket.accept()
    
    #message=ConnectionSocket.recv(2048) #je recois le message venant dans la scoket server
    
    ##ConnectionSocket.send(modifiedMessage)
    
    #ClientSocket.send(message) #je redirige le message vers le server
    
    #modifiedMessage=ClientSocket.recv(2048)# je recois le message modifié
    
    #ConnectionSocket.send(modifiedMessage)#je redirige vers la socket connection
    
    #ConnectionSocket.close()















