import pandas
import random
import tensorflow as tf
import requests

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
    print(result["run"]["stdout"])
    return result["run"]["stdout"]

# https://www.youtube.com/watch?v=5qgk9QJ4rdQ
def testModel(inputs, outputs):
    rows = []
    for i in range(len(inputs)):
        rows.append([int(inputs[i]), int(outputs[i])])
    df = pandas.DataFrame(rows)
    df.to_csv("dataset.csv", index = False, header = ["input", "output"])
    train_df = pandas.read_csv("dataset.csv")
    train_ds = tf.keras.pd_dataframe_to_tf_dataset(train_df, label="output")
    model = tf.keras.RandomForestModel()
    model.fit(train_ds)

def getAccuracy(sourceCode, language, version, runCount):
    inputs = []
    outputs = []
    for i in range(runCount):
        inputValue = str(random.randint(-10000, 10000))
        outputValue = str(callPiston(sourceCode, language, version, inputValue))
        inputs.append(inputValue)
        outputs.append(outputValue)
    return testModel(inputs, outputs)