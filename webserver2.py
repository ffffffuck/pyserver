from flask import Flask, request

app = Flask(__name__)

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


if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5000)


