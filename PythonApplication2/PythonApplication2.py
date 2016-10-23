from socket import *

Host = 'localhost'
Port = 21567
BufSize = 1024
ADDR = (Host, Port)

tcpCli = socket(AF_INET, SOCK_STREAM)
tcpCli.connect(ADDR)

while True:
    data = input('> ')
    if not data :
        break;
    tcpCli.send(data)
    data = tcpCli.recv(BufSize)
    if not data :
        print (data)

tcpCli.close() 