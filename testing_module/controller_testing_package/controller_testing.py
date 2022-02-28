'''
This module is entry point for controller testing
'''
import time
from shared.logging_config import setup_logger
from shared.constants import (TESTING_COUNTER, CONTROLLER_OUTPUT_LENGTH)
from shared.loggers import (controller_data_logger, controller_error_logger, controller_general_logger)

from .controller_validator import controller_validation_function

def controller_testing_function(ser):
    """This function will receive controller data from serial and will get it validated.

    Args:
        ser (_obj_): serial connection object
    """    
    controller_general_logger.info("Controller testing started")
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

            try:
                controller_data_logger.info(str(info))
            except:
                controller_error_logger.error("Controller log not added")

            if info.split(',')[0]=="DIAG_CONTROLLER_START" and len(info) == CONTROLLER_OUTPUT_LENGTH:
                res = controller_validation_function(ser,info)

                if res == False:

                    time.sleep(1)
                    ser.write(b"DIAG_CONTROLLER_STOP\t")
                    time.sleep(1)
                    
                    controller_general_logger.info("DIAG_CONTROLLER_STOP command ran because controller output did not validated. (Check above logs for more info) ")
                    return False
            else:
                error_counter += 1
                controller_general_logger.critical("Wrong  Controller input received: %s" %str(info))

                if error_counter >= 4:

                    time.sleep(1)
                    ser.write(b"DIAG_CONTROLLER_STOP\t")
                    time.sleep(1)
                    
                    controller_general_logger.info("DIAG_CONTROLLER_STOP command ran because wrong controller input received several times.")
                    return False
            
            time.sleep(5)
        
        time.sleep(1)
        ser.write(b"DIAG_CONTROLLER_STOP\t")
        time.sleep(1)

        controller_general_logger.info("DIAG_CONTROLLER_STOP command ran and CONTROLLER TESTING SUCCESSFULL.")
        return True

    except:
        time.sleep(1)
        ser.write(b"DIAG_CONTROLLER_STOP\t")
        time.sleep(1)
        
        controller_error_logger.error("DIAG_CONTROLLER_STOP command ran in exception handling in controller_testing_function ")
        return False