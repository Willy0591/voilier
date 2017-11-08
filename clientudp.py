import socket
import sys
ip ="127.0.0.1"
iD=22
taille=2
safran=30
gv=90
port = 5050

trame=bytearray([iD, taille, safran, gv]);
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto (trame,(ip , 5050))
data,addr=sock.recvfrom(1024)
    
lat= ord(data[4])<<24 | ord(data[5])<<16 | ord(data[6])<<8 | ord(data[7])
lat_f = float(lat)/10000000

if ord(data[4]) > 127:
    lat = (~lat) &0xFFFFFFFF
    lat = (lat+1)*-1 
lat_f = float(lat)/10000000

longe=ord(data[8])<<24  | ord(data[9])<<16 | ord(data[10])<<8 | ord(data[11])


if ord(data[8]) > 127:
    longe = (~longe) &0xFFFFFFFF
    longe = (longe+1)*-1 
longe_f = float(longe)/10000000

print"ID=", ord(data[0])
print"Taille=", ord(data[1])
print "Vvent=", ord(data[2])
print "Dvent=", ord(data[3])
print "Gite=" , ord(data[12])
print "latitude=",lat_f
print "longitude=",longe_f

