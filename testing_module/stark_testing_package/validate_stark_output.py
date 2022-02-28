from shared.sha256_converter import converter as hash
from shared.constants import (DEFAULT_EXPECTED_OUTPUT, SERIAL_DATA_LOG_FILENAME)

from shared.loggers import (stark_error_logger)

def verify_serial(serial_data: str) -> bool:
    
    """This function will verify whether serial ouput is right or wrong

    Args:
        serial_data (str): it contains serial output in string format

    Returns:
        bool: return whether expected output and serial output are equal or not
    """
    try:
        serial_data_list = list(serial_data.split(','))

        serial_data_string = ",".join(serial_data_list[2:-1]) 
        
        return hash(serial_data_string) == hash(DEFAULT_EXPECTED_OUTPUT)
    
    except Exception as e:
        
        stark_error_logger.error("Serial Data not verified")
        return False