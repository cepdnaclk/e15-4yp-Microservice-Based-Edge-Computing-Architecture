# Load libraries
from threading import Timer

from sklearn.model_selection import train_test_split
import numpy as np

import requests
from flask import Flask
import json

from json import JSONEncoder
import time
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

# Ip adresses of system devices
testbed_ip_address = "192.168.1.112"

air_condition_data_array = []
passenger_count_data_array = []
window_opening_data_array = []
pitch_data_array = []
rain_intensity_data_array = []
visibility_data_array = []
driver_rush_data_array = []
speed_data_array = []

speed_x_train_data = []
speed_x_test_data = []
speed_y_train_data = []
speed_y_test_data = []
speed_input = []

ac_x_train = []
ac_x_test = []
ac_y_train = []
ac_y_test = []
ac_input = []

time_get_roof_speed_data = 0
time_get_roof_driver_rush_data = 0
time_get_roof_visibility_data = 0
time_get_roof_rain_intensity_data = 0
time_get_roof_pitch_data = 0
time_get_roof_ac_data = 0
time_get_roof_passenger_data = 0
time_get_roof_window_data = 0
time_get_speed_input = 0
time_get_speed_x_train = 0
time_get_speed_x_test = 0
time_get_speed_y_test = 0
time_get_speed_y_train = 0
time_get_ac_control_input = 0
time_get_ac_control_x_test = 0
time_get_ac_control_x_train = 0
time_get_ac_control_y_test = 0
time_get_ac_control_y_train = 0
time_testbed_pitch_data = 0
time_testbed_rain_intensity_data = 0
time_testbed_visibility_data = 0
time_testbed_driver_rush_data = 0
time_testbed_vehicle_speed_data = 0
time_testbed_air_condition_data = 0
time_testbed_passenger_count_data = 0
time_testbed_window_opening_data = 0
time_function_ac_control_train_split = 0
time_function_speed_train_split = 0
total = 0


def write_to_csv(fileName, data):
    with open(fileName, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Data:", data])


# Sent Data To the FOG

@app.route('/roof/speed_data', methods=['GET'])
# @cache.cached(timeout=300)
def speed_data():
    global speed_data_array
    global time_get_roof_speed_data
    start_time = time.time()
    number_array = speed_data_array
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    time_get_roof_speed_data = time.time() - start_time
    print("---speed time_get_roof_speed_data %s seconds ---" % time_get_roof_speed_data)
    print("----roof speed_data amount of data = %s ------" % len(number_array))
    write_to_csv('time_get_roof_speed_data.csv', time_get_roof_speed_data)
    return encodedNumpyData


@app.route('/roof/driver_rush_data', methods=['GET'])
# @cache.cached(timeout=300)
def driver_rush_data():
    global driver_rush_data_array
    global time_get_roof_driver_rush_data
    start_time = time.time()
    start_time = time.time()
    number_array = driver_rush_data_array
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    time_get_roof_driver_rush_data = time.time() - start_time
    print("--- time_get_roof_driver_rush_data %s seconds ---" % time_get_roof_driver_rush_data)
    print("----roof driver_rush_data amount of data = %s ------" % len(number_array))
    write_to_csv('time_get_roof_driver_rush_data.csv', time_get_roof_driver_rush_data)
    return encodedNumpyData


@app.route('/roof/visibility_data', methods=['GET'])
# @cache.cached(timeout=300)
def visibility_data():
    global visibility_data_array
    global time_get_roof_visibility_data
    start_time = time.time()
    number_array = visibility_data_array
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    time_get_roof_visibility_data = time.time() - start_time
    print("---speed time_get_roof_visibility_data %s seconds ---" % time_get_roof_visibility_data)
    print("----roof visibility_data amount of data = %s ------" % len(number_array))
    write_to_csv('time_get_roof_visibility_data.csv', time_get_roof_visibility_data)
    return encodedNumpyData


@app.route('/roof/rain_intensity_data', methods=['GET'])
# @cache.cached(timeout=300)
def rain_intensity_data():
    global rain_intensity_data_array
    global time_get_roof_rain_intensity_data
    start_time = time.time()
    number_array = rain_intensity_data_array
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    time_get_roof_rain_intensity_data = time.time() - start_time
    print("-- time_get_roof_rain_intensity_data %s seconds ---" % time_get_roof_rain_intensity_data)
    print("----roof rain_intensity_data amount of data = %s ------" % len(number_array))
    write_to_csv('time_get_roof_rain_intensity_data.csv', time_get_roof_rain_intensity_data)
    return encodedNumpyData


@app.route('/roof/pitch_data', methods=['GET'])
# @cache.cached(timeout=300)
def pitch_data():
    global pitch_data_array
    global time_get_roof_pitch_data
    start_time = time.time()
    number_array = pitch_data_array
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    time_get_roof_pitch_data = time.time() - start_time
    print("--- time_get_roof_pitch_data %s seconds ---" % time_get_roof_pitch_data)
    print("----roof pitch_data amount of data = %s ------" % len(number_array))
    write_to_csv('time_get_roof_pitch_data.csv', time_get_roof_pitch_data)
    return encodedNumpyData


@app.route('/roof/ac_data', methods=['GET'])
# @cache.cached(timeout=300)
def ac_data():
    global air_condition_data_array
    global time_get_roof_ac_data
    start_time = time.time()
    number_array = air_condition_data_array
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    time_get_roof_ac_data = time.time() - start_time
    print("--- time_get_roof_ac_data %s seconds ---" % time_get_roof_ac_data)
    print("----roof ac_data amount of data = %s ------" % len(number_array))
    write_to_csv('time_get_roof_ac_data.csv', time_get_roof_ac_data)
    return encodedNumpyData


@app.route('/roof/passenger_data', methods=['GET'])
# @cache.cached(timeout=300)
def passenger_data():
    global passenger_count_data_array
    global time_get_roof_passenger_data
    start_time = time.time()
    number_array = passenger_count_data_array
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    time_get_roof_passenger_data = time.time() - start_time
    print("--- time_get_roof_passenger_data %s seconds ---" % time_get_roof_passenger_data)
    print("----roof passenger_data amount of data = %s ------" % len(number_array))
    write_to_csv('time_get_roof_passenger_data.csv', time_get_roof_passenger_data)
    return encodedNumpyData


@app.route('/roof/window_data', methods=['GET'])
# @cache.cached(timeout=300)
def window_data():
    global window_opening_data_array
    global time_get_roof_window_data
    start_time = time.time()
    number_array = window_opening_data_array
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    time_get_roof_window_data = time.time() - start_time
    print("--- time_get_roof_window_data %s seconds ---" % time_get_roof_window_data)
    print("----roof window_data amount of data = %s ------" % len(number_array))
    write_to_csv('time_get_roof_window_data.csv', time_get_roof_window_data)
    return encodedNumpyData


# Speed REST Apis

@app.route('/speed/input', methods=['GET'])
# @cache.cached(timeout=300)
def speed_input_list():
    global speed_input
    global time_get_speed_input
    start_time = time.time()
    number_array = speed_input
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    time_get_speed_input = time.time() - start_time
    print("--- time_get_speed_input %s seconds ---" % time_get_speed_input)
    print("----speed input amount of data = %s ------" % len(number_array))
    write_to_csv('time_get_speed_input.csv', time_get_speed_input)
    return encodedNumpyData


@app.route('/speed/x_train', methods=['GET'])
# @cache.cached(timeout=300)
def speed_x_train():
    global speed_x_train_data
    global time_get_speed_x_train

    start_time = time.time()
    number_array = speed_x_train_data
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    time_get_speed_x_train = time.time() - start_time
    print("--- time_get_speed_x_train %s seconds ---" % time_get_speed_x_train)
    print("----speed x_train amount of data = %s ------" % len(number_array))
    write_to_csv('time_get_speed_x_train.csv', time_get_speed_x_train)
    return encodedNumpyData


@app.route('/speed/x_test', methods=['GET'])
# @cache.cached(timeout=300)
def speed_x_test():
    global speed_x_test_data
    global time_get_speed_x_test
    start_time = time.time()
    number_array = speed_x_test_data
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    time_get_speed_x_test = time.time() - start_time
    print("--- time_get_speed_x_test %s seconds ---" % time_get_speed_x_test)
    print("----speed x_test_amount of data = %s ------" % len(number_array))
    write_to_csv('time_get_speed_x_test.csv', time_get_speed_x_test)
    return encodedNumpyData


@app.route('/speed/y_test', methods=['GET'])
# @cache.cached(timeout=300)
def speed_y_test():
    global speed_y_test_data
    global time_get_speed_y_test
    start_time = time.time()
    number_array = speed_y_test_data
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    time_get_speed_y_test = time.time() - start_time
    print("--- time_get_speed_y_test %s seconds ---" % time_get_speed_y_test)
    print("----speed y_test_amount of data = %s ------" % len(number_array))
    write_to_csv('time_get_speed_y_test.csv', time_get_speed_y_test)
    return encodedNumpyData


@app.route('/speed/y_train', methods=['GET'])
# @cache.cached(timeout=300)
def speed_y_train():
    global speed_y_train_data
    global time_get_speed_y_train
    start_time = time.time()
    number_array = speed_y_train_data
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    time_get_speed_y_train = time.time() - start_time
    print("--- time_get_speed_y_train %s seconds ---" % time_get_speed_y_train)
    print("----speed x_test_amount of data = %s ------" % len(number_array))
    write_to_csv('time_get_speed_y_train.csv', time_get_speed_y_train)
    return encodedNumpyData


# AC REST Apis

@app.route('/ac_control/input', methods=['GET'])
# @cache.cached(timeout=300)
def ac_control_input_list():
    global ac_input
    global time_get_ac_control_input

    start_time = time.time()
    number_array = ac_input
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    time_get_ac_control_input = time.time() - start_time
    print("--- time_get_ac_control_input %s seconds ---" % time_get_ac_control_input)
    print("----ac_control input amount of data = %s ------" % len(number_array))
    write_to_csv('time_get_ac_control_input.csv', time_get_ac_control_input)
    return encodedNumpyData


@app.route('/ac_control/x_train', methods=['GET'])
# @cache.cached(timeout=300)
def ac_control_x_train():
    global ac_x_train
    global time_get_ac_control_x_train
    print(type(ac_x_train))
    start_time = time.time()
    number_array = ac_x_train
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    time_get_ac_control_x_train = time.time() - start_time
    print("--- time_get_ac_control_x_train %s seconds ---" % time_get_ac_control_x_train)
    print("----ac_control x_train amount of data = %s ------" % len(number_array))
    write_to_csv('time_get_ac_control_x_train.csv', time_get_ac_control_x_train)
    return encodedNumpyData


@app.route('/ac_control/x_test', methods=['GET'])
# @cache.cached(timeout=300)
def ac_control_x_test():
    global ac_x_test
    global time_get_ac_control_x_test

    start_time = time.time()
    number_array = ac_x_test
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    time_get_ac_control_x_test = time.time() - start_time
    print("--- time_get_ac_control_x_test %s seconds ---" % time_get_ac_control_x_test)
    print("----ac_control x_test amount of data = %s ------" % len(number_array))
    write_to_csv('time_get_ac_control_x_test.csv', time_get_ac_control_x_test)
    return encodedNumpyData


@app.route('/ac_control/y_test', methods=['GET'])
# @cache.cached(timeout=300)
def ac_control_y_test():
    global ac_y_test
    global time_get_ac_control_y_test
    start_time = time.time()
    number_array = ac_y_test
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    time_get_ac_control_y_test = time.time() - start_time
    print("--- time_get_ac_control_y_test %s seconds ---" % time_get_ac_control_y_test)
    print("----ac_control y_test amount of data = %s ------" % len(number_array))
    write_to_csv('time_get_ac_control_y_test.csv', time_get_ac_control_y_test)
    return encodedNumpyData


@app.route('/ac_control/y_train', methods=['GET'])
# @cache.cached(timeout=300)
def ac_control_y_train():
    global ac_y_train
    global time_get_ac_control_y_train

    start_time = time.time()
    number_array = ac_y_train
    numpyData = {"array": number_array}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    time_get_ac_control_y_train = time.time() - start_time
    print("--- time_get_ac_control_y_train %s seconds ---" % time_get_ac_control_y_train)
    print("----ac_control y_train amount of data = %s ------" % len(number_array))
    write_to_csv('time_get_ac_control_y_train.csv', time_get_ac_control_y_train)
    return encodedNumpyData


# Getting Data From Testbed

def get_pitch_data():
    global pitch_data_array
    global time_testbed_pitch_data
    start_time = time.time()
    try:
        req = requests.get("http://" + testbed_ip_address + ":5000//data/pitch")
        req_text = req.text[1:-1]
        number = ""
        # number_array = []
        for i in req_text:
            if i == ',':
                # number_array.append(number)
                pitch_data_array.append(float(number))
                number = ""
                continue
            number = number + i
        # number_array = [float(i) for i in number_array]

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    time_testbed_pitch_data = time.time() - start_time
    print("--- time_testbed_pitch_data %s seconds ---" % time_testbed_pitch_data)
    # return number_array


def get_rain_intensity_data():
    global rain_intensity_data_array
    global time_testbed_rain_intensity_data
    start_time = time.time()
    try:
        req = requests.get("http://" + testbed_ip_address + ":5000//data/rainIntensity")
        req_text = req.text[1:-1]
        number = ""
        # number_array = []
        for i in req_text:
            if i == ',':
                # number_array.append(number)
                rain_intensity_data_array.append(float(number))
                number = ""
                continue
            number = number + i
        # number_array = [float(i) for i in number_array]

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    time_testbed_rain_intensity_data = time.time() - start_time
    print("--- time_testbed_rain_intensity_data %s seconds ---" % time_testbed_rain_intensity_data)

    # return number_array


def get_visibility_data():
    global visibility_data_array
    global time_testbed_visibility_data
    start_time = time.time()
    try:
        req = requests.get("http://" + testbed_ip_address + ":5000//data/visibility")
        req_text = req.text[1:-1]
        number = ""
        # number_array = []
        for i in req_text:
            if i == ',':
                # number_array.append(number)
                visibility_data_array.append(float(number))
                number = ""
                continue
            number = number + i
        # number_array = [float(i) for i in number_array]

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    time_testbed_visibility_data = time.time() - start_time
    print("--- time_testbed_visibility_data %s seconds ---" % time_testbed_visibility_data)
    # return number_array


def get_driver_rush_data():
    global driver_rush_data_array
    global time_testbed_driver_rush_data
    start_time = time.time()
    try:
        req = requests.get("http://" + testbed_ip_address + ":5000//data/driver_rush")
        req_text = req.text[1:-1]
        number = ""
        # number_array = []
        for i in req_text:
            if i == ',':
                # number_array.append(number)
                driver_rush_data_array.append(float(number))
                number = ""
                continue
            number = number + i
        # number_array = [float(i) for i in number_array]

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    time_testbed_driver_rush_data = time.time() - start_time
    print("--- time_testbed_driver_rush_data %s seconds ---" % time_testbed_driver_rush_data)
    # return number_array


def get_vehicle_speed_data():
    global speed_data_array
    global time_testbed_vehicle_speed_data
    start_time = time.time()
    try:
        req = requests.get("http://" + testbed_ip_address + ":5000//data/vehicleSpeed")
        req_text = req.text[1:-1]
        number = ""
        # number_array = []
        for i in req_text:
            if i == ',':
                # number_array.append(number)
                speed_data_array.append(float(number))
                number = ""
                continue
            number = number + i
        # print(speed_data_array)
        # number_array = [float(i) for i in number_array]

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    time_testbed_vehicle_speed_data = time.time() - start_time
    print("--- time_testbed_vehicle_speed_data %s seconds ---" % time_testbed_vehicle_speed_data)
    # return number_array


def get_air_condition_data():
    global air_condition_data_array
    global time_testbed_air_condition_data
    start_time = time.time()
    try:
        req = requests.get("http://" + testbed_ip_address + ":5000//data/airConditionStatus")
        req_text = req.text[1:-1]
        number = ""
        # number_array = []
        for i in req_text:
            if i == ',':
                # number_array.append(number)
                air_condition_data_array.append(float(number))
                number = ""
                continue
            number = number + i
        # number_array = [float(i) for i in number_array]

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    time_testbed_air_condition_data = time.time() - start_time
    print("--- time_testbed_air_condition_data %s seconds ---" % time_testbed_air_condition_data)
    # return number_array


def get_passenger_count_data():
    global passenger_count_data_array
    global time_testbed_passenger_count_data
    start_time = time.time()
    try:
        req = requests.get("http://" + testbed_ip_address + ":5000//data/passengerCount")
        req_text = req.text[1:-1]
        number = ""
        # number_array = []
        for i in req_text:
            if i == ',':
                # number_array.append(number)
                passenger_count_data_array.append(float(number))
                number = ""
                continue
            number = number + i
        # number_array = [float(i) for i in number_array]

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    time_testbed_passenger_count_data = time.time() - start_time
    print("--- time_testbed_passenger_count_data %s seconds ---" % time_testbed_passenger_count_data)
    # return number_array


def get_window_opening_data():
    global window_opening_data_array
    global time_testbed_window_opening_data
    start_time = time.time()
    try:
        req = requests.get("http://" + testbed_ip_address + ":5000//data/windowOpening")
        req_text = req.text[1:-1]
        number = ""
        # number_array = []
        for i in req_text:
            if i == ',':
                # number_array.append(number)
                window_opening_data_array.append(float(number))
                number = ""
                continue
            number = number + i
        # number_array = [float(i) for i in number_array]

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    time_testbed_window_opening_data = time.time() - start_time
    print("--- time_testbed_window_opening_data %s seconds ---" % time_testbed_window_opening_data)
    # return number_array


# AC Train Split

def ac_control_train_split():
    global time_function_ac_control_train_split
    start_time = time.time()
    global air_condition_data_array, window_opening_data_array, passenger_count_data_array, ac_x_train, ac_x_test, \
        ac_y_train, ac_y_test, ac_input

    window_opening_data = [int(i) for i in window_opening_data_array]
    passenger_count_data = [int(i) for i in passenger_count_data_array]

    air_condition_data = [int(i) for i in air_condition_data_array]

    X = np.array((passenger_count_data, window_opening_data)).T
    Y = air_condition_data

    if len(X) == len(Y):
        ac_input = X.copy()

        ac_x_train, ac_x_test, ac_y_train, ac_y_test = train_test_split(X, Y, test_size=0.20, random_state=0)

    time_function_ac_control_train_split = time.time() - start_time
    print("--- time_function_ac_control_train_split %s seconds ---" % time_function_ac_control_train_split)
    write_to_csv('time_function_ac_control_train_split.csv', time_function_ac_control_train_split)


# Speed Train Split

def speed_train_split():
    global pitch_data_array, passenger_count_data_array, rain_intensity_data_array, \
        visibility_data_array, driver_rush_data_array, speed_data_array, \
        speed_x_train_data, speed_x_test_data, speed_y_train_data, speed_y_test_data, speed_input
    global time_function_speed_train_split
    start_time = time.time()

    pitch_data = [int(i) for i in pitch_data_array]
    passenger_count_data = [int(i) for i in passenger_count_data_array]
    rain_intensity_data = [int(i) for i in rain_intensity_data_array]
    visibility_data = [int(i) for i in visibility_data_array]
    driver_rush_data = [int(i) for i in driver_rush_data_array]

    speed_data = [float(i) for i in speed_data_array]

    X = np.array(
        (pitch_data, passenger_count_data, rain_intensity_data, visibility_data, driver_rush_data)).T
    Y = speed_data

    if len(X) == len(Y):

        for i in range(len(Y)):
            if Y[i] == 0:
                Y[i] = 0
            elif Y[i] <= 5:
                Y[i] = 1
            elif Y[i] <= 10:
                Y[i] = 2
            elif Y[i] <= 15:
                Y[i] = 3
            elif Y[i] <= 20:
                Y[i] = 4
            elif Y[i] > 20:
                Y[i] = 5
                Y[i] = 5

        speed_input = X.copy()

        speed_x_train_data, speed_x_test_data, speed_y_train_data, speed_y_test_data = train_test_split(X, Y,
                                                                                                        test_size=0.20
                                                                                                        ,
                                                                                                        random_state=0)

        time_function_speed_train_split = time.time() - start_time
        print("--- time_function_speed_train_split %s seconds ---" % time_function_speed_train_split)
        write_to_csv('time_function_speed_train_split.csv', time_function_speed_train_split)
        # print(speed_y_train_data)


@app.route('/roof/processing/time', methods=['GET'])
# @cache.cached(timeout=300)
def processing_time():
    global total
    global time_get_roof_speed_data
    global time_get_roof_driver_rush_data
    global time_get_roof_visibility_data
    global time_get_roof_rain_intensity_data
    global time_get_roof_pitch_data
    global time_get_roof_ac_data
    global time_get_roof_passenger_data
    global time_get_roof_window_data
    global time_get_speed_input
    global time_get_speed_x_train
    global time_get_speed_x_test
    global time_get_speed_y_test
    global time_get_speed_y_train
    global time_get_ac_control_input
    global time_get_ac_control_x_test
    global time_get_ac_control_x_train
    global time_get_ac_control_y_test
    global time_get_ac_control_y_train
    global time_function_ac_control_train_split
    global time_function_speed_train_split
    total = time_get_roof_speed_data + time_get_roof_driver_rush_data + time_get_roof_visibility_data + time_get_roof_rain_intensity_data + \
            time_get_roof_pitch_data + time_get_roof_ac_data + time_get_roof_passenger_data + time_get_roof_passenger_data + time_get_roof_window_data + \
            time_get_speed_input + time_get_speed_x_train + time_get_speed_x_test + time_get_speed_y_test + time_get_speed_y_train + time_get_ac_control_input + \
            time_get_ac_control_x_test + time_get_ac_control_x_train + time_get_ac_control_y_test + time_get_ac_control_y_train + time_function_ac_control_train_split + \
            time_function_ac_control_train_split + time_function_speed_train_split
    write_to_csv('processing_Total.csv', total)
    return str(total)


def automated_train_split():
    ac_control_train_split()
    speed_train_split()


passenger_data_automated = RepeatedTimer(5, get_passenger_count_data)
window_data_automated = RepeatedTimer(5, get_window_opening_data)
ac_data_automated = RepeatedTimer(5, get_air_condition_data)
pitch_data_automated = RepeatedTimer(5, get_pitch_data)
rain_intensity_data_automated = RepeatedTimer(5, get_rain_intensity_data)
visibility_data_automated = RepeatedTimer(5, get_visibility_data)
driver_rush_data_automated = RepeatedTimer(5, get_driver_rush_data)
speed_data_automated = RepeatedTimer(5, get_vehicle_speed_data)


train_split_automated = RepeatedTimer(11, automated_train_split)
time_automated = RepeatedTimer(1, processing_time)

b = datetime.datetime.now()
print("Execution Time:")
print(b - a)

if __name__ == '__main__':
    app.run(port=3001, host='0.0.0.0')
