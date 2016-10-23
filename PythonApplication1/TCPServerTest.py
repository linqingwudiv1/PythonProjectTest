#python 3.5 TCp Client Exma
from socket import *
from time import ctime

Host = 'localhost'
Port = 21567
BufSize = 1024
ADDR = (Host, Port)

tcpSerSocket = socket(AF_INET, SOCK_STREAM)
tcpSerSocket.bind(ADDR)
tcpSerSocket.listen(5)


while True:
    print ('wait conn ')
    conn, addr = tcpSerSocket.accept()
    print ('IP Addr:', addr)

    while True:
        data = conn.recv(BufSize)
        print (data.decode())
        if not data:
            break;
        conn.send(('ready return test :'+ data.decode()).encode('utf-8'))
    conn.close()
tcpSerSocket.close()