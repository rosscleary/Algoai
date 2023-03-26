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
    inputLowerBound = request.get_json()["inputLow"]
    inputUpperBound = request.get_json()["inputHigh"]
    runCount = request.get_json()["runCount"]
    programInformation = {
        "language": 'c++',
        "version": '10.2.0',
        "program": program,
        "inputLowerBound": int(inputLowerBound),
        "inputUpperBound": int(inputUpperBound),
        "runCount": int(runCount)
    }
    accuracy = getAccuracy(programInformation)
    return make_response({ "randomforest": accuracy["randomforest"] , "linearregression": accuracy["linearregression"] }, 200)
