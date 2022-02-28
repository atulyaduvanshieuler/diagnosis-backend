#!/usr/bin/env python
# coding: utf-8

"""
This example shows how sending a single message works.
"""
from __future__ import print_function
import time
from file_handling import can_ids_for_real_output as can_ids
from file_handling import can_data_for_real_output as can_data
from file_handling import sleeping_time
from file_handling import exact_time

import can


def convert_to_hex(x):
    return int(x, 16)


def send_data(can_ids, can_data):
    # print(can_ids,can_data)

    # this uses the default configuration (for example from the config file)
    # see https://python-can.readthedocs.io/en/stable/configuration.html
    bus = can.interface.Bus(bustype="socketcan", channel="can0", bitrate=250000)

    # Using specific buses works similar:
    # bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=250000)
    # bus = can.interface.Bus(bustype='pcan', channel='PCAN_USBBUS1', bitrate=250000)
    # bus = can.interface.Bus(bustype='ixxat', channel=0, bitrate=250000)
    # bus = can.interface.Bus(bustype='vector', app_name='CANalyzer', channel=0, bitrate=250000)
    # ....

    count = 0
    id_data_list = list(zip(can_ids, can_data))

    for i in range(len(id_data_list)):
        id = id_data_list[i][0]
        cdata = id_data_list[i][1]

        cdata = list(map(convert_to_hex, cdata))
        id = convert_to_hex(id)

        msg = can.Message(arbitration_id=id, data=cdata, is_extended_id=False)

        print(i)
        print(exact_time[i])
        print(sleeping_time[i])
        time.sleep(sleeping_time[i] * 0.001)

        try:

            bus.send(msg)
            print("Message sent on {}".format(bus.channel_info))
            count += 1
        except can.CanError:
            print(can)
            print("Message NOT sent")
    print(count)


send_data(can_ids, can_data)
