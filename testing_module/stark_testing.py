"""
Entry_point  for stark testing.
"""
import time
import can
from constants import (INPUT_MSG, TESTING_COUNTER, CAN_INPUT_ID)
from send_and_receive_to_stark import send_receive_validate

def stark_testing_function(can_bus,ser):
    """This is the entry point for stark testing.

    Args:
        can_bus (_object_): can_bus connection object
        ser (_object_): serial connection object
    """
    
    time.sleep(1)
    ser.write(b"DIAG_STARK_START\t")
    time.sleep(1)
    print("Stark testing started")

    #why for loop not a decorator? because we can later on modify out input or can give 
    #multiple different inputs
    counter=0

    while counter < TESTING_COUNTER:
        counter+=1

        if counter==1:
            
            #it is for clearing the buffer of serial before actual testing can start
            #why not put it in the send_and_receive_to_can file because that module
            #has no counter to keep track of which msg to drop
            
            msg_buffer_size = ser.inWaiting()
            data = ser.read(msg_buffer_size)
            can_msg=can.Message(
                                arbitration_id = CAN_INPUT_ID,
                                data = INPUT_MSG,
                                is_extended_id = False,
                            )
            can_bus.send(can_msg)
            time.sleep(1)
            continue

        res = send_receive_validate(can_bus,ser,INPUT_MSG)
        if res==False:
            time.sleep(1)
            ser.write(b"DIAG_STARK_STOP\t")
            time.sleep(1)
            return False
    
    time.sleep(1)
    ser.write(b"DIAG_STARK_STOP\t")
    time.sleep(1)
    return True




