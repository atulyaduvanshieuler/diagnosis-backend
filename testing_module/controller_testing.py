'''
This module is entry point for controller testing
'''
import time
from constants import TESTING_COUNTER
from controller_validator import controller_validation_function

def controller_testing_function(ser):
    """This function will receive controller data from serial and will get it validated.

    Args:
        ser (_obj_): serial connection object
    """    

    ser.write(b"DIAG_CONTROLLER_START\t")
    time.sleep(7)

    for counter in range(TESTING_COUNTER):

        msg_buffer_size = ser.inWaiting()
        data = ser.read(msg_buffer_size)
        info = data.decode("UTF-8")

        if info.split(',')[0]=="DIAG_CONTROLLER_START":
            res = controller_validation_function(ser,info)

            if res == False:
                ser.write(b"DIAG_BMS_STOP\t")
                return False
        time.sleep(5)
    
    ser.write(b"DIAG_BMS_STOP\t")
    return True