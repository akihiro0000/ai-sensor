# -*- coding: utf-8 -*-

import config
import json
import os


def init():
    pass


def send_sensor_data(payload):
    fn = config.SENSOR_DATA_FILE
    jsonStr = json.dumps(payload)

    try:
        f = open(fn, mode='r+b')
        f.seek(0, os.SEEK_END)
    except FileNotFoundError:
        f = open(fn, mode='w+b')

    if f.tell() < 4:
        f.seek(0, os.SEEK_SET)
        f.write(('[\n  ' + jsonStr + '\n]\n').encode())
    else:
        f.seek(f.tell() - 3, os.SEEK_SET)
        f.write((',\n  ' + jsonStr + '\n]\n').encode())


def send_log_information(payload):
    fn = config.LOG_INFORMATION_FILE
    jsonStr = json.dumps(payload)

    try:
        f = open(fn, mode='r+b')
        f.seek(0, os.SEEK_END)
    except FileNotFoundError:
        f = open(fn, mode='w+b')

    if f.tell() < 4:
        f.seek(0, os.SEEK_SET)
        f.write(('[\n  ' + jsonStr + '\n]\n').encode())
    else:
        f.seek(f.tell() - 3, os.SEEK_SET)
        f.write((',\n  ' + jsonStr + '\n]\n').encode())


if __name__ == '__main__':
    import time

    init()
    send_sensor_data({
        'Time': time.time(),
        'CO2_1': 0.0,
        'CO2_2': 1.0,
        'TEMP_1': 2.0,
        'TEMP_2': 3.0,
        'HUMI_1': 4.0,
        'HUMI_2': 5.0,
    })
    send_log_information({
        'Time': time.time(),
        'SensorAppLog': 'ログ情報',
    })
