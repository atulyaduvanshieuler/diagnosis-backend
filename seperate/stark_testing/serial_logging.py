"""
    Collects serial logs and parses them
"""
import serial, time
from constants import (CHECK_BUFFER_DATA_COUNTER, SERIAL_DATA_LOG_FILENAME)
from validating_serial_output import verify_serial

# TODO: Use Logger instead of print

def log_serial(shared_memory=[]):
    """
    Args:
        shared_memory (list, optional): _description_. Defaults to [].
    """  

    addr = "/dev/ttyUSB2"  ## serial port to read data from
    baud = 115200  ## baud rate for instrument

    # Reuse serial object from can_send
    ser = serial.Serial(
        port=addr,
        baudrate=baud,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        xonxoff=True,
        timeout=0,
    )
 

    count = 0
    count_false = 0
    
    with open(SERIAL_DATA_LOG_FILENAME, "a") as data_file:
        while True:
            msg_buffer_size = ser.inWaiting()

            if msg_buffer_size > 0:
                count += 1

                if count < CHECK_BUFFER_DATA_COUNTER:
                    continue

                data = ser.read(msg_buffer_size)
                info = data.decode("UTF-8")
                data_file.write(info)
                res = verify_serial(info)

                # code does not breaks if count_false >= 1 because
                # 
                if res == False:
                    count_false += 1

                if count == 6:
                    shared_memory.append(count_false <= 1)
                    break
            else:
                # add logger
                pass
            time.sleep(5)

    ser.close()
