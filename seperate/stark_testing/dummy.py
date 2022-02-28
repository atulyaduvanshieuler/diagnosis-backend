import serial
import time
ser = serial.Serial(port="/dev/ttyUSB0", baudrate=115200)
time.sleep(1)
ser.write(b"DIAG_BMS_STOP\t")
time.sleep(1)
ser.write(b"DIAG_CONTROLLER_STOP\t")
time.sleep(1)
ser.write(b"DIAG_STARK_STOP\t")
time.sleep(1)