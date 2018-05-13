# _*_ coding: utf-8 _*_

from flask import Flask, request
from flask_socketio import SocketIO, emit

import threading

app = Flask(__name__)
socketio = SocketIO

@app.route('/')
def HelloWorld():

    return "My IoT Server"

@app.route('/tv', methods=['GET'])
def TVAction():
    action = request.args.get("action")

    tvon = '티비를 켭니다'
    tvoff = '티비를 끕니다'


    if action == "on":
        print(tvon)
        return tvon
    if action == "off":
        print(tvoff)
        return tvoff

@app.route('/light', methods=['GET'])
def LightAction():
    action = request.args.get("action")

    lighton = '전등을 켭니다'
    lightoff = '전등을 끕니다'


    if action == "on":
        print(lighton)
        return lighton
    if action == "off":
        print(lightoff)
        return lightoff

@app.route('/door', methods=['GET'])
def DoorAction():
    action = request.args.get("action")

    dooropen = '문을 엽니다'
    doorclose = '문을 닫습니다'


    if action == "open":
        print(dooropen)
        return dooropen
    if action == "close":
        print(doorclose)
        return doorclose


if __name__ == "__main__":
        app.run(host="0.0.0.0",port=5000)


