#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 16:50:38 2019

@author: nassim
"""

from socket import *
index=1
while index<=1000 :
    """envoyer plusieurs requetes sur le meme clients"""
    ClientSocket=socket(AF_INET,SOCK_STREAM)
    Serverport=3030
    Servername='127.0.0.1'
    ClientSocket.connect((Servername,Serverport))
    
    message=('entrez une phrase en Miniscule :')
    index=index+1
    ClientSocket.sendall(message.encode("utf_8"))
    modifiedMessage=ClientSocket.recv(5120).decode("utf8")
    print("l'index est egal actuellement à ",index)
    print("votre message en Majuscule est :",modifiedMessage)
    
    ClientSocket.close()