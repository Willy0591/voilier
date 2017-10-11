import socket
import sys
IP ="192.168.0.233"
PORT = 5050
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto ("salut willy",(IP , 5050))
