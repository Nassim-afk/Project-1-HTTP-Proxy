#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 18:40:59 2019

@author: nassim
"""
from socket import *

Serverport=8965

ServerSocket=socket(AF_INET,SOCK_STREAM)
#ServerSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
ServerSocket.bind(('',Serverport))
ServerSocket.listen(1)
print('server ready')

while True :
    
    ConnectionSocket, address=ServerSocket.accept()
    message=ConnectionSocket.recv(2048)
    modifiedMessage= message.upper()
    ConnectionSocket.sendall(modifiedMessage)
    ConnectionSocket.close()