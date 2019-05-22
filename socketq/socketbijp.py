# coding=utf8
import socket
HOST = '127.0.0.1'
PORT = 21567

#创建socket对象
sk=socket.socket()
#发起连接
sk.connect((HOST, PORT))
#客户端启动
while True:
    server_response=input("我：")
    sk.sendall(bytes(server_response,encoding="utf8"))
    if server_response=='exit':
        break
    #接收数据
    server_reply=sk.recv(1024)
    print(server_reply)
    print(str(server_reply,"utf8"))
sk.close()