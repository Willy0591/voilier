#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
iD=17
taille=25
vvent=10
dvent=14
lat=22.12345
longe=11.75642
gite=2
ipserv="127.0.0.1"
divis= int (lat*1000000)

lat1=(divis>>24)&0xFF
lat2=(divis>>16)&0xFF
lat3=(divis>>8)&0xFF
lat4=(divis)&0xFF

port=5050
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((ipserv, port))

while True:
    data,addr=sock.recvfrom(1024)
    tramerep=bytearray ([iD, taille, vvent, dvent, gite, lat1, lat2, lat3, lat4])
    sock.sendto(tramerep,(addr[0],addr[1]))

    print"ID= ", ord(data[0])
    print"Taille= ", ord(data[1])
    print"Safran= ", ord(data[2]),"°"
    print "Gv= ",ord(data[3]),"°"
