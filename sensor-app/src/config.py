# -*- coding: utf-8 -*-

import os
import sys

MQTT_KEEP_ALIVE = 60    # [sec.]

try:
    MQTT_BROKER_HOST = os.environ['MQTT_BROKER_HOST']
    MQTT_BROKER_PORT = int(os.environ['MQTT_BROKER_PORT'])

    MQTT_SENSOR_DATA_TOPIC = os.environ['MQTT_SENSOR_DATA_TOPIC']
    MQTT_LOG_INFORMATION_TOPIC = os.environ['MQTT_LOG_INFORMATION_TOPIC']

    SENSOR_DATA_FILE = os.environ['SENSOR_DATA_FILE']
    LOG_INFORMATION_FILE = os.environ['LOG_INFORMATION_FILE']
except KeyError as ex:
    sys.exit('No environment variable is set. {0.args[0]}'.format(ex))
