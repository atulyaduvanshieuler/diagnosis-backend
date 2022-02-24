"""
This file will feed input to can and
will receive and validate serial output.
"""

import time
import can
import logging
from constants import (CAN_INPUT_ID, CHECK_BUFFER_DATA_COUNTER, STARK_OUTPUT_LENGTH)
from validate_stark_output import verify_serial


def send_receive_validate(can_bus,ser,input_msg):
    """This function will send to can,receive and validate the serial ouput.

    Args:
        can_bus (_object_): can connection object
        ser (_object_): serial connection object
        input_msg (_string_): What input to send to can
    """

    can_msg=can.Message(
        arbitration_id = CAN_INPUT_ID,
        data = input_msg,
        is_extended_id = False,
    )

    try:
        can_bus.send(can_msg)
    except can.CanError:
        logging.error("Message Not Sent")
        print("Message NOT sent")
    
    time.sleep(5)

    msg_buffer_size = ser.inWaiting()
    data = ser.read(msg_buffer_size)
    info = data.decode("UTF-8")

    if info.split(",")[0] == "DIAG_STARK_START":
        if len(info) == STARK_OUTPUT_LENGTH:
            res = verify_serial(info)
            if res==True:
                return True
            else:
                return False
        else:
            logging.critical("Following Message received: %s" %str(info))
    else:
        logging.critical("Following Message received: %s" %str(info))









    








