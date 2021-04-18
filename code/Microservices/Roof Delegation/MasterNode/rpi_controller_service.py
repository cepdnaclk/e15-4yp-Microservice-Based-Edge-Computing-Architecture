# Load libraries
import json
from json import JSONEncoder
from threading import Timer

import numpy as np
import requests
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

numberOfConnectedEdgeNodes = 0
ac_control_ip = "192.168.1.106"
speed_ip = "192.168.1.106"
accuracy_ip = "192.168.1.105"
confusion_ip = "192.168.1.105"
classification_ip = "192.168.1.105"
processing_ip = "192.168.1.100"

edge_device_list = {"devices": []}


def switch_service(switching_device_ip, switch_offload_service_name):
    global speed_ip
    global accuracy_ip
    global classification_ip
    global confusion_ip
    global processing_ip
    global ac_control_ip
    if switch_offload_service_name == "speed":
        speed_ip = switching_device_ip
    elif switch_offload_service_name == "accuracy":
        accuracy_ip = switching_device_ip
    elif switch_offload_service_name == "classification":
        classification_ip = switching_device_ip
    elif switch_offload_service_name == "confusion":
        confusion_ip = switching_device_ip
    elif switch_offload_service_name == "processing":
        processing_ip = switching_device_ip
    elif switch_offload_service_name == "ac_control":
        ac_control_ip = switching_device_ip
    # publish new service IPs to Every Edge Nodes:
    json_map = {"ac_control_ip": ac_control_ip, "speed_ip": speed_ip, "accuracy_ip": accuracy_ip,
                "confusion_ip": confusion_ip, "classification_ip": classification_ip,
                "processing_ip": processing_ip}
    json_ip_address_list = json.dumps(json_map)
    for device in edge_device_list["devices"]:
        ip = device["ipAddress"] + "/updateIPAddresses"
        requests.post(ip, json=json_ip_address_list)


@app.route('/offLoadData', methods=['POST'])
def sendNodeOffLoadData():
    global numberOfConnectedEdgeNodes
    offLoadData = request.get_json()

    # ToDo: Get Data From Json
    ip = offLoadData['ipAddress']
    offLoadCount = offLoadData['offLoad']
    ac_control = offLoadData['ac_control']
    # Get time sets too...
    totalTime = 0
    for device in edge_device_list["devices"]:
        if device["ipAddress"] == ip:
            device["offLoadCount"] = offLoadCount
            device["ac_control"] = ac_control
            # Add time sets
        totalTime = totalTime + device["offLoadCount"]

    if (numberOfConnectedEdgeNodes > 1):
        maxDeviceFactor = 1 / (numberOfConnectedEdgeNodes)
        minDeviceFactor = 1 / (numberOfConnectedEdgeNodes + 1)
        switch_offload_service_name = ""
        switching_device_ip = ""
        for device in edge_device_list["devices"]:
            deviceOffloadingFactor = (device["offLoadCount"] / totalTime)
            if deviceOffloadingFactor > maxDeviceFactor:
                # Off Loaded
                print("OffLoaded")

                # indivitual Service Time
                ac_control = device["ac_control"]
                speed = device["speed"]
                accuracy = device["accuracy"]
                confusion = device["confusion"]
                classification = device["classification"]
                processing = device["processing"]

                max = np.max(ac_control, speed, accuracy, confusion, classification, processing)

                if max == ac_control:
                    switch_offload_service_name = "ac_control"
                elif max == speed:
                    switch_offload_service_name = "speed"
                elif max == accuracy:
                    switch_offload_service_name = "accuracy"
                elif max == confusion:
                    switch_offload_service_name = "confusion"
                elif max == classification:
                    switch_offload_service_name = "classification"
                elif max == processing:
                    switch_offload_service_name = "processing"

            elif deviceOffloadingFactor < minDeviceFactor:
                # Low Level
                print("Not Offloaded, Available resources")
                switching_device_ip = device["ipAddress"]
            else:
                if switching_device_ip == "":
                    switching_device_ip = device["ipAddress"]

        # Now Let's Change the services
        switch_service(switching_device_ip, switch_offload_service_name)


@app.route('/connectNode', methods=['POST'])
def connectNodes():
    ip = request.data
    isDeviceFound = False
    global edge_device_list
    for device in edge_device_list["devices"]:
        if device["ipAddress"] == ip:
            isDeviceFound = True
    if not isDeviceFound:
        device = {}
        device["ipAddress"] = ip
        device["offLoadCount"] = 0
        edge_device_list["devices"].append(device)
        global numberOfConnectedEdgeNodes
        numberOfConnectedEdgeNodes = numberOfConnectedEdgeNodes + 1

    json_map = {"connected_nodes": numberOfConnectedEdgeNodes}
    return json.dumps(json_map)


@app.route('/getConnectedNodes', methods=['GET'])
def getConnectedNodes():
    global numberOfConnectedEdgeNodes
    json_map = {"connected_nodes": numberOfConnectedEdgeNodes}
    return json.dumps(json_map)


@app.route('/ipaddresses', methods=['GET'])
def getRunningServicesIpAddresses():
    json_map = {"ac_control_ip": ac_control_ip, "speed_ip": speed_ip, "accuracy_ip": accuracy_ip,
                "confusion_ip": confusion_ip, "classification_ip": classification_ip,
                "processing_ip": processing_ip}
    result = json.dumps(json_map)
    return result


@app.route('/ipaddresses/ac_control_ip', methods=['POST'])
def setac_control_ipIpAddresses():
    ip = request.form.get('ac_control_ip')
    ac_control_ip = ip
    json_map = {"ac_control_ip": ac_control_ip, "speed_ip": speed_ip, "accuracy_ip": accuracy_ip,
                "confusion_ip": confusion_ip, "classification_ip": classification_ip,
                "processing_ip": processing_ip}
    result = json.dumps(json_map)
    return result


@app.route('/ipaddresses/speed_ip', methods=['POST'])
def setac_control_ipIpAddresses():
    ip = request.form.get('speed_ip')
    ac_control_ip = ip
    json_map = {"ac_control_ip": ac_control_ip, "speed_ip": speed_ip, "accuracy_ip": accuracy_ip,
                "confusion_ip": confusion_ip, "classification_ip": classification_ip,
                "processing_ip": processing_ip}
    result = json.dumps(json_map)
    return result


@app.route('/ipaddresses/accuracy_ip', methods=['POST'])
def setac_control_ipIpAddresses():
    ip = request.form.get('accuracy_ip')
    ac_control_ip = ip
    json_map = {"ac_control_ip": ac_control_ip, "speed_ip": speed_ip, "accuracy_ip": accuracy_ip,
                "confusion_ip": confusion_ip, "classification_ip": classification_ip,
                "processing_ip": processing_ip}
    result = json.dumps(json_map)
    return result


@app.route('/ipaddresses/confusion_ip', methods=['POST'])
def setac_control_ipIpAddresses():
    ip = request.form.get('confusion_ip')
    ac_control_ip = ip
    json_map = {"ac_control_ip": ac_control_ip, "speed_ip": speed_ip, "accuracy_ip": accuracy_ip,
                "confusion_ip": confusion_ip, "classification_ip": classification_ip,
                "processing_ip": processing_ip}
    result = json.dumps(json_map)
    return result


@app.route('/ipaddresses/classification_ip', methods=['POST'])
def setac_control_ipIpAddresses():
    ip = request.form.get('classification_ip')
    ac_control_ip = ip
    json_map = {"ac_control_ip": ac_control_ip, "speed_ip": speed_ip, "accuracy_ip": accuracy_ip,
                "confusion_ip": confusion_ip, "classification_ip": classification_ip,
                "processing_ip": processing_ip}
    result = json.dumps(json_map)
    return result


@app.route('/ipaddresses/processing_ip', methods=['POST'])
def setac_control_ipIpAddresses():
    ip = request.form.get('processing_ip')
    ac_control_ip = ip
    json_map = {"ac_control_ip": ac_control_ip, "speed_ip": speed_ip, "accuracy_ip": accuracy_ip,
                "confusion_ip": confusion_ip, "classification_ip": classification_ip,
                "processing_ip": processing_ip}
    result = json.dumps(json_map)
    return result


if __name__ == '__main__':
    app.run(port=3006, debug=True, host='0.0.0.0')
