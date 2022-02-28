import can
from constants import (serial_port, serial_baudrate,can_bustype, can_channel, can_bitrate)

def can_receive():
    bus = can.interface.Bus(bustype=can_bustype, channel=can_channel,
        bitrate=can_bitrate)
    for msg in bus:
        print(bus)
        
can_receive()
