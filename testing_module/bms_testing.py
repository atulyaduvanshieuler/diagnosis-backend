"""
This module is the entry point for bms testing
"""
import time
import logging
from constants import TESTING_COUNTER
from bms_validator import bms_validation_function

def bms_testing_function(ser):
    
    """
        It will receive bms data from serial port and get it validated

    Args:
        can_bus (_type_): can connection object
        ser (_type_): serial connection object
    """

    ser.write(b"DIAG_BMS_START\t")
    time.sleep(7)

    counter=0
    error_counter=0

    while counter < TESTING_COUNTER:

        msg_buffer_size = ser.inWaiting()
        data = ser.read(msg_buffer_size)
        info = data.decode("UTF-8")

        if info.split(',')[0]=="DIAG_BMS_START":
            counter+=1
            res = bms_validation_function(ser,info)

            if res == False:
                ser.write(b"DIAG_BMS_STOP\t")
                return False

        else:
            error_counter+=1
            
            if error_counter < 3:
                logging.critical("For BMS Diagnosis following message received: " %info)
            else:
                #May Need to remove this part and also remove error_counter while removing this
                
                logging.error("Stark Repetedly gave following output: %s" %info)
                return False

        time.sleep(5)
    
    ser.write(b"DIAG_BMS_STOP\t")
    return True















