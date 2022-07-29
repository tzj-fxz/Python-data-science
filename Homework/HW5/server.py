#TODO
#服务端，jupyter上不宜运行，故将代码保存到本地，再通过命令行运行
import socket
import time
import re

news=[]
with open('news.txt','r',encoding='utf-8') as f:
    news=f.readlines()

print("initializing server host information")
port = 2828
host = '0.0.0.0'
address = (host, port)
print("initializing server host socket")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(6)
print("waiting for connecting")
while True:
    conn, addr = server.accept()
    print("client information:", addr)
    matchst = conn.recv(100).decode('utf-8', errors='ignore')
    while matchst != '':
        l = []
        for newspiece in range(len(news)):
            if re.search(matchst, news[newspiece]) != None:
                l.append(newspiece)
        conn.send(str(l).encode('utf-8'))
        matchst = conn.recv(100).decode('utf-8', errors='ignore')
    conn.close()
