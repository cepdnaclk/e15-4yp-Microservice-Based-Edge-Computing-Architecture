# Load libraries
import csv
import json
import socket
import time
from json import JSONEncoder
from threading import Timer

import numpy as np
import requests
# from dask.tests.test_system import psutil
from flask import Flask, request


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

cpu_usage_data = 0
memory_usage_data = 0
raspberry_temperature_data = 0
performance_data = 0
total = 0
rasp1_status = 0
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
requests.post("http://0.0.0.0:3006/connectNode", data=local_ip)


def send_off_load_data(off_load_score):
    json_map = {"ipAddress": local_ip,
                "offLoad": off_load_score
                }
    result = json.dumps(json_map)
    requests.post("http://0.0.0.0:3006/offLoadData", json=result)


def write_to_csv(fileName, data):
    with open(fileName, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Data:", data])


@app.route('/updateIPAddresses', methods=['POST'])
def updateIpAddresses():
    ipAddressJson = request.get_json()
    ac_control_ip = ipAddressJson['ac_control_ip']
    speed_ip = ipAddressJson['speed_ip']
    accuracy_ip = ipAddressJson['accuracy_ip']
    classification_ip = ipAddressJson['classification_ip']
    confusion_ip = ipAddressJson['confusion_ip']
    processing_ip = ipAddressJson['processing_ip']
    # Send those IP's to other servicese...


@app.route('/roof/rasp1/total_time', methods=['GET'])
def performance():
    ac_time = get_ac_control_time()
    speed_time = get_speed_time()
    rasp1_time = ac_time + speed_time
    ac_time = 0
    speed_time = 0
    print("time", rasp1_time)
    return str(rasp1_time)


@app.route('/roof/performance/time', methods=['GET'])
def performance_time():
    global total

    global cpu_usage_data
    global memory_usage_data
    global performance_data
    total = cpu_usage_data + memory_usage_data + performance_data
    write_to_csv('performance_tme_total.csv', total)
    return float(total)


def get_ac_control_time():
    try:
        req = requests.get("http://localhost:3003/roof/ac_control/time")
        ac_time = float(req.text)

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return ac_time


def get_speed_time():
    try:
        req = requests.get("http://localhost:3201/roof/speed/time")
        speed_time = float(req.text)

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return speed_time


def automated_data_request():
    # get_cpu_measure_data()
    performance()
    # get_memory_usage()
    # net_usage()
    # network_io()
    performance_time()


# data_request_automated = RepeatedTimer(1, automated_data_request)


if __name__ == '__main__':
    app.run(port=3009, debug=True, host='0.0.0.0')
