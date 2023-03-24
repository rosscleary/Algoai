import random
import requests
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

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
    result = requests.post('https://emkc.org/api/v2/piston/execute', json = data).json()
    return result["run"]["stdout"]

def testModel(inputs, outputs):
    X = np.array(inputs).reshape(-1, 1)
    y = np.array(outputs).reshape(-1, 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.5, random_state = 1)
    model = RandomForestClassifier(n_estimators = 100)
    print(X_train)
    print(y_train)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(y_test)
    print(y_pred)
    return metrics.accuracy_score(y_test, y_pred)

def getAccuracy(sourceCode, language, version, runCount):
    inputs = []
    outputs = []
    for i in range(runCount):
        inputValue = str(random.randint(1, 10000))
        outputValue = str(callPiston(sourceCode, language, version, inputValue))
        inputs.append(int(inputValue))
        outputs.append(int(outputValue))
    return testModel(inputs, outputs)