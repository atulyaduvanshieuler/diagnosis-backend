""" It checks whether serial output is right or wrong. """
from constants import default_expected_output
from shared import converter as hash
from expected_output import hash_expected_output


#data comes in this format '14112,43794,14112'
def verify_serial(serial_data: str) -> bool:
    """

    Args:
        serial_data (str): _description_

    Returns:
        bool: _description_
    """
    serial_data_list = list(serial_data.split(','))
    serial_data_string = ",".join(serial_data_list[1:-1])

    hashed_data = hash.converter(serial_data_string)
    
    return hashed_data == hash_expected_output(default_expected_output)
