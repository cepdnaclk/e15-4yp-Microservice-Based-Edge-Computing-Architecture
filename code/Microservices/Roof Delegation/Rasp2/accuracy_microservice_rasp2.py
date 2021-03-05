# Load libraries
from sklearn.metrics import accuracy_score
import numpy as np

import requests
from flask import Flask

import json
from json import JSONEncoder

import time
from threading import Timer
import datetime
import csv

a = datetime.datetime.now()


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

ac_accuracy = 0
speed_accuracy = 0


time_ac_control_accuracy = 0
time_speed_accuracy = 0
time_ac_control_accuracy_function = 0
time_speed_accuracy_function = 0
total = 0


def write_to_csv(fileName, data):
    with open(fileName, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Data:", data])


@app.route('/ac_control/accuracy', methods=['GET'])
def ac_status_accuracy():
    global ac_accuracy
    global time_ac_control_accuracy

    start_time = time.time()
    accuracy_value = ac_accuracy
    time_ac_control_accuracy = time.time() - start_time
    print("---ac accuracy %s seconds ---" % time_ac_control_accuracy)
    write_to_csv('time_ac_control_accuracy.csv', accuracy_value)
    write_to_csv('ac_control_accuracy.csv', time_ac_control_accuracy)
    return str(accuracy_value)


@app.route('/speed/accuracy', methods=['GET'])
def speed_accuracy_output():
    global speed_accuracy
    global time_speed_accuracy
    start_time = time.time()
    accuracy_value = speed_accuracy
    time_speed_accuracy = time.time() - start_time
    print("---ac accuracy %s seconds ---" % time_speed_accuracy)
    write_to_csv('speed_accuracy.csv', accuracy_value)
    write_to_csv('time_speed_accuracy.csv', time_speed_accuracy)

    return str(accuracy_value)


def get_ac_control_y_test_data():
    global time_get_ac_control_y_test_data
    start_time = time.time()
    try:
        req = requests.get("http://localhost:3001/ac_control/y_test")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    time_get_ac_control_y_test_data = time.time() - start_time
    print("--- time_get_ac_control_y_test_data %s seconds ---" % time_get_ac_control_y_test_data)
    write_to_csv('time_ac_control_get_y_test_data.csv', time_get_ac_control_y_test_data)
    return finalNumpyArray


def get_ac_control_predict_data():
    global time_get_ac_control_predict_data
    start_time = time.time()
    try:
        req = requests.get("http://localhost:3003/ac_control/predict")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    time_get_ac_control_predict_data = time.time() - start_time
    print("---time_get_ac_control_predict_data %s seconds ---" % time_get_ac_control_predict_data)
    return finalNumpyArray


def get_speed_y_test_data():
    global time_get_speed_y_test_data
    start_time = time.time()
    try:
        req = requests.get("http://localhost:3001/speed/y_test")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    time_get_speed_y_test_data = time.time() - start_time
    print("---time_get_speed_y_test_data %s seconds ---" % time_get_speed_y_test_data)
    return finalNumpyArray


def get_speed_predict_data():
    global time_get_speed_predict_data
    start_time = time.time()
    try:
        req = requests.get("http://localhost:3201/speed/predict")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    time_get_speed_predict_data = time.time() - start_time
    print("---time_get_speed_predict_data %s seconds ---" % time_get_speed_predict_data)
    return finalNumpyArray


def ac_control_accuracy():
    global time_ac_control_accuracy_function
    start_time = time.time()
    global ac_accuracy

    y_test = get_ac_control_y_test_data()
    predict_data = get_ac_control_predict_data()

    print("y_test len", len(y_test))
    print("predict len", len(predict_data))

    ac_accuracy = accuracy_score(y_test[:len(predict_data)], predict_data)
    print('AC Control Accuracy: ', ac_accuracy)
    time_ac_control_accuracy_function = time.time() - start_time
    write_to_csv('time_ac_control_accuracy_function.csv', time_ac_control_accuracy_function)


def speed_accuracy_check():
    global time_speed_accuracy_function
    start_time = time.time()
    global speed_accuracy
    y_test = get_speed_y_test_data()
    predict_data = get_speed_predict_data()

    print("y_test len", len(y_test))
    print("predict len", len(predict_data))

    speed_accuracy = accuracy_score(y_test[:len(predict_data)], predict_data)
    print('Speed Accuracy: ', speed_accuracy)
    time_speed_accuracy_function = time.time() - start_time
    write_to_csv('time_speed_accuracy_function.csv', time_speed_accuracy_function)


@app.route('/roof/accuracy/time', methods=['GET'])
# @cache.cached(timeout=300)
def accuracy_time():
    global total
    global time_ac_control_accuracy
    global time_speed_accuracy

    total = time_ac_control_accuracy + time_speed_accuracy

    write_to_csv('accuracy_time_Total.csv', total)
    return str(total)


ac_accuracy_automated = RepeatedTimer(25, ac_control_accuracy)
speed_accuracy_automated = RepeatedTimer(25, speed_accuracy_check)
time_automated = RepeatedTimer(5, accuracy_time)

b = datetime.datetime.now()
print("Execution Time:")
print(b - a)

if __name__ == '__main__':
    app.run(port=3002, host='0.0.0.0', debug=True)
