#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 15:10:40 2019

@author: nassim
"""

from socket import *

serverPort =5455
serverName='127.0.0.1'
clientSocket = socket(AF_INET,SOCK_STREAM)

clientSocket.connect((serverName,serverPort))

"""vrai format de la Request="GET /alger.jpg HTTP/1.1\r\nHost: google.com\r\n\r\n"""
Request="GET /alger.jpg HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n"
"""Request="cache.txt"""

clientSocket.send(Request.encode('utf-8'))
MessageReply=clientSocket.recv(2048)
print(MessageReply.decode('utf-8'))