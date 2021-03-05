# Load libraries
import numpy as np
from numpy import argmax

import requests
from flask import Flask

import json
from json import JSONEncoder

import time
from threading import Timer


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_der(x):
    return sigmoid(x) * (1 - sigmoid(x))


def softmax(A):
    expA = np.exp(A)
    return expA / expA.sum(axis=1, keepdims=True)


def predict(wh, bh, wo, bo, X_test):
    zh = np.dot(X_test, wh) + bh
    ah = sigmoid(zh)
    zo = np.dot(ah, wo) + bo
    ao = softmax(zo)
    return ao


# config = {
#     "DEBUG": True,  # some Flask specific configs
#     "CACHE_TYPE": "simple",  # Flask-Caching related configs
#     "CACHE_DEFAULT_TIMEOUT": 300
# }

app = Flask(__name__)

# app.config.from_mapping(config)
# cache = Cache(app)

y_predict_array = []


@app.route('/speed/output', methods=['GET'])
# @cache.cached(timeout=300)
def output_data():
    start_time = time.time()
    number_array = output()
    number_array = np.array(number_array)
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---output_data %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


def get_roof_wh():
    try:
        req = requests.get("http://localhost:3201/roof/wh")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_roof_bh():
    try:
        req = requests.get("http://localhost:3201/roof/bh")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_roof_wo():
    try:
        req = requests.get("http://localhost:3201/roof/wo")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_roof_bo():
    try:
        req = requests.get("http://localhost:3201/roof/bo")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_input_data():
    try:
        req = requests.get("http://localhost:3001/speed/input")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def output():
    wh = get_roof_wh()
    bh = get_roof_bh()
    bo = get_roof_bo()
    wo = get_roof_wo()

    x = get_input_data()

    output = []

    predictions = predict(wh, bh, wo, bo, x)

    for i in range(len(x)):
        n = argmax(predictions[i])
        output.append(n)

    print(output)
    print(type(output))
    return output


# model_train_automated = RepeatedTimer(15, model_train)

if __name__ == '__main__':
    app.run(port=3202, host='0.0.0.0')
