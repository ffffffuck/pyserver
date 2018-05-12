# -*- coding: utf-8 -*-
from ServerSetting import *
from StrList import *

def Comunication():
    TV = 0
    Light = 0
    TVlist = ["티", "비", "T", "V", "t", "v"]
    Lightlist = ["불", "전", "등", "조", "명"]

    for i in TVlist:
        if i in sentencelist and "꺼" in sentencelist:
            TV = 0
            print(StringList.TVoff)
            connectionSocket.send(StringList.TVoff.encode())
            return TV

        if i in sentencelist and "켜" in sentencelist:
            TV = 1
            print(StringList.TVon)
            connectionSocket.send(StringList.TVon.encode())
            return TV

    for j in Lightlist:
        if j in sentencelist and "꺼" in sentencelist:
            Light = 0
            print(StringList.Lightoff)
            connectionSocket.send(StringList.Lightoff.encode())
            return Light
        if j in sentencelist and "켜" in sentencelist:
            Light = 1
            print(StringList.Lighton)
            connectionSocket.send(StringList.Lightoff.encode())
            return Light

def Server():
    global sentence
    global sentencelist
    global connectionSocket

    print("<<   서버 시작   >>")
    while 1:
        connectionSocket, addr = setting.serverSocket.accept()
        sentence = connectionSocket.recv(1024)
        sentence = sentence.decode()
        sentencelist = list(sentence)

        Comunication()

        connectionSocket.close()

if __name__=='__main__':
    Server()