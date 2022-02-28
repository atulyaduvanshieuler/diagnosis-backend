"""
This file will feed input to can and
will receive and validate serial output.
"""

import time
import can
from shared.loggers import (stark_general_logger, stark_data_logger, stark_error_logger)
from shared.constants import (CAN_INPUT_ID, CHECK_BUFFER_DATA_COUNTER, STARK_OUTPUT_LENGTH)
from validate_stark_output import verify_serial


def send_receive_validate(can_bus,ser,input_msg):
    """This function will send to can,receive and validate the serial ouput.

    Args:
        can_bus (_object_): can connection object
        ser (_object_): serial connection object
        input_msg (_string_): What input to send to can
    """
    try:

        can_msg=can.Message(
            arbitration_id = CAN_INPUT_ID,
            data = input_msg,
            is_extended_id = False,
        )


        try:
            can_bus.send(can_msg)
        except can.CanError:
            stark_error_logger.error("CAN Message Not Sent")
        
        time.sleep(5)



        msg_buffer_size = ser.inWaiting()
        data = ser.read(msg_buffer_size)



        try:
            info = data.decode("UTF-8")
        except:

            stark_data_logger.info(str(info))
            stark_error_logger.error("Stark Output can be decoded in UTF-8. Following output received: %s" %str(info))

            return False



        try:
            stark_data_logger.info(str(info))
        except:
            stark_error_logger.error("Stark logs not added")



        if info.split(",").count("DIAG_STARK_START") == 1:
            res = verify_serial(info)
            if res==True:
                stark_general_logger.info("Stark output verified.")
                return True
            else:
                stark_error_logger.info("Stark output not verified.(Reasons may be anything. Check above reasons to see reason.")
                return False
        else:
            stark_data_logger.critical("Wrong  Stark Input received: %s" %str(info))

    except Exception as e:
        stark_error_logger.error(e)
        return False









    








