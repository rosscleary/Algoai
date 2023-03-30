import random
import requests
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import tensorflow as tf


def callPiston(sourceCode, language, version, input):
    data = {
        'language': language,
        'version': version,
        'files': [
            {
                'content': sourceCode,
            },
        ],
        'stdin': input,
    }
    result = requests.post(
        'https://emkc.org/api/v2/piston/execute', json=data).json()
    return result["run"]["stdout"]


def testRandomForestModel(inputs, outputs):
    X = np.array(inputs).reshape(-1, 1)
    y = np.array(outputs).reshape(-1, 1)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.5, random_state=1)
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return metrics.accuracy_score(y_test, y_pred)


def testLinearRegressionModel(inputs, outputs):
    X = np.array(inputs).reshape(-1, 1)
    y = np.array(outputs).reshape(-1, 1)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.5, random_state=1)
    model = LinearRegression()
    model.fit(X_train, y_train)
    return np.mean(np.round(model.predict(X_test)) == y_test)


def testNeuralNetworkModel(inputs, outputs):
    X = np.array(inputs).reshape(-1, 1)
    y = np.array(outputs).reshape(-1, 1)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.5, random_state=1)
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(1, activation="relu"),
        tf.keras.layers.Dense(1, activation="relu"),
    ])
    model.compile(optimizer="adam", loss="mean_squared_error")
    model.fit(X_train, y_train, epochs=100)
    return np.mean(np.round(model.predict(X_test)) == y_test)


def getAccuracy(programInformation):
    inputs = []
    outputs = []
    for i in range(programInformation["runCount"]):
        inputValue = str(random.randint(
            programInformation["inputLow"], programInformation["inputHigh"]))
        outputValue = str(callPiston(
            programInformation["sourceCode"], programInformation["language"], programInformation["version"], inputValue))
        inputs.append(int(inputValue))
        outputs.append(int(outputValue))
    accuraccyData = {
        "randomforest": testRandomForestModel(inputs, outputs),
        "linearregression": testLinearRegressionModel(inputs, outputs),
        "neuralnetwork": testNeuralNetworkModel(inputs, outputs),
    }
    return accuraccyData
