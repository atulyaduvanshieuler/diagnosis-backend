'''
This module is entry point for controller testing
'''
from selectors import EpollSelector
import time
import logging
from constants import (TESTING_COUNTER, CONTROLLER_OUTPUT_LENGTH)
from controller_validator import controller_validation_function

def controller_testing_function(ser):
    """This function will receive controller data from serial and will get it validated.

    Args:
        ser (_obj_): serial connection object
    """    
    logging.info("Controller testing started")
    print("Controller Testing started")
    time.sleep(1)
    ser.write(b"DIAG_CONTROLLER_START\t")
    time.sleep(1)

    try:
        counter=0
        error_counter = 0
        while counter < TESTING_COUNTER:
            counter+=1

            msg_buffer_size = ser.inWaiting()
            data = ser.read(msg_buffer_size)
            info = data.decode("UTF-8")
            if counter==1:
                continue

            if info.split(',')[0]=="DIAG_CONTROLLER_START" and len(info) == CONTROLLER_OUTPUT_LENGTH:
                res = controller_validation_function(ser,info)

                if res == False:
                    time.sleep(1)
                    ser.write(b"DIAG_CONTROLLER_STOP\t")
                    time.sleep(1)
                    logging.info("DIAG_CONTROLLER_STOP command ran in try in controller_testing_function ")
                    return False
            else:
                error_counter += 1
                if error_counter >= 4:
                    time.sleep(1)
                    ser.write(b"DIAG_CONTROLLER_STOP\t")
                    time.sleep(1)
                    return False
            
            time.sleep(5)
        
        time.sleep(1)
        ser.write(b"DIAG_CONTROLLER_STOP\t")
        time.sleep(1)
        logging.info("DIAG_CONTROLLER_STOP command ran and controller testing successful.")
        return True

    except:
        time.sleep(1)
        ser.write(b"DIAG_CONTROLLER_STOP\t")
        time.sleep(1)
        logging.info("DIAG_CONTROLLER_STOP command ran in exception handling in controller_testing_function ")
        return False