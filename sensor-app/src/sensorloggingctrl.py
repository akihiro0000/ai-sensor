# -*- coding: utf-8 -*-

import fileclient
import mqttclient
import time


def init():
    mqttclient.init()
    fileclient.init()

def send_sensor_data(payload):
    mqttclient.send_sensor_data(payload)
    fileclient.send_sensor_data(payload)


def send_log_information(payload):
    mqttclient.send_log_information(payload)
    fileclient.send_log_information(payload)


if __name__ == '__main__':
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
