# Load libraries
import numpy as np
from numpy import argmax
import requests
from flask import Flask

import json
from json import JSONEncoder
import csv
import time
from threading import Timer
import datetime

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


app = Flask(__name__)

fog_ip_address = "192.168.1.112"
cloud_ip_address = "34.126.124.227"

time_speed_predict = 0
time_speed_output = 0
time_speed_get_x_train_data = 0
time_speed_get_y_train_data = 0
time_speed_get_x_test_data = 0
time_speed_get_y_test_data = 0
time_speed_get_input_data = 0
time_speed_get_fog_wh = 0
time_speed_get_fog_bh = 0
time_speed_get_fog_wo = 0
time_speed_get_fog_bo = 0
time_speed_get_cloud_wh = 0
time_speed_get_cloud_bh = 0
time_speed_get_cloud_wo = 0
time_speed_get_cloud_bo = 0
time_speed_get_roof_accuracy = 0
time_speed_get_fog_accuracy = 0
time_speed_get_cloud_accuracy = 0
time_speed_model_train = 0
total = 0


y_predict_array = []

input_nodes = 5
hidden_nodes = 8
output_labels = 6
wh = np.random.rand(input_nodes, hidden_nodes)
bh = np.random.randn(hidden_nodes)
wo = np.random.rand(hidden_nodes, output_labels)
bo = np.random.randn(output_labels)


def write_to_csv(fileName, data):
    with open(fileName, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Data:", data])


@app.route('/speed/predict', methods=['GET'])
# @cache.cached(timeout=300)
def predict_data():
    global time_speed_predict
    start_time = time.time()
    number_array = predict_output()
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    time_speed_predict = time.time() - start_time
    print("---speed time_speed_predict %s seconds ---" % time_speed_predict)
    print("----speed predict amount of data = %s ------" % len(number_array))
    write_to_csv('time_speed_predict.csv', time_speed_predict)
    return encodedNumpyData


# @app.route('/speed/output', methods=['GET'])
# # @cache.cached(timeout=300)
# def output_data():
#     global time_speed_output
#     start_time = time.time()
#     number_array = output()
#     numpyData = {"array": number_array}
#     encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
#     time_speed_output = time.time() - start_time
#     print("---speed time_speed_output %s seconds ---" % time_speed_output)
#     print("----speed output amount of data = %s ------" % len(number_array))
#     write_to_csv('time_speed_output.csv', time_speed_output)
#
#     return encodedNumpyData

@app.route('/roof/wh', methods=['GET'])
# @cache.cached(timeout=300)
def wh_data():
    global wh

    start_time = time.time()
    number_array = wh
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---output_data %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/roof/bh', methods=['GET'])
# @cache.cached(timeout=300)
def bh_data():
    global bh

    start_time = time.time()
    number_array = bh
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---output_data %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/roof/wo', methods=['GET'])
# @cache.cached(timeout=300)
def wo_data():
    global wo

    start_time = time.time()
    number_array = wo
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---output_data %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


@app.route('/roof/bo', methods=['GET'])
# @cache.cached(timeout=300)
def bo_data():
    global bo

    start_time = time.time()
    number_array = bo
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("---output_data %s seconds ---" % (time.time() - start_time))
    return encodedNumpyData


def get_x_train_data():
    global time_speed_get_x_train_data
    start_time = time.time()
    try:
        req = requests.get("http://localhost:3001/speed/x_train")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    time_speed_get_x_train_data = time.time() - start_time
    print("---speed time_speed_get_x_train_data %s seconds ---" % time_speed_get_x_train_data)
    return finalNumpyArray


def get_y_train_data():
    global time_speed_get_y_train_data
    start_time = time.time()
    try:
        req = requests.get("http://localhost:3001/speed/y_train")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    time_speed_get_y_train_data = time.time() - start_time
    print("---speed time_speed_get_y_train_data %s seconds ---" % time_speed_get_y_train_data)
    return finalNumpyArray


def get_x_test_data():
    global time_speed_get_x_test_data
    start_time = time.time()
    try:
        req = requests.get("http://localhost:3001/speed/x_test")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    time_speed_get_x_test_data = time.time() - start_time
    print("---speed time_speed_get_x_test_data %s seconds ---" % time_speed_get_x_test_data)
    return finalNumpyArray


def get_y_test_data():
    global time_speed_get_y_test_data
    start_time = time.time()
    try:
        req = requests.get("http://localhost:3001/speed/y_test")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    time_speed_get_y_test_data = time.time() - start_time
    print("---speed time_speed_get_y_test_data %s seconds ---" % time_speed_get_y_test_data)
    return finalNumpyArray


def get_input_data():
    global time_speed_get_input_data
    start_time = time.time()
    try:
        req = requests.get("http://localhost:3001/speed/input")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    time_speed_get_input_data = time.time() - start_time
    print("---speed time_speed_get_input_data %s seconds ---" % time_speed_get_input_data)
    return finalNumpyArray


def get_fog_wh():
    global time_speed_get_fog_wh
    start_time = time.time()
    try:
        req = requests.get("http://" + fog_ip_address + ":4201/fog/wh")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    time_speed_get_fog_wh = time.time() - start_time
    print("---speed time_speed_get_fog_wh %s seconds ---" % time_speed_get_fog_wh)
    return finalNumpyArray


def get_fog_bh():
    global time_speed_get_fog_bh
    start_time = time.time()
    try:
        req = requests.get("http://" + fog_ip_address + ":4201/fog/bh")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    time_speed_get_fog_bh = time.time() - start_time
    print("---speed time_speed_get_fog_bh %s seconds ---" % time_speed_get_fog_bh)
    return finalNumpyArray


def get_fog_wo():
    global time_speed_get_fog_wo
    start_time = time.time()
    try:
        req = requests.get("http://" + fog_ip_address + ":4201/fog/wo")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    time_speed_get_fog_wo = time.time() - start_time
    print("---speed time_speed_get_fog_wo %s seconds ---" % time_speed_get_fog_wo)
    return finalNumpyArray


def get_fog_bo():
    global time_speed_get_fog_bo
    start_time = time.time()
    try:
        req = requests.get("http://" + fog_ip_address + ":4201/fog/bo")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    time_speed_get_fog_bo = time.time() - start_time
    print("---speed time_speed_get_fog_bo %s seconds ---" % time_speed_get_fog_bo)
    return finalNumpyArray


def get_cloud_wh():
    global time_speed_get_cloud_wh
    start_time = time.time()
    try:
        req = requests.get("http://" + cloud_ip_address + ":5201/cloud/wh")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    time_speed_get_cloud_wh = time.time() - start_time
    print("---speed time_speed_get_cloud_wh %s seconds ---" % time_speed_get_cloud_wh)
    return finalNumpyArray


def get_cloud_bh():
    global time_speed_get_cloud_bh
    start_time = time.time()
    try:
        req = requests.get("http://" + cloud_ip_address + ":5201/cloud/bh")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    time_speed_get_cloud_bh = time.time() - start_time
    print("---speed time_speed_get_cloud_bh %s seconds ---" % time_speed_get_cloud_bh)
    return finalNumpyArray


def get_cloud_wo():
    global time_speed_get_cloud_wo
    start_time = time.time()
    try:
        req = requests.get("http://" + cloud_ip_address + ":5201/cloud/wo")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    time_speed_get_cloud_wo = time.time() - start_time
    print("---speed time_speed_get_cloud_wo %s seconds ---" % time_speed_get_cloud_wo)
    return finalNumpyArray


def get_cloud_bo():
    global time_speed_get_cloud_bo
    start_time = time.time()
    try:
        req = requests.get("http://" + cloud_ip_address + ":5201/cloud/bo")
        decodedArrays = json.loads(req.text)

        finalNumpyArray = np.asarray(decodedArrays["array"])

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    time_speed_get_cloud_bo = time.time() - start_time
    print("---speed time_speed_get_cloud_bo %s seconds ---" % time_speed_get_cloud_bo)
    return finalNumpyArray


def get_roof_accuracy():
    global time_speed_get_roof_accuracy
    start_time = time.time()
    try:
        req = requests.get("http://localhost:3002/speed/accuracy")
        accuracy = float(req.text)

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    time_speed_get_roof_accuracy = time.time() - start_time
    print("---speed time_speed_get_roof_accuracy %s seconds ---" % time_speed_get_roof_accuracy)
    return accuracy


def get_fog_accuracy():
    global time_speed_get_fog_accuracy
    start_time = time.time()
    try:
        req = requests.get("http://" + fog_ip_address + ":4002/speed/accuracy")
        accuracy = float(req.text)

    except requests.exceptions.ConnectionError:
        return 0.0
    time_speed_get_fog_accuracy = time.time() - start_time
    print("---speed time_speed_get_fog_accuracy %s seconds ---" % time_speed_get_fog_accuracy)
    return accuracy


def get_cloud_accuracy():
    global time_speed_get_cloud_accuracy
    start_time = time.time()
    try:
        req = requests.get("http://" + cloud_ip_address + ":5002/speed/accuracy")
        accuracy = float(req.text)

    except requests.exceptions.ConnectionError:
        return 0.0
    time_speed_get_cloud_accuracy = time.time() - start_time
    print("---speed time_speed_get_cloud_accuracy %s seconds ---" % time_speed_get_cloud_accuracy)
    return accuracy


def model_train():
    global time_speed_model_train
    start_time = time.time()
    global y_predict_array, wh, wo, bh, bo

    y_train = get_y_train_data()
    # print("y_train", y_train)
    x_train = get_x_train_data()
    x_test = get_x_test_data()
    y_test = get_y_test_data()

    if len(x_test) == len(y_test) and len(x_train) == len(y_train):

        # create a matrix for one hot encoding
        one_hot_labels = np.zeros((len(y_train), 6))
        for i in range(len(y_train)):
            # print("Y_train", y_train)
            # print("Y_train i", y_train[i])
            one_hot_labels[i, y_train[i]] = 1

        # input_nodes = 5
        # hidden_nodes = 8
        # output_labels = 6
        # wh = np.random.rand(input_nodes, hidden_nodes)
        # bh = np.random.randn(hidden_nodes)
        # wo = np.random.rand(hidden_nodes, output_labels)
        # bo = np.random.randn(output_labels)
        lr = 10e-4

        error_cost = []

        for epoch in range(5000):
            ############# feedforward

            # Phase 1
            zh = np.dot(x_train, wh) + bh
            ah = sigmoid(zh)
            zo = np.dot(ah, wo) + bo
            ao = softmax(zo)

            ########## Back Propagation

            ########## Phase 1

            dcost_dzo = ao - one_hot_labels
            dzo_dwo = ah

            dcost_wo = np.dot(dzo_dwo.T, dcost_dzo)

            dcost_bo = dcost_dzo

            ########## Phases 2

            dzo_dah = wo
            dcost_dah = np.dot(dcost_dzo, dzo_dah.T)
            dah_dzh = sigmoid_der(zh)
            dzh_dwh = x_train
            dcost_wh = np.dot(dzh_dwh.T, dah_dzh * dcost_dah)

            dcost_bh = dcost_dah * dah_dzh

            # Update Weights ================

            wh -= lr * dcost_wh
            bh -= lr * dcost_bh.sum(axis=0)

            wo -= lr * dcost_wo
            bo -= lr * dcost_bo.sum(axis=0)

            if epoch % 200 == 0:
                loss = np.sum(-one_hot_labels * np.log(ao))
                # print('Loss function value: ', loss)
                error_cost.append(loss)

        # End of for loop (End of training phase)

        roof_accuracy = get_roof_accuracy()
        fog_accuracy = get_fog_accuracy()
        cloud_accuracy = get_cloud_accuracy()

        print("roof", roof_accuracy)
        print("fog", fog_accuracy)

        if fog_accuracy > roof_accuracy:

            if cloud_accuracy > fog_accuracy:
                wh = get_cloud_wh()
                bh = get_cloud_bh()
                wo = get_cloud_wo()
                bo = get_cloud_bo()
            else:
                wh = get_fog_wh()
                bh = get_fog_bh()
                wo = get_fog_wo()
                bo = get_fog_bo()

        # Make predictions
        predictions = predict(wh, bh, wo, bo, x_test)

        y_predict = []
        for i in range(len(y_test)):
            n = argmax(predictions[i])
            y_predict.append(n)
        y_predict_array = np.array(y_predict)

        print("y_pred", y_predict_array)
        time_speed_model_train = time.time() - start_time
        print("---speed time_speed_model_train %s seconds ---" % time_speed_model_train)
        write_to_csv('time_speed_model_train.csv', time_speed_model_train)


def predict_output():
    global y_predict_array
    # model_train()

    return y_predict_array


@app.route('/roof/speed/time', methods=['GET'])
# @cache.cached(timeout=300)
def speed_time():
    global total
    global time_speed_predict
    global time_speed_output
    global time_speed_get_x_train_data
    global time_speed_get_y_train_data
    global time_speed_get_x_test_data
    global time_speed_get_y_test_data
    global time_speed_get_input_data
    global time_speed_model_train
    total = time_speed_predict + time_speed_output + time_speed_get_x_train_data + time_speed_get_y_train_data + \
            time_speed_get_x_test_data + time_speed_get_y_test_data + time_speed_get_input_data + time_speed_model_train

    write_to_csv('speed_time_Total.csv', total)
    return str(total)


model_train_automated = RepeatedTimer(15, model_train)
time_automated = RepeatedTimer(1, speed_time)
b = datetime.datetime.now()
print("Execution Time:")
print(b - a)

if __name__ == '__main__':
    app.run(port=3201, host='0.0.0.0')
