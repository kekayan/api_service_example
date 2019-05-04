from flask import Flask,request
import requests
import json
app = Flask(__name__)

@app.route("/codetostate")
def getstate():
    code = request.args.get('code')
    url="http://dataservice.default.svc.cluster.local/codes"
    response = requests.get(url)
    data = json.loads(response.text)
    result=data[code.upper()]
    return result

@app.route("/statetocode")
def getcode():
    state = request.args.get('state')
    url="http://dataservice.default.svc.cluster.local/states"
    response = requests.get(url)
    data = json.loads(response.text)
    result=data[state.lower()]
    return json.dumps(result)

@app.route("/")
def welcome():
    return "welcome to api service"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True,port=80)