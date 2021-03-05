# Load libraries
import csv

import numpy as np

from sklearn.metrics import classification_report

import requests
from flask import Flask

import json
from json import JSONEncoder

import time
import datetime

a = datetime.datetime.now()


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


app = Flask(__name__)
time_ac_classification_report_output = 0
time_speed_classification_report_output = 0
total = 0
# time_get_ac_control_y_test_data = 0
# time_get_ac_control_predict_data = 0
# time_get_speed_y_test_data = 0
# time_get_speed_predict_data = 0


def write_to_csv(fileName, data):
    with open(fileName, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Data:", data])


@app.route('/ac_control/classification_report', methods=['GET'])
def ac_classification_report_output():
    global time_ac_classification_report_output
    start_time = time.time()
    ac_control_classification_report_function()
    time_ac_classification_report_output = time.time() - start_time
    print("---time_ac_classification_report_output ac %s seconds ---" % time_ac_classification_report_output)
    write_to_csv('time_ac_classification_report_output.csv', time_ac_classification_report_output)
    return "classification report"
    # return str(confusion_matrix_value)


@app.route('/speed/classification_report', methods=['GET'])
def speed_classification_report_output():
    global time_speed_classification_report_output
    start_time = time.time()
    speed_classification_report_function()
    time_speed_classification_report_output = time.time() - start_time
    print("---time_speed_classification_report_output ac %s seconds ---" % time_speed_classification_report_output)
    write_to_csv('time_speed_classification_report_output.csv', time_speed_classification_report_output)
    return "classification report"
    # return str(confusion_matrix_value)


def get_ac_control_y_test_data():
    global time_get_ac_control_y_test_data
    start_time = time.time()
    try:
        req = requests.get("http://192.168.1.100:3001/ac_control/y_test")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    time_get_ac_control_y_test_data = time.time() - start_time
    print("---time_get_ac_control_y_test_data %s seconds ---" % time_get_ac_control_y_test_data)
    return finalNumpyArray


def get_ac_control_predict_data():
    global time_get_ac_control_predict_data
    start_time = time.time()
    try:
        req = requests.get("http://192.168.1.106:3003/ac_control/predict")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    time_get_ac_control_predict_data = time.time() - start_time
    print("---time_get_ac_control_predict_data  %s seconds ---" % time_get_ac_control_predict_data)
    return finalNumpyArray


def get_speed_y_test_data():
    global time_get_speed_y_test_data
    start_time = time.time()
    try:
        req = requests.get("http://192.168.1.100:3001/speed/y_test")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    time_get_speed_y_test_data = time.time() - start_time
    print("---time_ac_classification_report_output ac %s seconds ---" % time_get_speed_y_test_data)
    return finalNumpyArray


def get_speed_predict_data():
    global time_get_speed_predict_data
    start_time = time.time()
    try:
        req = requests.get("http://192.168.1.106:3201/speed/predict")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    time_get_speed_predict_data = time.time() - start_time
    print("---time_get_speed_predict_data %s seconds ---" % time_get_speed_predict_data)
    return finalNumpyArray


def ac_control_classification_report_function():
    print('classification_report: ')
    y_test = get_ac_control_y_test_data()
    predict_data = get_ac_control_predict_data()

    print("y_test len", len(y_test))
    print("predict len", len(predict_data))

    print(classification_report(y_test[:len(predict_data)], predict_data))


def speed_classification_report_function():
    print('classification_report: ')
    y_test = get_speed_y_test_data()
    predict_data = get_speed_predict_data()

    print("y_test len", len(y_test))
    print("predict len", len(predict_data))

    print(classification_report(y_test[:len(predict_data)], predict_data))


@app.route('/roof/classification/time', methods=['GET'])
# @cache.cached(timeout=300)
def speed_time():
    global total
    global time_ac_classification_report_output
    global time_speed_classification_report_output

    total = time_ac_classification_report_output + time_speed_classification_report_output

    write_to_csv('classification_time_Total.csv', total)
    return str(total)


b = datetime.datetime.now()
print("Execution Time:")
print(b - a)

if __name__ == '__main__':
    app.run(port=3005, host='0.0.0.0', debug=True)
