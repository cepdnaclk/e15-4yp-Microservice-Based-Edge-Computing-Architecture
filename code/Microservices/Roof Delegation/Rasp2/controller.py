# Load libraries
import csv
from threading import Timer
import numpy as np
from flask import Flask
from json import JSONEncoder
import requests
import json


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

offload_service_name = ""
ac_control_ip = "192.168.1.106"
speed_ip = "192.168.1.106"
accuracy_ip = "192.168.1.105"
confusion_ip = "192.168.1.105"
classification_ip = "192.168.1.105"
processing_ip = "192.168.1.100"


@app.route('/roof/update/ip', methods=['GET'])
def send_ip():
    json_map = {"ac_control_ip": ac_control_ip, "speed_ip": speed_ip, "accuracy_ip": accuracy_ip,
                "confusion_ip": confusion_ip, "classification_ip": classification_ip, "processing_ip": processing_ip}
    result = json.dumps(json_map)
    return result


def write_to_csv(fileName, data):
    with open(fileName, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Data:", data])


def get_total_time():
    rasp1_time = get_rasp1_time()
    rasp2_time = get_rasp2_time()
    rasp3_time = get_rasp3_time()
    total = rasp1_time + rasp2_time + rasp3_time
    return float(total)


def rasp1_factor():
    rasp1_time = get_rasp1_time()
    total = get_total_time()
    factor = rasp1_time / total
    print('rasp1_factor', factor)
    return factor


def rasp2_factor():
    rasp2_time = get_rasp2_time()
    total = get_total_time()
    factor = rasp2_time / total
    print('rasp2_factor', factor)
    return factor


def rasp3_factor():
    rasp3_time = get_rasp3_time()
    total = get_total_time()
    factor = rasp3_time / total
    print('rasp3_factor', factor)
    return factor


def ac_control_factor():
    ac_time = get_ac_control_time()
    total = get_total_time()
    factor = ac_time / total
    print('ac_control_factor', factor)
    return factor


def speed_factor():
    speed = get_speed_time()
    total = get_total_time()
    factor = speed / total
    print('speed_factor', factor)
    return factor


def accuracy_factor():
    accuracy_time = get_accuracy_time()
    total = get_total_time()
    factor = accuracy_time / total
    print('accuracy_factor', factor)
    return factor


def classification_factor():
    classification_time = get_classification_time()
    total = get_total_time()
    factor = classification_time / total
    print('classification_factor', factor)
    return factor


def confusion_factor():
    confusion_time = get_confusion_time()
    total = get_total_time()
    factor = confusion_time / total
    print('confusion_factor', factor)
    return factor


# def controller_factor():
#     controller_time = get_controller_time()
#     total = get_total_time()
#     factor = controller_time / total
#     print('controller_factor', factor)
#     return factor


def processing_factor():
    processing_time = get_processing_time()
    total = get_total_time()
    factor = processing_time / total
    print('processing_factor', factor)
    return factor


def offload_service():
    global offload_service_name
    if total_max.raspberry == 'Rasp1':
        offload_service_name = rasp1_max.raspberry

    if total_max.raspberry == 'Rasp2':
        offload_service_name = rasp2_max.raspberry

    if total_max.raspberry == 'Rasp3':
        offload_service_name = rasp3_max.raspberry
    return offload_service_name


def get_rasp1_time():
    try:
        req = requests.get("http://localhost:3006/roof/rasp1/total_time")
        rasp1_time = float(req.text)

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return rasp1_time


def get_rasp2_time():
    try:
        req = requests.get("http://localhost:3007/roof/rasp2/total_time")
        rasp2_time = float(req.text)

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return rasp2_time


def get_rasp3_time():
    try:
        req = requests.get("http://localhost:3008/roof/rasp3/total_time")
        rasp3_time = float(req.text)

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return rasp3_time


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


def get_processing_time():
    try:
        req = requests.get("http://localhost:3001/roof/processing/time")
        processing_time = float(req.text)

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return processing_time



def automated_data_request():
    rasp1_factor()
    rasp2_factor()
    rasp3_factor()
    ac_control_factor()
    accuracy_factor()
    confusion_factor()
    classification_factor()
    # controller_factor()
    processing_factor()


data_request_automated = RepeatedTimer(60, automated_data_request)

if __name__ == '__main__':
    app.run(port=3011, debug=True, host='0.0.0.0')
