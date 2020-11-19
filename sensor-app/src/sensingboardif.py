# -*- coding: utf-8 -*-

import gpiod
import time
import random


def init():
    _gpio_chip = (
        gpiod.chip(0),
        gpiod.chip(1),
    )

    global _gpio_reset
    global _gpio_supply_monitor_led
    global _gpio_communication_led
    global _gpio_backbone_led

    _gpio_reset = _gpio_chip[0].get_line(140)
    _gpio_supply_monitor_led = _gpio_chip[1].get_line(2)
    _gpio_communication_led = _gpio_chip[1].get_line(0)
    _gpio_backbone_led = _gpio_chip[0].get_line(64)

    config = gpiod.line_request()
    config.request_type = gpiod.line_request.DIRECTION_OUTPUT
    for line in (_gpio_reset, _gpio_supply_monitor_led, _gpio_communication_led, _gpio_backbone_led):
        line.request(config)

    _gpio_reset.set_value(0)
    _gpio_supply_monitor_led.set_value(0)
    _gpio_communication_led.set_value(0)
    _gpio_backbone_led.set_value(0)


def perform_reset():
    _gpio_reset.set_value(1)
    time.sleep(0.2)
    _gpio_reset.set_value(0)


def set_supply_monitor_led(on):
    _gpio_supply_monitor_led.set_value(1 if on else 0)


def set_communication_led(on):
    _gpio_communication_led.set_value(1 if on else 0)


def set_backbone_led(on):
    _gpio_backbone_led.set_value(1 if on else 0)


def get_sk3703_values():
    return {
        'co2': random.uniform(500.0, 5000.0),
        'temperature': random.uniform(10.0, 30.0),
        'humidity': random.uniform(0.0, 100.0),
    }


def get_cdm7160_values():
    return {
        'co2': random.uniform(500.0, 5000.0),
    }


def get_sen11295_values():
    return {
        'temperature': random.uniform(10.0, 30.0),
        'humidity': random.uniform(0.0, 100.0),
    }


if __name__ == '__main__':
    init()
    print(get_sk3703_values())
    print(get_cdm7160_values())
    print(get_sen11295_values())
    set_supply_monitor_led(True)
    time.sleep(1)
    set_communication_led(True)
    time.sleep(1)
    set_backbone_led(True)
    time.sleep(1)
    perform_reset()
    set_supply_monitor_led(False)
    set_communication_led(False)
    set_backbone_led(False)
