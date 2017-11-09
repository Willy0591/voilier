import socket
class Voilierclient:

    def __init__(self):
        self.id=0
        self.ipserv=""
        self.port=0
        self.valsf=0
        self.valgv=0
        self.git=0
        self.lat=0
        self.longe=0
        self.vitvent=0
        self.orientvent=0
        self.taille=0
    
    def intcom(self,ip,port):
        self.ipserveur=ip
        self.port=port
        self.sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def txrx(self):
        trame=bytearray([self.id, 2, self.valsf, self.valgv]);
        self.sock.sendto(trame,(self.ipserveur , self.port))
        data,addr=self.sock.recvfrom(1024)
    
        lat= ord(data[4])<<24 | ord(data[5])<<16 | ord(data[6])<<8 | ord(data[7])

        if ord(data[4]) > 127:
            lat = (~lat) &0xFFFFFFFF
            lat = (lat+1)*-1 
        lat_f = float(lat)/10000000

        longe=ord(data[8])<<24  | ord(data[9])<<16 | ord(data[10])<<8 | ord(data[11])

        if ord(data[8]) > 127:
            longe = (~longe) &0xFFFFFFFF
            longe = (longe+1)*-1 
        longe_f = float(longe)/10000000
    
        self.id+=1
        self.taille=ord(data[1])
        self.vitvent=ord(data[2])
        self.orientvent=ord(data[3])
        self.lat= float(lat)/10000000
        self.longe=float(longe)/10000000
        self.gite=ord (data[12])
    

monVoilierClient=Voilierclient()
monVoilierClient.intcom("127.0.0.1",5050)
monVoilierClient.valsf=30
monVoilierClient.id=22
monVoilierClient.valgv=90
monVoilierClient.txrx()
print "latitude =",monVoilierClient.lat
print "longitude =",monVoilierClient.longe
print "id =",monVoilierClient.id
print "taille =",monVoilierClient.taille
print "vitvent =",monVoilierClient.vitvent
print "orientvent =",monVoilierClient.orientvent
print "gite =",monVoilierClient.gite



   
    
    
