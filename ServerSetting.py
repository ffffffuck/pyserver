from socket import *

class setting:
    HOST = ''
    PORT = 5000
    BUFFSIZE = 1024
    ADDR = (HOST,PORT)
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(ADDR)
    serverSocket.listen(100)