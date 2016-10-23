from socket import *

Host = 'localhost'
Port = 21567
BufSize = 1024
ADDR = (Host, Port)

UDPSerSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('> ')
    if not data :
        break;
    UDPSerSocket.sendto('linqing test')
    data ,ADDR = UDPSerSocket.recvfrom(BufSize)
    if not data :
        print (data)  

UDPSerSocket.close() 