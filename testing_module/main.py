'''
This is the entry point of diagnosis of stark , bms and controller.

'''
import time
import can
import serial
from shared.loggers import general_logger, error_logger
from stark_testing_package import test_stark
from bms_testing_package import test_bms
from controller_testing_package import test_controller
from shared.stop_diagnosis_mode import diag_stop_function
from shared.constants import (SERIAL_PORT, SERIAL_BAUDRATE, CAN_BUSTYPE, CAN_CHANNEL, CAN_BITRATE)
from shared.response_object import test_resp

try:
    can_bus = can.interface.Bus(bustype=CAN_BUSTYPE, channel=CAN_CHANNEL,bitrate=CAN_BITRATE)
except:
    general_logger.error("Can Bus connection Problem")

try:
    ser = serial.Serial(
            port = SERIAL_PORT,
            baudrate = SERIAL_BAUDRATE,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            xonxoff=True,
            timeout=0,
        )
except:
    general_logger.error("Serial connection Problem")


def test_all_parts():

    """This is the main function which will be invoked in flask.

    Returns:
        _type_: _description_
    """

    diag_stop_function(ser)

    if test_stark(can_bus,ser):
        if test_bms(ser):
            if test_controller(ser):
                diag_stop_function(ser)
                general_logger.info("All Tests Passed")
                test_resp["test_status"] = "All Tests Passed"
                return test_resp
            else:
                diag_stop_function(ser)
                general_logger.info("Controller Testing Failed")
                test_resp["test_status"] = "Controller Testing Failed"
                return test_resp
        else:
            diag_stop_function(ser)
            general_logger.info("BMS Testing Failed")
            test_resp["test_status"] = "BMS Testing Failed"
            return test_resp
    else:
        diag_stop_function(ser)
        general_logger.info("Stark Testing Failed")
        test_resp["test_status"] = "Stark Testing Failed"
        return test_resp
    


    

    
    


