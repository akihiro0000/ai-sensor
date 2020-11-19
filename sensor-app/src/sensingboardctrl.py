#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from transitions import Machine, State
import sensingboardif
import sensorloggingctrl
import sys
import time

itself = sys.modules[__name__]

states = (
    State(name='INIT'),
    State(name='ST0'),
    State(name='ST1'),
    State(name='ST2'),
    State(name='ST3'),
    State(name='ST4'),
    State(name='ST5'),
)

transitions = (
    {'trigger': 'reset', 'source': 'INIT', 'dest': 'ST0'},
    {'trigger': 'initialized', 'source': 'ST0', 'dest': 'ST1'},
    {'trigger': 'started_of_sensing_board', 'source': 'ST1', 'dest': 'ST2'},
    {'trigger': 'start_timeout_of_sensing_board',
        'source': 'ST1', 'dest': 'ST5'},
    {'trigger': 'got_sensor_data', 'source': 'ST2', 'dest': 'ST3'},
    {'trigger': 'got_sensing_board_info', 'source': 'ST3', 'dest': 'ST4'},
    {'trigger': 'next_capture_time_elapsed', 'source': 'ST4', 'dest': 'ST2'},
    {'trigger': 'sensing_board_failed', 'source': 'ST4', 'dest': 'ST5'},
)

doactions = {
    'INIT': 'init_do',
    'ST0': 'st0_do',
    'ST1': 'st1_do',
    'ST2': 'st2_do',
    'ST3': 'st3_do',
    'ST4': 'st4_do',
    'ST5': 'st5_do',
}


def init_do():
    print('INIT')
    reset()


def st0_do():
    print('ST0: Initialize Sensor App')
    sensorloggingctrl.init()
    sensingboardif.init()
    sensingboardif.perform_reset()

    initialized()


def st1_do():
    print('ST1: Wait for boot of Sensing Board')

    started_of_sensing_board()


def st2_do():
    print('ST2: Get sensor data')
    sensor_data = {
        'sk3703': sensingboardif.get_sk3703_values(),
        'cdm7160': sensingboardif.get_cdm7160_values(),
        'sen11295': sensingboardif.get_sen11295_values(),
    }
    sensorloggingctrl.send_sensor_data({
        'Time': time.time(),
        'CO2_1': sensor_data['sk3703']['co2'],
        'CO2_2': sensor_data['cdm7160']['co2'],
        'TEMP_1': sensor_data['sk3703']['temperature'],
        'TEMP_2': sensor_data['sen11295']['temperature'],
        'HUMI_1': sensor_data['sk3703']['humidity'],
        'HUMI_2': sensor_data['sen11295']['humidity'],
    })

    got_sensor_data()


def st3_do():
    print('ST3: Get information of Sensing Board')
    sensorloggingctrl.send_log_information({
        'Time': time.time(),
        'SensorAppLog': 'payload',
    })

    got_sensing_board_info()


def st4_do():
    print('ST4: Wait for next capture time')
    time.sleep(1)

    next_capture_time_elapsed()


def st5_do():
    print('ST5: Sensing Board failed')


def action():
    func = getattr(itself, doactions[state])
    func()


machine = Machine(model=itself, states=states,
                  transitions=transitions, initial='ST0', auto_transitions=False)


if __name__ == '__main__':
    while True:
        action()
