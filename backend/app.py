from helpers import getAccuracy
from flask import Flask
from flask import request
from flask import make_response
from flask_cors import CORS, cross_origin
import pymongo
from pymongo.server_api import ServerApi
import certifi

app = Flask(__name__)
CORS(app)


client = pymongo.MongoClient("mongodb+srv://algoai:BBNDyrFpa9ef5lzl@cluster0.cb9skyz.mongodb.net/?retryWrites=true&w=majority",
                             server_api=ServerApi('1'), tlsCAFile=certifi.where())
db = client.test

try:
    db.authenticate("algoai", "dRhlu31HofP3BS44")
except:
    print("Authentication failed")


@app.route("/")
def home():
    return "Route"


@app.route("/processProgram", methods=['POST'])
def processPrgram():
    sourceCode = request.get_json()["program"]
    inputLow = request.get_json()["inputLow"]
    inputHigh = request.get_json()["inputHigh"]
    runCount = request.get_json()["runCount"]
    programInformation = {
        "sourceCode": sourceCode,
        "language": 'c++',
        "version": '10.2.0',
        "inputLow": int(inputLow),
        "inputHigh": int(inputHigh),
        "runCount": int(runCount),
    }
    accuracy = getAccuracy(programInformation)
    parsedProgram = {
        "sourceCode": sourceCode,
        "language": 'c++',
        "version": '10.2.0',
        "inputLow": int(inputLow),
        "inputHigh": int(inputHigh),
        "runCount": int(runCount),
        "randomForestAccuracy": accuracy["randomforest"],
        "linearRegressionAccuracy": accuracy["linearregression"],
        "neuralNetworkAccuracy": accuracy["neuralnetwork"],
    }
    db.programs.insert_one(parsedProgram)
    return make_response({"randomforest": accuracy["randomforest"], "linearregression": accuracy["linearregression"], "neuralnetwork": accuracy["neuralnetwork"]}, 200)

@app.route("/programs", methods=['GET'])
def getProgram():
    parsedPrograms = []
    for program in db.programs.find():
        parsedPrograms.append({
            "id": str(program["_id"]),
            "sourceCode": str(program["sourceCode"]),
            "language": str(program["language"]),
            "version": str(program["version"]),
            "inputLow": int(program["inputLow"]),
            "inputHigh": int(program["inputHigh"]),
            "runCount": int(program["runCount"]),
            "randomForestAccuracy": int(program["randomForestAccuracy"]),
            "linearRegressionAccuracy": int(program["linearRegressionAccuracy"]),
            "neuralNetworkAccuracy": int(program["neuralNetworkAccuracy"]),
        })
    return make_response({"programs": parsedPrograms}, 200)
