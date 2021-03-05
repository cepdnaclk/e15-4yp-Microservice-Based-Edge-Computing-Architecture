# Load libraries
import csv
import os
import time
from threading import Timer
import numpy as np
from dask.tests.test_system import psutil
from flask import Flask
from json import JSONEncoder
import requests
import json
import psutil
import sys
from subprocess import Popen


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


def write_to_csv(fileName, data):
    with open(fileName, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Data:", data])


@app.route('/roof/rasp2/total_time', methods=['GET'])
def performance():
    accuracy_time = get_accuracy_time()
    classification_time = get_classification_time()
    confusion_time = get_confusion_time()
    rasp2_time = accuracy_time + classification_time + confusion_time
    accuracy_time = 0
    classification_time = 0
    confusion_time = 0
    print("time", rasp2_time)
    return str(rasp2_time)


@app.route('/roof/rasp2/memory', methods=['GET'])
def get_memory_usage():
    global memory_usage_data
    memory_usage_data = psutil.virtual_memory().percent
    print('Memory usage:', memory_usage_data)
    write_to_csv('memory_usage_data.csv', memory_usage_data)
    return memory_usage_data


def get_cpu_measure_data():
    global cpu_usage_data
    cpu_usage_data = psutil.cpu_percent()
    print("cpu", cpu_usage_data)
    write_to_csv('cpu_usage_data.csv', cpu_usage_data)
    return cpu_usage_data


def get_system_load():
    system_load = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
    print('system_load:', system_load)
    write_to_csv('system_load.csv', system_load)
    return system_load


def network_io():
    bytes_sent = psutil.net_io_counters().bytes_sent
    bytes_recv = psutil.net_io_counters().bytes_recv
    packets_sent = psutil.net_io_counters().packets_sent
    packets_recv = psutil.net_io_counters().packets_recv
    errin = psutil.net_io_counters().errin
    errout = psutil.net_io_counters().errout
    dropin = psutil.net_io_counters().dropin
    dropout = psutil.net_io_counters().dropout
    write_to_csv('bytes_sent.csv', bytes_sent)
    write_to_csv('bytes_recv.csv', bytes_recv)
    write_to_csv('packets_sent.csv', packets_sent)
    write_to_csv('packets_recv.csv', packets_recv)
    write_to_csv('errin.csv', errin)
    write_to_csv('errout.csv', errout)
    write_to_csv('dropin.csv', dropin)
    write_to_csv('dropout.csv', dropout)


def net_usage(inf="wlan0"):  # change the inf variable according to the interface
    net_stat = psutil.net_io_counters(pernic=True, nowrap=True)[inf]
    net_in_1 = net_stat.bytes_recv
    net_out_1 = net_stat.bytes_sent
    time.sleep(1)
    net_stat = psutil.net_io_counters(pernic=True, nowrap=True)[inf]
    net_in_2 = net_stat.bytes_recv
    net_out_2 = net_stat.bytes_sent

    net_in = round((net_in_2 - net_in_1) / 1024 / 1024, 3)
    net_out = round((net_out_2 - net_out_1) / 1024 / 1024, 3)

    # print(f"Current net-usage:\nIN: {net_in} MB/s, OUT: {net_out} MB/s")
    write_to_csv('net_in.csv', net_in)
    write_to_csv('net_out.csv', net_out)


@app.route('/roof/performance/time', methods=['GET'])
# @cache.cached(timeout=300)
def performance_time():
    global total

    global cpu_usage_data
    global memory_usage_data
    global performance_data
    total = cpu_usage_data + memory_usage_data + performance_data
    write_to_csv('performance_tme_total.csv', total)
    return total


def get_accuracy_time():
    try:
        req = requests.get("http://localhost:3002/roof/accuracy/time")
        accuracy_time = float(req.text)

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return accuracy_time


def get_classification_time():
    try:
        req = requests.get("http://localhost:3005/roof/classification/time")
        classification_time = float(req.text)

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return classification_time


def get_confusion_time():
    try:
        req = requests.get("http://localhost:3004/roof/confusion/time")
        confusion_time = float(req.text)

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return confusion_time


def get_controller_time():
    try:
        req = requests.get("http://localhost:3011/roof/controller/time")
        controller_time = float(req.text)

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return controller_time


#
# def run():
#     rasp1_status = get_rasp1_status()
#     if rasp1_status == 1:
#         for process in psutil.process_iter():
#             if process.cmdline() == ['python3', 'update.py']:
#                 print('process found')
#                 Popen(['python3', 'update.py']
#             print('process not found')

def automated_data_request():
    get_cpu_measure_data()
    performance()
    get_memory_usage()
    net_usage()
    network_io()
    performance_time()


data_request_automated = RepeatedTimer(1, automated_data_request)

if __name__ == '__main__':
    app.run(port=3007, debug=True, host='0.0.0.0')
