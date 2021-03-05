# Load libraries
from threading import Timer

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

import requests
from flask import Flask, jsonify

import json

from json import JSONEncoder

import time


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


app = Flask(__name__)

distance = 0
fuel = 0


@app.route('/cloud/can_go', methods=['GET'])
# @cache.cached(timeout=300)
def speed_data():

    start_time = time.time()
    number_array = model_train()
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---y_train %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


def get_ac_control_data():
    try:
        req = requests.get("http://localhost:3103/ac_control/output")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_speed_data():
    try:
        req = requests.get("http://localhost:3202/speed/output")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return finalNumpyArray


def get_amount_fuel_data():
    global distance, fuel

    try:
        req = requests.get("http://localhost:6201/cloud/get_mobile_data")
        decodedArrays = json.loads(req.text)

        distance = float(decodedArrays["distance"])
        fuel = float(decodedArrays["fuel"])

        print(distance)
        print(fuel)

    except requests.exceptions.ConnectionError:
        return "Service unavailable"


def model_train():
    global distance, fuel

    get_amount_fuel_data()

    speed_output = [float(i) for i in get_speed_data()]
    ac_output = [float(i) for i in get_ac_control_data()]

    print(len(speed_output))
    print(len(ac_output))

    if len(speed_output) > len(ac_output):
        min = len(ac_output)
    else:
        min = len(speed_output)

    X = np.array((speed_output[:min], ac_output[:min])).T

    df = pd.DataFrame(X)

    print("df")
    print(df)

    # dataset = pd.read_csv("datasettt.csv")
    # df = dataset.iloc[:, [0, 1]]

    print(df)

    kmeans = KMeans(n_clusters=4, random_state=0)
    kmeans = kmeans.fit(df)

    df['labels'] = kmeans.labels_
    print(df['labels'].values.tolist())
    # interpretation of cluster values
    l = len(kmeans.labels_)
    for i in range(l):
        if kmeans.labels_[i] == 3:
            kmeans.labels_[i] = 1

        elif kmeans.labels_[i] == 0:
            kmeans.labels_[i] = 3

        elif kmeans.labels_[i] == 2:
            kmeans.labels_[i] = 4

        elif kmeans.labels_[i] == 1:
            kmeans.labels_[i] = 2

    df['labels'] = kmeans.labels_
    y = df['labels'].values

    array = df.values
    X = array[:, 0:2]

    # split the data set
    X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=0)

    # Make predictions for validating dataset
    model = LogisticRegression(solver='liblinear', multi_class='ovr')
    model.fit(X_train, Y_train)
    predictions = model.predict(X_validation)

    # Evaluate predictions
    print('Accuracy: ', accuracy_score(Y_validation, predictions))

    print('confusion_matrix: ')
    print(confusion_matrix(Y_validation, predictions))

    print('classification_report: ')
    print(classification_report(Y_validation, predictions))

    ###############check whether the vehicle can reach to the destination or not?################
    predict = model.predict([[4, 2]])
    print(predict)
    # distance = 250
    # litre = 20

    if predict == 1:
        rate = 11
    elif predict == 2:
        rate = 12.5
    elif predict == 3:
        rate = 13.5
    elif predict == 4:
        rate = 15

    output = rate * fuel

    if output >= distance:
        print(1)
        return 1
    elif output < distance:
        print(0)
        return 0


# passenger_data_automated = RepeatedTimer(5, get_passenger_count_data)

if __name__ == '__main__':
    app.run(port=6202, host='0.0.0.0')
