'''
This is the entry point of diagnosis of stark , bms and controller.

'''

import can
import serial
import logging
from constants import (SERIAL_PORT, SERIAL_BAUDRATE, CAN_BUSTYPE, CAN_CHANNEL, CAN_BITRATE)
from stark_testing import stark_testing_function
from bms_testing import bms_testing_function
from controller_testing import controller_testing_function

try:
    can_bus = can.interface.Bus(bustype=CAN_BUSTYPE, channel=CAN_CHANNEL,bitrate=CAN_BITRATE)
except:
    logging.error("Can Bus connection Problem")

try:
    ser = serial.Serial(
            port = SERIAL_PORT,
            baudrate = SERIAL_BAUDRATE,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            xonxoff=True,
            timeout=0,
        )
except:
    logging.error("Serial connection Problem")

logging.basicConfig(filename = "stark_logs.txt",
                    filemode = "a",
                    format = '%(asctime)s %(levelname)s-%(message)s',
                    datefmt = '%Y-%m-%d %H:%M:%S')

def test_all_parts():
    """This is the main function which will be invoked in flask.

    Returns:
        _type_: _description_
    """
    if stark_testing_function(can_bus,ser):
        if bms_testing_function(ser):
            if controller_testing_function(ser):
                return "All Tests Passed"
            else:
                return "Controller Testing Failed"
        else:
            return "BMS Testing Failed"
    else:
        return "Stark Testing Failed"
    
print(test_all_parts())

    

    
    


