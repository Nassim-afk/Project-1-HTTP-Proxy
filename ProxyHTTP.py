#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 15:22:22 2019

@author: nassim
"""

from socket import *
import time
import time
import os

serverName = '127.0.0.1'
proxyPort = 1234
serverPort=631
proxySocket = socket(AF_INET,SOCK_STREAM)
proxySocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
proxySocket.bind(('',proxyPort))
proxySocket.listen(5) 
print('Proxy ready') 
#******************************************************************************
def handle_client(clientSocket): 
    received = clientSocket.recv(4096)
    
    loggeur(received)      #enregistrer la requête GET du client avec l’heure de la requète et la taille de la réponse
    interdit=censure(received)   #le fichier demandé est dans la liste interdite ==0
    enreg=cache(received)   #le fichier demandé est dans le cache==0 sinon 
    
    if interdit==1 :           #le fichier n'est pas dans la liste interdite
        if enreg==1 :
            Get_from_server(clientSocket,received) #Get file from server
        else :
            envoi_Direct(clientSocket,received) #Get file from cache
    else :             
        Err="HTTP/1.1 404 File Not Found\r\n\r\n"
        clientSocket.send(Err.encode())
        
    clientSocket.close()
                    
#******************************************************************************    
def envoi_Direct( clientSocket,received): 
    if not received:
                clientSocket.close() 
    else:  
        proxySocket = socket(AF_INET,SOCK_STREAM)
        proxySocket.connect((serverName,serverPort))
        proxySocket.send(received)
        Message=proxySocket.recv(4096)
        OKreply="HTTP/1.1 200 OK\r\n\r\n"
        clientSocket.sendall(OKreply.encode())
        while Message:
            Message=proxySocket.recv(4096)
            clientSocket.send(Message)
        proxySocket.close()
        clientSocket.close()
#******************************************************************************               
def Get_from_server(clientSocket,received):
    fichier = received.split()[1]
    fichier=fichier[1:]
    try:
        with open(fichier,'rb') as f : 
            OKreply="HTTP/1.1 200 OK\r\n\r\n"
            clientSocket.send(OKreply.encode())    
            file=f.read()
            while file:
                clientSocket.sendall(file)
                file = f.read()
    except:
        Err="HTTP/1.1 404 File Not Found\r\n\r\n"
        clientSocket.send(Err.encode())
    clientSocket.close()

#******************************************************************************    
def cache (req) :
    file = req.split()[1]
    """je le rends au format caract"""
    file=str(file[1:].decode()) #===>text.txt
    with open("cache.txt",'r') as f :    
        fichier=f.read()
        look=fichier.find(file)
        if look != -1 :
            print("le fichier__"+file+"__est déja enregistré dans le cache")
            k=0
        else:
            print("le fichier__"+file+"__n'est pas enregistré dans le cache")
            temp=open("cache.txt",'a') 
            #ecire le contenu quand c'est du texte (!ne marche pas avec les images!)
            """temp2=open(file,"r")
            content=temp2.read() #lire le contenu du fichier demander 
            temp.write(file)     #ecrire le nom du fichier 
            temp.write(" :\n")
            temp.write(content)  #ecrire le contenu du fichier
            k=1
            temp.close()
            temp2.close()
            f.close()"""
            
            
            temp.write('\n'+file)
            k=1
            temp.close()
            f.close()
    return k
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
def censure (request):
    file = request.split()[1]
    file=str(file[1:].decode())
    with open("censure.txt",'r') as f :    
        fichier=f.read()
        look=fichier.find(file)
        if look == -1 :
            print("le fichier demandé__"+file+" __n'est dans pas la liste interdite")
            k=1
            
        else:
            print("le fichier demandé__"+file+" __est dans la liste interdite")
            k=0
        f.close()
    return k
#******************************************************************************                         
while True:  
    connectionSocket, address = proxySocket.accept()   
    handle_client(connectionSocket)
       
 
  


