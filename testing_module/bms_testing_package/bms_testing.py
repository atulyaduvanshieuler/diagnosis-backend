"""
This module is the entry point for bms testing
"""
import time
import uuid
from shared.constants import (TESTING_COUNTER, BMS_OUTPUT_LENGTH)
from shared import ser
from shared import (bms_data_logger,bms_error_logger,bms_general_logger)
from bms_testing_package.bms_validator import bms_validation_function


def bms_testing_function(_uuid = None):
    
    """
        It will receive bms data from serial port and get it validated from bms_validator.py

    Args:
        can_bus (_type_): can connection object
        ser (_type_): serial connection object
    """

    if _uuid == None:
        _uuid = str(uuid.uuid4())

    bms_general_logger.info("uuid - %s message - BMS testing started" %_uuid )
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
                bms_error_logger.error("uuid - %s message - BMS log not added " %_uuid)

            if info.split(',').count("DIAG_BMS_START") == 1:

                res = bms_validation_function(info,_uuid)

                if res == False:

                    time.sleep(1)
                    ser.write(b"DIAG_BMS_STOP\t")
                    time.sleep(1)
                    
                    bms_general_logger.critical("uuid - %s message - BMS output was somehow wrong. (For reasons check above logs or data_logs file.) " %_uuid )
                    return False
            else:
                error_counter += 1
                bms_general_logger.critical("uuid - %s message - Wrong BMS output: %s "  %_uuid %str(info))

                if error_counter >= 4:
                    #May Need to remove this part and also remove error_counter while removing this
                    
                    time.sleep(1)        
                    ser.write(b"DIAG_BMS_STOP\t")
                    time.sleep(1)

                    bms_general_logger.critical("uuid - %s message - DIAG_BMS_STOP command ran because of error_counter limit exceeded" %_uuid )

                    return False

            time.sleep(5)

        time.sleep(1)        
        ser.write(b"DIAG_BMS_STOP\t")
        time.sleep(1)

        bms_general_logger.info("uuid - %s message - DIAG_BMS_STOP command ran and BMS TESTING SUCCESSFULL" %_uuid )
        
        return True

    except Exception as e:

        bms_error_logger.error(e)
        time.sleep(1)
        ser.write(b"DIAG_BMS_STOP\t")
        time.sleep(1)
        bms_error_logger.info("uuid - %s message - DIAG_BMS_STOP command ran in exception handling in bms_testing_function" %_uuid )

        return False