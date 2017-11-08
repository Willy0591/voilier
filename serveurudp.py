#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
iD=17
taille=25
vvent=10
dvent=14
lat=48.409427
longe=-4.486572
gite=2
ipserv="127.0.0.1"

divis= int (lat*10000000) 
lat1=(divis>>24)&0xFF
lat2=(divis>>16)&0xFF
lat3=(divis>>8)&0xFF
lat4=(divis)&0xFF


divis2= int (longe*10000000)
longe1=(divis2>>24)&0xFF
longe2=(divis2>>16)&0xFF
longe3=(divis2>>8)&0xFF
longe4=(divis2)&0xFF

port=5050
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((ipserv, port))

while True:
    data,addr=sock.recvfrom(1024)
    tramerep=bytearray ([iD, taille, vvent, dvent,lat1, lat2, lat3, lat4, longe1, longe2, longe3, longe4, gite])
    sock.sendto(tramerep,(addr[0],addr[1]))

    print"ID= ", ord(data[0])
    print"Taille= ", ord(data[1])
    print"Safran= ", ord(data[2]),"°"
    print "Gv= ",ord(data[3]),"°"
    
