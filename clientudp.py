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
    
lat1=float(ord (data[5])<<24)
lat2=lat1+(ord (data[6])<<16)
lat3=lat2+(ord(data[7])<<8)
lat4=lat3+(ord (data[8]))
divis = (lat4/1000000)

print"ID=", ord(data[0])
print"Taille=", ord(data[1])
print "Vvent=", ord(data[2])
print "Dvent=", ord(data[3])
print "Gite=" , ord(data[4])
print "latitude",divis
