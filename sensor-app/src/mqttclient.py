# -*- coding: utf-8 -*-

import config
import json
import paho.mqtt.client as mqtt

_client = mqtt.Client()


def init():
    _client.connect(config.MQTT_BROKER_HOST,
                    config.MQTT_BROKER_PORT, config.MQTT_KEEP_ALIVE)


def send_sensor_data(payload):
    jsonStr = json.dumps(payload)
    _client.publish(config.MQTT_SENSOR_DATA_TOPIC, jsonStr)


def send_log_information(payload):
    jsonStr = json.dumps(payload)
    _client.publish(config.MQTT_LOG_INFORMATION_TOPIC, jsonStr)
