from __future__ import print_function
import serial, time, io, datetime
from serial import Serial
import sys

sys.path.append("/home/warmongr/diagnosis/diagnosis/stark_testing")
import validating_serial_output
import time


def log_serial(shared_memory=[]):
    addr = "/dev/ttyUSB0"  ## serial port to read data from
    baud = 115200  ## baud rate for instrument

    ser = serial.Serial(
        port=addr,
        baudrate=baud,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        xonxoff=True,
        timeout=0,
    )

    print("Connected to: " + ser.portstr)

    filename = "stark_serial_log.txt"
    datafile = open(filename, "a")

    ## this will store each line of data
    seq = []
    count = 0  ## row index
    countTrue = 0
    countFalse = 0
    while True:

        size = ser.inWaiting()

        if size:
            count = count + 1

            if count < 2:
                continue

            data = ser.read(size)
            string = data.decode("UTF-8")
            datafile.write(string)
            res = validating_serial_output.parsing(string)

            if res == False:
                countFalse += 1
            else:
                countTrue += 1

            if count == 5:
                if countFalse >= 1:
                    shared_memory.append(False)
                    print("Show on the frontend that data received was wrong somehow")
                    break
                else:
                    shared_memory.append(True)
                    print("Show on the frontend that stark is functioning ok")
                    break

            print(string)
        else:
            print("no data")
        time.sleep(5)
        # for i in ser.readline():

        # print(i)
        # seq.append(i) ## convert from ACSII?
        # joined_seq = ''.join(str(v) for v in seq) ## Make a string from array
        # print(joined_seq)

        # if i == '\n':
        #     datafile.write("Line: " + str(count) + "" + str(datetime.datetime.now()) + joined_seq) ## append a timestamp to each row of data
        #     res=validating_output.parsing(joined_seq)
        #     #res=True
        #     if res==True:
        #         print("Stark Successfully Validated")
        #     else:
        #         print("Stark Test Failed")
        #     seq = []
        #     count += 1

    datafile.close()
    ser.close()
