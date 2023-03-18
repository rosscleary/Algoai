from flask import Flask
from flask import request
from flask import make_response
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

from helpers import getAccuracy

@app.route("/")
def home():
    return "Route"

@app.route("/processProgram", methods=['POST'])
def processPrgram():
    program = request.get_json()["program"]
    print(program)
    accuracy = getAccuracy(program, 'c++', '10.2.0', 10)
    accuracy = 50
    return make_response({ "accuracy": accuracy })
