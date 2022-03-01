"""
Entry_point  for stark testing.
"""
import time
import can
import uuid
from shared.constants import (INPUT_MSG, TESTING_COUNTER, CAN_INPUT_ID)
from shared import (can_bus, ser)
from shared import stark_error_logger
from send_and_receive_to_stark import send_receive_validate


def stark_testing_function(_uuid = None) -> bool:
    """This is the entry point for stark testing.

    Args:
        _uuid (_str_): uuid for each request
    """
    
    if _uuid == None:
        _uuid = str(uuid.uuid4())
    
    time.sleep(1)
    ser.write(b"DIAG_STARK_START\t")
    time.sleep(1)
    print("Stark testing started")

    try:

        #why for loop not a decorator? because we can later on modify out input or can give 
        #multiple different inputs
        counter=0

        while counter < TESTING_COUNTER:
            counter+=1
            
            #Measure taken because of serial behaviour
            if counter==1:
                
                #it is for clearing the buffer of serial before actual testing can start
                #why not put it in the send_and_receive_to_can file because that module
                #has no counter to keep track of which msg to drop
                
                msg_buffer_size = ser.inWaiting()
                ser.read(msg_buffer_size)
                
                can_msg=can.Message(
                                    arbitration_id = CAN_INPUT_ID,
                                    data = INPUT_MSG,
                                    is_extended_id = False,
                                )
                can_bus.send(can_msg)
                
                time.sleep(1)
                continue

            res = send_receive_validate(INPUT_MSG, _uuid)
            
            if res==False:
                
                time.sleep(1)
                ser.write(b"DIAG_STARK_STOP\t")
                time.sleep(1)

                return False
        
        time.sleep(1)
        ser.write(b"DIAG_STARK_STOP\t")
        time.sleep(1)

        return True
    except Exception as e:

        stark_error_logger.error("uuid - %s message - Following error in stark testing: %s" %_uuid %e)
        
        time.sleep(1)
        ser.write(b"DIAG_STARK_STOP\t")
        time.sleep(1)
        
        return False





