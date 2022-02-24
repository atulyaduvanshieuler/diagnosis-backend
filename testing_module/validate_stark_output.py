from sha256_converter import converter as hash
from constants import (DEFAULT_EXPECTED_OUTPUT, SERIAL_DATA_LOG_FILENAME)

import logging

def verify_serial(serial_data: str) -> bool:
    
    """This function will verify whether serial ouput is right or wrong

    Args:
        serial_data (str): it contains serial output in string format

    Returns:
        bool: return whether expected output and serial output are equal or not
    """
    
    serial_data_list = list(serial_data.split(','))

    try:
        with open(SERIAL_DATA_LOG_FILENAME, "a") as data_file:
            data_file.write(serial_data_list)
    except:
        logging.error("Stark logs not added")

    serial_data_string = ",".join(serial_data_list[2:-1]) 
    
    return hash(serial_data_string) == hash(DEFAULT_EXPECTED_OUTPUT)