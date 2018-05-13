from StrList import *

def Comunication(sentence,sentencelist,connectionSocket):
    TV = 0
    Light = 0
    TVlist = ["티", "비", "T", "V", "t", "v"]
    TVlist = ['t','v','T','V']
    Lightlist = ["불", "전", "등", "조", "명"]

    if True:
        for i in TVlist:
            if i in sentencelist and "꺼" in sentencelist:
                TV = 0
                print(StringList.TVoff)
                connectionSocket.send(StringList.TVoff.encode())
                return "TV : "+str(TV)

            if i in sentencelist and "켜" in sentencelist:
                TV = 1
                print(StringList.TVon)
                connectionSocket.send(StringList.TVon.encode())
                return "TV : "+str(TV)

        for j in Lightlist:
            if j in sentencelist and "꺼" in sentencelist:
                Light = 0
                print(StringList.Lightoff)
                connectionSocket.send(StringList.Lightoff.encode())
                return "Light : "+str(Light)
            if j in sentencelist and "켜" in sentencelist:
                Light = 1
                print(StringList.Lighton)
                connectionSocket.send(StringList.Lightoff.encode())
                return "Light : "+str(Light)
        else:
            print(sentence)
            connectionSocket.send(sentence.encode())
            return "에코입니당"