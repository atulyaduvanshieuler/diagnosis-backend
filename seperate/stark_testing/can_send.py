"""
"""
import can
import time
import serial
import threading

from constants import (serial_port, serial_baudrate,
    can_bustype, can_channel, can_bitrate)
from serial_logging import log_serial

ser = serial.Serial(port=serial_port, baudrate=serial_baudrate)
bus = can.interface.Bus(bustype=can_bustype, channel=can_channel,
    bitrate=can_bitrate)


def send_data():
    """
    """
    can_send_serial_logging_shared_memory = []

    time.sleep(0.1)
    ser.write(b"DIAG_STARK_START\t")

    msg = can.Message(
        arbitration_id=0x7A1,
        data=[0xAB, 0x12, 00, 00, 00, 00, 00, 00],
        is_extended_id=False,
    )

    serial_thread = threading.Thread(
        target=log_serial, args=(can_send_serial_logging_shared_memory,)
    )
    serial_thread.start()

    while True:
        try:
            if can_send_serial_logging_shared_memory != []:
                if can_send_serial_logging_shared_memory[0] == True:
                    ser.write(b"DIAG_STARK_STOP\t")
                    time.sleep(5)
                    return True
                else:
                    return False
            bus.send(msg)
        except can.CanError:
            print("Message NOT sent")
        time.sleep(1)

send_data()
