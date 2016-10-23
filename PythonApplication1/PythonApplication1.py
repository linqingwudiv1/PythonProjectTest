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
    print ('lian jie ')
    conn, addr = tcpSerSocket.accept()
    print ('ds:', addr)

    while True:
        data = conn.recv(BufSize)
        if not data:
            break;
        conn.send('[%s] %s' %(bytes(ctime(), 'utf-8'), data))
    conn.close()
tcpSerSocket.close()