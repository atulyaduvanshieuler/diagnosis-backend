'''
This module will establish a can and serial connection.
'''

import can
import serial
from shared.constants import (SERIAL_PORT, SERIAL_BAUDRATE, CAN_BUSTYPE, CAN_CHANNEL, CAN_BITRATE)
from shared.loggers import (general_logger, error_logger)


try:
    can_bus = can.interface.Bus(bustype=CAN_BUSTYPE, channel=CAN_CHANNEL,bitrate=CAN_BITRATE)
except:
    can_bus = {}
    general_logger.error("Can Bus connection Problem")


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
    ser = {}
    error_logger.error("Serial connection Problem")
