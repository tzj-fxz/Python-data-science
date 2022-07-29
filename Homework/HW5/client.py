#客户端，jupyter上不宜运行，故将代码保存到本地，再通过命令行运行
import socket
import time
host = '127.0.0.1'
port = 2828
client = socket.socket()
client.connect((host, port))

searchlist=['全国.*委员会', '中国.*协会', '中美建交']
for st in searchlist:
    client.send(st.encode('utf-8'))
    data = client.recv(100).decode('utf-8', errors='ignore')
    print(data)
client.send(''.encode('utf-8'))
client.close()
