from flask import Flask
from flask import request
from flask import make_response
from flask_cors import CORS, cross_origin
import pymongo
from pymongo.server_api import ServerApi
import certifi

app = Flask(__name__)
CORS(app)

from helpers import getAccuracy

client = pymongo.MongoClient("mongodb+srv://algoai:BBNDyrFpa9ef5lzl@cluster0.cb9skyz.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'), tlsCAFile=certifi.where())
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
    db.programs.insert_one(programInformation)
    return make_response({ "randomforest": accuracy["randomforest"] , "linearregression": accuracy["linearregression"] }, 200)

# get route with path /program that gets programs from mongodb database
@app.route("/programs", methods=['GET'])
def getProgram():
    parsedPrograms = []
    for program in db.programs.find():
        print(program)
        parsedPrograms.append({
            "id": str(program["_id"]),
            "sourceCode": program["program"],
            "language": program["language"],
            "version": program["version"],
        })
    return make_response({ "programs": parsedPrograms }, 200)