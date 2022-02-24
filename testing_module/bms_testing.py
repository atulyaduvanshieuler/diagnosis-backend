"""
This module is the entry point for bms testing
"""
import time
import logging
from constants import (TESTING_COUNTER, BMS_OUTPUT_LENGTH)
from bms_validator import bms_validation_function

def bms_testing_function(ser):
    
    """
        It will receive bms data from serial port and get it validated

    Args:
        can_bus (_type_): can connection object
        ser (_type_): serial connection object
    """
    logging.critical("BMS testing started")
    print("BMS testing started")
    time.sleep(1)
    ser.write(b"DIAG_BMS_START\t")
    time.sleep(1)

    

    try:
        counter=0
        error_counter=0
        
        while counter < TESTING_COUNTER:
            counter+=1

            msg_buffer_size = ser.inWaiting()
            data = ser.read(msg_buffer_size)
            info = data.decode("UTF-8")
            
            if counter==1:
                continue

            if info.split(',')[0]=="DIAG_BMS_START" and len(info) == BMS_OUTPUT_LENGTH:
                res = bms_validation_function(ser,info)

                if res == False:
                    time.sleep(1)
                    ser.write(b"DIAG_BMS_STOP\t")
                    time.sleep(1)
                    return False
            else:
                error_counter += 1
                
                if error_counter < 4:
                    logging.critical("For BMS Diagnosis following message received: %s " %str(info))
                else:
                    #May Need to remove this part and also remove error_counter while removing this
                    time.sleep(1)        
                    ser.write(b"DIAG_BMS_STOP\t")
                    time.sleep(1)
                    logging.info("DIAG_BMS_STOP command ran because of error_counter limit exceeded")
                    logging.error("Stark Repetedly gave following output: %s" %str(info))
                    return False

            time.sleep(5)
        time.sleep(1)        
        ser.write(b"DIAG_BMS_STOP\t")
        time.sleep(1)
        logging.info("DIAG_BMS_STOP command ran and bms testing successful")
        return True

    except Exception as e:
        logging.error(e)
        time.sleep(1)
        ser.write(b"DIAG_BMS_STOP\t")
        time.sleep(1)
        logging.info("DIAG_BMS_STOP command ran in exception handling in bms_testing_function")
        return False















