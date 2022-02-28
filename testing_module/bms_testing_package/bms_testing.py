"""
This module is the entry point for bms testing
"""
import time
from shared.constants import (TESTING_COUNTER, BMS_OUTPUT_LENGTH)
from shared.connections import ser
from shared.loggers import (bms_data_logger,bms_error_logger,bms_general_logger)


from bms_testing_package.bms_validator import bms_validation_function


def bms_testing_function():
    
    """
        It will receive bms data from serial port and get it validated from bms_validator.py

    Args:
        can_bus (_type_): can connection object
        ser (_type_): serial connection object
    """

    bms_general_logger.info("BMS testing started")
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

            # Measures taken because of serial behaviour
            if counter==1:
                continue

            try:
                bms_data_logger.info(str(info))
            except:
                bms_error_logger.error("BMS log not added ")

            if info.split(',').count("DIAG_BMS_START") == 1:

                res = bms_validation_function(ser,info)

                if res == False:

                    time.sleep(1)
                    ser.write(b"DIAG_BMS_STOP\t")
                    time.sleep(1)
                    
                    bms_general_logger.critical("BMS output was somehow wrong. (For reasons check above logs or data_logs file.) ")
                    return False
            else:
                error_counter += 1
                bms_general_logger.critical("Wrong BMS output: %s " %str(info))

                if error_counter >= 4:
                    #May Need to remove this part and also remove error_counter while removing this
                    
                    time.sleep(1)        
                    ser.write(b"DIAG_BMS_STOP\t")
                    time.sleep(1)

                    bms_general_logger.critical("DIAG_BMS_STOP command ran because of error_counter limit exceeded")

                    return False

            time.sleep(5)

        time.sleep(1)        
        ser.write(b"DIAG_BMS_STOP\t")
        time.sleep(1)

        bms_general_logger.info("DIAG_BMS_STOP command ran and BMS TESTING SUCCESSFULL")
        
        return True

    except Exception as e:

        bms_error_logger.error(e)
        time.sleep(1)
        ser.write(b"DIAG_BMS_STOP\t")
        time.sleep(1)
        bms_error_logger.info("DIAG_BMS_STOP command ran in exception handling in bms_testing_function")

        return False