"""
This module will validate the bms output.
"""
import time
import logging
from constants import SERIAL_DATA_LOG_FILENAME

def bms_validation_function(ser,bms_output):
    """This function will take bms_output as string and will parse it 
        and will match it to the expected ouput

    Args:
        bms_output (_str_): bms output as string
    """    

    bms_output_list = bms_output.split(",")

    try:
        with open(SERIAL_DATA_LOG_FILENAME, "a") as data_file:
            data_file.write(bms_output_list)
    except:
        logging.error("BMS log not added ")

    try:
        if float(bms_output_list[5]) < 0 or float(bms_output_list[5]) > 100:
            print("The value of Pack Q SoC Trimmed is %s" % bms_output_list[5])
            return False
        return True
    except:
        time.sleep(1)
        ser.write(b"DIAG_BMS_STOP\t")
        time.sleep(1)
        logging.info("DIAG_BMS_STOP command ran in bms_validation_function exception handling")





