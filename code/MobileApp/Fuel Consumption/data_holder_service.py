# Load libraries
import numpy as np
from flask import Flask, request
import json
from json import JSONEncoder
import queue


class DataHolder:
    __instance = None

    @staticmethod
    def get_instance():
        if DataHolder.__instance is None:
            DataHolder()
        return DataHolder.__instance

    def __init__(self):
        if DataHolder.__instance is not None:
            raise Exception("This is a singleton")
        else:
            self.__mobile_data_q = queue.Queue()

            DataHolder.__instance = self

    def add_mobile_data(self, data):
        if data is not None:
            self.__mobile_data_q.put(data)

    def get_mobile_data(self):
        if not self.__mobile_data_q.empty():
            return self.__mobile_data_q.get(timeout=100)
        return "No data found"


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


app = Flask(__name__)


@app.route('/cloud/add_mobile_data', methods=['POST'])
def add_mobile_data_to_queue():
    record = json.loads(request.data)
    print(record)
    DataHolder.get_instance().add_mobile_data(record)
    return "success"


@app.route('/cloud/get_mobile_data', methods=['GET'])
def get_mobile_to_queue():
    return DataHolder.get_instance().get_mobile_data()


if __name__ == '__main__':
    app.run(port=6201, host='0.0.0.0')
