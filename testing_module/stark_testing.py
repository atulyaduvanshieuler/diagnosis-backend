"""
Entry_point  for stark testing.
"""
import time
from constants import (INPUT_MSG, TESTING_COUNTER)
from send_and_receive_to_stark import send_receive_validate

def stark_testing_function(can_bus,ser):
    """This is the entry point for stark testing.

    Args:
        can_bus (_object_): can_bus connection object
        ser (_object_): serial connection object
    """
    
    
    ser.write(b"DIAG_STARK_START\t")
    time.sleep(0.1)

    #why for loop not a decorator? because we can later on modify out input or can give 
    #multiple different inputs

    for i in range(TESTING_COUNTER):
        res = send_receive_validate(can_bus,ser,INPUT_MSG)
        if res==False:
            ser.write(b"DIAG_STARK_STOP\t")
            time.sleep(0.1)
            return False
    
    ser.write(b"DIAG_STARK_STOP\t")
    time.sleep(0.1)
    return True




