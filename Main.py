# -*- coding: utf-8 -*-
from ServerSetting import *
from Comu import *
import http.server


def Server():
    global sentence
    global sentencelist
    global connectionSocket

    print("<<   서버 시작   >>")
    print("클라이언트 응답 대기중..")
    while True:
        connectionSocket, addr = setting.serverSocket.accept()
        sentence = connectionSocket.recv(1024)
        sentence = sentence.decode()
        print(connectionSocket)
        sentencelist = list(sentence)

        a = Comunication(sentence,sentencelist,connectionSocket)

        connectionSocket.close()

        print(a)


if __name__=='__main__':
    Server()