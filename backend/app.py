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
    accuracy = getAccuracy(program, 'c++', '10.2.0', 10)
    return make_response({ "accuracy": accuracy })
